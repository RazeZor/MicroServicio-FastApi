import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

USUARIO_BD = os.getenv("DB_USER")
CONTRASENA_BD = os.getenv("DB_PASSWORD")
SERVIDOR_BD = os.getenv("DB_HOST")
PUERTO_BD = os.getenv("DB_PORT")
NOMBRE_BD = os.getenv("DB_NAME")

CLAVE_SECRETA = os.getenv("SECRET_KEY")
MINUTOS_EXPIRACION_TOKEN = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

URL_BD = f"mysql+pymysql://{USUARIO_BD}:{CONTRASENA_BD}@{SERVIDOR_BD}:{PUERTO_BD}/{NOMBRE_BD}"

motor = create_engine(URL_BD, echo=True)
SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor)
