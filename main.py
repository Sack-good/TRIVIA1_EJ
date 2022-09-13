BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import time

import random

iniciar_trivia = True
intentos = 0

puntaje = random.randint(0, 10)
print(BLUE + "Bienvenido a mi trivia sobre la FPF")
print("Pondremos a prueba tus conocimientos")
print("Tienes", puntaje, "puntos")
nombre = input("Ingresa tu nombre:")
print("Me gusta tu nombre", nombre)
while iniciar_trivia == True:
 intentos += 1
 
  
 print("\nIntento número:", intentos)
 print("Danos 2 segundos por favor")
 time.sleep(2)
  #PREGUNTA1
 print(YELLOW + "1) ¿En que año fue su primer mundial de peru?")
 print("a)1928")
 print("b)1932")
 print("c)1940")
 print("d)1930")

 respuesta1 = input("\ntu respuesta:")

 while respuesta1 not in ("a", "b", "c", "d"):
    respuesta1 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

 if respuesta1 == "a":
    print(RED + "es incorrecto!", nombre, " no fue en el 1928" + RESET)
 elif respuesta1 == "b":
    print(RED + "es incorrecto!", nombre, " no fue en el 1932" + RESET)
 elif respuesta1 == "c":
    print(RED + "es incorrecto!", nombre, " no fue en el 1940" + RESET)

 else:
    puntaje += 10
    print("muy bien", nombre, "!")

 print(YELLOW + nombre, "llevas", puntaje, "puntos" + RESET)

 print("\n")
 #PREGUNTA2
 print(CYAN + "2) ¿A cuantos mundiales debuto hasta ahora Peru?")
 print("a)3")
 print("b)5")
 print("c)9")
 print("d)7")

 respuesta2 = input("\ntu respuesta:")

 while respuesta2 not in ("a", "b", "c", "d"):
    respuesta2 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

 if (respuesta2 == "a"):
    print(RED + "es incorrecto!", nombre, "no es 3" + RESET)
 elif (respuesta2 == "c"):
    print(RED + "es incorrecto!", nombre, "no es 9" + RESET)
 elif (respuesta2 == "d"):
    print(RED + "es incorrecto!", nombre, "no es 7" + RESET)

 else:
    puntaje += 10
    print("muy bien", nombre, "!")

 print(CYAN + nombre, "llevas", puntaje, "puntos" + RESET)

 print("\n")
 #PREGUNTA3
 print(MAGENTA + "3) ¿En que año se creo la FPF?")
 print("a)1930")
 print("b)1920")
 print("c)1922")
 print("d)1935")

 respuesta3 = input("\ntu respuesta:")

 while respuesta3 not in ("a", "b", "c", "d"):
    respuesta3 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

 if (respuesta3 == "a"):
    print(RED + "es incorrecto!", nombre, "no se creo en 1930" + RESET)
 elif (respuesta3 == "b"):
    print(RED + "es incorrecto!", nombre, "no se creo en 1920" + RESET)
 elif (respuesta3 == "d"):
    print(RED + "es incorrecto!", nombre, "no se creo en 1935" + RESET)

 else:
    puntaje += 10
    print("muy bien", nombre, "!")

 print(MAGENTA + nombre, "llevas", puntaje, "puntos" + RESET)

 print("\n")
 #PREGUNTA 4
 print(
    GREEN +
    "4)¿Cual de estos 5 directores tecnicos duro mas años dirigiendo al Peru?")
 print("a)Juan carlos oblitas")
 print("b)Roberto mosquera vera")
 print("c)Ricardo gareca")
 print("d)Sergio markarian")

 respuesta4 = input("\ntu respuesta:")

 while respuesta4 not in ("a", "b", "c", "d"):
    respuesta4 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

 if respuesta4 == "a":
    print(RED + "es incorrecto", nombre, "no fue Juan carlos oblitas" + RESET)
    puntaje = puntaje - 5
 elif respuesta4 == "b":
    print(RED + " esta mal", nombre, "no fue Roberto mosquera vera" + RESET)
    puntaje = puntaje / 2
 elif respuesta4 == "d":
    print(RED + "incorrecto", nombre, "no fue Sergio markarian" + RESET)
    puntaje = puntaje + 1
 else:
    print("correcto!...")
    puntaje = puntaje * 2

 print(GREEN + "gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje,
      "puntos." + RESET)


  
 print(WHITE+"\n¿Deseas intentar la trivia nuevamente?")

 repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar:"+RESET).lower()

 if repetir_trivia != "si":
  print("\nEspero" + nombre + "que lo hayas pasado bien, hasta pronto!")
  iniciar_trivia = False