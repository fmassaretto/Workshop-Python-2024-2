

def calculo():
    tipo_operacao:str = input('Digite qual operação deseja fazer: soma, subtrair, multiplicar ou dividir: ')
    x = int(input('Digite o valor x: '))
    y = int(input('Digite o valor y: '))

    '''
        Eu uso a funcao .lower() que vai deixar o que o usuario digitou ali em cima em minuscula,
        pois o usário pode escrever de diversas formas: Soma, SOMA, SoMa
    '''
    if(tipo_operacao.lower() == 'soma'):
        ... # no lugar do '...' coloque a chamada da função soma do calculadora.py
    elif(tipo_operacao.lower() == 'subtrair'):
        pass # no lugar do 'pass' coloque a chamada da função subtrair do calculadora.py
    elif(tipo_operacao.lower() == 'multiplicar'):
        ... # no lugar do '...' coloque a chamada da função multiplicar do calculadora.py
    elif(tipo_operacao.lower() == 'dividir'):
        pass # no lugar do 'pass' coloque a chamada da função dividir do calculadora.py
    else:
        print('Operação invalida! Digite uma operação valida soma, subtrair, multiplicar ou dividir!')

'''
    Obs.: Quando eu quero definir uma funcao, if/else, for, while etc mas ainda nao tenho certeza
    do que quero fazer dentro dele posso colocar o ... ou pass, assim a IDE não vai reclamar
    
    ex.:
    def funcao_que_depois_vou_implementar():
        pass
'''

def finalizou():
    print('Finalizando...')

'''
    nao é obrigatório esse if, mas é considerado uma boa prática de programação
    e poderia chamar a funcao calculo() diretamente
    
    o __name__ (atenção: sao dois underscore de cada lado!!) vai retornar '__main__'
    onde o codigo for executado, por exemplo: executando esse código, esse arquivo python é o '__main__'
    , se vc executar outro arquivo python (por exemplo: o calculadora.py) agora esse vai ser o '__main__'
'''
if __name__ == '__main__':                    
    calculo()                
    finalizou()
