import psycopg2

def connect_to_database():
    return psycopg2.connect(
        dbname="school",
        user="postgres",
        password="123",
        host="127.0.0.1",
        port="5432"
    )

def get_all_students():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def filter_students(specialization, language):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE specialization = %s AND language_of_study = %s ORDER BY avg_professional_score DESC, total_avg_score DESC", (specialization, language))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def insert_student(full_name, specialization, language_of_study, avg_professional_score, total_avg_score):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (full_name, specialization, language_of_study, avg_professional_score, total_avg_score) VALUES (%s, %s, %s, %s, %s)",
                (full_name, specialization, language_of_study, avg_professional_score, total_avg_score))
    conn.commit()
    cur.close()
    conn.close()

def delete_student(id):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()

def get_student_by_id(student_id):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def update_student(student_id, full_name, specialization, language_of_study, avg_professional_score, total_avg_score):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("UPDATE students SET full_name = %s, specialization = %s, language_of_study = %s, avg_professional_score = %s, total_avg_score = %s WHERE id = %s",
                (full_name, specialization, language_of_study, avg_professional_score, total_avg_score, student_id))
    conn.commit()
    cur.close()
    conn.close()
