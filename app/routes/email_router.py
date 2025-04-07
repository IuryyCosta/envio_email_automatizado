
from fastapi import APIRouter
from app.controllers.email_controller import EmailController

router = APIRouter()

@router.get("/enviar-email-relatorio")
def enviar_relatorio_manual():
    """
        Rota para enviar o relatório por email manualmente.
        Pode ser usado por uma rota de integração externa ou por um job de agendamento.
    """
    return EmailController.enviar_email_com_relatorio()
