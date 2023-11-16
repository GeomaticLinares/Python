# Geodesicas a UTM
import math

semi_eje_mayor = 6378137
prim_excentricidad = 0.00669438
seg_excentricidad = 0.006739497
valor_asub0 = 0.9983242985
valor_asub2 = 0.002514607064
valor_asub4 = 0.000002639
valor_asub6 = 0.00000000341805
valor_meridiano_central=0.9996


print(" *** Bienvenido *** ")
print("De Geodesicas a UTM")
print(" ")
print("Ingrese las Coord. Geodesicas LATITUD")


grad_lat = input("Ingrese los Grados: ")
min_lat = input("Ingrese los Minutos: ")
seg_lat = input("Ingrese los Segundos: ")

x1 = float(grad_lat)
x2 = float(min_lat) / 60
x3 = float(seg_lat) / 3600
latitud = x1 + x2 + x3


lat1 = input("Ingrese (S) para Latitud Sur y ENTER para Latitud Norte: ")
if lat1 == "S" or lat1 == "s":
    lat = float(latitud)*-1
    

    
alt_elipsoidal = input("Ingrese Alt. Elipsoidal: ")



print(" ")
print("Ingrese las Coord. Geodesicas LONGITUD")
grad_long = input("Ingrese los Grados: ")
min_long = input("Ingrese los Minutos: ")
seg_long = input("Ingrese los Segundos: ")

x4 = float(grad_long)
x5 = float(min_long) / 60
x6 = float(seg_long) / 3600
longitud = x4 + x5 + x6

long1 = input("Ingrese (O) para Longitud OESTE y ENTER para Longitud ESTE: ")
if long1 == "O" or long1 == "o":
    long = float(longitud)*- 1

print("")

zona_utm = ((float(long)/6)+31)//1
print(f"ZONA UTM: {zona_utm}")

meridiano_central = ((float(zona_utm)*6)-183)
print(f"Meridiano Central es: {meridiano_central}")

valor_t = math.tan(float(lat)*math.pi/180)


n_cuadrados = float(seg_excentricidad)*(math.pow(math.cos(float(lat)*math.pi/180),2))



delta_long = ((float(long)-float(meridiano_central))/180)*math.pi



cur_vert = float(semi_eje_mayor)/(math.sqrt(1-float(prim_excentricidad)*
                                            math.pow(math.sin(float(lat)*math.pi/180),2)))
print(f"El Radio de la Vertical Prima es: {cur_vert}")


semi_esteA = float(delta_long)*(math.cos(float(lat)*math.pi/180))*float(cur_vert)



semi_esteB = ((math.pow(float(delta_long)*(math.cos(float(lat)*math.pi/180)),3)*
               float(cur_vert)*(1-math.pow(float(valor_t),2)))+float(n_cuadrados))/6



semi_esteC = (math.pow(float(delta_long)*(math.cos(float(lat)*math.pi/180)),5)*
              float(cur_vert)*(5-18*float(valor_t)+math.pow(float(valor_t),4))/120)                            



semi_esteD = (float(semi_esteA) + float(semi_esteB) + float(semi_esteC))

esteE = 500000 + (float(valor_meridiano_central) * float(semi_esteD))



sem_norteA = float(semi_eje_mayor)*(float(valor_asub0)*(float(lat)*math.pi/180)-
                                    float(valor_asub2)*(math.sin(2*(float(lat)*math.pi/180)))+
                                    float(valor_asub4)*(math.sin(4*(float(lat)*math.pi/180)))-
                                    float(valor_asub6)*(math.sin(6*(math.pi/180))))



sem_norteB = float(sem_norteA)+(((math.pow(float(delta_long)*(math.cos(float(lat)*math.pi/180)),2)*
                                float(cur_vert)*float(valor_t))/2)+(math.pow(float(delta_long)*(math.cos(float(lat)*math.pi/180)),4)*
                                float(cur_vert)*float(valor_t)*(5-(math.pow(float(valor_t),2))+9*float(n_cuadrados)+4*
                                (math.pow(float(n_cuadrados),2)))/24)+
                                (math.pow(float(delta_long)*(math.cos(float(lat)*math.pi/180)),6)*
                                 float(cur_vert)*float(valor_t)*(61-58*(math.pow(float(valor_t),2))+math.pow(float(valor_t),4))/720))
                                  
                                                                  
norte_n = 10000000+(float(valor_meridiano_central)*float(sem_norteB))

print("")
print(f"La Coordenada UTM ESTE es: {esteE}")
print(f"La Coordenada UTM NORTE es: {norte_n}")










