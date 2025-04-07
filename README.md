# 📬 Envio de E-mail Automatizado

Este projeto é uma aplicação em Python que agenda e envia e-mails automaticamente com um relatório diário em anexo. Ele pode ser executado como um serviço contínuo usando o PM2, garantindo que o processo esteja sempre ativo.

---

## 🧹 Funcionalidades

- Agendamento automático de envio de e-mails diários em horário configurado.
- Geração de relatório automatizado.
- Leitura de configurações via `.env`.
- Integração com serviços de e-mail.
- Suporte para execução contínua com PM2.

---

## ✨ Tecnologias utilizadas

- Python 3.11+
- FastAPI (opcional)
- APScheduler
- Uvicorn (opcional)
- Python-dotenv
- PM2 (para execução contínua)
- smtplib/email para envio de e-mails

---

## 📁 Estrutura do Projeto

```
envio_email_automatizado/
├── app/
│   ├── jobs/
│   │   └── scheduler.py
│   ├── routes/
│   │   └── email_router.py
│   ├── services/
│   │   └── email_report.py
│   └── utils/
│       └── helpers.py
├── __pycache__/
│   └── [arquivos de cache do Python]
├── .gitignore
├── README.md
├── debug.py
├── ecosystem.config.js
├── main.py
├── requirements.txt
└── teste.ipynb
```

---

## ⚙️ Configuração

1. **Clone o projeto**

```bash
git clone https://github.com/IuryyCosta/envio_email_automatizado.git
cd envio_email_automatizado
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**

```bash
python -m venv venv
venv\Scripts\activate   # No Windows
source venv/bin/activate  # No Linux/Mac
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Configure o arquivo `.env`**

Crie um arquivo `.env` na raiz com as seguintes variáveis:

```env
EXECUTION_HOUR=16
EXECUTION_MINUTE=30

EMAIL_HOST=smtp.seuprovedor.com
EMAIL_PORT=587
EMAIL_USERNAME=seu@email.com
EMAIL_PASSWORD=sua_senha
EMAIL_FROM=seu@email.com
EMAIL_TO=destinatario@email.com
```

---

## ▶️ Como rodar o projeto

### ✅ Rodando diretamente com Python

```bash
python main.py
```

O agendador será iniciado e continuará rodando indefinidamente, executando a tarefa no horário configurado.

### ♻️ Rodando com PM2 (recomendado para produção)

1. **Instale o PM2 (se ainda não tiver)**

```bash
npm install -g pm2
```

2. **Execute com PM2**

```bash
pm2 start ecosystem.config.js
```

3. **Comandos úteis do PM2**

```bash
pm2 logs envio-email        # Ver os logs
pm2 restart envio-email     # Reiniciar o processo
pm2 stop envio-email        # Parar o processo
pm2 delete envio-email      # Remover do PM2
```

---

## 🥪 Testando

Você pode testar localmente alterando o horário no `.env` para alguns minutos à frente e observando o log do terminal ou usando `pm2 logs`.

---

