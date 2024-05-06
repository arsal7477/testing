import psycopg2

def main():
    hostname = 'localhost'
    database = 'postgres'
    username = 'postgres'
    pwd = 'pgadmin4'
    port_id = 5432

    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )

        cur = conn.cursor()

        # # Create table if not exists
        # create_script = '''CREATE TABLE IF NOT EXISTS abc (
        #                     id SERIAL PRIMARY KEY,
        #                     a INT,
        #                     b VARCHAR(20)
        #                   )'''

        # cur.execute(create_script)
        # conn.commit()

        # print("Table created successfully!")

        # # Insert some sample data
        # cur.execute("INSERT INTO abc (a, b) VALUES (1, 'Data1')")
        # cur.execute("INSERT INTO abc (a, b) VALUES (2, 'Data2')")
        # cur.execute("INSERT INTO abc (a, b) VALUES (%s, %s), (%s, %s), (%s, %s)", (3, 'data3', 4, 'data4', 5, 'data5'))
        # conn.commit()

        # print("Data inserted successfully!")
        # # Select data from the table where id = 1
        # cur.execute("SELECT * FROM abc WHERE id = 1")
        # row = cur.fetchone()

        # print("Data where id = 1:")
        # print(row)

        cur.execute("Select * from abc where id < 4")
        row =cur.fetchall()
        print('data')
        print(row)


    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL:", e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
