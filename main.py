# Codigo que que realzia as tarefas da atividade de Calculo Numérico
#Bibliotecas importadas:
import numpy as np

#---------------------------------Funções da Interpolação Polinomial---------------------------------
# Função de Interpolação Polinomial:
def interpolacao_polinomial(x, y):
    # Calculando os coeficientes do polinômio interpolador:
    coef_poli_inter = np.polyfit(x, y, 1)

    # Tratando erros, arredondando o coeficiente do polinômio interpolador:
    coef_poli_inter = np.round(coef_poli_inter, 5)

    # Criando o Polinômio Interpolador:
    #polinomio = np.poly1d(coef_poli_inter)

    return(coef_poli_inter)

# Função para aplicar o Polinômio Interpolador em novas entradas
def aplicar_inter_poli(array_poli, new_values):
    # Criando um array auxiliar
    aux_resultado = np.array([])

    for number in new_values:
        i = 0
        aux_poli = []
        while(i < len(array_poli)):
            aux_poli.append(number**(len(array_poli) - 1 - i) * (array_poli[i]))
            i = i + 1
        aux_resultado = np.append(aux_resultado, sum(aux_poli))
    return aux_resultado
            

#---------------------------------Funções para Calcular a Integral---------------------------------
# Função para Calcular a área do Trapezio:
def areaTrapezio(b, B, h):
    return ((B + b)*h/2)

# Função para gerar a lista de Áreas dos Trapézios
def gerarListaAreas(listX, listY):
    listAreas = [];
    i = 0;
    while(i < len(listX) - 1):
        listAreas.append(areaTrapezio(listY[i+1], listY[i], listX[i+1] - listX[i]))
        i += 1

    return listAreas

#---------------------------------Funções do Método da Bisseção---------------------------------

# Função que calcula o Coeficiente de Inclinação:
def coef_inclinacao(x, y, x2, xy):
    return (len(x) * sum(xy) - sum(x) * sum(y)) / (len(x) * sum(x2) - sum(x) * sum(x))
    
# Função que calcula o Intercepto:
def intercepto(x, y, CoefInc):
    return  (sum(y) / len(y)) - (sum(x) / len(x)) * CoefInc

#--------------------------------------MAIN--------------------------------------

# Declaração do X:
x = np.array([0,2,4,6,8,10])

 # Declaração do Y:
y = np.array([0,4,8,12,16,20])

# ---------- Interpolação Polinomial ----------
tempos_n_medidos = np.array([1,3,5,7,9,11])

print(f"Interpolação Polinolial: {interpolacao_polinomial(x, y)}")

print(f"Interpolação Polinolial Aplicada: {aplicar_inter_poli(interpolacao_polinomial(x, y), tempos_n_medidos)}")

# ---------- Integral ----------
print(f'\n')
lisAreas = gerarListaAreas(x, y)

# A integral é a soma da lista de Trapézios
print(f'Integral : {sum(lisAreas)}')


