import resend
import os
from dotenv import load_dotenv
import io
import logging
import base64

# 🔹 Carregar variáveis de ambiente
load_dotenv()

# 🔹 Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class SendEmail:
    def __init__(self):
        """Inicializa a classe com as configurações de e-mail"""
        self.email_from = os.getenv("EMAIL_FROM")
        self.email_to = os.getenv("EMAIL_TO")
        self.resend_api_key = os.getenv("RESEND_API_KEY")

        # 🔹 Inicializar o Resend com a API Key
        resend.api_key = self.resend_api_key

        # 🔹 Variáveis da classe
        self.assunto = ""
        self.destinatarios = []
        self.copia = []
        self.copia_oculta = []

    def carregar_mensagem(self, mensagem):
        """Monta a mensagem HTML do e-mail"""
        return f"""
        <html>
            <body>
                {mensagem}
            </body>
        </html>
        """

    def anexar_arquivos(self, arquivos):
        """
        Converte arquivos para o formato adequado para o Resend.

        Args:
            arquivos (dict): {"nome_arquivo.pdf": io.BytesIO}

        Returns:
            list: Lista de anexos formatados corretamente
        """
        anexos = []
        if arquivos:
            for nome, conteudo in arquivos.items():
                anexos.append(
                    {
                        "filename": nome,
                        "content": base64.b64encode(conteudo.getvalue()).decode("utf-8")  # ✅ Corrige binários
                    }
                )
                logger.info(f"Anexo adicionado: {nome}")
        return anexos

    def enviar_email(self, mensagem, arquivos=None, imagens=None):
        """
        Envia um e-mail via Resend.

        Args:
            mensagem (str): Corpo do e-mail em HTML.
            arquivos (dict, optional): {"nome_arquivo.pdf": io.BytesIO}.
            imagens (dict, optional): {"logo.png": io.BytesIO}.
        """
        try:
            email_body = self.carregar_mensagem(mensagem)
            attachments = self.anexar_arquivos(arquivos)

            response = resend.Emails.send(
                {
                    "from": self.email_from,
                    "to": self.destinatarios if self.destinatarios else [self.email_to],
                    "cc": self.copia if self.copia else None,
                    "bcc": self.copia_oculta if self.copia_oculta else None,
                    "subject": self.assunto,
                    "html": email_body,
                    "attachments": attachments if attachments else None,
                }
            )

            if response.get("error"):
                raise Exception(response["error"]["message"])

            logger.info(f"E-mail enviado com sucesso para {self.destinatarios + self.copia}!")
            return {"message": "Email sent successfully"}

        except Exception as e:
            logger.error(f"Erro ao enviar e-mail: {e}")
            return {"error": str(e)}

# ✅ Testando envio de e-mail
if __name__ == "__main__":
    email_controller = SendEmail()
    email_controller.assunto = "Atendimento Paciente - Relatório de Erros"
    email_controller.destinatarios = [os.getenv("EMAIL_TO")]

    # Simulando um anexo (arquivo em memória)
    fake_file = io.BytesIO("Este é um arquivo de teste.".encode("utf-8"))
    arquivos = {"relatorio.pdf": fake_file}

    try:
        result = email_controller.enviar_email("<h1>Teste de E-mail</h1><p>Este é um teste</p>", arquivos)
        print(result)
    except Exception as e:
        print(e)
