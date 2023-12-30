import pandas as pd

def verifica_ganhadores(jogos, numeros_sorteados):
    ganhadores = {'6': [], '5': [], '4': []}
    for i, numeros_jogo in enumerate(jogos):
        # Verifica se o valor é um número
        if not pd.isna(numeros_jogo):
            numeros_jogo = [int(numero.rstrip(',')) for numero in str(numeros_jogo).replace(',', ' ').split()]
            acertos = set(numeros_jogo) & set(numeros_sorteados)
            if len(acertos) == 6:
                ganhadores['6'].append(i + 1)
            elif len(acertos) == 5:
                ganhadores['5'].append(i + 1)
            elif len(acertos) == 4:
                ganhadores['4'].append(i + 1)
    return ganhadores

def main():
    # Lê os jogos realizados a partir de uma planilha Excel
    arquivo_excel = r"C:\Users\...\arquivo_com_seus_jogos.xlsx" #aqui você coloca o caminho da sua planilha do excel com os jogos, ver nota no "read me"
    coluna_numeros = 'Números'  # Substitua 'Números' pelo nome correto da sua coluna, ver nota no "read me"
    jogos = pd.read_excel(arquivo_excel)[coluna_numeros]

    # Números sorteados
    numeros_sorteados = input("Digite os números sorteados, separados por espaço: ").replace(',', ' ').split()
    numeros_sorteados = [int(numero.rstrip(',')) for numero in numeros_sorteados]

    # Verifica ganhadores
    ganhadores = verifica_ganhadores(jogos, numeros_sorteados)

    # Exibe resultados
    if ganhadores['6']:
        print("Parabéns! Você acertou as 6 dezenas nos seguintes jogos:", ganhadores['6'])
    elif ganhadores['5']:
        print("Você acertou 5 dezenas nos seguintes jogos:", ganhadores['5'])
    elif ganhadores['4']:
        print("Você acertou 4 dezenas nos seguintes jogos:", ganhadores['4'])
    else:
        print("Infelizmente, você não ganhou em nenhum jogo.")

if __name__ == "__main__":
    main()
