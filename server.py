import requests
import psycopg2


def sendRequest(request):
    number = int(request.data)

    cur.execute(f"SELECT * FROM data WHERE number = {number}")

    if cur.fetchone() is not None:
        return f"ERROR: Число {number} уже в базе"

    cur.execute("SELECT * FROM data ORDER BY id DESC LIMIT 1")
    last_number = cur.fetchone()[1]

    if number != last_number + 1:
        return f"ERROR: Число, большее, чем {number} уже в базе"

    cur.execute(f"INSERT INTO data (number) VALUES {number + 1}")
    conn.commit()
    return str(number + 1)


if __name__ == '__main__':
    while True:
        conn = psycopg2.connect(
        host     = "localhost",
        database = "mydb",
        user     = "m4slina",
        password = "1qa2ws3ed",
        port=5432
            )
        
        cur = conn.cursor()
        request  = requests.get("http://localhost:8000")
        response = sendRequest(request)
        requests.post("http://localhost:8000", data=response)