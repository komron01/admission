PGDMP         6                |            school    15.4    15.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    82188    school    DATABASE     ~   CREATE DATABASE school WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Kazakhstan.1252';
    DROP DATABASE school;
                postgres    false            �            1259    82215    students    TABLE     K  CREATE TABLE public.students (
    id integer NOT NULL,
    full_name character varying(100),
    specialization character varying(50),
    language_of_study character varying(50),
    avg_professional_score numeric(3,2),
    total_avg_score numeric(3,2),
    application_date timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.students;
       public         heap    postgres    false            �            1259    82214    students_id_seq    SEQUENCE     �   CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.students_id_seq;
       public          postgres    false    215            �           0    0    students_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;
          public          postgres    false    214            d           2604    82218    students id    DEFAULT     j   ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);
 :   ALTER TABLE public.students ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215            �          0    82215    students 
   TABLE DATA           �   COPY public.students (id, full_name, specialization, language_of_study, avg_professional_score, total_avg_score, application_date) FROM stdin;
    public          postgres    false    215   �       �           0    0    students_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.students_id_seq', 161, true);
          public          postgres    false    214            g           2606    82220    students students_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.students DROP CONSTRAINT students_pkey;
       public            postgres    false    215            �   �   x�345�L���U ��_��y��b��Ƌ�v]�qa'�����05�4202�50�52S04�24�26�3�4��4�60�24�D6i҅E�&�b1�������D������l��!�w~nQ~�BHiNbR~ejV�C4@5������̍-�N����� dRLw     