from switchcase import switch


#obtençao de valores(entrada)
print("Operadores")

print("+ - * / ")

print("Digite o caracter da operação")

sinal = input()

while(sinal!= '+' and sinal!='-' and sinal!='*' and sinal!="/"): #Validação de operador
    print("\n operador invalido digite novamente")
    print("+ - * /")
    sinal = input()

print("Digite o operando 1: ")
oper1 = float(input())
print("Digite o operando 2")
oper2 = float(input())

while (sinal == "/" and oper2 ==0): #Tentativa de divisao de zero
    print("Tentativa de divisao a zero")
    print("Digite o operando 2: ")
    oper2 = float(input())

#calculo da operação(Processamento)

resultado = 0.0 #Variavel que armazena o resultado calculado

if(sinal == '+ '):
    resultado = oper1 + oper2
elif(sinal =='-'):
    resultado = oper1 - oper2
elif (sinal == '*'):
    resultado = oper1 * oper2
elif (sinal == '/'):
    resultado = oper1 / oper2

#Exibiçao do resultado(saida)

print('\n' + str(oper1) + str(sinal) + str(oper2)+" = "+ str(resultado))