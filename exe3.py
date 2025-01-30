DADOS DE ENTRADA 

{
    "faturamento_diario": [5000, 7000, 6000, 0, 8000, 0, 7500, 6500, 9000, 0, 8500, 7500, 7200, 7800, 6700, 6500, 0, 6000, 8000, 7500, 7000, 0, 8000, 7200, 7400, 6900, 6700, 8000, 7500]
}



import json

# Função para calcular os valores solicitados
def calcular_faturamento(dados_faturamento):
    dias_com_faturamento = [valor for valor in dados_faturamento if valor > 0]
    
    menor = min(dias_com_faturamento)
    maior = max(dias_com_faturamento)
    media = sum(dias_com_faturamento) / len(dias_com_faturamento)
    dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media)
    
    return menor, maior, dias_acima_media, media

# Carregar dados de faturamento do arquivo JSON
with open('faturamento.json', 'r') as arquivo:
    dados_faturamento = json.load(arquivo)['faturamento_diario']

# Calcular e exibir os resultados
menor, maior, dias_acima_media, media = calcular_faturamento(dados_faturamento)

print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
print(f"Média de faturamento: R${media:.2f}")
