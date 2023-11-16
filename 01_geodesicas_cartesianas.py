# Geodesicas a Cartesianas
import math
semi_eje_mayor = 6378137
prim_excentricidad = 0.00669438
print("Bienvenido")
print("*De geodesicas a Cartesianas*")

print("---LATITUD GEODESICA---")
grad_latitud = input("Grado: ")
min_latitud = input("Minuto: ")
seg_latitud = input("Segundo: ")

x1 = int(grad_latitud)
x2 = int(min_latitud) /60
x3 = float(seg_latitud) /3600

latitud = x1 + x2 + x3
print(f"{latitud}")

lat = input("Ingrese(S)Latitud SUR y ENTER para Latitud Norte: ")
if lat == "S" or lat == "s":
   print(latitud*-1)
else:
    print(latitud *1)

alt_elipsoidal = input("Ingrese la Alt. Elipsoidal: ")

print("---LONGITUD GEODESICA---")
grad_longitud = input("Grado: ")
min_longitud = input("Minuto: ")
seg_longitud = input("Segundo: ")

x4 = int(grad_longitud)
x5 = int(min_longitud) /60
x6 = float(seg_longitud) /3600

longitud = x4 + x5 + x6
print(f"{longitud}")

long = input("Ingrese(O)Longitud OESTE y ENTER para Longitud ESTE: ")
if long == "O" or long == "o":
   print(longitud*-1)
else:
    print(longitud *1)

#radio de Curvatura de la Primera vertical
cur_vert = semi_eje_mayor/(math.sqrt(1-prim_excentricidad*
                       math.pow(math.sin((latitud*math.pi/180)),2)))
print(f"La Vertical Prima es: {cur_vert}")

#Calculo de la Coordenada Geocentrica X
coord_x = ((math.cos(latitud*math.pi/180)*
           math.cos(longitud*math.pi/180))*
           (float(cur_vert) + float(alt_elipsoidal)))


#Calculo de la Coordenada Geocentrica Y
coord_y = (float(cur_vert) + float(alt_elipsoidal))*(math.cos(latitud*math.pi/180)*
             math.sin(longitud*math.pi/180))


#Calculo de la Altura Geocentrica Z
altura_z = ((((1-prim_excentricidad)*
             float(cur_vert))+float(alt_elipsoidal))*(math.sin(latitud*math.pi/180)))
print("---Coord. Geocentrica---")
print("   ")
print(f"La Coord. X es: {coord_x}")
print(f"La Coord. Y es: {coord_y}")
print(f"La Alt. Z es: {altura_z}")            
