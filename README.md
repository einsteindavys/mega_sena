# mega_sena
Esse aqui é para ajudar você que fez bolão e tem que conferir muitos jogos, abasta seguir os passo indicados e ser feliz conferindo seus jogos, desde já boa sorte!


Observações para fazer funcionar o sistema:

para fazer funcionar, você precisará ter o arquivo em xlsx, e indicar o caminho na linha com o nome arquivo_excel = r'aqui você colocar onde você salvou o arquivo no seu computador, dar um exemplo simples, se ele estiver salvo na pasta de documentos: C:\Users\ nome do usuário \Documents\ nome do arquivo.xlsx

para fazer funcionar, você precisará também criar os jogos na planilha mantendo essa regra nos títulos das colunas, e nas linha:

Título das colunas --->Jogo	numero
título das linhas ---> Jogo 1	07 14 27 32 39 46
                       Jogo 2	12 29 35 49 53 55

o jogo 1 está em uma célula, e os número em outro célula, nessa célula onde estão os números eles devem ser separados por espaços e não vírgulas.


Local no código onde vocês devem fazer alterações citadas acima:

def main():
    # Lê os jogos realizados a partir de uma planilha Excel
    arquivo_excel = r"C:\Users\...\arquivo_com_seus_jogos.xlsx" #aqui você coloca o caminho da sua planilha do excel com os jogos, ver nota no "read me"
    coluna_numeros = 'Números'  # Substitua 'Números' pelo nome correto da sua coluna, ver nota no "read me"
    jogos = pd.read_excel(arquivo_excel)[coluna_numeros]
