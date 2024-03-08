# # 1) Resultado do código abaixo:
# indice = 13
# k = soma = 0
# while k < indice:
#     k += 1
#     soma += k

# print(soma)
# # Resultado = 91


# # 2) Informe se um número faz parte da sequência de Fibonacci
# def fibonacci(n):
#     sequencia = [0, 1]
#     ult_numero = sequencia[-1] + sequencia[-2]
#     while ult_numero <= n:
#         ult_numero = sequencia[-1] + sequencia[-2]
#         sequencia.append(ult_numero)
#     print(sequencia)
#     return f"O numero {n} esta na sequencia" if n in sequencia else f"O numero {n} nao pertence a sequencia"

# n = 34
# result = fibonacci(n)
# print(result)


# 3) Descubra a lógica e complete a sequência
# a) numeros ímpares: 9
# b) potências de 2: 128
# c) quadrado dos números naturais: 49
# d) quadrado dos números pares: 100
# e) sequência de fibonacci: 13
# f) números que começam com D: 200


# 4) Entendendo que cada lâmpada está em uma sala diferente e considerando que todas as lâmpadas estão inicialmente apagadas:
# Primeiro, ligaria um dos interruptores e deixaria ligado por alguns minutos, 
# em seguida desligaria ele e acenderia outro e então olharia as salas, gerando os casos:

# * Na primeira ida a uma sala e tem uma lâmpada acesa:
# - quem a controla é o interruptor que deixei ligado
# - logo, na segunda ida a uma sala, a lâmpada estará apagada, então verificaria se a 
# temperatura dela está quente, se sim, quem a controla é o interruptor que liguei por uns instantes e depois desliguei; 
# mas caso a temperatura esteja fria, o seu interruptor é o que eu não mexi

# * Na primeira ida a uma sala e tem uma lâmpada apagada:
# - iria conferir a temperatura da lâmpada e caso esteja quente, quem controla é o interruptor que deixei ligado por alguns instantes,
# mas caso esteja fria, quem controla é o interruptor que não mexi
# - na segunda ida à sala, caso tenha uma lâmpada acesa, é a do interruptor que deixei ligado, 
# mas caso ainda esteja apagada, por eliminação da verificação anterior, dá pra saber as restantes


# 5) Inverta a ordem de uma string
def inverte_string(str):
    print(str[::-1])

inverte_string('matheus')
