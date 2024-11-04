import pytest
from sqlalchemy.orm import sessionmaker
from database import (
    create_tables,
    drop_tables,
    add_subject,
    update_student,
    delete_teacher,
    engine,
    subject_table,
    student_table,
    teacher_table,
)


# Фикстура для создания соединения с базой данных
@pytest.fixture
def connection():
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
def setup_database():
    create_tables()
    yield
    drop_tables()


# Тест на добавление нового предмета
def test_add_subject(session):
    add_subject(session, 16, 'Art')

    result = session.query(subject_table).filter_by(subject_id=16).first()
    assert result.subject_title == 'Art'

    # Удаление добавленного предмета
    delete_stmt = subject_table.delete().where(
        subject_table.c.subject_id == 16
    )
    session.execute(delete_stmt)
    session.commit()


# Тест на обновление студента
def test_update_student(session):
    existing_user_id = 11548
    if session.query(student_table).filter_by(
        user_id=existing_user_id
    ).first() is None:
        session.execute(student_table.insert().values(
            user_id=existing_user_id,
            level='Intermediate',
            education_form='Full-Time',
            subject_id=1
        ))
        session.commit()

    update_student(session, existing_user_id, 'Advanced')

    result = session.query(student_table).filter_by(
        user_id=existing_user_id
    ).first()
    assert result.level == 'Advanced'

    # Возврат к предыдущему состоянию
    update_student(session, existing_user_id, 'Intermediate')


# Тест на удаление учителя
def test_delete_teacher(session):
    teacher_id = 29971
    if session.query(teacher_table).filter_by(
        teacher_id=teacher_id
    ).first() is None:
        session.execute(teacher_table.insert().values(
            teacher_id=teacher_id,
            email='teacher@example.com',
            group_id=101
        ))
        session.commit()

    delete_teacher(session, teacher_id)

    result = session.query(teacher_table).filter_by(
        teacher_id=teacher_id
    ).all()
    assert len(result) == 0
