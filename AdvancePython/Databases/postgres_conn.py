import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost", user="postgres", password="postgres", dbname="postgres"
    )

    conn.autocommit = True

    with conn.cursor() as cursor:
        db_name = "student"

        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' created successfully!")
        else:
            print(f"Database '{db_name}' already exists.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        conn.close()
