import threading
import datetime
import time
import os
from dotenv import load_dotenv
from app.services.email_report import enviar_email_com_relatorio
from app.utils.settings import EXECUTION_HOUR, EXECUTION_MINUTE

load_dotenv()

""" EXECUTION_HOUR = int(os.getenv("EXECUTION_HOUR", 8))
EXECUTION_MINUTE = int(os.getenv("EXECUTION_MINUTE", 0)) """

print(EXECUTION_HOUR, EXECUTION_MINUTE)
print(f"[🕒] Hora de execução programada para: {EXECUTION_HOUR:02d}:{EXECUTION_MINUTE:02d}")

def schedule_execution():
    def schedule_next():
        now = datetime.datetime.now()
        next_execution = now.replace(hour=EXECUTION_HOUR, minute=EXECUTION_MINUTE, second=0, microsecond=0)

        if now >= next_execution:
            next_execution += datetime.timedelta(days=1)

        delay = (next_execution - now).total_seconds()

        print(f"[⏰] Próxima execução agendada para: {next_execution.strftime('%Y-%m-%d %H:%M:%S')}")

        timer = threading.Timer(delay, execute_and_reschedule)
        timer.daemon = True
        timer.start()

    def execute_and_reschedule():
        print(f"[🚀] Executando relatório em: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        try:
            enviar_email_com_relatorio()
            print("[✅] Relatório enviado com sucesso.")
        except Exception as e:
            print(f"[❌] Erro durante envio de relatório: {e}")
        schedule_next()

    schedule_next()

