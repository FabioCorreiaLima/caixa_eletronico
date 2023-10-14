from banco import *
#cores utilizadas
#verde = \033[1;32m
#preto = \033[1;30m
#verde = \033[1;32m
#vermelho = \033[1;31m

while True:
    cabecalho('\033[1;32m<<<AGENCIA BANCARIA>>>\033[m')
    cabecalho('''\033[1;91m
[1] Incluir Pessoa
[2] Preechimento Ficha
[3] Reletorio
          \033[m''')
    opc = validar_int('\033[1;36mInforme uma opção: \033[m', '\033[1;31mDigite apenas números.\033[m')
    if opc == 2324:
        break
    elif opc == 1:
        system('cls')
        cabecalho('\033[1;32m<<< INCLUIR PESSOA >>>\033[1;32m')
        cadastrar_cliente()
        system('cls')
    elif opc == 2:
        system('cls')
        cabecalho('\033[1;32m<<< LANCAR FICHA >>>\033[m')
        lancar_ficha()
        system('cls')
    else:
        system('cls')
        cabecalho('\033[1;32m<<< RELATORIO >>>\033[m')
        relatorio_resumo()
        sleep(2)
        system('cls')
cabecalho('\033[1;32m<<< FINALIZADO >>>\033[m')