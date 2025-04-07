from app.services.email_report import enviar_email_com_relatorio

class EmailController:

    @staticmethod
    def enviar_email_com_relatorio():
        """
            Dispara o envio do relatório por email Manualmente 
            pode ser usado por uma rota de integração externa ou por um job
            de agendamento. 
          """
        try:
            resultado = enviar_email_com_relatorio()
            return {"message": "Email enviado com sucesso", "resultado": resultado}
        except Exception as e:
            return {"Status": "Erro", "message": str(e)}