# mega_sena Ver. 2.0
Verificador de Ganhadores de Loteria

Este projeto tem como objetivo verificar automaticamente quais jogos realizados em uma planilha Excel acertaram os números sorteados em um concurso de loteria.  

# Funcionalidades
- Lê os jogos realizados a partir de uma planilha Excel, (ainda vou fazer um sistema de reconheciento dos jogos para gerar o aquivo automático de leitura e criação da planilha, ou seja, ainda precisa fazer o levantamento manual das informações).
- Permite inserir os números sorteados manualmente via prompt.
- Verifica os acertos de cada jogo e classifica os ganhadores conforme a quantidade de dezenas corretas (6, 5, 4, 3 ou 2).
- Exibe mensagens personalizadas para cada nível de acerto.

# Como usar
1. Instale as dependências necessárias:
  
   pip install pandas
  
2. Configure o caminho do arquivo Excel no código:
   
   arquivo_excel = r"C:\Users\NOMEDOARQUIVO.xlsx" ---> Substitua pelo caminho correto da sua planilha.

3. Certifique-se de que a planilha contenha uma coluna chamada "Números" (ou ajuste o nome da coluna no código).

4. Execute o script:
   
   python nome_do_arquivo.py

# Exemplo de saída
- Caso um jogo acerte 6 dezenas:
  
  Parabéns! Você acertou as 6 dezenas nos seguintes jogos: [1, 5]
  
- Caso acerte menos:
  
  Você acertou 4 dezenas nos seguintes jogos: [2, 7, 9]
  
- Se não houver ganhadores:
  
  Infelizmente, você não ganhou em nenhum jogo.
