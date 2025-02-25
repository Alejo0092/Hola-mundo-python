print ("Hola mundo")




#ejercicios


#1-ejercicio de INC
#Indice de Masa coprporal (INC)

print("Calculador de INC\n")

#Variables del problema

while ocurrio_error is True:
try:          
      peso = float(input("Ingrese su peso en kilogramos: "))
    
except ValueError:
    print("el valor ingresado no es valido")
    ocurrio_error= True
    continue 
    
    altura = float(input("Ingrese su altura en metros: "))
except ValueError:
    print("el valor ingresado no es valido")
    ocurrio_error= True

    indice = peso / (estatura**2)
  print(f"su indice de masa corporal es: {indice:.2f}")

              #Condiciones 
  if indice < 18.5:
    print("Usted tiene bajo peso")

  elif indice >=18.5 and indice > 25:
    print("Usted tiene un peso normal")

  elif indice >= 25 and indice < 30:
   print("Usted tiene sobrepeso") 

  elif indice >= 30:
   print("Usted tiene obesidad")
  else: 
    print("fin del programa")

          #variables
    peso = 0.0
    altura = 0.0
    ocurrio_error = True


#información
#peso bajo = < 18.5
#peso normal = 18.5 - 24.9
#sobrepeso = 25 - 29.9
#obesidad = > 30
