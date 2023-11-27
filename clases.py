import pygame
from constantes import * 

class Personaje():
    def __init__(self, x, y, ancho, alto, color):
        self.rectangulo = pygame.Rect(x, y, ancho, alto)
        self.posicion_inicial = (x, y)
        self.color = color
        self.moviendose = False
        self.grupo_sprites = pygame.image.load("Juego\grupoSprites.png").convert_alpha()
        self.frame_actual = 0
        self.direccion_vista = "derecha"
        self.hb_izq = pygame.Rect(self.rectangulo.x - 5, self.rectangulo.y, 5, 50)
        self.hb_izq_2 = pygame.Rect(self.rectangulo.x - 55, self.rectangulo.y, 5, 50)
        self.hb_der = pygame.Rect(self.rectangulo.x + 50, self.rectangulo.y, 5, 50)
        self.hb_der_2 = pygame.Rect(self.rectangulo.x + 100, self.rectangulo.y, 5, 50)
        self.hb_arriba = pygame.Rect(self.rectangulo.x, self.rectangulo.y - 5, 50, 5)
        self.hb_arriba_2 = pygame.Rect(self.rectangulo.x, self.rectangulo.y - 55, 50, 5)
        self.hb_abajo = pygame.Rect(self.rectangulo.x, self.rectangulo.y + 50, 50, 5)
        self.hb_abajo_2 = pygame.Rect(self.rectangulo.x, self.rectangulo.y + 100, 50, 5)

    def obtener_imagen(self, frame):
        sprites = self.grupo_sprites
        imagen = pygame.Surface((50, 50)).convert_alpha()
        imagen.blit(self.grupo_sprites, (0, 0), ((frame * 24), 0, 24, 24))
        imagen = pygame.transform.smoothscale(imagen, (100, 100))
        imagen.set_colorkey(COLOR_NEGRO)

        return imagen
    
    def invertir_imagen_horizontal(self, imagen):
        imagen_invertida = pygame.transform.flip(imagen, True, False)
        imagen_invertida.convert_alpha()
        imagen_invertida.set_colorkey(COLOR_NEGRO)

        return imagen_invertida
    
    def dibujarse(self, superficie):

        tecla = self.direccion_personaje()

        # FRAMES CORRIENDO
        frame_2 = self.obtener_imagen(23)
        frame_3 = self.obtener_imagen(22)
        frame_4 = self.obtener_imagen(21)
        frame_5 = self.obtener_imagen(20)
        frame_6 = self.obtener_imagen(19)
        frame_7 = self.obtener_imagen(18)

        # FRAMES CORRIENDO INVERTIDOS
        frame_2_invertido = self.invertir_imagen_horizontal(frame_2)
        frame_3_invertido = self.invertir_imagen_horizontal(frame_3)
        frame_4_invertido = self.invertir_imagen_horizontal(frame_4)
        frame_5_invertido = self.invertir_imagen_horizontal(frame_5)
        frame_6_invertido = self.invertir_imagen_horizontal(frame_6)
        frame_7_invertido = self.invertir_imagen_horizontal(frame_7)

        # FRAMES QUIETO
        frame_8 = self.obtener_imagen(1)
        frame_9 = self.obtener_imagen(2)
        frame_10 = self.obtener_imagen(3)
        frame_11 = self.obtener_imagen(4)

        # Invertir frames quieto
        frame_8_invertido = self.invertir_imagen_horizontal(frame_8)
        frame_9_invertido = self.invertir_imagen_horizontal(frame_9)
        frame_10_invertido = self.invertir_imagen_horizontal(frame_10)
        frame_11_invertido = self.invertir_imagen_horizontal(frame_11)

        lista_frame_corriendo = [frame_2, frame_3, frame_4, frame_5, frame_6, frame_7]
        lista_frames_quieto = [frame_8, frame_9, frame_10, frame_11]
        lista_frame_corriendo_invertida = [frame_2_invertido, frame_3_invertido, frame_4_invertido, frame_5_invertido, frame_6_invertido, frame_7_invertido]
        lista_frames_quieto_invertidos = [frame_8_invertido, frame_9_invertido, frame_10_invertido, frame_11_invertido]

        if self.direccion_vista == "derecha":
            if self.moviendose:
                self.actualizar_frames(lista_frame_corriendo)
                frame_actual = lista_frame_corriendo[int(self.frame_actual)]
                superficie.blit(frame_actual, (self.rectangulo.x, self.rectangulo.y))
            else:
                if self.direccion_vista == "derecha":
                    self.actualizar_frames(lista_frames_quieto)
                    frame_actual = lista_frames_quieto[int(self.frame_actual)]
                    superficie.blit(frame_actual, (self.rectangulo.x, self.rectangulo.y))
        elif self.direccion_vista == "izquierda":
            if self.moviendose:
                self.actualizar_frames(lista_frame_corriendo_invertida)
                frame_actual = lista_frame_corriendo_invertida[int(self.frame_actual)]
                superficie.blit(frame_actual, (self.rectangulo.x - 50, self.rectangulo.y))
            else:
                self.actualizar_frames(lista_frames_quieto_invertidos)
                frame_actual = lista_frames_quieto_invertidos[int(self.frame_actual)]
                superficie.blit(frame_actual, (self.rectangulo.x - 50, self.rectangulo.y))

    def actualizar_frames(self, lista_frames):
        if self.frame_actual >= (len(lista_frames) - 0.5): #FIX improvisado para que no se salga del index.
            self.frame_actual = 0
        else:
            self.frame_actual += 0.2

    def mover(self, ancho, alto):
        self.rectangulo.x += ancho
        self.rectangulo.y += alto

    def manejar_teclas(self, lista_cajas, escenario):

        colisiones_muros = self.colision_con_muros(escenario)
        colisiones_cajas = self.colisiones_cajas(lista_cajas)
        tecla = self.direccion_personaje()

        if not self.moviendose:
            if tecla == "derecha":
                if "hb_derecha" not in colisiones_muros and "hb_derecha" not in colisiones_cajas:
                    self.mover(50, 0)
                    self.moviendose = True
                elif "hb_derecha" in colisiones_cajas:
                    if "hb_derecha_2" in colisiones_muros or "hb_derecha_2" in colisiones_cajas:
                        self.mover(0, 0)
                        self.moviendose = False
                    else:
                        self.mover(50, 0)
                        self.moviendose = True
            elif tecla == "izquierda":
                if "hb_izquierda" not in colisiones_muros and "hb_izquierda" not in colisiones_cajas:
                    self.mover(-50, 0)
                    self.moviendose = True
                elif "hb_izquierda" in colisiones_cajas:
                    if "hb_izquierda_2" in colisiones_muros or "hb_izquierda_2" in colisiones_cajas:
                        self.mover(0, 0)
                        self.moviendose = False
                    else:
                        self.mover(-50, 0)
                        self.moviendose = True
            elif tecla == "arriba":
                if "hb_arriba" not in colisiones_muros and "hb_arriba" not in colisiones_cajas:
                    self.mover(0, -50)
                    self.moviendose = True
                elif "hb_arriba" in colisiones_cajas:
                    if "hb_arriba_2" in colisiones_muros or "hb_arriba_2" in colisiones_cajas:
                        self.mover(0, 0)
                        self.moviendose = False
                    else:
                        self.mover(0, -50)
                        self.moviendose = True
            elif tecla == "abajo":
                if "hb_abajo" not in colisiones_muros and "hb_abajo" not in colisiones_cajas:
                    self.mover(0, 50)
                    self.moviendose = True
                elif "hb_abajo" in colisiones_cajas:
                    if "hb_abajo_2" in colisiones_muros or "hb_abajo_2" in colisiones_cajas:
                        self.mover(0, 0)
                        self.moviendose = False
                    else:
                        self.mover(0, 50)
                        self.moviendose = True
        else:
            self.moviendose = False

        self.hb_izq = pygame.Rect(self.rectangulo.x - 5, self.rectangulo.y, 5, 50)
        self.hb_izq_2 = pygame.Rect(self.rectangulo.x - 55, self.rectangulo.y, 5, 50)
        self.hb_der = pygame.Rect(self.rectangulo.x + 50, self.rectangulo.y, 5, 50)
        self.hb_der_2 = pygame.Rect(self.rectangulo.x + 100, self.rectangulo.y, 5, 50)
        self.hb_arriba = pygame.Rect(self.rectangulo.x, self.rectangulo.y - 5, 50, 5)
        self.hb_arriba_2 = pygame.Rect(self.rectangulo.x, self.rectangulo.y - 55, 50, 5)
        self.hb_abajo = pygame.Rect(self.rectangulo.x, self.rectangulo.y + 50, 50, 5)
        self.hb_abajo_2 = pygame.Rect(self.rectangulo.x, self.rectangulo.y + 100, 50, 5)

    def colision_con_muros(self, escenario):
        
        posiciones_elementos = escenario.generar_posiciones_elementos()
        lista_colisiones = []

        for elemento in posiciones_elementos:
            rectangulo = elemento['rectangulo']

            if elemento['tipo'] == "#":
                if self.hb_abajo.colliderect(rectangulo):
                    lista_colisiones.append("hb_abajo")
                if self.hb_arriba.colliderect(rectangulo):
                    lista_colisiones.append("hb_arriba")
                if self.hb_izq.colliderect(rectangulo):
                    lista_colisiones.append("hb_izquierda")
                if self.hb_der.colliderect(rectangulo):
                    lista_colisiones.append("hb_derecha")
                if self.hb_abajo_2.colliderect(rectangulo):
                    lista_colisiones.append("hb_abajo_2")
                if self.hb_arriba_2.colliderect(rectangulo):
                    lista_colisiones.append("hb_arriba_2")
                if self.hb_izq_2.colliderect(rectangulo):
                    lista_colisiones.append("hb_izquierda_2")
                if self.hb_der_2.colliderect(rectangulo):
                    lista_colisiones.append("hb_derecha_2")
                
        return lista_colisiones

    def colisiones_cajas(self, lista_cajas):
    
        lista_colisiones = []

        for caja in lista_cajas:
            rectangulo = caja.rectangulo
            if self.hb_abajo.colliderect(rectangulo):
                lista_colisiones.append("hb_abajo")
            if self.hb_arriba.colliderect(rectangulo):
                lista_colisiones.append("hb_arriba")
            if self.hb_izq.colliderect(rectangulo):
                lista_colisiones.append("hb_izquierda")
            if self.hb_der.colliderect(rectangulo):
                lista_colisiones.append("hb_derecha")
            if self.hb_abajo_2.colliderect(rectangulo):
                lista_colisiones.append("hb_abajo_2")
            if self.hb_arriba_2.colliderect(rectangulo):
                lista_colisiones.append("hb_arriba_2")
            if self.hb_izq_2.colliderect(rectangulo):
                lista_colisiones.append("hb_izquierda_2")
            if self.hb_der_2.colliderect(rectangulo):
                lista_colisiones.append("hb_derecha_2")

        return lista_colisiones
    
    def direccion_personaje(self):
        tecla = pygame.key.get_pressed()
        retorno = False

        if tecla[pygame.K_LEFT]:
            retorno = "izquierda"
            self.direccion_vista = "izquierda"
        elif tecla[pygame.K_RIGHT]: 
            retorno = "derecha"
            self.direccion_vista = "derecha"
        elif tecla[pygame.K_UP]:
            retorno = "arriba"
        elif tecla[pygame.K_DOWN]:
            retorno = "abajo"

        return retorno

    def reiniciar_posicion(self):
        self.rectangulo.x, self.rectangulo.y = self.posicion_inicial

