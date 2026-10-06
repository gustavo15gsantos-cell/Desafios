# Na mesma linha dos exercicios anteriores crie uma função chamada pode_ver_filme que recebe a idade e a classificação indicativa do filme
# classificacao: 'L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'

#Exemplo:
# idade = 10
# classificacao = 'Maior de 12'
# resposta = "Não pode assitir o filme"

def pode_ver_filme(idade, classificacao):
    if classificacao == 'L':
        idade_minima = 0
    elif classificacao == 'Maior de 12':
        idade_minima = 12
    elif classificacao == 'Maior de 14':
        idade_minima = 14
    elif classificacao == 'Maior 16':
        idade_minima = 16
    elif classificacao == 'Maior 18':
        idade_minima = 18
    else:
        return "Classificação inválida"
    
    if idade >= idade_minima:
        resposta = "Pode assistir ao filme"
    else:
        resposta = "Não pode assitir o filme"
        
    print(resposta)
    return resposta

# Exemplo de uso:
pode_ver_filme(10, 'Maior de 12')