import pytest
from sqlalchemy.orm import sessionmaker
from database import (
    create_tables,
    drop_tables,
    add_subject,
    update_student,
    delete_teacher,
    engine,
    student_table,
    teacher_table,
    get_subject,
    delete_subject,
    get_student,
    get_teacher
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
    result = get_subject(session, 16)
    assert result.subject_title == 'Art'

    delete_subject(session, 16)
    result = get_subject(session, 16)
    assert result is None


# Тест на обновление студента
def test_update_student(session):
    existing_user_id = 11548
    if get_student(session, existing_user_id) is None:
        session.execute(student_table.insert().values(
            user_id=existing_user_id,
            level='Intermediate',
            education_form='Full-Time',
            subject_id=1
        ))
        session.commit()

    update_student(session, existing_user_id, 'Advanced')
    result = get_student(session, existing_user_id)
    assert result.level == 'Advanced'

    # Возврат к предыдущему состоянию
    update_student(session, existing_user_id, 'Intermediate')


# Тест на удаление учителя
def test_delete_teacher(session):
    teacher_id = 29971
    if not get_teacher(session, teacher_id):
        session.execute(teacher_table.insert().values(
            teacher_id=teacher_id,
            email='teacher@example.com',
            group_id=101
        ))
        session.commit()

    delete_teacher(session, teacher_id)
    result = get_teacher(session, teacher_id)
    assert len(result) == 0