class Caja():
    
    def __init__(self, x, y, color, ancho, alto):
        self.rectangulo = pygame.Rect(x, y, ancho, alto)
        self.posicion_inicial = (x, y)
        self.imagen = pygame.image.load("Juego\caja.png")
        self.imagen_reescalada = pygame.transform.smoothscale(self.imagen, (50, 50))
        self.color = color
        self.hb_izq = pygame.Rect(self.rectangulo.x - 5, self.rectangulo.y, 5, 50)
        self.hb_der = pygame.Rect(self.rectangulo.x + 50, self.rectangulo.y, 5, 50)
        self.hb_arriba = pygame.Rect(self.rectangulo.x, self.rectangulo.y - 5, 50, 5)
        self.hb_abajo = pygame.Rect(self.rectangulo.x, self.rectangulo.y + 50, 50, 5)

    def mover(self, ancho, alto):
        self.rectangulo.x += ancho
        self.rectangulo.y += alto

    def dibujar(self, superficie):
        superficie.blit(self.imagen_reescalada, (self.rectangulo.x, self.rectangulo.y))

    def arrastrarse(self, personaje, lista_cajas, escenario):
        colision_pared = self.colision_con_muros(escenario)
        colision_personaje = self.rectangulo.colliderect(personaje.rectangulo)
        colision_caja = self.colisiona_con_otras_cajas(lista_cajas)
        direccion = self.direccion_caja()

        if colision_personaje:
            tecla = self.direccion_caja()

            if direccion == "izquierda":
                if (colision_caja == "izquierda" or colision_pared == "izquierda"):
                    self.mover(0, 0)
                elif (colision_caja != "izquierda" or colision_pared != "izquierda"):
                    self.mover(-50, 0)
            elif direccion == "derecha":
                if (colision_caja == "derecha" or colision_pared == "derecha"):
                    self.mover(0, 0)
                elif direccion == "derecha" and (colision_caja != "derecha" or colision_pared != "derecha"):
                     self.mover(50, 0)
            elif direccion == "arriba":
                if (colision_caja == "arriba" or colision_pared == "arriba"):
                    self.mover(0, 0)
                elif (colision_caja != "arriba" or colision_pared != "arriba"):
                    self.mover(0, -50)
            elif direccion == "abajo":
                if (colision_caja == "abajo" or colision_pared == "abajo"):
                    self.mover(0, 0)
                elif (colision_caja != "abajo" or colision_pared != "abajo"):
                    self.mover(0, 50)

        self.hb_izq = pygame.Rect(self.rectangulo.x - 5, self.rectangulo.y, 5, 50)
        self.hb_der = pygame.Rect(self.rectangulo.x + 50, self.rectangulo.y, 5, 50)
        self.hb_arriba = pygame.Rect(self.rectangulo.x, self.rectangulo.y - 5, 50, 5)
        self.hb_abajo = pygame.Rect(self.rectangulo.x, self.rectangulo.y + 50, 50, 5)

    def colision_con_muros(self, escenario):
    
        direccion = self.direccion_caja()
        retorno = False
        posiciones_elementos = escenario.generar_posiciones_elementos()

        for elemento in posiciones_elementos:
            rectangulo = elemento['rectangulo']

            if elemento['tipo'] == "#":
                if self.hb_abajo.colliderect(rectangulo) and direccion == "abajo":
                    retorno = "abajo"
                elif self.hb_arriba.colliderect(rectangulo) and direccion == "arriba":
                    retorno = "arriba"
                elif self.hb_izq.colliderect(rectangulo) and direccion == "izquierda":
                    retorno = "izquierda"
                elif self.hb_der.colliderect(rectangulo) and direccion == "derecha":
                    retorno = "derecha"

        return retorno
    
    def colision_con_suelo_especial(self, escenario):
    
        retorno = False
        posiciones_elementos = escenario.generar_posiciones_elementos()

        for elemento in posiciones_elementos:
            rectangulo = elemento['rectangulo']

            if elemento['tipo'] == "F":
                if self.rectangulo.colliderect(rectangulo):
                    retorno = "suelo_especial"

        return retorno

    def direccion_caja(self):
        tecla = pygame.key.get_pressed()
        retorno = False
        if tecla[pygame.K_LEFT]: 
            retorno = "izquierda"
        if tecla[pygame.K_RIGHT]: 
            retorno = "derecha"
        if tecla[pygame.K_UP]:
            retorno = "arriba"
        if tecla[pygame.K_DOWN]:
            retorno = "abajo"
        return retorno

    def colisiona_con_otras_cajas(self, lista_cajas):
        retorno = False
        for otra_caja in lista_cajas:
            if self is not otra_caja:
                if self.hb_izq.colliderect(otra_caja.rectangulo):
                    retorno = "izquierda"
                if self.hb_der.colliderect(otra_caja.rectangulo):
                    retorno = "derecha"
                if self.hb_arriba.colliderect(otra_caja.rectangulo):
                    retorno = "arriba"
                if self.hb_abajo.colliderect(otra_caja.rectangulo):
                    retorno = "abajo"

        return retorno

    def reiniciar_posicion(self):
        self.rectangulo.x, self.rectangulo.y = self.posicion_inicial
