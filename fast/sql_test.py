from sqlalchemy import text
from sqlalchemy.future import create_engine as future_create_engine

# future_engine = future_create_engine("sqlite+pysqlite:///:memory:", echo=True)
future_engine = future_create_engine("sqlite:////home/ofir/fast.db", echo=True)


def create_db():
    with future_engine.begin() as conn:
        conn.execute(text("CREATE TABLE some_table (x int, y int, text TEXT)"))
        conn.execute(
            text("INSERT INTO some_table (x, y, text) VALUES (:x, :y, :text)"),
            [{"x": 1, "y": 1, "text": "one"}, {"x": 2, "y": 4, "text": "two"}]
        )
    conn.commit()




def show_data():
    with future_engine.begin() as conn:
        result = conn.execute(text("SELECT 'hello world', 1 + 5"))
        resp = result.all()
        print(f"1 : {resp}")
        print(f"2 : {resp}")

        return resp


def show_data_2():
    resp = []
    with future_engine.begin() as conn:
        result = conn.execute(text("SELECT x,y FROM some_table"))
        for row in result:
            resp.append(f"x: {row.x} , y : {row.y}")
    return resp


def show_all():
    print("-------------------------show_all--------------------------")
    resp = []
    with future_engine.begin() as conn:
        result = conn.execute(text("SELECT * FROM employee"))
        for row in result:
            resp.append(f"id: {row.id} , name : {row.name} , salary : {row.salary} ")
    return resp



def initialize_db():
    create_db()
    print("done")
