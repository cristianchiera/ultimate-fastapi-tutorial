from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

# Cambiamos la URI de conexión para PostgreSQL
SQLALCHEMY_DATABASE_URI = "postgresql://cchiera:Chiera+3@10.100.1.80:5432/remanofe"  # 1

# Creamos el motor de la base de datos
engine = create_engine(  # 2
    SQLALCHEMY_DATABASE_URI
    # No es necesario 'connect_args' para PostgreSQL
)

# Creamos la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # 4

def test_connection():
    try:
        # Creamos una sesión para probar la conexión
        with SessionLocal() as session:
            session.execute(text("SELECT 1"))  # Ejecuta una consulta de prueba
        print("Conexión exitosa.")
    except OperationalError as e:
        print("Error de conexión:", e)

#test_connection()