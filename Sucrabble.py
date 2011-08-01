import pygame
import game
from pygame import Rect
import gtk

black = 0, 0, 0
white = 255, 255, 255
gray = 192,192,192
green = 100, 255, 100
red = 255, 150, 150
blue = 150, 150, 255
# Tamanho del tablero
BOARD_SIZE = 15 
# Tamanho de la celda del atril
ATRIL = 60
# Tamanho de la celda del tablero
BOARD = 40

class Sucrabble:

    def __init__(self):
        # contendra la referencia a la pantalla
        self.screen = None
        self.tablero = []
        self.atril = []
        # se lee la imagen
        self.image = pygame.image.load("Recursos/ficha.png")
        self.image_vacia=pygame.image.load("Recursos/ficha-vacia.png")
        self.image.set_colorkey(white)
        self.juego=game.Game()
    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    def dibujar_celda(self, topleft, width,image,letra_name=None):
        """ 
        Coloca la imagen de la celda en la posicion "topleft", 
        con un ancho "width".
        Retrona un Rect que representa la posicion y el tamanho
        de la celda.
        """
        x, y = topleft 
        height = width # siempre es cuadrado
        # TO DO: cada celda, de acuerdo a su posicion, debe tener una 
        # imagen correspondiente.
        # Se cambia el tamanho de la imagen y se dibuja
        image = pygame.transform.scale(image, (width-1, height-1))
        self.screen.blit(image, topleft)
        if not (letra_name==None):
            letra = pygame.image.load("Recursos/Letras/"+str(letra_name)+".png")
            letra.set_colorkey(white)
            letra = pygame.transform.scale(letra, (width-10, height-10))
            self.screen.blit(letra, (topleft[0] + 4, topleft[1] + 4))
        return Rect(x, y, width, height)

    def dibujar_tablero(self, x_inicial, y_inicial):
        # recibe la posicion topleft donde se dibujara el tablero 
        x, y = x_inicial, y_inicial
        #self.image = pygame.image.load("Recursos/ficha-vacia.png")
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                r = self.dibujar_celda((x,y), BOARD, self.image_vacia)
                self.tablero.append(r)
                x = x + BOARD
            x = x_inicial
            y = y + BOARD
        
    def dibujar_atril(self, x_inicial, y_inicial):
        # recibe la posicion topleft donde se dibujara el atril 
        x, y = x_inicial, y_inicial
        self.letra=self.juego.get_user_letters()
        for i in range(7):
            r = self.dibujar_celda((x,y), ATRIL,self.image,self.letra[i].get_character())
            self.atril.append(r)
            x = x + ATRIL
        
    def load_picture(self,image,width,escala,rect):
        height = width # siempre es cuadrado
        # imagen correspondiente.
        # Se cambia el tamanho de la imagen y se dibuja
        image = pygame.transform.scale(image, (width-escala, height-escala))
        self.screen.blit(image,rect)
          
    def run(self):
        self.screen = pygame.display.set_mode()
        #self.screen = pygame.display.set_mode((800,600)) 
        self.screen.fill(gray)
        center = self.screen.get_rect().center
        # TO DO: las posiciones deben ser relativas al tamanho 
        # de la pantalla
        self.dibujar_tablero(center[0] - BOARD*7+BOARD/2,20)
        self.dibujar_atril(center[0] - ATRIL*3 , center[1] + BOARD*7)
        pygame.display.flip()
        self.quit = False
        colocarFicha = False
        seleccionarFicha = True
        while not self.quit: 
            while gtk.events_pending():
                gtk.main_iteration()
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y =event.pos
                    if colocarFicha:
                        for celda in self.tablero:
                            if celda.collidepoint(mouse_x, mouse_y):
                                #pygame.draw.rect(self.screen, blue, celda)
                                #self.load_picture(self.image,BOARD,1,celda)
                                self.dibujar_celda(celda.topleft, BOARD,self.image,ficha_atril)
                                # Agregar el movimiento a la lista de movimientos
                                # Poner en modo seleccionar ficha
                                colocarFicha = False
                                seleccionarFicha = True
                    elif seleccionarFicha:
                        i=-1;
                        for celda in self.atril:
                            i=i+1;
                            if celda.collidepoint(mouse_x, mouse_y):
                                #pygame.draw.rect(self.screen, red, celda)
                                self.load_picture(self.image_vacia,ATRIL,1,celda)
                                # Poner en modo colocar fihca
                                colocarFicha = True
                                x,y = celda.topleft
                                #index = ((center[0] - 210) - x)/ATRIL
                                #print self.letra
                                ficha_atril = self.letra[i].get_character()
                                #print "\nindex",index,"\nletra",self.letra[index].get_character()
                                seleccionarFicha = False
                    pygame.display.flip()

if __name__ == '__main__' :
    pygame.init()
    pygame.display.set_caption("PyGame intro")
    game = Sucrabble()
    game.run()
