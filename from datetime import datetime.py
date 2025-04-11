from datetime import datetime
ahora = datetime.now()
print(ahora.year)#Año de hoy
print(ahora.strftime('%A')) #Dia de hoy
fecha = datetime(2025,10,4)
print(fecha.strftime('%B')) #Mesde una fecha
str_fecha = '05/06/09 14:58:00'
fecha_obj =datetime.strptime(str_fecha,'%d/%m/%y %H:%M:%S')
ahora - fecha_obj
print(ahora - fecha_obj)
