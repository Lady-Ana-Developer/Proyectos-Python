# coding: utf-8


# Importar las funciones necesarias de los módulos RPi,
# y time.
import RPi.GPIO as GPIO
import time

# Pin GPIO donde está conectado el activador (entrada) del
# sensor HC-SR04.
TRIG = 23

# Pin GPIO donde está conectado el eco (salida) del sensor
# HC-SR04.
ECHO = 24

# Indicar que se usa el esquema de numeración de pines
# de BCM (Broadcom SOC channel), es decir los números de
# pines GPIO (General-Purpose Input/Output).
GPIO.setmode(GPIO.BCM)
PIN_PIR = 7
GPIO.setup(PIN_PIR, GPIO.IN)
# Establecer que TRIG es un canal de salida.
GPIO.setup(TRIG, GPIO.OUT)

# Establecer que ECHO es un canal de entrada.
GPIO.setup(ECHO, GPIO.IN)

print ("Medición de distancias en progreso")

try:
    # Ciclo infinito.
    # Para terminar el programa se debe presionar Ctrl-C.
    while True:

        # Apagar el pin activador y permitir un par de
        # segundos para que se estabilice.
        GPIO.output(TRIG, GPIO.LOW)
        print ("Esperando a que el sensor se estabilice")
        time.sleep(2)

        # Encender el pin activador por 10 microsegundos
        # y después volverlo a apagar.
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        print ("Iniciando eco")
        
        while True:
            pulso_inicio = time.time()
            if GPIO.input(PIN_PIR):
                GPIO.input(ECHO) == GPIO.HIGH
                time.sleep(1)
                print("Nada se mueve")
                time.sleep(1)
                break

        while True:
            pulso_fin = time.time()
            if GPIO.input(ECHO) == GPIO.LOW:
                print("Movimiento detectado")
                break

            # La medición del tiempo es en segundos.
            duracion = pulso_fin - pulso_inicio

            # Calcular la distancia usando la velocidad del
            # sonido y considerando que la duración incluye
            # la ida y vuelta.
            distancia = (34300 * duracion) / 2

            # Imprimir resultado.
            print ("Distancia: %.2f cm" % distancia)

finally:
    # Reiniciar todos los canales de GPIO.
    GPIO.cleanup()