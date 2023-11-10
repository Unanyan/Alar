from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    text,
    CheckConstraint,
)
from config.settings import DATABASE_URL


engine = create_engine(DATABASE_URL)

metadata = MetaData()

data_1 = Table(
    "data_1",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    CheckConstraint("id BETWEEN 1 AND 10 OR id BETWEEN 31 AND 40", name="id_range_1"),
    extend_existing=True,
)

data_2 = Table(
    "data_2",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    CheckConstraint("id BETWEEN 11 AND 20 OR id BETWEEN 41 AND 50", name="id_range_2"),
    extend_existing=True,
)

data_3 = Table(
    "data_3",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    CheckConstraint("id BETWEEN 21 AND 30 OR id BETWEEN 51 AND 60", name="id_range_3"),
    extend_existing=True,
)

metadata.drop_all(engine)

with engine.begin() as connection:
    metadata.create_all(connection)


data_to_insert_1 = [
    {"id": 1, "name": "Data 1-1"},
    {"id": 2, "name": "Data 1-2"},
    {"id": 32, "name": "Data 1-32"},
]

insert_query_1 = text("INSERT INTO data_1 (id, name) VALUES (:id, :name)")

with engine.begin() as connection:
    for entry in data_to_insert_1:
        connection.execute(insert_query_1, entry)

data_to_insert_2 = [
    {"id": 12, "name": "Data 2-1"},
    {"id": 15, "name": "Data 2-2"},
    {"id": 45, "name": "Data 2-3"},
]

insert_query_2 = text("INSERT INTO data_2 (id, name) VALUES (:id, :name)")

with engine.begin() as connection:
    for entry in data_to_insert_2:
        connection.execute(insert_query_2, entry)

data_to_insert_3 = [
    {"id": 22, "name": "Data 3-1"},
    {"id": 25, "name": "Data 3-2"},
    {"id": 55, "name": "Data 3-3"},
]

insert_query_3 = text("INSERT INTO data_3 (id, name) VALUES (:id, :name)")

with engine.begin() as connection:
    for entry in data_to_insert_3:
        connection.execute(insert_query_3, entry)
