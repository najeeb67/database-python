import sqlite3
from src.database import connect_database

def create_tables():
    connection = connect_database()
    cursor = connection.cursor()

    # Create database table subjects
    cursor.execute(
        '''CREATE TABLE subjects (
        subject_id VARCHAR(244) PRIMARY KEY ,
        subject_title VARCHAR(244),
        student_id INTEGER
        )'''
    )


    # # Create database table student_records
    cursor.execute(
        '''CREATE TABLE student_records (
        student_id INTEGER PRIMARY KEY,
        subject_id VARCHAR(244),
        student_name VARCHAR(244),
        exam_id INTEGER,
        date_of_birth DATETIME,
        address VARCHAR(244),
        FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
        )'''
    )

    # Create database table invigilators
    cursor.execute(
        '''CREATE TABLE invigilators(
        invigilator_id INTEGER PRIMARY KEY,
        full_name VARCHAR(244),
        subject_id VARCHAR(244),
        date DATETIME,
        attendence_mark VARCHAR(244)
        )'''
    )

    # # Create database table exam_timetable
    cursor.execute(
        '''CREATE TABLE exam_timetable (
        exam_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        firstname VARCHAR(244) NOT NULL,
        lastname VARCHAR(244) NOT NULL,
        group_id VARCHAR(244),
        course_name VARCHAR(244),
        exam_duration VARCHAR(244),
        invigilator_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES student_records (student_id),
        FOREIGN KEY (invigilator_id) REFERENCES invigilators (invigilator_id)
        )'''
    )


    # # Create database table teachers
    cursor.execute(
        '''CREATE TABLE teachers(
        teacher_id INTEGER PRIMARY KEY,
        teacher_name VARCHAR(244) NOT NULL,
        course_name VARCHAR(244) NOT NULL,
        subject_id VARCHAR(244),
        FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
        )'''
    )


    # # Create database table teacher_invigilators
    cursor.execute(
        '''CREATE TABLE teacher_invigilators (
        teacher_id INTEGER,
        invigilator_id INTEGER,
        PRIMARY KEY (teacher_id, invigilator_id),
        FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id),
        FOREIGN KEY (invigilator_id) REFERENCES invigilators (invigilator_id)
        )'''
    )



    # # Create database table exam_records
    cursor.execute(
        '''CREATE TABLE exam_records(
        exam_record_id INTEGER PRIMARY KEY,
        subject_id VARCHAR(244),
        teacher_id INTEGER,
        group_id VARCHAR(244),
        FOREIGN KEY(subject_id) REFERENCES subjects (subject_id),
        FOREIGN KEY(teacher_id) REFERENCES teachers (teacher_id)
        )'''
    )

    # # Create database table exam_boards
    cursor.execute(
        '''CREATE TABLE exam_boards(
        exam_board_id INTEGER PRIMARY KEY,
        exam_board_name VARCHAR(244),
        subject_id VARCHAR(244),
        director_name VARCHAR(244),
        qualification_name VARCHAR(244),
        company_address VARCHAR(244),
        FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
        )'''
    )

    # # Create database table student_exam_records
    cursor.execute(
        '''CREATE TABLE student_exam_records(
        student_id INTEGER,
        exam_record_id INTEGER,
        PRIMARY KEY (student_id, exam_record_id),
        FOREIGN KEY (student_id) REFERENCES student_records(student_id),
        FOREIGN KEY (exam_record_id) REFERENCES exam_records(exam_record_id)
        )'''
    )

    # # Create database table exam_record_subject
    cursor.execute(
        '''CREATE TABLE exam_record_subject (
        exam_record_id INTEGER,
        subject_id VARCHAR(244),
        PRIMARY KEY (exam_record_id, subject_id),
        FOREIGN KEY (exam_record_id) REFERENCES exam_records(exam_record_id),
        FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
        )'''
    )

    # Create database table exam_board_exam_record
    cursor.execute(
        '''CREATE TABLE exam_board_exam_record (
        exam_board_id INTEGER,
        exam_record_id INTEGER,
        PRIMARY KEY (exam_board_id, exam_record_id),
        FOREIGN KEY (exam_board_id) REFERENCES exam_boards (exam_board_id),
        FOREIGN KEY (exam_record_id) REFERENCES exam_records (exam_record_id)
      )'''
    )

    # # Create database table teacher and subject

    cursor.execute(
        '''CREATE TABLE teacher_subjects (
        teacher_id INTEGER,
        subject_id VARCHAR(244),
        PRIMARY KEY (teacher_id, subject_id),
        FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id),
        FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
        )'''
    )

 # Sample data for subjects
    cursor.executemany(
        '''INSERT INTO subjects (subject_id, subject_title, student_id) 
           VALUES (?, ?, ?)''',
        [
            ('AD778','Art & Design Qual345', 7045),
            ('MS324','Mathematics Qual324', 7068),
            ('SC290','Combined Science Qual290', 7024),
            ('DT453','Design & Technology Qual453', 7052),
            ('EN882','English Qual882', 7011),
            ('GE617','Geography Qual617',7096),
            ('HS003','History Qual003',7035),
            ('SP969','Spanish Qual 969',7099),

            # Add more sample data as needed
        ]
    )

    cursor.executemany(
        '''INSERT INTO student_records (student_id, subject_id, student_name, exam_id, date_of_birth, address) 
        VALUES (?, ?, ?, ?, ?, ?)''',
        [
            (7045, 'AD778', 'Henry Cavill', '1', '2005-02-26', '21 Sowerby Close, London, SE9 6HA'),
            (7052, 'DT453', 'Abi Gale', '4', '2005-11-12', 'Flat 10, Paxton House, Morecambe Street, London, SE17 1DS'),
            (7011, 'EN882', 'Piper Herron', '5', '2004-12-31', 'Flat 7, Hever House, 7 Lovelinch Close, London, SE15 1HA'),
            (7096, 'GE617', 'Mia Woodhall', '6', '2005-05-23', '2 Francis Mews, London, SE12 0HQ'),
            (7035, 'HS003', 'Zak Erron', '7', '2005-09-09', 'Birchmere Business Park, Nathan Way, London, SE28 0AF'),
            (7068, 'MS324', 'Ray Shears', '2', '2004-08-19', 'Flat 8, Gregory House, Brook Lane, London, SE3 8AS'),
            (7024, 'SC290', 'Lila Keel', '3', '2004-07-06', '13A King William Walk, London, SE10 9JH'),
            (7099, 'SP969', 'Harley Lavson', '8', '2004-06-18', 'Gwen Villa, Felltram Way, London, SE7 7RD'),
            # Add more sample data as needed
        ]
    )

      # Sample data for invigilators
    cursor.executemany(
        '''INSERT INTO invigilators (invigilator_id, full_name, subject_id, date, attendence_mark) 
           VALUES (?, ?, ?, ?, ?)''',
        [
            (1, 'Sue Cupples', "AD778", '2024-02-26 10:00:00', "Yes"),
            (2, 'Liz Borne', "MS324", '2024-02-27 14:00:00', "Yes"),
            (3, 'David Howard', "SC290", '2024-2-06 17:00:00', "Yes"),
            (4, 'Elise Manghani', "DT453", '2024-03-1 13:00:00', "Yes"),
            (5, 'Elise Manghani', "EN882", '2024-02-29 15:00:00', "Yes"),
            (6, 'Liz Borne', "GE617", '2024-02-12 16:00:00', "Yes"),
            (7, 'Sue Cupples', "HS003", '2024-02-20 18:00:00', "Yes"),
            (8, 'David Howard', "SP969", '2024-01-03 19:00:00', "Yes"),
            # Add more sample data as needed
        ]
    )

    # Sample data for exam_timetable
    cursor.executemany(
        '''INSERT INTO exam_timetable (exam_id, student_id, firstname, lastname, group_id, course_name, exam_duration, invigilator_id) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        [
            (1, 7045, 'Henry', 'Cavill', "11bART", 'Art Exam', '1 Hour', 1),
            (2, 7068, 'Ray', 'Shears', "13yMaths", 'Maths Exam', '2 Hours', 2),
            (3, 7024, 'Lila', 'Keel', "12dScience", 'Science Exam', '1 Hour AND 45 Mintus', 3),
            (4, 7052, 'Abi', 'Gale', "17vDesign & Technology", 'Design & Technology Exam', '2 Hour', 4),
            (5, 7011, 'Piper', 'Herron', "9tEnglish", 'English Exam', '3 Hour AND 20 Mintus', 5),
            (6, 7096, 'Mia', 'Woodhall', "4rGeography", 'Geography Exam', '1 Hour AND 45 Mintus', 6),
            (7, 7035, 'Zak', 'Erron', "8pHistory", 'History Exam', '1 Hour', 7),
            (8, 7099, 'Zak', 'Brron', "5kSpanish", 'Spanish Exam', '3 Hour AND 20 Mintus', 8),
            # Add more sample data as needed
        ]
    )

    # Sample data for teachers
    cursor.executemany(
        '''INSERT INTO teachers (teacher_id, teacher_name, course_name, subject_id) 
           VALUES (?, ?, ?, ?)''',
        [
            (1,'Mrs Town', 'Art, Spanish', "AD778"),
            (2, 'Miss Wilson', 'Design Technology, English', "MS324"),
            (3, 'Mr Gyrd', 'Geography, Maths', "SC290"),
            (4, 'Mr Hobbins', 'Science, History', "DT453"),
            (5, 'Ms Bevan', 'Science, History', "EN882"),
            (6, 'Mr Howell', 'Geography, Maths', "GE617"),
            (7, 'Mrs Wong', 'Design Technology, English', "HS003"),
            (8, 'Miss Smith', 'Art, Spanish', "SP969"),
            # Add more sample data as needed
        ]
    )

     # Sample data for teacher_invigilators
    cursor.executemany(
        '''INSERT INTO teacher_invigilators (teacher_id, invigilator_id) 
           VALUES (?, ?)''',
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 4),
            (6, 3),
            (7, 1),
            (8, 3),
            # Add more sample data as needed
        ]
    )


     # Sample data for exam_records
    cursor.executemany(
        '''INSERT INTO exam_records (exam_record_id, subject_id, teacher_id, group_id) 
           VALUES (?, ?, ?, ?)''',
        [
            (1, "AD778", 1, "11bART"),
            (2, "MS324", 2, "13yMaths"),
            (3, "SC290", 3, "12dScience"),
            (4, "DT453", 4, "17vDesign & Technology"),
            (5, "EN882", 5, "9tEnglish"),
            (6, "GE617", 6, "4rGeography"),
            (7, "HS003", 7, "8pHistory"),
            (8, "SP969", 8, "5kSpanish"),
            # Add more sample data as needed
        ]
    )

    # Sample data for exam_boards
    cursor.executemany(
        '''INSERT INTO exam_boards (exam_board_id, subject_id, director_name, exam_board_name, qualification_name, company_address) 
           VALUES (?, ?, ?, ?, ?, ?)''',
        [
            (1, "AD778", "Steven Harring", 'Art (AQA) Board',"GCSE", '60 Main Road Central London EC2V7NA'),
            (2, "MS324", "Ebony Fewins", 'Maths (Edexcel) Board',"GCSE", '12 New Street Luton LU7 2PH'),
            (3, "SC290", "Toran Singh", 'Science (JCQ) Board',"GCSE", '33 Queens Road Slough SL9 0QR'),
            (4, "DT453", "Natalie Rose", 'Design & Technology (OCR) Board',"GCSE", '65 The Drive Cambridge CB2 9FE'),
            (5, "EN882", "Steven Harring", 'English (AQA) Board',"GCSE", '60 Main Road Central London EC2V7NA'),
            (6, "GE617", "Natalie Rose", 'Geography (OCR) Board',"GCSE", '65 The Drive Cambridge CB2 9FE'),
            (7, "HS003", "Toran Singh", 'History (Edexcel) Board',"GCSE", '33 Queens Road Slough SL9 0QR'),
            (8, "SP969", "Ebony Fewins", 'Spanish (JCQ) Board',"GCSE",'12 New Street Luton LU7 2PH'),
            # Add more sample data as needed
        ]
    )


      # Sample data for student_exam_records
    cursor.executemany(
        '''INSERT INTO student_exam_records (student_id, exam_record_id) 
           VALUES (?, ?)''',
        [
            (7045, 1),
            (7068, 2),
            (7024, 3),
            (7052, 4),
            (7011, 5),
            (7096, 6),
            (7035, 7),
            (7099, 8),
            # Add more sample data as needed
        ]
    )

     # Sample data for exam_record_subject
    cursor.executemany(
        '''INSERT  INTO exam_record_subject (exam_record_id, subject_id) 
           VALUES (?, ?)''',
        [
            (1, "AD778"),
            (2, "MS324"),
            (3, "SC290"),
            (4, "DT453"),
            (5, "EN882"),
            (6, "GE617"),
            (7, "HS003"),
            (8, "SP969"),
            # Add more sample data as needed
        ]
    )

    # Sample data for exam_board_exam_record
    cursor.executemany(
        '''INSERT  INTO exam_board_exam_record (exam_board_id, exam_record_id) 
           VALUES (?, ?)''',
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            # Add more sample data as needed
        ]
    )

    cursor.executemany(
        '''INSERT INTO teacher_subjects (teacher_id, subject_id) 
           VALUES (?, ?)''',
        [
            (1, "AD778"),
            (2, "MS324"),
            (3, "SC290"),
            (4, "DT453"),
            (5, "EN882"),
            (6, "GE617"),
            (7, "HS003"),
            (8, "SP969"),
            # Add more sample data as needed
        ]
    )


    # Grant SELECT permission on views to the read-only user
    # cursor.execute("GRANT SELECT ON view_exam_student_info TO read_only_user;")
    # cursor.execute("GRANT SELECT ON view_exam_records_with_students TO read_only_user;")

    connection.commit()
    connection.close()
# create_tables()