// index.js

function filterResults(specialization, group) {
   
    var rows = document.getElementById('results-body').getElementsByTagName('tr');
    for (var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName('td');
        if (cells.length > 0) {
            var fio = cells[1].textContent;
            var groupText = cells[2].textContent;
            if (fio.includes(specialization) && groupText.includes(group)) {
                rows[i].style.display = '';
            } else {
                rows[i].style.display = 'none';
            }
        }
    }
}

function filterSpecialization(specialization) {
    document.getElementById('group-options').style.display = 'block';
    // Дополнительная логика для фильтрации по специальности
}

function filterGroup() {
    var selectedSpecialization = document.getElementById('specialization-select').value;
    var selectedLanguage = document.getElementById('language-select').value;

    // Отправляем запрос на сервер
    fetch('/filter', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            specialization: selectedSpecialization,
            language: selectedLanguage
        })
    })
    .then(response => response.json())
    .then(data => {
        // Обновляем таблицу результатов с полученными данными
    
        updateResultsTable(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
var is_authenticated;

document.addEventListener("DOMContentLoaded", function() {
    var authInfo = document.getElementById('auth-info');
    var is_authenticated_l = authInfo.getAttribute('data-auth');

    // Преобразование значения в логический тип
    is_authenticated = is_authenticated_l === 'True'; 
})


function updateResultsTable(data) {
    // Очищаем текущие данные в таблице
    var tbody = document.getElementById('results-body');
    tbody.innerHTML = '';

    // Преобразуем массив массивов в массив объектов
    var students = data.map(function(row) {
        return {
            student_id: row[0],
            full_name: row[1],
            specialization: row[2],
            language_of_study: row[3],
            avg_professional_score: row[4],
            total_avg_score: row[5],
            application_date: new Date(row[6]) // Преобразуем строку с датой в объект Date
        };
    });

    // Форматирование даты без времени с учетом локального часового пояса
    var dateFormatter = new Intl.DateTimeFormat('ru', {
        day: 'numeric',
        month: 'long',
        timeZone: 'Asia/Almaty' // Часовой пояс "Astana"
    });

    // Добавляем новые данные в таблицу
    students.forEach(function(student, index) {
        var dateWithoutTime = new Date(student.application_date);
        dateWithoutTime.setHours(0, 0, 0, 0); // Устанавливаем время на полночь
        var formattedDate = dateFormatter.format(dateWithoutTime); // Форматируем дату
        var row = "<tr>" +
            "<td>" + (index + 1) + "</td>" +
            "<td>" + student.full_name + "</td>" +
            "<td>" + student.specialization + "</td>" +
            "<td>" + student.language_of_study + "</td>" +
            "<td>" + student.avg_professional_score + "</td>" +
            "<td>" + student.total_avg_score + "</td>" +
            "<td>" + formattedDate + "</td>"; // Отображаем отформатированную дату
    
        // Проверяем, авторизован ли пользователь
        if (is_authenticated) {
            row += "<td><img src='/static/pencil.png' width='20' height='20' alt='Редактировать' onclick=\"editStudent('" + student.student_id + "')\">" +
                   "<img src='/static/bin.png' width='20' height='20' alt='Удалить' onclick=\"deleteStudent('" + student.student_id + "')\"></td>";
        }
        
        row += "</tr>";
        tbody.innerHTML += row;
    });
}

function redirectToLogin() {
    window.location.href = '/login';
}

function redirectToEditPage(student_id) {
    window.location.href = '/edit_student?student_id=' + encodeURIComponent(student_id);
}

function editStudent(student_id) {
    redirectToEditPage(student_id);
}
function deleteStudent(student_id) {
    
    if (confirm('Вы уверены, что хотите удалить этого студента?')) {
        // Отправляем запрос на удаление студента на сервер
        fetch('/delete_student', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                student_id: student_id
            })
        })
        .then(response => response.json())
        .then(data => {
            // Если удаление прошло успешно, обновляем таблицу результатов
            filterGroup();
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}
