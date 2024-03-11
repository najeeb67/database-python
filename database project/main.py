from src.table_creation import create_tables
from src.queries import execute_query, query_1,query_2,query4,query5,query_3
from datetime import datetime


def format_date(date_str):
    try:
        formatted_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').strftime('%dth %B %Y, %I:%M %p')
        return formatted_date
    except ValueError as e:
        print(f"Error formatting date: {e}")
        return None


def main():
    # Uncomment the line below if you need to recreate the tables
    create_tables()


    result_query_1 = query_1()
    print(result_query_1)

    result_query_2 = query_2()
    print(result_query_2)

    result_query_5 = query5()
    print(result_query_5)

    result_query_4 = query4()
    print(result_query_4)
    result_query_3 = query_3()
    print(result_query_3)
  

if __name__ == "__main__":
    main()
