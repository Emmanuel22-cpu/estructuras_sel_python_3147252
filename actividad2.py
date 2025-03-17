estado_civil = input("Ingresa tu estado civil:(soltero/casado/comprometido)")
edad = int(input("Ingresa tu edad: "))
temperamento = input("Ingresa tu temperamento:(buena persona/mala persona)")
fisico = input("Ingresa tu físico:(lindo/a/feo/a)")
salario = int(input("Ingresa tu salario: "))

if estado_civil == "casado" or estado_civil == "comprometido":
    print("No puedes acercarte a esa persona")
elif edad < 18:
    print("No puedes acercarete a esa persona, porque no tiene la edad suficiente")
elif temperamento == "mala persona":
    print("No puedes acercarte a esa persona, porque te generaria estres")
elif fisico == "feo":
    print("No puedes acercarte a esa persona, porque no le atraes fisicamente")
elif salario < 2000000:
     print("No puedes acercarte a esa persona, porque no puedes pagar una cena romantica")
else:
    print("Puedes acercarte a esa persona")
print("Fin del programa")
     