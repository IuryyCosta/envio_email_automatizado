from app.database.config import test_connection , get_connection

def main():
    # Testar a conexão com o banco de dados Oracle
    #test_connection()
    conn = get_connection()
    try:
        # Executar uma query SQL
        with conn.cursor() as query:
            query.execute(""" 
                 SELECT 
                    S.SUCESSO,
                    E.ERROS
                FROM 
                    (SELECT DISTINCT 
                            COUNT(TP_STATUS) SUCESSO,
                            TP_STATUS    
                        FROM 
                            TBL_INM_ATENDIMENTO 
                        WHERE 
                                TRUNC(TO_DATE(DT_ALTA, 'YYYY-MM-DD"T"HH24:MI:SS')) = TRUNC(SYSDATE - 1)
                                AND TP_STATUS IN ('T')
                        GROUP BY  TP_STATUS) S,
                    (SELECT DISTINCT 
                        COUNT(TP_STATUS)ERROS,
                        TP_STATUS    
                    FROM 
                        TBL_INM_ATENDIMENTO 
                    WHERE 
                            TRUNC(TO_DATE(DT_ALTA, 'YYYY-MM-DD"T"HH24:MI:SS')) = TRUNC(SYSDATE - 1)
                            AND TP_STATUS IN ('E')
                    GROUP BY  TP_STATUS) E
            WHERE 1=1
                """)
             # Buscar todos os resultados
            result = query.fetchall()

             # Formatar os resultados no mesmo formato do JavaScript
            tratamento = [
                {"Erros": row[1], "SUcessos": row[0]} for row in result
            ]
            print("Tratamento:", tratamento)
            
    except Exception as e:
        print(f"❌ Erro ao executar a query: {e}")

if __name__ == "__main__":
    main()