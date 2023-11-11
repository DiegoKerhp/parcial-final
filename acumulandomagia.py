cl= str(input("Entró un cliente? (si/no):"))
ac = 0
contador = 0
ttc = 0
noc = 0
quec = 0
acv1 = 0
acv2 = 0
acv3 = 0
acv4 = 0
while cl == "si": 
  c = str(input("Compra algo?  (si/no): "))
  if c == "si":
     ac += 1
     quec = str(input("Que compro?  Varita de sauco [1] varita de espino [2]  varita [3]  varita de acebo [4]" ))

     if quec == "1":
       acv1 += 1
     elif quec == "2":
       acv2 += 1
     elif quec == "3":
       acv3 += 1
     elif quec == "4":
       acv4 += 1
     cl = str(input("Entró un cliente? (si/no): "))
     ttc += 1
     noc = ttc - ac
     print(f"Los clientes que compraron productos son {ac}")
     print(f"Los clientes que no compraron {noc}")
     print(f"El total de clientes sería {ttc}")
     print(f"Las varitas de sauco son {acv1}, las varitas de espino son {acv2}, las varitas de sauce son {acv3}, las varitas de acebo son {acv4}")




#https://replit.com/join/nvbeunabph-diegok3

a = input("Escribe el nombre: ")
b = a.split()
c = b.count("Alexa")

if c == 1:
    print("Dime cómo puedo ayudarte?")
elif c > 1:
    print("¡Tranquilo, solo di mi nombre una vez!")


#https://replit.com/join/ekbvddcmlz-diegok3

ab = int(input("¿Cuántas lecturas de temperatura tienes? "))
ac = 0
ad = 0
ae = 0

while ac < ab:
      ac += 1
      t = float(input("Escribe la temperatura: "))
      if t >= 10 and t <= 40:
          pass
      else:
          ae += 1

print("Número de lecturas fuera del rango:", ae)
po = (ae * 100) / ab
print("Porcentaje de lecturas fuera del rango:", po)


# https://replit.com/join/etvunnkdfv-diegok3

gryffindor_score = 0
slytherin_score = 0

while True:
      quidditch_events = input("¿Qué pasó (goal/snitch/foul)? ").lower()

      if quidditch_events == "goal":
          equipo = input("¿Quién lo anotó (gryffindor o slytherin)? ").lower()
          if equipo == "gryffindor":
              gryffindor_score += 10
              print("Gryffindor gana 10 puntos!")
          elif equipo == "slytherin":
              slytherin_score += 10
              print("Slytherin gana 10 puntos!")

      elif quidditch_events == "snitch":
          equipo = input("¿Quién lo anotó (gryffindor o slytherin)? ").lower()
          if equipo == "gryffindor":
              gryffindor_score += 150
              print("Gryffindor gana 150 puntos!")
          elif equipo == "slytherin":
              slytherin_score += 150
              print("Slytherin gana 150 puntos!")

      elif quidditch_events == "foul":
          equipo = input("¿Quién lo anotó (gryffindor o slytherin)? ").lower()
          if equipo == "gryffindor":
              gryffindor_score -= 30
              print("Gryffindor pierde 30 puntos!")
          elif equipo == "slytherin":
              slytherin_score -= 30
              print("Slytherin pierde 30 puntos!")

      print(f"Gryffindor: {gryffindor_score}")
      print(f"Slytherin: {slytherin_score}")

      continuar = input("¿Fin del juego (si o no)? ").lower()
      if continuar != 'no':
          break

if gryffindor_score > slytherin_score:
      print("Gryffindor gana!")
elif slytherin_score > gryffindor_score:
      print("Slytherin gana!")
else:
      print("Empate!")
