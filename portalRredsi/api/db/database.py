from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from core.config import settings

# Crear el motor de base de datos
engine = create_engine(settings.DATABASE_URL, echo=True, pool_pre_ping=True)
# Crear la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        # Deshabilitar el modo seguro
        db.execute("SET SQL_SAFE_UPDATES = 0")
        yield db
    finally:
        # Habilitar el modo seguro si es necesario
        db.execute("SET SQL_SAFE_UPDATES = 1")
        db.close()

# solo para prueba
# Función para probar la conexión a la base de datos
def test_db_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Conexión exitosa a la base de datos")
    except Exception as e:
        print("Error al conectar a la base de datos:", e)