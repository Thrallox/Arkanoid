import pygame as pg 
import sys
import random
import entidades

#Se crea la clase de nuestro juego 
class Game:
    def __init__(self): #Metodo init para iniciar la clase 
        self.pantalla = pg.display.set_mode((800,600))
        pg.display.set_caption("Futuro Arkanoid")
        self.pelota = entidades.Pelota(400,300,10,10,(251,202,239),25)

#Bucle principal que mantiene nuestro juego activo y procesando eventos 
    def bucle_principal(self):
        game_over = False
        while not game_over: 
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            

            if self.pelota.rect.left <= 0 or self.pelota.rect.right >= 800:
                self.pelota.vx = -self.pelota.vx

            if self.pelota.rect.top <= 0 or self.pelota.rect.bottom >= 600:
                self.pelota.vy = -self.pelota.vy

            self.pelota.x += self.pelota.vx
            self.pelota.y += self.pelota.vy

            self.pantalla.fill((0,0,255))
            self.pantalla.blit(self.pelota.imagen,(self.pelota.x, self.pelota.y))



            pg.display.flip()



#Inicia todos los modulos de pygame necesarios para que funcione
if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_principal()
