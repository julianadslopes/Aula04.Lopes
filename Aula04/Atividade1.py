import os

os.system ("cls")

# n = int(input("Número: "))

# if not (10 <= n <= 50):
#     print("Fora do Intervalo")
# else:
#     print("Dentro do Intervalo")    

###########################################################

resp = input("Informe F para Feminino ou M para Masculino: ").upper()

# if resp != "":
#     sexo = resp[0]
#     if sexo == "F":
#         print ("Feminino")
#     elif sexo == "M":
#         print ("Masculino")
#     else:
#         print ("Inválido")    
# else: 
#     print("Vazio")

####### OUTRA FORMA #######
if resp != "":
    sexo = resp[0]
    if sexo == "F" or sexo == "M":
        if sexo == "F"
            print ("Feminino")
        elif sexo == "M":
            print ("Masculino")
        else:
            print ("Inválido")    
else: 
    print("Vazio")

    
