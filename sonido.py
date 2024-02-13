import pygame
import time

pygame.init()

DURACION_PUNTO = 100
DURACION_RAYA = DURACION_PUNTO * 3  # Una raya es tres veces la duración de un punto
DURACION_ENTRE_ELEMENTOS = DURACION_PUNTO  # Tiempo entre puntos y rayas dentro de un carácter
DURACION_ENTRE_CARACTERES = DURACION_PUNTO * 3  # Tiempo entre caracteres
DURACION_ENTRE_PALABRAS = DURACION_PUNTO * 7  # Tiempo entre palabras

# Función para reproducir un carácter Morse
def reproducir_caracter(caracter):
    if caracter == '.':
        pygame.mixer.Sound("punto.wav").play()
        time.sleep(DURACION_PUNTO / 1000)  # Convertir a segundos
    elif caracter == '-':
        pygame.mixer.Sound("raya.wav").play()
        time.sleep(DURACION_RAYA / 1000)  # Convertir a segundos

# Función para reproducir una palabra Morse
def reproducir_palabra(palabra):
    for i, caracter in enumerate(palabra):
        reproducir_caracter(caracter)
        if i < len(palabra) - 1:
            time.sleep(DURACION_ENTRE_ELEMENTOS / 1000)  # Convertir a segundos

# Función para convertir texto a Morse y reproducirlo
def texto_a_morse(texto,diccionario):
    for i, letra in enumerate(texto):
        if letra in diccionario:
            codigo_morse = diccionario[letra]
            reproducir_palabra(codigo_morse)
            if i < len(texto) - 1:
                time.sleep(DURACION_ENTRE_CARACTERES / 1000)  # Convertir a segundos
    time.sleep(DURACION_ENTRE_PALABRAS / 1000)  # Convertir a segundos

