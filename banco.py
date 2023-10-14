import mysql.connector
from mysql.connector import Error
from datetime import datetime as dt
from random import randint
from time import sleep
from os import system



#validando inteiro
def validar_int(msg,msg1):
    while True:
        try:
            v = int(input(f'{msg}'))
            if v < 4 and v > 0 or v == 2324:
                return v
            else:
                print('\033[0;31mIforme apenas os números de 1 a 3.\033[m')
                
        except:
            print(f'{msg1}')

# validando sexo
def validar_sexo(s):
    while True:
        s = input(f'{s}').strip().upper()
        if s.isalpha():
            if s == 'F' or s == 'M':
                return s
            else:
                print('\033[0;31mInforme F - FEMININO ou M - MASCULINO.\033[m')
        else:
            print('\033[0;31mInforme apenas letras.\033[m')

#verificando se o nome é só letra
def is_alpha_space(str):
    return all(char.isalpha() or char.isspace() for char in str)

#validar nome
def validar_nome(n):
    while True:
        s1 = input(f'{n}').upper()

        if not (is_alpha_space(s1) and len(s1) >4):
            print('\033[0;31mValores inválidos ou nome curto demais.\033[m')
        else:
            return s1

        
#pegando o tipo de oparacao
def tipo_operacao(p):
    while True:
        print('''\033[1;91m
[0] Deposito
[1] Retirada
            \033[m''')
        try:
            res = int(input(f'{p}'))
            if res == 0:
                res = 'DEPOSITO'
                return res
            elif res == 1:
                res = 'RETIRADA'
                return res
            else:
                print('\033[0;31mDigite apenas 0 ou 1.\033[m')
        except:
            print('\033[0;31mInforme apenas números.\033[m')

#validando data
def data(d):
    while True:
        try:
            #Pegando data digitada em mode String
            nascimento = input(f'{d}').strip()
            #Convertendo a String para data
            nascimento = dt.strptime(nascimento,'%Y/%m/%d')
            return nascimento
        except:
            print('\033[0;31mInforme a data no formato ano, mes, dia.\033[m')

# verificando se é cliente ou nao.
def verficar_se_e_cliente(v):
   while True:
        print('''\033[1;91m
[0] Sim
[1] Não
            \033[m''')
        try:
            res = int(input(f'{v}'))
            if res == 0:
                res = 'SIM'
                return res
            elif res == 1:
                res = 'NAO'
                return res
            else:
                print('\033[0;31mDigite apenas 0 ou 1.\033[m')
        except:
            print('\033[0;31mInforme apenas números.\033[m')
 
#cabeçalho
def cabecalho(txt):
    print('\033[1;90m=\033[m'*45)
    print(txt.center(45))
    print('\033[1;90m=\033[m'*45)
    
#inclusao de pessoas
def cadastrar_cliente():
    nome_cliente = validar_nome('\033[1;36mInforme o nome: \033[m')
    try:
        #chamando o banco de dados
        conexao = mysql.connector.connect(host = 'localhost', 
                                user = 'root',
                                password = '96204684',
                                database ='agencia_bancaria')
        cursor = conexao.cursor()
        
        #Inserindo novo cliente no banco de dados
        comando = f'INSERT INTO  nome_cliente (NOME_CLIENTE) VALUES ("{nome_cliente}")'
        cursor.execute(comando)
        #salvando dados no banco
        conexao.commit()
        
        print('\033[1;32mRegistros inseridos na tabela.\033[m')
        sleep(2)
        system('cls')
        
    except Error:
        print('\033[0;31mFalha ao inserir dados no MySQL.\033[m')
        
