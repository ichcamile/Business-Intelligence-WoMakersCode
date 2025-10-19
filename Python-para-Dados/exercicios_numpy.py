import numpy as np

# Exercício 1: Criação de Arrays Aleatórios
print("\n") 
print("1. Crie um array com 4 linhas e 3 colunas com valores aleatórios.")
print() 
array_4x3 = np.random.rand(4, 3)
print("Array 4x3 com valores aleatórios:")
print(array_4x3)
print("--------------------------")

# Exercício 2: Array de Inteiros Aleatórios
print("\n")
print("2. Crie um array 3x5 com inteiros aleatórios entre 10 e 50.")
print()
array_inteiros = np.random.randint(10,51,size=(3,5))
print("Array 3x5 com inteiros aleatórios entre 10 e 50:")
print(array_inteiros)
print("--------------------------")
print("\n")

#Exericio 3: Array Preenchido com Zeros
print("3. Crie um array com 5 colunas e 10 linhas inicializados com zeros.")
print()
array_zeros = np.zeros((10,5))
print("Array 10x5 preenchido com zeros:")
print(array_zeros)
print("--------------------------")
print("\n")

#Exericio 4: Array de Sequência de Números
print("4. Crie um array que vá entre 0 e 90 pulando de 4 em 4.")
print()
array_sequencia = np.arange(0,91,4)
print("Array de 0 a 90 pulando de 4 em 4:")
print(array_sequencia)
print("--------------------------")
print("\n")

#Exericio 5: Redimensionamento de Array (Reshape)
print("5. Reduza o array (5,7) a apenas uma dimensão.")
