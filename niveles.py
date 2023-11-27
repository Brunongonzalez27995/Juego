from clases import *
from constantes import *

# JUEGO

ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])

# MENU

fondo_menu = pygame.image.load("Juego\MENU.png")
fondo_menu_reescalado =  pygame.transform.smoothscale(fondo_menu, (800, 600))
pygame.font.init()

# TEXTO

def imprimir_texto(texto, posicion, superficie, color_texto, tamaño_texto, fuente = pygame.font.Font()):
    fuente = pygame.font.Font("Juego\\upheavtt.ttf", tamaño_texto)
    texto = texto
    texto_renderizado = fuente.render(texto, True, color_texto)
    rect_texto = texto_renderizado.get_rect()
    rect_texto.topleft = posicion
    superficie.blit(texto_renderizado, rect_texto)

    return rect_texto

tex_jugar = "JUGAR"
tex_scores = "SCORES"
tex_salir = "SALIR"
tex_tiempo = "TIEMPO"
tex_sonido = "MÚSICA"
tex_mas = "+"
tex_menos = "-"
tex_nivel = "NIVEL"
tex_tu_tiempo = "TU TIEMPO:"
tex_tu_nombre = "INTRODUCE TU NOMBRE:"
tex_guardar_score = "GUARDAR"
tex_lineas = "_____________"
tex_linea = "|"
tex_mejores = "MEJORES"
tex_menu = "MENU"
tex_reiniciar = "REINICIAR"

# NIVEL 1

escenario_matriz_nv_1 =  [
    [" ", " ", "#", "#", "#", " ", " ", " "],
    [" ", " ", "#", "F", "#", " ", " ", " "],
    [" ", " ", "#", "S", "#", "#", "#", "#"],
    ["#", "#", "#", "S", "S", "S", "F", "#"],
    ["#", "F", "S", "S", "S", "#", "#", "#"],
    ["#", "#", "#", "#", "S", "#", " ", " "],
    [" ", " ", " ", "#", "F", "#", " ", " "],
    [" ", " ", " ", "#", "#", "#", " ", " "]
]
imagen_nv_1 = "Juego\pantalla1.jpg"
cajas_nv_1 = [Caja(350, 300, COLOR_ROJO, 50, 50),Caja(350, 250, COLOR_VERDE, 50, 50),Caja(450, 250, COLOR_AZUL, 50, 50),Caja(400, 350, COLOR_NEGRO, 50, 50)]
personaje_nv_1 = Personaje(400, 300, 50, 50, COLOR_NARANJA)
escenario_nv_1 = Escenario(escenario_matriz_nv_1, 200, 100)

Nivel_1 = Nivel(1, escenario_matriz_nv_1, imagen_nv_1, cajas_nv_1, personaje_nv_1, ventana, escenario_nv_1)

# NIVEL 2

escenario_matriz_nv_2 = [
    ["#", "#", "#", "#", "#", " ", " ", " ", " "],
    ["#", "S", "S", "S", "#", " ", " ", " ", " "],
    ["#", "S", "S", "S", "#", " ", "#", "#", "#"],
    ["#", "S", "S", "S", "#", " ", "#", "F", "#"],
    ["#", "#", "#", "S", "#", "#", "#", "F", "#"],
    [" ", "#", "#", "S", "S", "S", "S", "F", "#"],
    [" ", "#", "S", "S", "S", "#", "S", "S", "#"],
    [" ", "#", "S", "S", "S", "#", "#", "#", "#"],
    [" ", "#", "#", "#", "#", "#", " ", " ", " "],
]
imagen_nv_2 = "Juego\pantalla1.jpg"
cajas_nv_2 = [Caja(275, 175, COLOR_ROJO, 50, 50),Caja(325, 175, COLOR_VERDE, 50, 50),Caja(275, 225, COLOR_NEGRO, 50, 50)]
personaje_nv_2 = Personaje(225, 125, 50, 50, COLOR_NARANJA)
escenario_nv_2 = Escenario(escenario_matriz_nv_2, 175, 75)

