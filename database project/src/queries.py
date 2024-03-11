import sqlite3
from src.database import connect_database
from datetime import datetime

connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()

def execute_query(query, params=None):
    connection = connect_database()
    cursor = connection.cursor()

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        result = cursor.fetchall()
        connection.commit()
        return result
    except Exception as e:
        print(f"Error executing query: {e}")
        print(f"Query: {query}")
        return None
    finally:
        connection.close()



# Business Requirement Queries
#query1
        
def query_1():
    connection = connect_database()
    cursor = connection.cursor()
    exam_id = 1  # Replace with the specific exam ID
    cursor.execute(
        f'''
        SELECT sr.student_name, sr.address
        FROM student_records sr
        JOIN exam_timetable et ON sr.student_id = et.student_id
        WHERE et.exam_id = {exam_id};
        '''
    )
    result = cursor.fetchall()
    connection.close()
    return result

#query2
def query_2():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(
        '''
        SELECT t.teacher_name, ts.subject_id
        FROM teachers t
        JOIN teacher_subjects ts ON t.teacher_id = ts.teacher_id;
        '''
    )
    result = cursor.fetchall()
    connection.close()
    return result

#query4
def query4():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(
        """
    SELECT eb.exam_board_name, COUNT(er.exam_record_id) AS record_count
    FROM exam_boards eb
    LEFT JOIN exam_board_exam_record eber ON eb.exam_board_id = eber.exam_board_id
    LEFT JOIN exam_records er ON eber.exam_record_id = er.exam_record_id
    GROUP BY eb.exam_board_name;
    """
    )
    result = cursor.fetchall()
    connection.close()
    return result

#query5
def query5():
    connection = connect_database()
    cursor = connection.cursor()
    subject_id = 'SC290'  # Replace with the specific subject ID
    cursor.execute(
        f'''
        SELECT eb.exam_board_name, eb.director_name, eb.qualification_name, eb.company_address
        FROM exam_boards eb
        JOIN subjects s ON eb.subject_id = s.subject_id
        WHERE s.subject_id = '{subject_id}';
        '''
    )
    result = cursor.fetchall()
    connection.close()
    return result


#query3
def query_3():
    connection = connect_database()
    cursor = connection.cursor()
    try:
        cursor.execute(
            '''
                SELECT
                er.subject_id,
                AVG(CAST(REPLACE(REPLACE(SUBSTRING(et.exam_duration, 1, CHARINDEX(' Hour', et.exam_duration) - 1), ' AND ', ''), ' Mintus', '') AS FLOAT)) AS avg_exam_duration
                FROM
                exam_timetable et
                JOIN student_records sr ON et.student_id = sr.student_id
                JOIN exam_records er ON sr.subject_id = er.subject_id
                GROUP BY
                er.subject_id;

            '''
        )
        result = cursor.fetchall()
        connection.close()
        return result
    except Exception as e:
        connection.close()
        print(f"Error: {e}")
        return None

