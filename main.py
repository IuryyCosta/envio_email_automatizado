from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv
from app.routes.email_router import router as email_router
from app.jobs.scheduler import schedule_execution


# 🔹 Carrega variáveis do .env
load_dotenv()

# 🔹 Instância da aplicação
app = FastAPI(title="📬 Envio Automático de E-mail")

# 🔹 CORS Middleware (se for exposto em rede ou necessário para consumo externo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajuste isso conforme a necessidade
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Incluir rotas
app.include_router(email_router, prefix="/email", tags=["Relatório"])

# 🔁 Iniciar agendamento automático ao subir a API
schedule_execution()

# 🔹 Execução com Uvicorn (apenas quando não usado com PM2)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 3000)), reload=True)