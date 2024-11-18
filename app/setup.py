from sqlalchemy import URL, Engine, create_engine
from sqlalchemy.orm import sessionmaker


def get_engine() -> Engine:
    url = URL.create(
        drivername="mysql+pymysql",
        username="root",
        password="passw0rd",
        host="localhost",
        port=3306,
        database="db_test",
    )
    engine = create_engine(url)
    return engine


def get_session():
    session_pool = sessionmaker(autoflush=False, bind=get_engine())
    session = session_pool()
    try:
        yield session
    finally:
        session.close()