class Escenario():

    def __init__(self, matriz, x_inicial_matriz, y_inicial_matriz):
        self.matriz = matriz
        self.x_inicial_matriz = x_inicial_matriz
        self.y_inicial_matriz = y_inicial_matriz
        self.elemento_muro = "#"
        self.elemento_suelo = "S"
        self.elemento_suelo_especial = "F"
        self.tamaño_cuadricula = 50
        self.imagen_suelo_reescalada = pygame.transform.scale(
            pygame.image.load("Juego\piso.jpg"),
            (self.tamaño_cuadricula, self.tamaño_cuadricula)
        )
        self.rectangulo_suelo = self.imagen_suelo_reescalada.get_rect()
        self.imagen_suelo_reescalada_suelo_especial = pygame.transform.scale(
            pygame.image.load("Juego\pisoEspecial.jpg"),
            (self.tamaño_cuadricula, self.tamaño_cuadricula)
        )
        self.rectangulo_suelo_especial = self.imagen_suelo_reescalada.get_rect()
        self.imagen_muro_reescalada = pygame.transform.scale(
            pygame.image.load("Juego\ladrillo.png"),
            (self.tamaño_cuadricula, self.tamaño_cuadricula)
        )
        self.rectangulo_muro = self.imagen_muro_reescalada.get_rect()

    def dibujar_desde_matriz(self, superficie):
        for i, fila in enumerate(self.matriz):
            for j, elemento in enumerate(fila):
                x = j * self.tamaño_cuadricula + self.x_inicial_matriz
                y = i * self.tamaño_cuadricula + self.y_inicial_matriz

                if elemento == self.elemento_muro:
                    superficie.blit(self.imagen_muro_reescalada, (x, y))
                elif elemento == self.elemento_suelo:
                    superficie.blit(self.imagen_suelo_reescalada, (x, y))
                elif elemento == self.elemento_suelo_especial:
                    superficie.blit(self.imagen_suelo_reescalada_suelo_especial, (x, y))

    def generar_posiciones_elementos(self):
        posiciones = []

        for i, fila in enumerate(self.matriz):
            for j, elemento in enumerate(fila):
                x = j * self.tamaño_cuadricula + self.x_inicial_matriz
                y = i * self.tamaño_cuadricula + self.y_inicial_matriz

                posiciones.append({
                    'tipo': elemento,
                    'rectangulo': pygame.Rect(x, y, self.tamaño_cuadricula, self.tamaño_cuadricula),
                    'x_inicial_matriz': self.x_inicial_matriz,
                    'y_inicial_matriz': self.y_inicial_matriz
                })
        return posiciones

