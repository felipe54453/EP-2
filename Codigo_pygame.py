#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:51:07 2019

@author: joaoluizleaobueno
"""

import pygame
import random
from os import path

#diretorios de imagem e som
img_dir = path.join(path.dirname(__file__), 'sprites')

WIDTH = 380 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # F

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)




class Player(pygame.sprite.Sprite):

    def __init__(self, player_img):
        #construtor e coletar imagem 
        pygame.sprite.Sprite.__init__(self)    
        self.image = player_img 
        self.image = pygame.transform.scale(player_img, (45, 45))   
        self.image.set_colorkey(BLACK)   
        self.rect = self.image.get_rect()
            
        #posicoes
        self.rect.y = HEIGHT/2
        self.rect.x = (WIDTH/2)-30
        #raio
       

        self.speedx = 2 

        self.speedy = 2
       
    def update(self):
        self.rect.y += self.speedy 
        if self.rect.y <= 0:
            self.rect.y = 0
            self.speedy = 0 
        if self.speedy > 2:
            self.speedy = 2
        self.rect.x += self.speedx 
        if self.rect.x <= 0:
            self.rect.x = 0
            self.speedx = 0
        if self.speedy > 2:
            self.speedy = 2
        if self.speedx > 2:
            self.speedx = 2
            


class Tela_de_fundo(pygame.sprite.Sprite): 

   def __init__(self,base,x,y):

       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.transform.scale(base,(1,150))
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()

       # posicao 
       self.rect.x = x
       self.rect.y = y

       #velocidade
       self.speedx = 0
       self.speedy = -4.5 

   def update(self):
       self.rect.y += self.speedy 
       
class Carros_aleatorios(pygame.sprite.Sprite):

   def __init__(self, Carros_aleatorios,x):

       pygame.sprite.Sprite.__init__(self)

       #define a largura aleatoria do cano
       aleatorio = random.randint(100,350)

       self.image = pygame.transform.scale(Carros_aleatorios, (80, 600))       
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()

       #poscicoes 
       self.rect.top =  aleatorio
       self.rect.x = x

       self.speedx = 0
       self.speedy = -4.5



   #def update(self):
   def update(self):
       self.rect.y += self.speedy 
       if self.speedy > -4.5:
           self.speedy = -4.5

      
def load_assets(img_dir):
   assets = {}
   assets["Player"] = pygame.image.load(path.join(img_dir, "Player.png")).convert_alpha()
   assets["canodecima"] = pygame.image.load(path.join(img_dir, "upper_pipe_img.png")).convert_alpha()
   assets['canodebaixo']=pygame.image.load(path.join(img_dir, "lower_pipe_img.png")).convert_alpha()
   assets['barulho_pulo']=pygame.mixer.Sound(path.join(img_dir, 'swoosh.wav'))
   assets['background']=pygame.image.load(path.join(img_dir, "backgroundnovo.png")).convert_alpha()
   assets['barulho_pulo']=pygame.mixer.Sound(path.join(img_dir, 'swoosh.wav')) 
   assets['Tela_de_fundo'] = pygame.image.load(path.join(img_dir, "base.png"))
   assets['hit'] = pygame.mixer.Sound(path.join(img_dir, 'hit.wav'))
   assets['score0'] = pygame.image.load(path.join(img_dir, "0.png")).convert_alpha()
   assets['score1'] = pygame.image.load(path.join(img_dir, "1.png")).convert_alpha()
   assets['score2'] = pygame.image.load(path.join(img_dir, "2.png")).convert_alpha()
   assets['score3'] = pygame.image.load(path.join(img_dir, "3.png")).convert_alpha()
   assets['score4'] = pygame.image.load(path.join(img_dir, "4.png")).convert_alpha()
   assets['score5'] = pygame.image.load(path.join(img_dir, "5.png")).convert_alpha()
   assets['score6'] = pygame.image.load(path.join(img_dir, "6.png")).convert_alpha()
   assets['score7'] = pygame.image.load(path.join(img_dir, "7.png")).convert_alpha()
   assets['score8'] = pygame.image.load(path.join(img_dir, "8.png")).convert_alpha()
   assets['score9'] = pygame.image.load(path.join(img_dir, "9.png")).convert_alpha()   
   assets['song'] = pygame.mixer.Sound(path.join(img_dir, 'song.wav')) 
   assets['point'] = pygame.mixer.Sound(path.join(img_dir, 'point.wav'))
   assets['inicio'] = pygame.image.load(path.join(img_dir, "inicio.png")).convert_alpha()   
   assets['jod2'] = pygame.image.load(path.join(img_dir, "jod2.png")).convert_alpha()
   assets['jod3'] = pygame.image.load(path.join(img_dir, "jod3.png")).convert_alpha()
   assets['jod4'] = pygame.image.load(path.join(img_dir, "jod4.png")).convert_alpha()
   assets['jod5'] = pygame.image.load(path.join(img_dir, "jod5.png")).convert_alpha()
   assets['jod6'] = pygame.image.load(path.join(img_dir, "jod6.png")).convert_alpha()
   assets['jod7'] = pygame.image.load(path.join(img_dir, "jod8.png")).convert_alpha()
   assets['jod9'] = pygame.image.load(path.join(img_dir, "jod9.png")).convert_alpha()
   assets['Canodecima1'] = pygame.image.load(path.join(img_dir, "Canodecima1.png")).convert_alpha()
   assets['Canodebaixo1'] = pygame.image.load(path.join(img_dir, "Canodebaixo1.png")).convert_alpha()
   assets['background1'] = pygame.image.load(path.join(img_dir, "background.png")).convert_alpha()
   assets['gameover1'] = pygame.image.load(path.join(img_dir, "gameover1.png")).convert_alpha()
   assets['telainicial1'] = pygame.image.load(path.join(img_dir, "telainicial1.png")).convert_alpha()
   assets['jodpulando'] = pygame.image.load(path.join(img_dir, "jodpulando.png")).convert_alpha()
   assets['femalejod'] = pygame.image.load(path.join(img_dir, "femaleJod.png")).convert_alpha()
   assets['chooseyourskin'] = pygame.image.load(path.join(img_dir, "chooseyourskin.png")).convert_alpha()
   return assets      

def menu(screen):
	
	#Carrega a musica do jogo
	pygame.mixer.music.load(path.join(snd_dir, 'CarelessWhisper.mp3'))
	pygame.mixer.music.set_volume(0.4)
	pygame.mixer.music.play(loops=-1)

	assets = load_assets(img_dir)
	background = pygame.transform.scale(assets["menu"], (WIDTH, HEIGHT))
	background_rect = background.get_rect()
	state = MENU
	while state == MENU:
		screen.blit(background,background_rect)
		score_font= pygame.font.Font(path.join(fnt_dir, "i_fink_u_freeky.ttf"),50)
		text_surface= score_font.render("Benga dos Bengas", True, WHITE)
		text_rect= text_surface.get_rect()
		text_rect.centery = (HEIGHT/2)
		text_rect.centerx = (WIDTH/2)
		screen.blit(text_surface, text_rect)
		score_font= pygame.font.Font(path.join(fnt_dir, "i_fink_u_freeky.ttf"),28)
		text_surface= score_font.render("Aperte espaço para começar", True, WHITE)
		text_rect = text_surface.get_rect()
		text_rect.bottom = (HEIGHT -68)
		text_rect.centerx = (WIDTH/2)
		screen.blit(text_surface, text_rect)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					state = JOGO
		pygame.display.flip()
	return (state)
       
       
       
       
       
       