print('Hello World!') # imprime/mostra a mensagem Hello World! no terminal/console

# Isso aqui é um comentário (Ah vá?!)
"""
    Também é um comentário mas
    pode colocar o texto em
    multiplas linhas

    Comentários servem somente para deixar
    mais claro para o programador o que aquela
    parte faz mas o Python irá ignorar
    
    Informação: É mais utilizado o hashtag # do que as três aspas dupla
"""



# VARIAVEIS: Guardam algum valor 'dentro' delas

# Alguns tipos de dados simples do Python
# Obs.: O ': tipo' que vem depois do nome da variável é opcional no Python
idade: int = 25
idade1 = 35 # é do mesmo tipo que o anterior
print(idade1)
ponto_flutuante: float = 3.1415
booleano: bool = False

# Alguns tipos de dados compostos do Python
nome: str = 'Fábio'
lista: list = [1, 'alguma coisa', True] # Os itens podem ser de qualquer tipo
lista2: list[int] = [1, 2, 3] # Os itens só podem ser do tipo entre [], neste caso inteiro
array: tuple = (1, 2, 3)
unico: set = {1, 2, 3, 3}
dicionario: dict = {'Nome': nome, 'Idade': idade}
print(dicionario)
