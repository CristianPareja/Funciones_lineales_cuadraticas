import math
import matplotlib.pyplot as plt
print("Bienvenido a tu app de funciones lineales y cuadráticas") 
opcion = input("Elige el tipo de función: 1) lineal o 2) cuadrática: ") 
while opcion != '1' and opcion != '2': 
    opcion=input("Por favor, ingresa una opción válida (1 o 2):")
    
match opcion:
        case '1': 
            print("Función lineal del tipo y=ax+b")
            while True:
                 try:
                    a=float(input("Ingrese el valor de a: "))
                    if a!=0:
                        break
                    else:
                        print("Ingrese el valor de a (diferente de cero y que no sea una letra): ")
                 except ValueError:
                    print("Ingrese el valor de a (diferente de cero y que no sea una letra): ")

            b=float(input("Ingrese el valor de b: "))
            print(f"La funcion es: {a}x+{b}")
            ##pendiente
            m=a
            print(f"Pendiente: {m}")
            ##monotonia
            if m<0:
                print("Monotonia: Decreciente")
            else:
                print("Monotonia: Creciente")
            ##angulo de inclinacion
            angulo_rad = math.atan(m)
            angulo_gra = math.degrees(angulo_rad)
            angulo_gra = round(angulo_gra, 2)
            print(f"Angulo de inclinacion: {angulo_gra} grados")
            ##paridad
            if b==0:
                print("Paridad: Impar")
            else:
                print("Paridad: Ni Par ni Impar")
            ##Dominio
            print("Dominio: Reales")
            ##Rango
            print("Rango: Reales")
            ##Grafico
            x = list(range(-10, 11))
            y = [a * xi + b for xi in x]
            plt.plot(x, y, label=f'y = {a}x + {b}')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Gráfico de la Función Lineal') 
            plt.axhline(0, color='black',linewidth=0.5) 
            plt.axvline(0, color='black',linewidth=0.5) 
            plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5) 
            plt.legend() 
            plt.show()

        case '2': 
            print("Función cuadratica del tipo y=ax^2+bx+c")
            while True:
                 try:
                    a=float(input("Ingrese el valor de a: "))
                    if a!=0:
                        break
                    else:
                        print("Ingrese el valor de a (diferente de cero y que no sea una letra): ")
                 except ValueError:
                    print("Ingrese el valor de a (diferente de cero y que no sea una letra): ")

            b=float(input("Ingrese el valor de b: "))
            c=float(input("Ingrese el valor de c: "))
            print(f"La funcion es: {a}x^2+{b}x+{c}")
            ##Vertice
            vx=(-1)*(b/2*a)
            vx = round(vx, 2)
            vy=((4*a*c-b**2)/(4*a))
            vy = round(vy, 2)
            print(f"Vertice: ({vx},{vy})")
            ##Raices
            x1=((-1)*(b)+((b**2)-4*a*c)**0.5)/(2*a)
            x2=((-1)*(b)-((b**2)-4*a*c)**0.5)/(2*a)
            print(f"x1={x1}")
            print(f"x2={x2}")
            ##Dominio
            print("Dominio: Reales")
            ##Rango
            if a>0:
                print(f"Rango: [{vy},infinito(+)]")
            elif a<0:
                print(f"Rango: [infinito(-),{vy}]")
            ##monotonia
            if a>0:
                print(f"Monotonia: [{vy},infinito(+)] es Creciente y [infinito(+),{vy}] es Decreciente")
            elif a<0:
                print(f"Monotonia: [{vy},infinito(-)] es Decreciente y [infinito(-),{vy}] es Creciente")
            ##paridad
            if b==0 and (a!=0 and c!=0):
                print("Paridad: par")
            else:
                print("Paridad: Ni Par ni Impar")
            ##Punto maximo
            if a>0:
                print(f"Punto minimo en: ({vx},{vy})")
            elif a<0:
                print(f"Punto maximo en: ({vx},{vy})")
            ##Grafico
            x = [i for i in range(-10, 11)]
            y = [a * (xi ** 2) + b * xi + c for xi in x]
            plt.plot(x, y, label=f'y = {a}x^2 + {b}x + {c}') 
            plt.xlabel('x') 
            plt.ylabel('y') 
            plt.title('Gráfico de la Función Cuadrática') 
            plt.axhline(0, color='black', linewidth=1) 
            plt.axvline(0, color='black', linewidth=1) 
            plt.grid(color='gray', linestyle='--', linewidth=0.5) 
            plt.legend() 
            plt.show()

     
        
                
        