Implementacion con JWT  , AUTH , dependencias y docker, Para correr el programa
--> Docker compose , dockerfile Entre Otros

Documentación del Proyecto: Sistema de Gestión de Pacientes con FastAPI
Descripción General
Este es un sistema de gestión de pacientes desarrollado con FastAPI, 
un framework moderno de Python para construir APIs RESTful. El sistema permite gestionar información de pacientes y sus respectivos formularios médicos.

CrudPacientes/
├── 
├── Main.py                 # Punto de entrada de la aplicación
├── DB/                     # Configuración de la base de datos
│   └── conexion.py         # Configuración de la conexión a la base de datos
│   └── dependencias.py     # Dependencias de la base de datos
├── models/                 # Modelos de datos
│   └── modelos.py          # Definición de las entidades Paciente y Formulario
│   └── base.py             # Clase base para los modelos
├── RestController/         # Controladores de la API
│   └── RestCrudPacientes.py # Endpoints para gestión de pacientes
│   └── Cuestionario.py     # Endpoints para gestión de formularios
├── config/                 # Archivos de configuración
├── requirements.txt        # Dependencias del proyecto
├── dockerfile             # Configuración para Docker
└── docker-compose.yml     # Configuración para orquestación con Docker

Modelos de Datos
Paciente
rut (String, PK): Identificador único del paciente
nombre (String): Nombre del paciente
apellido (String): Apellido del paciente
edad (Integer): Edad del paciente
genero (String): Género del paciente
telefono (String): Número de teléfono
correo (String, único): Correo electrónico
direccion (String): Dirección del paciente
Formulario
id (Integer, PK): Identificador único del formulario
rut_paciente (String, FK): Referencia al paciente
respuesta1 (String): Primera respuesta del formulario
respuesta2 (String): Segunda respuesta del formulario
respuesta3 (String): Tercera respuesta del formulario
Endpoints Principales
Autenticación
GET /api/v1/pacientes/token - Genera un token de autenticación
Pacientes
GET /api/v1/pacientes/ - Lista todos los pacientes
POST /api/v1/pacientes/AgregarPaciente - Agrega un nuevo paciente
DELETE /api/v1/pacientes/eliminar/{rut_paciente} - Elimina un paciente por su RUT
Formularios
Los endpoints para formularios están definidos en Cuestionario.py
Configuración y Despliegue
Requisitos
Python 3.7+
PostgreSQL (u otra base de datos compatible con SQLAlchemy)
Docker (opcional, para despliegue en contenedores)
Instalación
Clonar el repositorio
Crear un entorno virtual: python -m venv .venv
Activar el entorno virtual:
Windows: .venv\Scripts\activate
Unix/MacOS: source .venv/bin/activate
Instalar dependencias: pip install -r requirements.txt
Configurar las variables de entorno en 
.env
Variables de Entorno
DATABASE_URL: URL de conexión a la base de datos
CLAVE_SECRETA: Clave secreta para JWT
MINUTOS_EXPIRACION_TOKEN: Tiempo de expiración del token
Ejecución
Modo desarrollo: python Main.py
Usando Uvicorn: uvicorn Main:app --reload
Docker
El proyecto incluye configuración para Docker:

docker-compose up para desplegar la aplicación con Docker
Seguridad
Autenticación basada en tokens JWT
CORS configurado (en desarrollo permite todos los orígenes)
Validación de datos en los endpoints
Documentación de la API
La documentación interactiva está disponible en:

/docs - Documentación Swagger UI
/redoc - Documentación ReDoc
Notas Adicionales
El proyecto sigue la arquitectura de capas (Modelo-Vista-Controlador)
Utiliza SQLAlchemy como ORM
Incluye manejo de errores y validación de datos
Configuración para desarrollo y producción