#cadastro das fichas
def lancar_ficha():
    #Pegando Nome Cliente
    nome_cliente = validar_nome('\033[1;36mInforme o nome: \033[m')
    #Pegando Sexo do Cliente
    sexo = validar_sexo('\033[1;36mInforme sexo [F/M] :\033[m')
    #Pegando a data de nascimento
    data_nascimento = data('\033[1;36mInforme a data no formato a/m/d: \033[m')
    #Pegando a operação a ser realizada
    operacao = tipo_operacao('\033[1;36mInforme a operação: \033[m')
    #Pegando qual caixa esta atendendo
    caixa = randint(1, 11)
    # Verificando se é cliente
    cliente = verficar_se_e_cliente('\033[1;36mÉ cliente? [sim ou nao] :\033[m')
    #Abrir Conexao
    try:
        conexao = mysql.connector.connect(host = 'localhost', 
                                    user = 'root',
                                    password = '96204684',
                                    database ='agencia_bancaria')
        cursor = conexao.cursor()
        #Pegar ID do nome do cliente
        comando = (f' SELECT * FROM nome_cliente WHERE NOME_CLIENTE = "{nome_cliente}" ')
        cursor.execute(comando)
        rs = cursor.fetchall()
    except Error:
        print('\033[1;31mTeve um erro ao fazer a conexão com o banco de dados\033[m')
        
    #Verifica se o Cliente ja está Cadastrado
    if len(rs) == 0:
        return print('\033[1;31mNome de usuario não cadastrado!\033[m')
        sleep(1)
    else:
        ID = rs[0][0]
    #Salvar fixa do cliente
    try:
        comando = (''' INSERT INTO cadastro_ficha(ID,CAIXA, NOME_CLIENTE, SEXO_CLIENTE, DATA_NASCIMENTO, OPERACAO_CLIENTE, CLIENTE) VALUES('%s','%s','%s','%s','%s','%s','%s') ''' % (ID,
                                                                                caixa,
                                                                                nome_cliente,
                                                                                sexo,
                                                                                data_nascimento,
                                                                                operacao,
                                                                                cliente
                              ))
        cursor.execute(comando)
        conexao.commit()
        sleep(1)
        cabecalho('\033[1;32mFicha realizada com sucesso.\033[m')
        system('cls')
    except Error:
        print('\033[1;31mNão foi possivel salvar os dados.\033[m')

#relatorio das fichas
def relatorio_resumo():
        try:   
            #abrindo a conexão com o banco de dados
            conexao = mysql.connector.connect(host = 'localhost', 
                                        user = 'root',
                                        password = '96204684',
                                        database ='agencia_bancaria')
            cursor = conexao.cursor()
            #Quantidade atendida total
            comando = (''' SELECT COUNT(CAIXA) FROM cadastro_ficha ''')
            cursor.execute(comando)
            rs = cursor.fetchall() # recebe o valor de retorno
            cabecalho('\033[1;32m<<< QUANTIDADE DE PESSOAS ATEMDIDAS >>>\033[1;32m')
            print('Foram atendido no total: ',str(rs[0][0]),' Pessoas')
            sleep(2)
        except Error:
            print('Erro')
            
        try:    
            #Caixa com mais atendimento
            comando = (''' SELECT MAX(CAIXA), MAX(CONTAGEM) FROM(SELECT CAIXA, COUNT(CAIXA) AS CONTAGEM FROM cadastro_ficha GROUP BY (CAIXA)) AS DB ''')
            cursor.execute(comando)
            rs = cursor.fetchall()
            cabecalho('\033[1;32m<<< CAIXA COM MAIOR ATENDIMENTO >>>\033[m')
            for c in rs:
                print(f'CAIXA :{c[0]} com {c[1]}')
        except:
            print('error')
        sleep(2)
        
        #Buscando Cliente Fenino
        comando = (''' SELECT  CAIXA, NOME_CLIENTE, SEXO_CLIENTE FROM cadastro_ficha1 WHERE SEXO_CLIENTE = 'F' ''')
        cursor.execute(comando)
        rs = cursor.fetchall()
        
        #Montado Tabela
        cabecalho('\033[1;32m<<< MULHERES QUE RECEBERAM ATENDIMENTO >>>\033[m')
        print(f'{"Caixa"}\t|{" Cliente"}\t|{" Sexo"}')
        for x in rs:
            print(f'{str(x[0]):<3}     | {str(x[1]):>8}      | {str(x[2]):>3}')
        sleep(2)
        
        #Buscando Operacao por cliente
        comando = (''' SELECT CAIXA, NOME_CLIENTE, OPERACAO_CLIENTE FROM cadastro_ficha WHERE OPERACAO_CLIENTE = 'DEPOSITO' ''')
        cursor.execute(comando)
        rs = cursor.fetchall()
        #Montado Tabela
        cabecalho('\033[1;32m<<< CLIENTES QUE REALIZARAM DEPOSITO >>>\033[m')
        print(f'{"Caixa"}\t|{" Cliente"}\t|{" Operação"}')
        if rs[0][2] == 'DEPOSITO':
            for r in rs:
                print(f'{str(r[0]):<3}     | {str(r[1]):>8}      | {str(r[2]):>10}')
        else:
            print('\033[1;31mNão tem registro de deposito\033[m')  
        sleep(2)
        
        while True:
            try:
                resposta = int(input('\n\033[1;36mDite 0 para voltar ao menu: \033[m'))
                if resposta == 0:
                    return resposta
                else:
                    print('\033[1;31mValor invalido. Informe 0 para sair.\033[m')
                    continue
            except:
                print('\033[1;31mDigite apenas 0.\033[m')
            


