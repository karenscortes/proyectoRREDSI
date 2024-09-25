from sqlalchemy.orm import Session
from sqlalchemy import text

def get_areas_conocimiento(db: Session):
    sql = text("SELECT * FROM areas_conocimiento")
    result = db.execute(sql).fetchall()
    return result