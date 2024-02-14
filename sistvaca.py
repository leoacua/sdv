# sistemas de vacaciones para empresa
print("*************************************") 
print("sistemas administrativo de vacaciónes")
print("************************************* \n")

Nombre =  str(input("escriba por favor su nombre: "))
clave_departamento = int(input("ingrese el numero clave: "))
antiguedad_empleado  = float(input("por favor introduce los años del empleado: "))
print("*************************************\n")

if (clave_departamento == 1):
    if (antiguedad_empleado >= 1) and (antiguedad_empleado < 2):
        print("El empleado",Nombre,"Tiene derecho a 6 dias de vacaciones")
    elif (antiguedad_empleado >= 2) and (antiguedad_empleado <= 6):
        print("El empleado",Nombre,"Tiene derecho a 14 dias de vacaciones")
    elif(antiguedad_empleado >= 7):
        print("El empleado",Nombre,"Tiene derecho a 20 dias de vacaciones")
    else:
         print("El empleado",Nombre,"No tiene derecho a vacaciones")

elif(clave_departamento == 2):
    if (antiguedad_empleado >= 1) and (antiguedad_empleado < 2):
        print("el empleado",Nombre,"tiene derecho a 7 dias de vacaciones")
    elif (antiguedad_empleado >= 2) and (antiguedad_empleado <= 6):
        print("el empleado",Nombre,"tiene derecho a 15 dias de vacaciones")
    elif(antiguedad_empleado >= 7):
        print("el empleado",Nombre,"tiene derecho a 22 dias de vacaciones")
    else:
         print("el empleado",Nombre,"auno tiene derecho a vacaciones")

elif(clave_departamento == 2):
    if (antiguedad_empleado >= 1) and (antiguedad_empleado < 2):
        print("el empleado",Nombre,"tiene derecho a 10 dias de vacaciones")
    elif (antiguedad_empleado >= 2) and (antiguedad_empleado <= 6):
        print("el empleado",Nombre,"tiene derecho a 20 dias de vacaciones")
    elif(antiguedad_empleado >= 7):
        print("el empleado",Nombre,"tiene derecho a 30 dias de vacaciones")
    else:
         print("el empleado",Nombre,"auno tiene derecho a vacaciones")

else:
    print("la clave de departamento no existe, vuelve a intentarlo")
           
    
    

#Dep01 = str(input("Departamento de atención a clinete (clave 1): "))
#Dep02 = str(input("Departamento de Logistica (clave 2): "))
#Gerencia = str(input("(Clave 3): "))

