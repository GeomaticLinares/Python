# Cartesianas a Geodesicas
import math
semi_eje_mayor = 6378137
semi_eje_menor = 6356752.314
prim_excentricidad = 0.00669438
seg_excentricidad = 0.006739497

print("***Bienvenido***")
print(" *De Geocentrica a Geodesicas* ")

coord_x = input("Ingrese La Coord. Geocentrica X: ")
coord_y = input("Ingrese La Coord. Geocentrica y: ")
coord_z = input("Ingrese La Coord. Geocentrica Z: ")

valor_p = math.sqrt(math.pow(float(coord_x),2)+math.pow(float(coord_y),2))

valor_teta = math.atan(((float(coord_z) * float(semi_eje_mayor))/
                       (float(valor_p)* float(semi_eje_menor))))

phi = math.atan((float(coord_z)+(float(seg_excentricidad)*float(semi_eje_menor)*
                                 math.pow(math.sin(float(valor_teta)),3)))
                /(float(valor_p)-(float(prim_excentricidad)*float(semi_eje_mayor)*
                 math.pow(math.cos(float(valor_teta)),3)))) 
print("")
print("  * Latitud *  ")
# Grados con decimales
grados =  (float(phi)*180/math.pi)

# Grados en Entero
grado2 = (((float(phi)*180/math.pi)*-1)//1)*-1

#los decimales del Grado
grado3 = (float(phi)*180/math.pi) + ((float(phi)*180/math.pi)*-1)//1

#decimales*60 / *-1 para cambiar el signo //1para obtener el entero
if grados < 0:
    minutos = (((float(grado3))* 60)*-1)//1


#Segundos
segundos = ((((float(grado3))* 60)*-1)) - ((((float(grado3))* 60)*-1)//1)
segundos1 = (((float(segundos)) * 60))

print(f" Grados:  {grado2}°")
print(f" Minutos:  {minutos}'")
print(f" Segundos: {segundos1}''")


#Calculo de la Longitud
lamda = math.atan(float(coord_y) / float(coord_x))
print("")
print("  * Longitud *  ")

grados = ((float(lamda))*180/math.pi)
grados1 = ((((float(lamda))*180/math.pi)*-1) //1)*-1
grados_1 = (((float(lamda))*180/math.pi)*-1) //1
grados2 = (((((float(lamda))*180/math.pi)*-1) //1) - ((((float(lamda))*180/math.pi)*-1)))*-1
minutos = (((((((float(lamda))*180/math.pi)*-1) //1) - ((((float(lamda))*180/math.pi)*-1)))*-1)*60)//1
segundos = (((((((((float(lamda))*180/math.pi)*-1) //1) - ((((float(lamda))*180/math.pi)*-1)))*-1)*60) -
(((((((float(lamda))*180/math.pi)*-1) //1) - ((((float(lamda))*180/math.pi)*-1)))*-1)*60)//1))*60

print(f" Grados:  {grados1}")
print(f" Minutos:  {minutos}")
print(f" Segundos: {segundos}")


#Vertical Prima

cur_vert = float(semi_eje_mayor)/(math.sqrt(1-(float(prim_excentricidad)*
                                               math.pow(math.sin(float(phi)),2))))
print("")
print(f"La Vertical Prima es: {cur_vert}")

# Altura Elipsoidal
alt_elipsoidal = (float(valor_p)/math.cos(float(phi))) - float(cur_vert)
print(f"Alt. Elipsoidal es: {alt_elipsoidal}")
