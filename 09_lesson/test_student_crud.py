from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

db_url = URL.create(
    "postgresql+psycopg",  # для psycopg v3
    username="postgres",
    password="7548",
    host="localhost",
    port=5432,
    database="student",
)
db = create_engine(db_url, future=True)

def exec_(sql, **params):
    # короткий помощник, чтобы не повторяться
    with db.begin() as conn:      # открываем транзакцию
        return conn.execute(sql, params)

def test_add_student():
    exec_(text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
        ON CONFLICT (user_id) DO UPDATE
          SET level=EXCLUDED.level,
              education_form=EXCLUDED.education_form,
              subject_id=EXCLUDED.subject_id
    """), user_id=999999, level='Intermediate', education_form='group', subject_id=1)

    level = exec_(text("SELECT level FROM student WHERE user_id=:user_id"),
                  user_id=999999).scalar_one()
    assert level == 'Intermediate'

def test_update_student():
    exec_(text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
        ON CONFLICT (user_id) DO NOTHING
    """), user_id=999998, level='Beginner', education_form='personal', subject_id=2)

    exec_(text("UPDATE student SET level=:level WHERE user_id=:user_id"),
          user_id=999998, level='Advanced')

    level = exec_(text("SELECT level FROM student WHERE user_id=:user_id"),
                  user_id=999998).scalar_one()
    assert level == 'Advanced'

def test_soft_delete_student():
    exec_(text("""
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, 'Tmp', 'tmp', 0)
        ON CONFLICT (user_id) DO NOTHING
    """), user_id=999997)

    exec_(text("DELETE FROM student WHERE user_id=:user_id"), user_id=999997)

    row = exec_(text("SELECT 1 FROM student WHERE user_id=:user_id"),
                user_id=999997).fetchone()
    assert row is None