class Nivel():

    def __init__(self, numero_nivel, matriz_nivel, ruta_imagen_de_fondo, lista_de_cajas, personaje, superficie, escenario):
        self.numero_nivel = numero_nivel
        self.matriz_nivel = matriz_nivel
        self.imagen_de_fondo = pygame.image.load(ruta_imagen_de_fondo)
        self.imagen_fondo_reescalada = pygame.transform.smoothscale(self.imagen_de_fondo, (800, 600))
        self.lista_de_cajas = lista_de_cajas
        self.personaje = personaje
        self.superficie = superficie
        self.escenario = escenario

    def dibujar_nivel(self):
        
        self.superficie.blit(self.imagen_fondo_reescalada, (0, 0))
        self.escenario.dibujar_desde_matriz(self.superficie)
        self.personaje.manejar_teclas(self.lista_de_cajas, self.escenario)
        self.personaje.dibujarse(self.superficie)
        for caja in self.lista_de_cajas:
            caja.colision_con_muros(self.escenario)
            caja.colisiona_con_otras_cajas(self.lista_de_cajas)
            caja.arrastrarse(self.personaje, self.lista_de_cajas, self.escenario)
            caja.dibujar(self.superficie)

    def pasar_de_nivel(self, lista_de_cajas):
        retorno = False
        lista_cajas_piso = []

        for caja in lista_de_cajas:
            if caja.colision_con_suelo_especial(self.escenario) != False:
                lista_cajas_piso.append("Colisión")

        if len(lista_cajas_piso) == len(lista_de_cajas):
            retorno = True

        return retorno

    def resetear_nivel(self):

        self.personaje.reiniciar_posicion()
        for caja in self.lista_de_cajas:
            caja.reiniciar_posicion()