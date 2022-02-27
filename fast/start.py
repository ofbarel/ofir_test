from datetime import datetime
from fastapi import FastAPI
from asyncio import run
from sqlalchemy import create_engine

from sql_test import initialize_db, show_data, show_data_2, show_all
from db.db_handler import get_user_sql, get_user_orm, add_user, remove_user, create_db, show_all_orm

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/2")
def root2():
    resp = show_data_2()
    print("bla")
    print(resp)

    return {"message": "222", "resp": resp}


@app.get("/get_all")
def get_all():
    print(show_all())


print(app)
# print(run(root()))

# create_db()
get_all()
add_user(777, "splinter", 32000)
get_all()
remove_user(555)
remove_user(777)
get_all()
show_all_orm()
