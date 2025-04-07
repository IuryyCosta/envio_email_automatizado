import io
import pandas as pd
from app.sql.querys import (GET_ERROS_ATENDIMENTO , 
                            GET_QUERY_MAIN ,
                            GET_QUERY_SUCESSOS_ERROS)
from app.utils.redenrizar_email import TemplateEmail
from app.utils.consultar_query import Query
from app.core.send_emails import SendEmail



def enviar_email_com_relatorio():
    # 🔹 Gerar HTML do template
    template_email = TemplateEmail()
    query = Query()

    df_diferenca = query.execute_query(GET_QUERY_MAIN)
    df_sucesso_erro = query.execute_query(GET_QUERY_SUCESSOS_ERROS)
    df_erros = query.execute_query(GET_ERROS_ATENDIMENTO)

       # 🔍 Verificação de segurança
    if df_diferenca is None or df_sucesso_erro is None or df_erros is None:
        print("❌ Um ou mais DataFrames retornaram None. Verifique as queries.")
        return
    
    html_email = template_email.gerar_html_email(
        dados_erros=df_erros,
        dados_qtd=df_sucesso_erro,
        dados_diferenca=df_diferenca
    )

    # 🔹 Criar Excel em memória
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
        df_erros.to_excel(writer, index=False, sheet_name="Erros")
        df_sucesso_erro.to_excel(writer, index=False, sheet_name="Sucesso_vs_Erros")
        df_diferenca.to_excel(writer, index=False, sheet_name="Diferencas")

    excel_buffer.seek(0)
    arquivos = {
        "relatorio_integracao.xlsx": excel_buffer
    }

    # 🔹 Enviar o e-mail com sua classe
    email_sender = SendEmail()
    email_sender.assunto = "📊 Relatório de Integração - Atendimento"
    email_sender.destinatarios = [email_sender.email_to]  # ou outro(s)
    
    resultado = email_sender.enviar_email(mensagem=html_email, arquivos=arquivos)
    print(resultado)