from app.jobs.scheduler import schedule_execution
import time

if __name__ == "__main__":
    print("[🔁] Agendador iniciado...")
    schedule_execution()

    # Mantém o processo vivo
    while True:
        time.sleep(60)
