# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento

import pandas as pd
import requests

df_ride = pd.read_csv("ncr_ride_bookings.csv")

# Questões:
# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 
status_completo = df_ride[df_ride['Booking Status'] == 'Completed']
len(status_completo)

# (0,5) 2 - Qual a proporção em relação ao total de corridas?
status_total = df_ride['Booking Status']
proporcao = len(status_total) / len(status_completo)
print(proporcao)

# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.
df_ride.groupby('Vehicle Type')['Ride Distance'].mean()

# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?
bike = df_ride[df_ride['Vehicle Type'] == 'Bike']
bike.groupby("Payment Method").size().idxmax()

# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?
status_completo['Booking Value'].sum()

# (0,5) 6 - E qual o ticket médio ("Booking Value")dessas corridas Completed?
status_completo['Booking Value'].mean()


# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“vendas - Brasil”).
# Dica: 
# Utilize a coluna FNTSIGLA para encontrar a serie da Fipe;
# Utilize a coluna SERNOME para encontrar as vendas de imoveis no Brasil;

url_ipea = "http://www.ipeadata.gov.br/api/odata4/Metadados"
response_ipea = requests.get(url_ipea)
response_ipea.status_code
dados_ipea = response_ipea.json()
dados_ipea = dados_ipea["value"]
df_ipea = pd.DataFrame(dados_ipea)

fipe = df_ipea['SERCODIGO'].str.contains('Fipe', case = False)
print(df_ipea.loc[fipe, ['SERCODIGO', 'FNTSIGLA', 'FNTNOME']])

imoveis = df_ipea['SERNOME'].str.contains('Imóveis', case = False)
print(df_ipea.loc[imoveis, ['SERNOME', 'FNTSIGLA', 'FNTNOME']])

# (1,5) 8 -  Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO=''
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame através da chave 'value' do retorno da api
# Selecione apenas as colunas datas (VALDATA) e os valores (VALVALOR).
# Exiba a Data e o Valor que teve o valor maximo de vendas.




# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
# response = requests.get(
#     f"{base_url}/preco/corrigido",
#     headers={"Authorization": f"Bearer {token}"},
#     params=params,
# )

url_vale = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTEzMTk1LCJpYXQiOjE3NzM5MjExOTUsImp0aSI6ImU2ZGFhM2U5ZGEzMzQzNzJiMzAwMTNmNzNkMTVkNzczIiwidXNlcl9pZCI6IjExMCJ9.aNw1HPkLXRviOgrZmrX7eCp6ZSBv0M-gLcQ6XT3nz2c"
params = {
    "ticker": "VALE3", 
    "data_ini": "2025-01-01", 
    "data_fim": "2025-12-31"
}
response_vale = requests.get(
     "https://laboratoriodefinancas.com/api/v2/preco/corrigido",
     headers = {"Authorization": "Bearer {eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTEzMTk1LCJpYXQiOjE3NzM5MjExOTUsImp0aSI6ImU2ZGFhM2U5ZGEzMzQzNzJiMzAwMTNmNzNkMTVkNzczIiwidXNlcl9pZCI6IjExMCJ9.aNw1HPkLXRviOgrZmrX7eCp6ZSBv0M-gLcQ6XT3nz2c}"},
     params = params
 )

response_vale.status_code
df_vale = pd.DataFrame(response_vale.json())
df_vale.dtypes
df_vale['abertura'] = df_vale['abertura'].astype(float)
df_vale['fechamento'] = df_vale['fechamento'].astype(float)
df_vale.dtypes
df_rentabilidade = df_vale['fechamento'].sum() - df_vale['abertura'].sum() 

# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
url_roe = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTEzMTk1LCJpYXQiOjE3NzM5MjExOTUsImp0aSI6ImU2ZGFhM2U5ZGEzMzQzNzJiMzAwMTNmNzNkMTVkNzczIiwidXNlcl9pZCI6IjExMCJ9.aNw1HPkLXRviOgrZmrX7eCp6ZSBv0M-gLcQ6XT3nz2c"
response_roe = requests.get(
     "https://laboratoriodefinancas.com/api/v2/bolsa/planilhao",
     headers = {"Authorization": "Bearer {eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTEzMTk1LCJpYXQiOjE3NzM5MjExOTUsImp0aSI6ImU2ZGFhM2U5ZGEzMzQzNzJiMzAwMTNmNzNkMTVkNzczIiwidXNlcl9pZCI6IjExMCJ9.aNw1HPkLXRviOgrZmrX7eCp6ZSBv0M-gLcQ6XT3nz2c}"},
     params = {"data_base": "2024-04-01"}
 )
response_roe.status_code
df_roe = pd.DataFrame(response_roe.json())
filtro_tec = df_roe['setor'] == 'tecnologia'
df_tec_roe = df_roe.loc[filtro_tec, ['ticker', 'setor', 'roe']]
df_tec_roe['roe'].idxmax()

# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )




# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?
