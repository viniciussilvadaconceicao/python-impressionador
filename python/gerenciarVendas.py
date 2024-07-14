def gerenciarVendas():
    meta = 130
    nao_bateu = []
    bateu = []
    print('-'*80)
    print('''
Primeiro quantos vendedores iram participar da bonificação
          
ATENÇÃO: SERÃO ACEITOS SOMENTE NÚMEROS INTEIROS SEM PONTO OU VÍRGULA
          ''')
    print('-'*80)
    cont = int(input('Quantos vendedores deseja cadastrar: '))
    print('\n')
    print('='*85)      
    print('''Bem vindo ao sistema de vendas.
Primeiro digite o nome do vendedor e confirme, logo após o programa irá perguntar 
o valor total de vendas desse vendedor.''')
    print('='*85) 
    print('\n')     
    for i in range(cont):
        funcionarios = dict()
        funcionarios['vendedor'] = str(input('Vendedor: ')).upper().strip()
        funcionarios['vendas']= float(input('Valor de vendas: '))
        print('\n')
        if funcionarios['vendas'] < meta:
            nao_bateu.append(funcionarios)
            
        elif funcionarios['vendas'] >= meta:
            bateu.append(funcionarios)
    print('\n')        
    print('='*44)
    print('NÃO BATERAM A META')  
    print('='*44)   
    for i in nao_bateu:
        print(f'{i["vendedor"]}')
    print('\n')
    print('='*44)
    print('Os vendedores que BATERAM A META!')  
    print('='*44)
    for i in bateu:
        print(f'{i["vendedor"]}')
    print('\n')

gerenciarVendas()