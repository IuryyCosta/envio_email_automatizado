from app.database.config import  get_connection
import pandas as pd
import os
import openpyxl


conn = get_connection()


class Query:
    def __init__(self):
        self.conn = get_connection()

    def execute_query(self, sql : str,  params=None):

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, params or ()) # execute the query with the given parameters
                colunas = [desc[0] for desc in cursor.description]
                dados = cursor.fetchall()
               
                if not dados:
                    return pd.DataFrame(columns=colunas)
                
                df=  pd.DataFrame(dados, columns=colunas)


                return df
            
        except Exception as e:
            print(f"❌ Erro ao executar a query: {e}")
            return None
        
    def transformar_df_para_excel(self, df: pd.DataFrame, nome_arquivo: str):
        try:
            # Criar caminho dinâmico
            base_dir = os.path.dirname(os.path.abspath(__file__))
            output_dir = os.path.join(base_dir, "output", "drgExcel")
            os.makedirs(output_dir, exist_ok=True)  # Criar pasta se não existir

            file_path = os.path.join(output_dir, nome_arquivo)
            df.to_excel(file_path, index=False , engine='openpyxl')

            print(f"✅ Arquivo salvo em: {file_path}")
        except Exception as e:
            print(f"❌ Erro ao gerar o arquivo Excel: {e}")
    
    def salvar_multiplos_df_excel(dfs : dict , nome_arquivo: str):
        try:
            # Criar caminho dinâmico
            base_dir = os.path.dirname(os.path.abspath(__file__))
            output_dir = os.path.join(base_dir, "output", "drgExcel")
            os.makedirs(output_dir, exist_ok=True)  # Criar pasta se não existir

            file_path = os.path.join(output_dir, nome_arquivo)
            
            with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                for sheet_name, df in dfs.items():
                    df.to_excel(writer, sheet_name=sheet_name, index=False)

            print(f"✅ Arquivo salvo em: {file_path}")
        except Exception as e:
            print(f"❌ Erro ao gerar o arquivo Excel: {e}")