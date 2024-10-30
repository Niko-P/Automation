from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
import pytest


# Фикстура для создания подключения к базе данных
@pytest.fixture(scope="module")
def engine():
    db_url = "postgresql://postgres:jn34b1r9@localhost:5432/QA"
    return create_engine(db_url)


# Фикстура для создания соединения с базой данных
@pytest.fixture
def connection(engine):
    conn = engine.connect()
    yield conn
    conn.close()


# Фикстура для создания сессии
@pytest.fixture
def session(connection):
    Session = sessionmaker(bind=connection)
    sess = Session()
    try:
        yield sess
    finally:
        sess.close()


# Фикстура для создания таблиц перед запуском тестов
@pytest.fixture(scope="module", autouse=True)
def create_tables(engine):
    metadata = MetaData()

    # Определение таблиц
    Table(
        'subject',
        metadata,
        Column('subject_id', Integer, primary_key=True),
        Column('subject_title', String),
    )

    Table(
        'student',
        metadata,
        Column('user_id', Integer, primary_key=True),
        Column('level', String),
        Column('education_form', String),
        Column('subject_id', Integer),
    )

    Table(
        'teacher',
        metadata,
        Column('teacher_id', Integer, primary_key=True),
        Column('email', String),
        Column('group_id', Integer),
    )

    # Создание таблиц
    metadata.create_all(engine)
    yield
    # Удаление таблиц после тестов
    metadata.drop_all(engine)


# Тест на добавление нового предмета
def test_add_subject(session):
    subject_table = Table(
        'subject',
        MetaData(),
        Column('subject_id', Integer, primary_key=True),
        Column('subject_title', String),
    )

    new_subject = {'subject_id': 16, 'subject_title': 'Art'}
    insert_stmt = subject_table.insert().values(**new_subject)
    session.execute(insert_stmt)
    session.commit()

    result = (
        session.query(subject_table)
        .filter_by(subject_id=new_subject['subject_id'])
        .first()
    )
    assert result.subject_title == new_subject['subject_title']

    # Удаление добавленного предмета
    delete_stmt = subject_table.delete().where(
        subject_table.c.subject_id == new_subject['subject_id']
    )
    session.execute(delete_stmt)
    session.commit()


# Тест на обновление студента
def test_update_student(session):
    student_table = Table(
        'student',
        MetaData(),
        Column('user_id', Integer, primary_key=True),
        Column('level', String),
        Column('education_form', String),
        Column('subject_id', Integer),
    )

    # Предполагаем, что запись уже существует
    # Вы можете заменить 11548 на актуальный user_id в вашей базе данных
    existing_user_id = 11548
    update_data = {'user_id': existing_user_id, 'level': 'Advanced'}

    # Проверка, существует ли запись
    if session.query(student_table).filter_by(
         user_id=existing_user_id).first() is None:
        # Если записи нет, создаем ее
        insert_stmt = student_table.insert().values(
            user_id=existing_user_id,
            level='Intermediate',
            education_form='Full-Time',
            subject_id=1  # Замените на актуальный subject_id
        )
        session.execute(insert_stmt)
        session.commit()

    # Обновление уровня
    update_stmt = (
        student_table.update()
        .where(student_table.c.user_id == existing_user_id)
        .values(level=update_data['level'])
    )
    session.execute(update_stmt)
    session.commit()

    result = (
        session.query(student_table)
        .filter_by(user_id=existing_user_id)
        .first()
    )
    assert result.level == update_data['level']

    # Возврат к предыдущему состоянию
    rollback_data = {'level': 'Intermediate'}
    rollback_stmt = (
        student_table.update()
        .where(student_table.c.user_id == existing_user_id)
        .values(**rollback_data)
    )
    session.execute(rollback_stmt)
    session.commit()


# Тест на удаление учителя
def test_delete_teacher(session):
    teacher_table = Table(
        'teacher',
        MetaData(),
        Column('teacher_id', Integer, primary_key=True),
        Column('email', String),
        Column('group_id', Integer),
    )

    # Предполагаем, что запись уже существует
    delete_data = {"teacher_id": 29971}

    # Проверка, существует ли запись
    if session.query(teacher_table).filter_by(
         teacher_id=delete_data['teacher_id']).first() is None:
        # Если записи нет, создаем ее
        insert_stmt = teacher_table.insert().values(
            teacher_id=delete_data['teacher_id'],
            email='teacher@example.com',
            group_id=101
        )
        session.execute(insert_stmt)
        session.commit()

    # Удаление записи
    delete_stmt = teacher_table.delete().where(
        teacher_table.c.teacher_id == delete_data["teacher_id"]
    )
    session.execute(delete_stmt)
    session.commit()

    result = (
        session.query(teacher_table)
        .filter_by(teacher_id=delete_data['teacher_id'])
        .all()
    )
    assert len(result) == 0
