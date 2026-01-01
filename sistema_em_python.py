import pandas as pd

def verifica_ganhadores(jogos, numeros_sorteados):
    ganhadores = {'6': [], '5': [], '4': [], '3': [], '2': []}
    for i, numeros_jogo in enumerate(jogos):
        if not pd.isna(numeros_jogo):
            # Substitui vírgulas, traços e espaços por espaço
            numeros_jogo = [int(numero) for numero in str(numeros_jogo).replace(',', ' ').replace('-', ' ').split()]
            acertos = set(numeros_jogo) & set(numeros_sorteados)
            if len(acertos) == 6:
                ganhadores['6'].append(i + 1)
            elif len(acertos) == 5:
                ganhadores['5'].append(i + 1)
            elif len(acertos) == 4:
                ganhadores['4'].append(i + 1)
            elif len(acertos) == 3:
                ganhadores['3'].append(i + 1)
            elif len(acertos) == 2:
                ganhadores['2'].append(i + 1)
    return ganhadores

def main():
    # Lê os jogos realizados a partir de uma planilha Excel
    arquivo_excel = r"C:\Users\NOMEDOARQUIVO.xlsx"  # coloque o caminho correto
    coluna_numeros = 'Números'  # aqui é o nome da primeira célula da coluna dos números, ou substitua pelo nome da coluna da sua planilha,
    jogos = pd.read_excel(arquivo_excel)[coluna_numeros]

    # Opção 1: Digitar o resultado do jogo manualmente no prompt (acho mais interessante usar esse)
    numeros_sorteados = input("Digite os números sorteados separados por espaço: ")
    numeros_sorteados = [int(num) for num in numeros_sorteados.replace(',', ' ').split()]

    # Opção 2: Fixar direto no script (descomente se preferir e comente para impedir o funcionamento da opção 1, mas eu preciso a opção 1),
    # numeros_sorteados = [6, 12, 23, 34, 45, 56]

    # Verifica ganhadores com base nos jogos informados na planilha
    ganhadores = verifica_ganhadores(jogos, numeros_sorteados)

    # Exibe resultados
    if ganhadores['6']:
        print("Parabéns! Você acertou as 6 dezenas nos seguintes jogos:", ganhadores['6'])
    elif ganhadores['5']:
        print("Você acertou 5 dezenas nos seguintes jogos:", ganhadores['5'])
    elif ganhadores['4']:
        print("Você acertou 4 dezenas nos seguintes jogos:", ganhadores['4'])
    elif ganhadores['3']:
        print("Você acertou 3 dezenas nos seguintes jogos:", ganhadores['3'])
    elif ganhadores['2']:
        print("Você acertou 2 dezenas nos seguintes jogos:", ganhadores['2'])
    else:
        print("Infelizmente, você não ganhou em nenhum jogo.")

if __name__ == "__main__":
    main()
