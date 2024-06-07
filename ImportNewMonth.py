import pandas as pd

# Carregar a planilha do mês 04
mes_04_df = pd.read_excel(r'C:\Programacao\Analise de dados\Python analise salarios\PagamentosMaio.xlsx')

# Carregar a planilha do mês 05
mes_05_df = pd.read_excel(r'C:\Programacao\Analise de dados\Python analise salarios\HISTORICOPAGAMENTOS.xlsx')

# Iterar sobre as linhas da planilha do mês 05
for index, row in mes_05_df.iterrows():
    # Extrair o nome do empregado
    nome_empregado = row['Nome Empregado']

    # Verificar se o nome já existe na planilha do mês 04
    if nome_empregado in mes_04_df['Nome Empregado'].values:
        # Obter o índice das linhas onde o nome do empregado aparece
        indices = mes_04_df[mes_04_df['Nome Empregado'] == nome_empregado].index.tolist()

        # Inserir a nova linha logo abaixo da última ocorrência do nome
        mes_04_df = pd.concat(
            [mes_04_df.iloc[:indices[-1] + 1], pd.DataFrame([row]), mes_04_df.iloc[indices[-1] + 1:]]
        ).reset_index(drop=True)
    else:
        # Adicionar a nova linha ao final da planilha
        mes_04_df = pd.concat([mes_04_df, pd.DataFrame([row])], ignore_index=True)

# Ordenar o DataFrame pela coluna 'Nome Empregado' e 'Data' para manter a ordem correta
mes_04_df['Data'] = pd.to_datetime(mes_04_df['Data'])
mes_04_df = mes_04_df.sort_values(by=['Nome Empregado', 'Data']).reset_index(drop=True)

# Configurar a Data para permanecer como Data abreviada
mes_04_df['Data'] = mes_04_df['Data'].dt.strftime('%d/%m/%Y')

# Salvar a nova planilha do mês 04
mes_04_df.to_excel(
    r'C:\Programacao\Analise de dados\Python analise salarios\PAGAMENTOSATUALIZADOS.xlsx',
    index=False
)