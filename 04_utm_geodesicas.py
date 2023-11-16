# UTM a Geodesicas
import math

semi_eje_mayor = 6378137
prim_excentricidad = 0.00669438
seg_excentricidad = 0.006739497

print("***Bienvenido***")
print(" *De UTM a Geodesicas* ")


print(" ")
coord_este = 477000.5102 #input("Ingrese Coord. ESTE: ")
coord_norte = 8666601.4038 #input("Ingrese Coord. NORTE: ")
coord_zona_utm = 18 #input("Ingrese ZONA UTM: ")


e1 = (1-math.sqrt(1-float(prim_excentricidad)))/(1+math.sqrt(1-float(prim_excentricidad)))


m1 = (float(coord_norte)-10000000)/0.9996


u = float(m1)/(float(semi_eje_mayor)*(1-(float(prim_excentricidad)/4)-
                          (3*math.pow(float(prim_excentricidad),2)/64)-
                                (5*math.pow(float(prim_excentricidad),3)/256)))


latitud_prima = float(u)+((3*float(e1)/2)-
                          (27*math.pow(float(e1),3)/32))*math.sin(2*float(u))+((21*math.pow(float(e1),2)/16)-
                (55*math.pow(float(e1),4)/32))*math.sin(4*float(u))+(151*math.pow(float(e1),3)/96)*math.sin(6*float(u))+(1097*(math.pow(float(e1),4))/512)*math.sin(8*float(u))



v1 = float(semi_eje_mayor)/(math.sqrt(1-float(prim_excentricidad)*
               math.pow(math.sin(float(latitud_prima)*math.pi/180),2)))


d1 = (float(coord_este)-500000)/(float(v1)*0.9996)



r1 = float(semi_eje_mayor)*(1-float(prim_excentricidad))/math.sqrt(math.pow(1-(float(prim_excentricidad)*
                              math.pow(math.sin(float(latitud_prima)),2)),3))



t1 = math.pow(math.tan(float(latitud_prima)),2)


c1 = float(seg_excentricidad)*math.pow(math.cos(float(latitud_prima)),2)


p = math.pow(float(d1),2)/2


q = -(5+3*float(t1)+10*float(c1)-4*math.pow(float(c1),2)-9*
     float(seg_excentricidad))*math.pow(float(d1),4)/24


s = (61+90*float(t1)+298*float(c1)+
     45*math.pow(float(t1),2)-252*
     float(seg_excentricidad)-
     3*math.pow(float(c1),2)) *math.pow(float(d1),6)/720


delta_latitud_prima = -(float(v1)*math.tan(float(latitud_prima))/
                        float(r1))*(float(p)+float(q)+float(s))


latitud1 = float(latitud_prima)+float(delta_latitud_prima)

# Calculo de la LATITUD
grad_latitud = float(latitud1)*180/math.pi*-1//1
grados = (float(latitud1)*180/math.pi*-1//1)*-1


min_latitud =(((float(latitud1)*180/math.pi)+
               (float(latitud1)*180/math.pi*-1//1))*60)*-1//1


seg_latitud = (((((float(latitud1)*180/math.pi)+
                  (float(latitud1)*180/math.pi*-1//1))*60)*-1)-
               (((float(latitud1)*180/math.pi)+
                 (float(latitud1)*180/math.pi*-1//1))*60)*-1//1)*60

print("   *** LATITUD ***   ")
print(f"Grados:   {grados} °")
print(f"Minutos:   {min_latitud} ' ")
print(f"Segundos:  {seg_latitud} '' ")
print(" ")

# Parametros de la LONGITUD

delta_cero = float(coord_zona_utm)*6-183

jj = float(d1)-(1+2*float(t1)+float(c1))*math.pow(float(d1),3)/6

xx = (5-2*float(c1)+28*float(t1)-
      3*math.pow(float(c1),2)+8*
    float(seg_excentricidad)+
      24*math.pow(float(t1),2))*math.pow(float(d1),5)/120

delta = (float(jj)+float(xx))/math.cos(float(latitud_prima))

long1 = float(delta_cero)+(float(delta)*180/math.pi)

long2 = (float(delta_cero)+(float(delta)*180/math.pi))*-1//1

longitud = ((float(delta_cero)+(float(delta)*180/math.pi))*-1//1)*-1



min_longitud = (((float(delta_cero)+(float(delta)*180/math.pi))*-1)-
                (float(delta_cero)+(float(delta)*180/math.pi))*-1//1)*60



seg_longitud = (((((float(delta_cero)+(float(delta)*180/math.pi))*-1)-
                  (float(delta_cero)+(float(delta)*180/math.pi))*-1//1)*60) -
                ((((float(delta_cero)+(float(delta)*180/math.pi))*-1)-
                  (float(delta_cero)+(float(delta)*180/math.pi))*-1//1)*60//1))*60


print("   *** LONGITUD ***   ")
print(f"Grados:   {longitud} ° ")
print(f"Minutos:   {min_longitud} ' ")
print(f"Segundos:  {seg_longitud} '' ")









