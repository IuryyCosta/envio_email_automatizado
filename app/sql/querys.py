
GET_ERROS_ATENDIMENTO = """
    SELECT DISTINCT 
        COUNT(DS_ERRO) AS QT_ERROS,
        DS_ERRO 
    FROM TBL_INM_ATENDIMENTO 
    WHERE 
        TRUNC(DT_PROCESSADO) = TRUNC(SYSDATE - 1)
        AND DS_ERRO <> 'NULL'
    GROUP BY DS_ERRO
"""

GET_QUERY_MAIN =""" 
        SELECT 
            COUNT(tasy.nr_atendimento) AS total_legado,
            COUNT(api.nr_atendimento) AS total_api,
            COUNT(tasy.nr_atendimento) - COUNT(api.nr_atendimento) AS diferenca
        FROM (
            -- Total de atendimentos de alta por período no Tasy
            SELECT DISTINCT 
                ap.nr_atendimento
            FROM 
                atendimento_paciente_v ap,
                sus_laudo_paciente a
            WHERE 
                a.dt_cancelamento IS NULL
                AND cd_convenio IN (4, 39)
                AND cd_setor_atendimento IN (
                    105,  -- UTI - Unidade de Terapia Intensiva - HA
                    108,  -- Unidade de Internação Cirúrgica - HA
                    109,  -- Unidade de Internação Clínica - HA
                    320,  -- Unidade Internação Hematologia - HA
                    632,  -- Centro Cirúrgico Grande - HA
                    639,  -- Unidade Internação de Iodoterapia - HA
                    344   -- Unidade Internação TMO - HA  
                )
                AND ie_tipo_atendimento = 1
                AND cd_estabelecimento = 2
                AND TRUNC(dt_alta) = TRUNC(SYSDATE - 1) -- Alteração para pegar o dia anterior
                AND a.nr_atendimento(+) = ap.nr_atendimento
        ) tasy
        LEFT JOIN (
            -- Total de atendimentos na tabela tbl_inm_atendimento
            SELECT DISTINCT 
                nr_atendimento
            FROM 
                tbl_inm_atendimento
            WHERE
                tp_status <> 'A'
                AND nr_atendimento IN (
                    SELECT DISTINCT 
                        ap.nr_atendimento
                    FROM 
                        atendimento_paciente_v ap,
                        sus_laudo_paciente a
                    WHERE 
                        a.dt_cancelamento IS NULL
                        AND cd_convenio IN (4, 39)
                        AND cd_setor_atendimento IN (
                            105,  -- UTI - Unidade de Terapia Intensiva - HA
                            108,  -- Unidade de Internação Cirúrgica - HA
                            109,  -- Unidade de Internação Clínica - HA
                            320,  -- Unidade Internação Hematologia - HA
                            632,  -- Centro Cirúrgico Grande - HA
                            639,  -- Unidade Internação de Iodoterapia - HA
                            344   -- Unidade Internação TMO - HA  
                        )
                        AND ie_tipo_atendimento = 1
                        AND cd_estabelecimento = 2
                        AND TRUNC(dt_alta) = TRUNC(SYSDATE - 1) -- Alteração para pegar o dia anterior
                        AND a.nr_atendimento(+) = ap.nr_atendimento
                ) 
        ) api 
        ON tasy.nr_atendimento = api.nr_atendimento
 """


GET_QUERY_SUCESSOS_ERROS = """ 
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
                """