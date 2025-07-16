import os

import sqlmodel
from sqlmodel import Session, SQLModel

DATABASE_URL = os.environ.get("SQL_SERVER_DB_CONNECTION")

if DATABASE_URL == "":
    raise NotImplementedError("Not SQL ConnectionString.")


engine = sqlmodel.create_engine(DATABASE_URL)

# TODO 當資料庫服務未建立時，此區會導致error，如[command]有使用[--reload]則服務停止，但容器還活著
def init_db(): # 不會創建資料庫的遷移
    print("creating database tables...")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session