import sqlite3
import pygame
import os
from niveles import *

# SAVEGAME
sqlite = sqlite3.connect("saves.db")
try:
    savegame = ''' create table savegame
    (
        id integer primary key autoincrement,
        nombre text,
        tiempo text
    )
    '''
    sqlite.execute(savegame)
except:
    print("Tabla ya existe.")
sqlite.close()

# JUEGO
FPS = pygame.time.Clock()
titulo = pygame.display.set_caption("Shove It!")
jugando = True
nivel = 0
tecla = pygame.key.get_pressed()
milisegundos = 0
tiempo_transcurrido = "00:00:00"
texto_ingresado = ""
contando_tiempo = False

# MUSICA
VOLUMEN = 1
pygame.mixer.init()
pygame.mixer.music.load('Juego\song.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(VOLUMEN)

# EVENTOS
paso_un_segundo = pygame.USEREVENT
comienza_timer = False
pygame.time.set_timer(paso_un_segundo, 1000)

# COMIENZO DE JUEGO
pygame.init()

while jugando:
    
    # NIVELES
    if nivel == 0:
        nivel_actual = "Nivel_0"
        tiempo_transcurrido = "00:00:00"
        texto_ingresado = ""
        ventana.blit(fondo_menu_reescalado, (0, 0))
        texto_jugar = imprimir_texto(tex_jugar, (270, 150), ventana, COLOR_BLANCO, 84)
        texto_score = imprimir_texto(tex_scores, (250, 250), ventana, COLOR_BLANCO, 84)
        texto_salir = imprimir_texto(tex_salir, (270, 350), ventana, COLOR_BLANCO, 84)
    
    elif nivel == 1:  
        contando_tiempo = True
        Nivel_1.dibujar_nivel()
        if Nivel_1.pasar_de_nivel(Nivel_1.lista_de_cajas):
            nivel += 1
            Nivel_1.resetear_nivel()
    
    elif nivel == 2:
        Nivel_2.dibujar_nivel()
        if Nivel_2.pasar_de_nivel(Nivel_2.lista_de_cajas):
            nivel += 1
            Nivel_2.resetear_nivel()

    elif nivel == 3:
        Nivel_3.dibujar_nivel()
        if Nivel_3.pasar_de_nivel(Nivel_3.lista_de_cajas):
            nivel += 1   
            Nivel_3.resetear_nivel()
    
    elif nivel == 4:
        Nivel_4.dibujar_nivel()
        if Nivel_4.pasar_de_nivel(Nivel_4.lista_de_cajas):
            nivel += 1   
            Nivel_4.resetear_nivel()
    
    elif nivel == 5:
        Nivel_5.dibujar_nivel()
        if Nivel_5.pasar_de_nivel(Nivel_5.lista_de_cajas):
            nivel += 1  
            Nivel_5.resetear_nivel()
    # TIEMPO
    if nivel != 0 and nivel != 6 and nivel != 7:

        segundos = milisegundos // 1000
        minutos = segundos // 60
        horas = minutos // 60

        segundos %= 60  
        minutos %= 60
        
        texto_nivel = imprimir_texto(tex_nivel, (400, 550), ventana, COLOR_BLANCO, 32)
        texto_nivel_numero = imprimir_texto(str(nivel), (520, 550), ventana, COLOR_BLANCO, 32)
        texto_tiempo_numero = imprimir_texto(tex_tiempo, (25, 550), ventana, COLOR_BLANCO, 32)
        texto_horas = imprimir_texto(str(horas).zfill(2) + " " + ":", (160, 550), ventana, COLOR_BLANCO, 32)
        texto_minutos = imprimir_texto(str(minutos).zfill(2) + " " + ":", (220, 550), ventana, COLOR_BLANCO, 32)
        texto_segundos = imprimir_texto(str(segundos).zfill(2), (280, 550), ventana, COLOR_BLANCO, 32)
        tiempo_transcurrido = str(horas).zfill(2) + ":" + str(minutos).zfill(2) + ":" + str(segundos).zfill(2)
    # PANTALLA FINAL
    if nivel == 6:

        ventana.blit(fondo_menu_reescalado, (0, 0))
        texto_tu_tiempo = imprimir_texto(tex_tu_tiempo, (80, 70), ventana, COLOR_BLANCO, 84)
        texto_tu_tiempo_score = imprimir_texto(tiempo_transcurrido, (80, 145), ventana, COLOR_AMARILLO, 124)
        texto_tu_nombre = imprimir_texto(tex_tu_nombre, (80, 270), ventana, COLOR_BLANCO, 36)
        texto_lineas = imprimir_texto(tex_lineas, (80, 280), ventana, COLOR_BLANCO, 84)
        texto_lineas = imprimir_texto(tex_lineas, (80, 340), ventana, COLOR_BLANCO, 84)
        texto_linea = imprimir_texto(tex_linea, (60, 340), ventana, COLOR_BLANCO, 84)
        texto_linea = imprimir_texto(tex_linea, (730, 340), ventana, COLOR_BLANCO, 84)
        texto_guardar_score = imprimir_texto(tex_guardar_score, (40, 550), ventana, COLOR_BLANCO, 32)
        texto_salir = imprimir_texto(tex_salir, (225, 550), ventana, COLOR_BLANCO, 32)
        texto_scores = imprimir_texto(tex_scores, (370, 550), ventana, COLOR_BLANCO, 32)     
        texto_nombre = imprimir_texto(texto_ingresado, (80, 340), ventana, COLOR_AMARILLO, 84)
    # NIVEL SCORES
    if nivel == 7:
        with sqlite3.connect("C:\\Users\\bruno\Desktop\\Programación\\saves.db") as sqlite:
            cursor = sqlite.execute("SELECT * FROM savegame ORDER BY tiempo ASC")

            fila_1 = cursor.fetchone()
            fila_2 = cursor.fetchone()
            fila_3 = cursor.fetchone()
            fila_4 = cursor.fetchone()
            fila_5 = cursor.fetchone()

            # Extraer valores de las filas
            nombre_1 = fila_1[1] if fila_1 else "VACIO"
            nombre_2 = fila_2[1] if fila_2 else "VACIO"
            nombre_3 = fila_3[1] if fila_3 else "VACIO"
            nombre_4 = fila_4[1] if fila_4 else "VACIO"
            nombre_5 = fila_5[1] if fila_5 else "VACIO"

            tiempo_1 = fila_1[2] if fila_1 else "00:00:00"
            tiempo_2 = fila_2[2] if fila_2 else "00:00:00"
            tiempo_3 = fila_3[2] if fila_3 else "00:00:00"
            tiempo_4 = fila_4[2] if fila_4 else "00:00:00"
            tiempo_5 = fila_5[2] if fila_5 else "00:00:00"

        ventana.blit(fondo_menu_reescalado, (0, 0))
        texto_salir = imprimir_texto(tex_salir, (50, 550), ventana, COLOR_BLANCO, 32)
        texto_mejores = imprimir_texto(tex_mejores, (270, 10), ventana, COLOR_BLANCO, 60)
        texto_scores = imprimir_texto(tex_scores, (180, 50), ventana, COLOR_BLANCO, 120)
        texto_nombre_1 = imprimir_texto("#1 " + nombre_1, (40, 200), ventana, COLOR_AMARILLO, 36)
        texto_nombre_2 = imprimir_texto("#2 " + nombre_2, (40, 270), ventana, COLOR_AMARILLO, 36)
        texto_nombre_3 = imprimir_texto("#3 " + nombre_3, (40, 340), ventana, COLOR_AMARILLO, 36)
        texto_nombre_4 = imprimir_texto("#4 " + nombre_4, (40, 410), ventana, COLOR_AMARILLO, 36)
        texto_nombre_5 = imprimir_texto("#5 " + nombre_5, (40, 480), ventana, COLOR_AMARILLO, 36)
        texto_score_1 = imprimir_texto(tiempo_1, (625, 200), ventana, COLOR_BLANCO, 36)
        texto_score_2 = imprimir_texto(tiempo_2, (625, 270), ventana, COLOR_BLANCO, 36)
        texto_score_3 = imprimir_texto(tiempo_3, (625, 340), ventana, COLOR_BLANCO, 36)
        texto_score_4 = imprimir_texto(tiempo_4, (625, 410), ventana, COLOR_BLANCO, 36)
        texto_score_5 = imprimir_texto(tiempo_5, (625, 480), ventana, COLOR_BLANCO, 36)
    # PANEL DE SONIDO
    texto_mas = imprimir_texto(tex_mas, (610, 550), ventana, COLOR_BLANCO, 32)
    texto_menos = imprimir_texto(tex_menos, (770, 550), ventana, COLOR_BLANCO, 32)
    texto_sonido = imprimir_texto(tex_sonido, (640, 550), ventana, COLOR_BLANCO, 32)

     # MANEJO DE EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        # EVENTOS DE TECLADO
        if event.type == pygame.KEYDOWN:
            if nivel == 6:
                if event.key == pygame.K_BACKSPACE and len(texto_ingresado) > 0:
                    texto_ingresado = texto_ingresado.rstrip(texto_ingresado[-1])

                elif len(texto_ingresado) < 13 and event.key != pygame.K_BACKSPACE: 
                    texto_ingresado += event.unicode
        # TIMER
        elif event.type == paso_un_segundo and nivel != 0 and nivel != 6:
            milisegundos += 1000
        # EVENTOS DE MOUSE
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()

            if texto_mas.collidepoint(x, y):
                VOLUMEN += 0.1
                pygame.mixer.music.set_volume(VOLUMEN)
            if texto_menos.collidepoint(x, y):
                if VOLUMEN < 0.0:
                    VOLUMEN = 0.0
                else:
                    VOLUMEN -= 0.1
                pygame.mixer.music.set_volume(VOLUMEN)

            if nivel == 0:
                if texto_jugar.collidepoint(x, y):
                    nivel = 1
                if texto_salir.collidepoint(x, y):
                    jugando = False
                if texto_score.collidepoint(x, y):
                    nivel = 7

            if nivel == 6:
                if texto_salir.collidepoint(x, y):
                    jugando = False
                if texto_guardar_score.collidepoint(x, y): 
                    try: 
                        with sqlite3.connect("C:\\Users\\bruno\Desktop\\Programación\\saves.db") as sqlite:
                            if tiempo_transcurrido != "00:00:00" and texto_ingresado != "":
                                sqlite.execute("insert into savegame(nombre, tiempo) values (?, ?)", (texto_ingresado, tiempo_transcurrido))
                                sqlite.commit()
                                nivel = 0
                            nivel = 0
                            contando_tiempo = False
                            milisegundos = 0    
                    except:
                        print("Error")
                if texto_scores.collidepoint(x, y):
                    nivel = 7
                    contando_tiempo = False
                    milisegundos = 0
            if nivel == 7:
                if texto_salir.collidepoint(x, y):
                    nivel = 0

    pygame.display.flip()
    FPS.tick(15)

pygame.quit()
