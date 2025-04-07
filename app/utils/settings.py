import logging
import os
import json
import socket
from platform import system
from dotenv import load_dotenv, find_dotenv

# Carregar variáveis de ambiente
load_dotenv(find_dotenv())

# ////////////////////////////////////////////
# Configuração do sistema e rede
# ////////////////////////////////////////////
SYSTEM = system()
PID = os.getpid()
HOST_NAME = socket.gethostname()
IP_ADDRESS = socket.gethostbyname(HOST_NAME)

# ////////////////////////////////////////////
# Configuração de Logs
# ////////////////////////////////////////////
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = logging._nameToLevel.get(LOG_LEVEL, logging.INFO)

# ////////////////////////////////////////////
# Configuração do Banco de Dados Oracle
# ////////////////////////////////////////////
ORACLE_CONFIG = {
    "host": os.getenv("ORACLE_HOST"),
    "port": os.getenv("ORACLE_PORT", "1521"),
    "user": os.getenv("ORACLE_USER"),
    "password": os.getenv("ORACLE_PASSWORD"),
    "database": os.getenv("ORACLE_DATABASE"),
    "lib_dir": os.getenv("ORACLE_LIB_DIR"),
    "connect_string": os.getenv("ORACLE_CONNECT_STRING"),
}

DATABASE_URL = (
    f"oracle+oracledb://{ORACLE_CONFIG['user']}:{ORACLE_CONFIG['password']}@"
    f"{ORACLE_CONFIG['connect_string']}"
)

# ////////////////////////////////////////////
# Configuração de E-mail (Resend)
# ////////////////////////////////////////////
EMAIL_CONFIG = {
    "api_key": os.getenv("RESEND_API_KEY"),
    "email_from": os.getenv("EMAIL_FROM"),
    "email_to": os.getenv("EMAIL_TO"),
}

# ////////////////////////////////////////////
# Configuração de Agendamento
# ////////////////////////////////////////////
EXECUTION_HOUR = int(os.getenv("EXECUTION_HOUR", 0))
EXECUTION_MINUTE = int(os.getenv("EXECUTION_MINUTE", 0))

# ////////////////////////////////////////////
# Configurações Gerais
# ////////////////////////////////////////////
HEADLESS = os.getenv("HEADLESS", "False").lower() in ("true", "1", "t")
CAPTCHA_MANUAL = os.getenv("CAPTCHA_MANUAL", "False").lower() in ("true", "1", "t")
LOW_CPU_USAGE = os.getenv("LOW_CPU_USAGE", "False").lower() in ("true", "1", "t")

# ////////////////////////////////////////////
# USER_AGENT
# ////////////////////////////////////////////
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    if SYSTEM == "Windows"
    else "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
)

# ////////////////////////////////////////////
# Exibir configurações carregadas (opcional, para debug)
# ////////////////////////////////////////////
if __name__ == "__main__":
    print("✅ Configurações carregadas com sucesso!")
    print("📌 Sistema Operacional:", SYSTEM)
    print("📌 IP da Máquina:", IP_ADDRESS)
    print("📌 Banco de Dados Oracle:", json.dumps(ORACLE_CONFIG, indent=2))
    print("📌 Configuração de E-mail:", json.dumps(EMAIL_CONFIG, indent=2))
    print("📌 Execução Agendada:", f"{EXECUTION_HOUR}:{EXECUTION_MINUTE}")
