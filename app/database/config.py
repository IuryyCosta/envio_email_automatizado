import os
import oracledb
import time
from dotenv import load_dotenv

# 🔹 Carregar variáveis de ambiente
load_dotenv()

# 🔹 Definir credenciais
oracle_user = os.getenv("ORACLE_USER")
oracle_password = os.getenv("ORACLE_PASSWORD")
oracle_host = os.getenv("ORACLE_HOST")
oracle_port = os.getenv("ORACLE_PORT", "1521")  # Padrão 1521
oracle_service_name = os.getenv("ORACLE_SERVICE_NAME")

# 🔹 Construir a string DSN corretamente
oracle_dsn = f"{oracle_host}:{oracle_port}/{oracle_service_name}"

# 🔹 Inicializar Oracle Client (se necessário)
oracle_lib_dir = os.getenv("ORACLE_LIB_DIR", "C:\\oracle\\instantclient_23_6")
if os.path.exists(oracle_lib_dir):
    oracledb.init_oracle_client(lib_dir=oracle_lib_dir)

# 🔹 Testar conexão
def test_connection():
    try:
        with oracledb.connect(
            user=oracle_user,
            password=oracle_password,
            dsn=oracle_dsn
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT SYSDATE FROM DUAL")
                result = cursor.fetchone()
                print(f"✅ Conexão bem-sucedida! 📅 Data no banco: {result[0]}")
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"❌ Erro ao conectar: {error.code} - {error.message}")

def get_connection():
    try:
        connection = oracledb.connect(
            user=oracle_user,
            password=oracle_password,
            dsn=oracle_dsn
        )
        return connection
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"❌ Erro ao conectar: {error.code} - {error.message}")
        return None