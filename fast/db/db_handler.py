from sqlalchemy.future import create_engine as future_create_engine
from sqlalchemy import select, delete, insert, func, text, literal_column
from sqlalchemy.orm import Session

from .employee import Employee
from .factory import Factory

# future_engine = future_create_engine("sqlite+pysqlite:///:memory:", echo=True)
future_engine = future_create_engine("sqlite:////home/ofir/fast.db", echo=True)


def add_user(id: int, name: str, salary: int = None, factory=3):
    print("-------------------------add_user--------------------------")
    with Session(future_engine) as session:
        query = session.query(Employee).filter(Employee.id == id)
        emp = session.execute(query).first()
        if not emp:
            new_emp = Employee(id, name, salary, factory)
            session.add(new_emp)
            session.commit()

        # insert_query = insert(Employee).values((888, "shareder", 12000, 3))
        # session.execute(insert_query)
        # session.commit()


def remove_user(id: int):
    with Session(future_engine) as session:
        query = session.query(Employee).filter(Employee.id == id)
        emp = session.execute(query).first()
        if not emp:
            print("user does not exist exception")
            return "user does not exist exception"
        delete_query = delete(Employee).filter(Employee.id == id)
        session.execute(delete_query)
        session.commit()


def get_user_sql():
    with Session(future_engine) as session:
        query = select(Employee).where(Employee.id == 333)
        resp = session.execute(query)
        for row in resp:
            print(row.Employee)


def show_all_orm():
    with Session(future_engine) as session:
        column_compare_factory = literal_column("Employee.factory") + " = " + literal_column("Factory.id")
        join_query = select(column_compare_factory, Employee.name,
                            Employee.salary, Factory.name, Factory.code_bonus,
                            Employee.salary + Factory.code_bonus).join(Factory.employee_table)
        resp = session.execute(join_query).all()
        for row in resp:
            x = row
        print(f"resp : {resp}")


def create_db():
    with Session(future_engine) as session:
        session.add_all([Factory(1, "tel-aviv", 3000), Factory(2, "haifa", 5000), Factory(3, "jerusalem", 8000)])
        session.add_all(
            [Employee(111, "leonardo", 25000, 1),
             Employee(222, "donatelo", 28000, 2),
             Employee(333, "rafael", 21000, 1),
             Employee(444, "michaelangelo", 17000, 3)])
        session.commit()