Nivel_2 = Nivel(2, escenario_matriz_nv_2, imagen_nv_2, cajas_nv_2, personaje_nv_2, ventana, escenario_nv_2)

# NIVEL 3

escenario_matriz_nv_3 = [
    [" ", "#", "#", "#", "#", " "],
    ["#", "#", "S", "S", "#", " "],
    ["#", "S", "S", "S", "#", " "],
    ["#", "#", "S", "S", "#", "#"],
    ["#", "#", "S", "S", "S", "#"],
    ["#", "F", "S", "S", "S", "#"],
    ["#", "F", "F", "F", "F", "#"],
    ["#", "#", "#", "#", "#", "#"],
]
imagen_nv_3 = "Juego\pantalla1.jpg"
cajas_nv_3 = [Caja(350, 200, COLOR_ROJO, 50, 50),Caja(350, 250, COLOR_ROJO, 50, 50),Caja(400, 300, COLOR_ROJO, 50, 50),Caja(350, 350, COLOR_VERDE, 50, 50),Caja(400, 400, COLOR_NEGRO, 50, 50)]
personaje_nv_3 = Personaje(300, 200, 50, 50, COLOR_NARANJA)
escenario_nv_3 = Escenario(escenario_matriz_nv_3, 250, 100)

Nivel_3 = Nivel(3, escenario_matriz_nv_3, imagen_nv_3, cajas_nv_3, personaje_nv_3, ventana, escenario_nv_3)

# NIVEL 4

escenario_matriz_nv_4 = [
    [" ", "#", "#", "#", "#", "#", "#", "#", " ", " "],
    [" ", "#", "S", "S", "S", "S", "S", "#", "#", "#"],
    ["#", "#", "S", "#", "#", "#", "S", "S", "S", "#"],
    ["#", "S", "S", "S", "S", "S", "S", "S", "S", "#"],
    ["#", "S", "F", "F", "#", "S", "S", "S", "#", "#"],
    ["#", "#", "F", "F", "#", "S", "S", "S", "#", " "],
    [" ", "#", "#", "#", "#", "#", "#", "#", "#", " "],
]
imagen_nv_4 = "Juego\pantalla1.jpg"
cajas_nv_4 = [Caja(250, 250, COLOR_ROJO, 50, 50),Caja(350, 300, COLOR_ROJO, 50, 50),Caja(500, 300, COLOR_ROJO, 50, 50),Caja(450, 350, COLOR_VERDE, 50, 50)]
personaje_nv_4 = Personaje(250, 300, 50, 50, COLOR_NARANJA)
escenario_nv_4 = Escenario(escenario_matriz_nv_4, 150, 150)

Nivel_4 = Nivel(4, escenario_matriz_nv_4, imagen_nv_4, cajas_nv_4, personaje_nv_4, ventana, escenario_nv_4)

# NIVEL 5

escenario_matriz_nv_5 = [
    [" ", "#", "#", "#", "#", "#", " ", " "],
    [" ", "#", "S", "S", "#", "#", "#", " "],
    [" ", "#", "S", "S", "S", "S", "#", "#"],
    ["#", "#", "#", "S", "#", "S", "#", "#"],
    ["#", "F", "#", "S", "#", "S", "S", "#"],
    ["#", "F", "S", "S", "S", "#", "S", "#"],
    ["#", "F", "S", "S", "S", "S", "S", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"]
]
imagen_nv_5 = "Juego\pantalla1.jpg"
cajas_nv_5 = [Caja(300, 350, COLOR_ROJO, 50, 50),Caja(350, 300, COLOR_ROJO, 50, 50),Caja(450, 400, COLOR_ROJO, 50, 50)]
personaje_nv_5 = Personaje(300, 150, 50, 50, COLOR_NARANJA)
escenario_nv_5 = Escenario(escenario_matriz_nv_5, 200, 100)

Nivel_5 = Nivel(5, escenario_matriz_nv_5, imagen_nv_5, cajas_nv_5, personaje_nv_5, ventana, escenario_nv_5)