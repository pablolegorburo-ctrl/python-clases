
contraseña = input("mimamamemima ")
longitud_minima = 8
longitud_maxima = 20

if longitud_minima < len(contraseña):
    print('MUY CORTA')
elif longitud_maxima < len(contraseña):
    print('MUY LARGA')
else:
    print("Contraseña ACEPTADA")


colores = ["rojo", "verde", "azul", "amarillo"]

for color in colores:
    print(color)





numeros= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
contador=0
while contador < 11:
    print(contador)
    contador= contador + 1


edad = 20

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")



def saludar(nombre):
    return "Hola, " + nombre
print(saludar("rafael"))

def cuentaCarateres(Palabra):
    if type(Palabra) == str:
        return len(Palabra)
    else:
        return "debo ser ejecutado con un string"
print(cuentaCarateres(4))   



hola = "Hola, soy un string"
print(hola[-1])




def obtener_nombre_completo(nombre, apellido):
    return nombre + " " + apellido
def main():
    usuarios = [
{"nombre": "Sofía"},
{"nombre": "Luis", "apellido": "Martínez"},
]
for usuario in usuarios:
    completo = obtener_nombre_completo(usuario["nombre"], 
                    usuario["apellido"])
    print(completo)
main()



