# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

def verificar_paridade(numero):
    if numero % 2 == 0:
        return f"O número{numero}é par: "
    else:
        return f"O numero {numero}é ímpar: "
resultado = verificar_paridade
print(resultado)
