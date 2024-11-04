from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Конфигурация базы данных
DB_URL = "postgresql://postgres:jn34b1r9@localhost:5432/QA"
engine = create_engine(DB_URL)

metadata = MetaData()

# Определение таблиц
subject_table = Table(
    'subject',
    metadata,
    Column('subject_id', Integer, primary_key=True),
    Column('subject_title', String),
)

student_table = Table(
    'student',
    metadata,
    Column('user_id', Integer, primary_key=True),
    Column('level', String),
    Column('education_form', String),
    Column('subject_id', Integer),
)

teacher_table = Table(
    'teacher',
    metadata,
    Column('teacher_id', Integer, primary_key=True),
    Column('email', String),
    Column('group_id', Integer),
)


def create_tables():
    metadata.create_all(engine)


def drop_tables():
    metadata.drop_all(engine)


def add_subject(session, subject_id, title):
    session.execute(subject_table.insert().values(
        subject_id=subject_id, subject_title=title
        ))
    session.commit()


def update_student(session, user_id, new_level):
    session.execute(
        student_table.update().where(
            student_table.c.user_id == user_id
            ).values(level=new_level)
    )
    session.commit()


def delete_teacher(session, teacher_id):
    session.execute(
        teacher_table.delete().where(teacher_table.c.teacher_id == teacher_id)
    )
    session.commit()
