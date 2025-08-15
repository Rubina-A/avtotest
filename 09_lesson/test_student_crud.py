import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

db_url = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password="7548",
    host="localhost",
    port=5432,
    database="student",
)
db = create_engine(db_url, future=True)


def test_add_student():
    sql = text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
    """)
    db.execute(sql, user_id=999999, level='Intermediate', education_form='group', subject_id=1)

    check_sql = text("SELECT * FROM student WHERE user_id = :user_id")
    result = db.execute(check_sql, user_id=999999).fetchone()
    assert result is not None
    assert result.level == 'Intermediate'


def test_update_student():
    # Добавим тестовую запись
    insert_sql = text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
    """)
    db.execute(insert_sql, user_id=999998, level='Beginner', education_form='personal', subject_id=2)

    # Обновим уровень
    update_sql = text("UPDATE student SET level = :level WHERE user_id = :user_id")
    db.execute(update_sql, level='Advanced', user_id=999998)

    # Проверим
    check_sql = text("SELECT level FROM student WHERE user_id = :user_id")
    updated = db.execute(check_sql, user_id=999998).fetchone()
    assert updated.level == 'Advanced'


def test_soft_delete_student():
    # Добавим тестовую запись
    insert_sql = text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
    """)
    db.execute(insert_sql, user_id=999997, level='Advanced', education_form='group', subject_id=3)

    # Soft delete — просто меняем education_form на 'deleted'
    delete_sql = text("UPDATE student SET education_form = 'deleted' WHERE user_id = :user_id")
    db.execute(delete_sql, user_id=999997)

    # Проверим
    check_sql = text("SELECT education_form FROM student WHERE user_id = :user_id")
    deleted = db.execute(check_sql, user_id=999997).fetchone()
    assert deleted.education_form == 'deleted'
