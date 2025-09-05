"""
Gioco Pong. La schermata di 'congratulazioni' e' incompleta.
"""

import pygame, random

 #colori
ROSA = pygame.Color("Pink")
BLU = pygame.Color("Blue")
BIANCO = pygame.Color("White")
NERO = pygame.Color("Black")
ROSSO = pygame.Color("Red")
VERDE = pygame.Color("Green")
GIALLO = pygame.Color("Yellow")
    
class Pong:
    
    def __init__(self):
        #variabili
        self.LARGHEZZA = 900  #larghezza schermo di gioco
        self.ALTEZZA = 550   #altezza schermo di gioco
        self.LARGHEZZA_racchetta = 15
        self.ALTEZZA_racchetta = 100
        self.LARGHEZZA_surf = self.LARGHEZZA-80
        self.ALTEZZA_surf = self.ALTEZZA-80
        self.raggio_palla = 12
        self.x_racchetta_1 = 5
        self.y_racchetta_1 = self.ALTEZZA//2-self.ALTEZZA_racchetta//2
        self.x_racchetta_2 = self.LARGHEZZA-self.LARGHEZZA_racchetta-5
        self.y_racchetta_2 = self.ALTEZZA//2-self.ALTEZZA_racchetta//2
        self.vel_y_racchetta_1 = 0
        self.vel_y_racchetta_2 = 0
        self.x_palla = self.LARGHEZZA//2
        self.y_palla = self.ALTEZZA//2
        self.vel_xy_palla = 0.8
        self.vel_x_palla=random.choice([-self.vel_xy_palla,self.vel_xy_palla])
        self.vel_y_palla=random.choice([-self.vel_xy_palla,self.vel_xy_palla])
        self.punteggio_giocatore_1 = 0
        self.punteggio_giocatore_2 = 0
        self.velocitaRacchettaSingolo = 2.7  #2.9 o 3 aumenta il livello di difficolta'
        self.x_testo_rivincita = 145
        self.y_testo_rivincita = 370
        self.x_testo_esci = 550
        self.y_testo_esci = 370
        self.colore_freccia_superiore = VERDE
        self.colore_freccia_inferiore = VERDE
        self.orologio = pygame.time.Clock()
        self.FPS = 60
        self.NOME_GIOCO = "Pong"
        self.goal = 5  #punteggio obiettivo
    
    #getters
    
    def get_y_racchetta_1(self):
        return self.y_racchetta_1
    
    def get_x_racchetta_1(self):
        return self.x_racchetta_1
    
    def get_y_racchetta_2(self):
        return self.y_racchetta_2
    
    def get_x_racchetta_2(self):
        return self.x_racchetta_2
    
    def getVel_y_racchetta_1(self):
        return self.vel_y_racchetta_1
    
    def getVel_y_racchetta_2(self):
        return self.vel_y_racchetta_2
        
    def get_x_palla(self):
        return self.x_palla
    
    def get_y_palla(self):
        return self.y_palla
    
    def getVel_x_palla(self):
        return self.vel_x_palla
    
    def getVel_y_palla(self):
        return self.vel_y_palla
    
    def get_raggio_palla(self):
        return self.raggio_palla
    def getVelocitaRacchettaSingolo(self):
        return self.velocitaRacchettaSingolo
        
    def get_vel_xy_palla(self):
        return self.vel_xy_palla
        
    def get_punteggio_giocatore_1(self):
        return self.punteggio_giocatore_1
    
    def get_punteggio_giocatore_2(self):
        return self.punteggio_giocatore_2
        
    def getColoreFrecciaInferiore(self):
        return self.colore_freccia_inferiore
        
    def getColoreFrecciaSuperiore(self):
        return self.colore_freccia_superiore  

    def getOrologio(self):
        return self.orologio
        
    def getFPS(self):
        return self.FPS
        
    def getGoal(self):
        return self.goal
        
        
    #setters
    
    def set_y_racchetta_1(self,y_racchetta_1):
        self.y_racchetta_1 = y_racchetta_1
    
    def set_x_racchetta_1(self,x_racchetta_1):
        self.x_racchetta_1 = x_racchetta_1
        
    def set_y_racchetta_2(self,y_racchetta_2):
        self.y_racchetta_2 = y_racchetta_2
    
    def set_x_racchetta_2(self,x_racchetta_2):
        self.x_racchetta_2 = x_racchetta_2
    
    def setVel_y_racchetta_1(self,vel_y_racchetta_1):
        self.vel_y_racchetta_1 = vel_y_racchetta_1
    
    def setVel_y_racchetta_2(self,vel_y_racchetta_2):
        self.vel_y_racchetta_2 = vel_y_racchetta_2
    
    def set_x_palla(self,x_palla):
        self.x_palla = x_palla
    
    def set_y_palla(self,y_palla):
        self.y_palla = y_palla
    
    def setVel_x_palla(self,vel_x_palla):
        self.vel_x_palla = vel_x_palla
        
    def setVel_y_palla(self,vel_y_palla):
        self.vel_y_palla = vel_y_palla
        
    def set_raggio_palla(self,raggio_palla):
        self.raggio_palla = raggio_palla
        
    def set_vel_xy_palla(self,vel_xy_palla):
        self.vel_xy_palla = vel_xy_palla
        
    def set_punteggio_giocatore_1(self,punteggio_giocatore_1):
        self.punteggio_giocatore_1 = punteggio_giocatore_1
    
    def set_punteggio_giocatore_2(self,punteggio_giocatore_2):
        self.punteggio_giocatore_2 = punteggio_giocatore_2
    
    def setColoreFrecciaInferiore(self,colore_freccia_inferiore):
        self.colore_freccia_inferiore = colore_freccia_inferiore
    
    def setColoreFrecciaSuperiore(self,colore_freccia_superiore):
        self.colore_freccia_superiore = colore_freccia_superiore
    
    def tasto_premuto_giocatore_singolo(self,tasto):
        if tasto == pygame.K_UP:
            self.setVel_y_racchetta_1(self.getVel_y_racchetta_1()-8)
        elif tasto == pygame.K_DOWN:
            self.setVel_y_racchetta_1(self.getVel_y_racchetta_1()+8)
        
    def tasto_lasciato_giocatore_singolo(self,tasto):
        if tasto == pygame.K_UP or tasto == pygame.K_DOWN:
            self.setVel_y_racchetta_1(0)
        
    def movimento_giocatore_singolo(self,schermata):
        self.set_y_racchetta_1(self.get_y_racchetta_1() + self.getVel_y_racchetta_1())
        if self.get_y_racchetta_1()<0:
            self.set_y_racchetta_1(0)
        elif self.get_y_racchetta_1()>self.ALTEZZA-self.ALTEZZA_racchetta:
            self.set_y_racchetta_1(self.ALTEZZA-self.ALTEZZA_racchetta)
        elif self.get_y_racchetta_2()<0:
            self.set_y_racchetta_2(0)
        elif self.get_y_racchetta_2()>self.ALTEZZA-self.ALTEZZA_racchetta:
            self.set_y_racchetta_2(self.ALTEZZA-self.ALTEZZA_racchetta)
        if self.get_y_racchetta_2()>self.y_palla and self.x_palla>self.LARGHEZZA//2:
            self.set_y_racchetta_2(self.get_y_racchetta_2()-self.getVelocitaRacchettaSingolo())
        elif self.get_y_racchetta_2()<self.y_palla and self.x_palla>self.LARGHEZZA//2:
            self.set_y_racchetta_2(self.get_y_racchetta_2()+self.getVelocitaRacchettaSingolo())
    
        schermata.fill(ROSA)
        pong.disegna_racchette(schermata)
        pong.posizione_palla_e_punteggio(schermata)
        pong.disegna_scritte_giocatore_singolo(schermata) 
        pygame.display.update()   
        
    def disegna_schermata(self):
        schermata = pygame.display.set_mode((self.LARGHEZZA, self.ALTEZZA))
        pygame.display.set_caption(self.NOME_GIOCO)
        return schermata
    
    def disegna_palla(self,schermata):
        palla = pygame.draw.circle(schermata, BLU, (self.x_palla, self.y_palla), self.raggio_palla,0)
        return palla
    
    def disegna_racchette(self,schermata):
        racchetta_sx = pygame.draw.rect(schermata, BLU, (self.x_racchetta_1, self.y_racchetta_1, self.LARGHEZZA_racchetta, self.ALTEZZA_racchetta), 0)
        racchetta_dx = pygame.draw.rect(schermata, BLU, (self.x_racchetta_2, self.y_racchetta_2, self.LARGHEZZA_racchetta, self.ALTEZZA_racchetta), 0)
        return racchetta_sx, racchetta_dx
        
    def posizione_palla_e_punteggio(self,schermata):   
        self.set_x_palla(self.get_x_palla() + self.getVel_x_palla())
        self.set_y_palla(self.get_y_palla() + self.getVel_y_palla())
        
        racchetta_sx,racchetta_dx = self.disegna_racchette(schermata)
    
        if self.get_y_palla()-self.get_raggio_palla()<0 or self.get_y_palla()+self.get_raggio_palla()>self.ALTEZZA:
            self.setVel_y_palla(self.getVel_y_palla()*(-1))        
        elif self.get_x_palla()-self.get_raggio_palla()<0:
            self.setVel_x_palla(random.choice([-self.get_vel_xy_palla(),self.get_vel_xy_palla()]))
            self.vel_y_palla=random.choice([-self.get_vel_xy_palla(),self.get_vel_xy_palla()])
            self.set_x_palla(self.LARGHEZZA//2)
            self.set_y_palla(self.ALTEZZA//2)

            self.set_punteggio_giocatore_2(self.get_punteggio_giocatore_2() + 1)
        elif self.get_x_palla()+self.get_raggio_palla()>self.LARGHEZZA:
            self.setVel_x_palla(random.choice([-self.get_vel_xy_palla(),self.get_vel_xy_palla()]))
            self.vel_y_palla=random.choice([-self.get_vel_xy_palla(),self.get_vel_xy_palla()])
            self.set_x_palla(self.LARGHEZZA//2)
            self.set_y_palla(self.ALTEZZA//2)

            self.set_punteggio_giocatore_1(self.get_punteggio_giocatore_1() + 1)
        elif racchetta_sx.colliderect(self.disegna_palla(schermata)):
            self.setVel_x_palla(self.get_vel_xy_palla())
        elif racchetta_dx.colliderect(self.disegna_palla(schermata)):
            self.setVel_x_palla(-self.get_vel_xy_palla())
        
        self.disegna_palla(schermata)
    
    
    def disegna_scritte_giocatore_singolo(self,schermata):
        font_giocatore_singolo = pygame.font.SysFont(None,30,False,True)
        font_punteggio_giocatore_1 = pygame.font.SysFont(None,80,True,False)
        font_punteggio_giocatore_2 = pygame.font.SysFont(None,80,True,False)
        testo_font_giocatore_singolo = font_giocatore_singolo.render("GIOCATORE SINGOLO! Punteggio (obiettivo: "+str(self.getGoal())+"): ",True,ROSSO)
        testo_font_punteggio_giocatore_1 = font_punteggio_giocatore_1.render(str(self.get_punteggio_giocatore_1()),True,ROSSO)
        testo_font_punteggio_giocatore_2 = font_punteggio_giocatore_2.render(str(self.get_punteggio_giocatore_2()),True,ROSSO)
        linea_sinistra = pygame.draw.line(schermata,NERO,(self.get_x_racchetta_1()+self.LARGHEZZA_racchetta//2,0),(self.get_x_racchetta_1()+self.LARGHEZZA_racchetta//2,self.ALTEZZA),1)
        linea_di_mezzo = pygame.draw.line(schermata,NERO,(self.LARGHEZZA//2,0),(self.LARGHEZZA//2,self.ALTEZZA),1)
        linea_destra = pygame.draw.line(schermata,NERO,(self.x_racchetta_2+self.LARGHEZZA_racchetta//2,0),(self.x_racchetta_2+self.LARGHEZZA_racchetta//2,self.ALTEZZA),1)
        contorno = pygame.draw.circle(schermata,NERO,(self.LARGHEZZA//2,self.ALTEZZA//2),self.raggio_palla+1,2)
        schermata.blit(testo_font_giocatore_singolo,(217,10))
        schermata.blit(testo_font_punteggio_giocatore_1,(350,35))
        schermata.blit(testo_font_punteggio_giocatore_2,(510,35))
        trattino_punteggio = pygame.draw.rect(schermata,ROSSO,(430,55,40,10),0)
        return testo_font_punteggio_giocatore_1,testo_font_punteggio_giocatore_2
    
    def freccie_surf(self,surf):
        coordinate_rettangolo_freccia_superiore = pygame.draw.rect(surf,self.colore_freccia_superiore,(self.LARGHEZZA_surf//2-5,155,10,60),0)
        coordinate_rettangolo_freccia_inferiore = pygame.draw.rect(surf,self.colore_freccia_inferiore,(self.LARGHEZZA_surf//2-5,255,10,60),0)
        coordinate_triangolo_freccia_superiore = [[self.LARGHEZZA_surf//2-5-10,155],[self.LARGHEZZA_surf//2-5+20,155],[self.LARGHEZZA_surf//2,125]]
        coordinate_triangolo_freccia_inferiore = [[self.LARGHEZZA_surf//2-5-10,255+60],[self.LARGHEZZA_surf//2-5+20,255+60],[self.LARGHEZZA_surf//2,345]]
        triangolo_freccia_superiore = pygame.draw.polygon(surf,self.colore_freccia_superiore,coordinate_triangolo_freccia_superiore,0)
        triangolo_freccia_inferiore = pygame.draw.polygon(surf,self.colore_freccia_inferiore,coordinate_triangolo_freccia_inferiore,0)
    
    def schermata_pre_gioco(self,schermata):
        surf = pygame.Surface((self.LARGHEZZA_surf,self.ALTEZZA_surf))
        surf.fill(BIANCO)
        font_1 = pygame.font.SysFont(None,42,True,False)
        font_2 = pygame.font.SysFont(None,25,False,False)
        font_giocatore_singolo = pygame.font.SysFont(None,50,False,True)
        font_multigiocatore = pygame.font.SysFont(None,50,False,True)
        surf_testo_1 = font_1.render("PONG! SELEZIONA LA MODALITA' DI GIOCO!",True,ROSSO)
        surf_testo_2 = font_2.render("(Usa la freccia superiore e inferiore e premi ENTER per selezionare)",True,ROSSO)
        surf_testo_giocatore_singolo = font_giocatore_singolo.render("GIOCATORE SINGOLO",True,VERDE)
        surf_testo_multigiocatore = font_multigiocatore.render("MULTIGIOCATORE",True,VERDE)
        surf.blit(surf_testo_1,(100,20))
        surf.blit(surf_testo_2,(130,50))
        surf.blit(surf_testo_giocatore_singolo,(220,90))
        surf.blit(surf_testo_multigiocatore,(250,350))
        palla_grande_surf = pygame.draw.circle(surf,VERDE,(self.LARGHEZZA_surf//2,self.ALTEZZA_surf//2),15)
        self.freccie_surf(surf)
        schermata.blit(surf,(40,40))   
    

    def disegna_scritte_multigiocatore(self,schermata):
        font_multigiocatore = pygame.font.SysFont(None,30,False,True)
        font_punteggio_giocatore_1 = pygame.font.SysFont(None,80,True,False)
        font_punteggio_giocatore_2 = pygame.font.SysFont(None,80,True,False)
        testo_font_multigiocatore = font_multigiocatore.render("MULTIGIOCATORE! Punteggio (obiettivo: 11): ",True,ROSSO)
        testo_font_punteggio_giocatore_1 = font_punteggio_giocatore_1.render(str(self.get_punteggio_giocatore_1()),True,ROSSO)
        testo_font_punteggio_giocatore_2 = font_punteggio_giocatore_2.render(str(self.get_punteggio_giocatore_2()),True,ROSSO)
        linea_sinistra = pygame.draw.line(schermata,NERO,(self.get_x_racchetta_1()+self.LARGHEZZA_racchetta//2,0),(self.get_x_racchetta_1()+self.LARGHEZZA_racchetta//2,self.ALTEZZA),1)
        linea_di_mezzo = pygame.draw.line(schermata,NERO,(self.LARGHEZZA//2,0),(self.LARGHEZZA//2,self.ALTEZZA),1)
        linea_destra = pygame.draw.line(schermata,NERO,(self.get_x_racchetta_2()+self.LARGHEZZA_racchetta//2,0),(self.get_x_racchetta_2()+self.LARGHEZZA_racchetta//2,self.ALTEZZA),1)
        contorno = pygame.draw.circle(schermata,NERO,(self.LARGHEZZA//2,self.ALTEZZA//2),self.get_raggio_palla()+1,2)
        schermata.blit(testo_font_multigiocatore,(230,10))
        schermata.blit(testo_font_punteggio_giocatore_1,(350,35))
        schermata.blit(testo_font_punteggio_giocatore_2,(510,35))
        trattino_punteggio = pygame.draw.rect(schermata,ROSSO,(430,55,40,10),0)
        return testo_font_punteggio_giocatore_1,testo_font_punteggio_giocatore_2
    
    def movimento_multigiocatore(self,schermata):
        self.set_y_racchetta_1(self.get_y_racchetta_1()+self.getVel_y_racchetta_1())
        self.set_y_racchetta_2(self.get_y_racchetta_2()+self.getVel_y_racchetta_2())
        if self.get_y_racchetta_1()<0:
            self.set_y_racchetta_1(0)
        elif self.get_y_racchetta_1()>self.ALTEZZA-self.ALTEZZA_racchetta:
            self.set_y_racchetta_1(self.ALTEZZA-self.ALTEZZA_racchetta)  
        elif self.get_y_racchetta_2()<0:
            self.set_y_racchetta_2(0)
        elif self.get_y_racchetta_2()>self.ALTEZZA-self.ALTEZZA_racchetta:
            self.set_y_racchetta_2(self.ALTEZZA-self.ALTEZZA_racchetta)

        schermata.fill(ROSA)
        pong.disegna_racchette(schermata)
        pong.posizione_palla_e_punteggio(schermata)
        pong.disegna_scritte_multigiocatore(schermata) 
        pygame.display.update()
    
    
    def tasto_premuto_multigiocatore(self,tasto):
        if tasto == pygame.K_w:
            self.vel_y_racchetta_1-=8
        elif tasto == pygame.K_s:
            self.vel_y_racchetta_1+=8
        elif tasto == pygame.K_UP:
            self.vel_y_racchetta_2-=8
        elif tasto == pygame.K_DOWN:
            self.vel_y_racchetta_2+=8
        
    
    def tasto_lasciato_multigiocatore(self,tasto):
        if tasto == pygame.K_w:
            self.vel_y_racchetta_1=0
        elif tasto == pygame.K_s:
            self.vel_y_racchetta_1=0
        elif tasto == pygame.K_UP:
            self.vel_y_racchetta_2=0
        elif tasto == pygame.K_DOWN:
            self.vel_y_racchetta_2=0
    

    
    def giocatore_1_vincitore(self,schermata):
        surf_vincitore_2 = pygame.Surface((self.LARGHEZZA_surf,self.ALTEZZA_surf))
        surf_vincitore_2.fill(BIANCO)
        premio_1 = pygame.font.SysFont(None,95,True,False)
        premio_2 = pygame.font.SysFont(None,70,True,False)
        testo_premio = premio_1.render("CONGRATULAZIONI!",True,NERO)
        testo_premio_giocatore_2 = premio_2.render("GIOCATORE 1, HAI VINTO!!!",True,NERO)
        rivincita = pygame.font.SysFont(None,70,False,True)
        esci = pygame.font.SysFont(None,70,False,True)
        testo_rivincita = rivincita.render("RIVINCITA",True,ROSSO)
        testo_esci = esci.render("ESCI",True,ROSSO)
        surf_vincitore_2.blit(testo_premio,(20,20))
        surf_vincitore_2.blit(testo_premio_giocatore_2,(30,120))
        surf_vincitore_2.blit(testo_rivincita,(self.x_testo_rivincita,self.y_testo_rivincita))
        surf_vincitore_2.blit(testo_esci,(self.x_testo_esci,self.y_testo_esci))
        rect_testo_rivincita = pygame.draw.rect(surf_vincitore_2,NERO,(self.x_testo_rivincita-5,self.y_testo_rivincita-5,260,50),2)
        rect_testo_esci = pygame.draw.rect(surf_vincitore_2,NERO,(self.x_testo_esci-5,self.y_testo_esci-5,135,50),2)
        schermata.fill(ROSA)
        self.disegna_racchette(schermata)
        schermata.blit(surf_vincitore_2,(40,40))
        pygame.display.update()
        pygame.mixer.music.stop()
        musica_schermata_iniziale = pygame.mixer.music.load("pong_schermata_iniziale.mp3")
        pygame.mixer.music.play(-1)
    
        return rect_testo_esci
    
    def giocatore_2_vincitore(self,schermata):
        surf_vincitore_2 = pygame.Surface((self.LARGHEZZA_surf,self.ALTEZZA_surf))
        surf_vincitore_2.fill(BIANCO)
        premio_1 = pygame.font.SysFont(None,95,True,False)
        premio_2 = pygame.font.SysFont(None,70,True,False)
        testo_premio = premio_1.render("CONGRATULAZIONI!",True,NERO)
        testo_premio_giocatore_2 = premio_2.render("GIOCATORE 2, HAI VINTO!!!",True,NERO)
        rivincita = pygame.font.SysFont(None,70,False,True)
        esci = pygame.font.SysFont(None,70,False,True)
        testo_rivincita = rivincita.render("RIVINCITA",True,ROSSO)
        testo_esci = esci.render("ESCI",True,ROSSO)
        surf_vincitore_2.blit(testo_premio,(20,20))
        surf_vincitore_2.blit(testo_premio_giocatore_2,(30,120))
        surf_vincitore_2.blit(testo_rivincita,(self.x_testo_rivincita,self.y_testo_rivincita))
        surf_vincitore_2.blit(testo_esci,(self.x_testo_esci,self.y_testo_esci))
        rect_testo_rivincita = pygame.draw.rect(surf_vincitore_2,NERO,(self.x_testo_rivincita-5,self.y_testo_rivincita-5,260,50),2)
        rect_testo_esci = pygame.draw.rect(surf_vincitore_2,NERO,(self.x_testo_esci-5,self.y_testo_esci-5,135,50),2)   
        schermata.fill(ROSA)
        pong.disegna_racchette(schermata)
        schermata.blit(surf_vincitore_2,(40,40))
        pygame.display.update()
        pygame.mixer.music.stop()
        musica_schermata_iniziale = pygame.mixer.music.load("pong_schermata_iniziale.mp3")
        pygame.mixer.music.play(-1)
    
        return rect_testo_esci
    
    def mostra_vincitore(self, schermata, numero_giocatore):
        surf = pygame.Surface((self.LARGHEZZA_surf, self.ALTEZZA_surf))
        surf.fill(BIANCO)

        font_titolo = pygame.font.SysFont(None, 95, True, False)
        font_msg = pygame.font.SysFont(None, 70, True, False)
        font_btn = pygame.font.SysFont(None, 60, True, False)

        titolo = font_titolo.render("CONGRATULAZIONI!", True, NERO)
        msg = font_msg.render(f"GIOCATORE {numero_giocatore}, HAI VINTO!!!", True, BLU)
        btn_rivincita = font_btn.render("RIVINCITA", True, ROSSO)
        btn_esci = font_btn.render("ESCI", True, ROSSO)

        rect_titolo = titolo.get_rect(center=(self.LARGHEZZA_surf//2, 100))
        rect_msg = msg.get_rect(center=(self.LARGHEZZA_surf//2, 200))
        rect_riv = btn_rivincita.get_rect(center=(self.LARGHEZZA_surf//2, 320))
        rect_exit = btn_esci.get_rect(center=(self.LARGHEZZA_surf//2, 420))

        pygame.draw.rect(surf, NERO, rect_riv.inflate(30, 15), 2)
        pygame.draw.rect(surf, NERO, rect_exit.inflate(30, 15), 2)
        surf.blit(titolo, rect_titolo)
        surf.blit(msg, rect_msg)
        surf.blit(btn_rivincita, rect_riv)
        surf.blit(btn_esci, rect_exit)

        schermata.fill(ROSA)
        schermata.blit(surf, (40, 40))
        pygame.display.update()

        scelta = None
        in_loop = True
        while in_loop:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if rect_riv.inflate(30, 15).collidepoint(evento.pos):
                        scelta = "rivincita"
                        in_loop = False
                    elif rect_exit.inflate(30, 15).collidepoint(evento.pos):
                        scelta = "esci"
                        in_loop = False

            self.orologio.tick(self.FPS)

        return scelta

#inizio programma                                           
if __name__ == "__main__":
    pygame.init()
    
    pong = Pong()
    
    schermata = pong.disegna_schermata()
    schermata.fill(ROSA)
    pong.disegna_racchette(schermata)
    pong.disegna_palla(schermata)
    pong.schermata_pre_gioco(schermata)
    musica_schermata_iniziale = pygame.mixer.music.load("pong_schermata_iniziale.mp3")
    #loop infinito della canzone
    pygame.mixer.music.play(-1)
    pygame.display.update()

    schermata_surf_aperta = True
    
    #schermata iniziale

    while schermata_surf_aperta:
        pygame.init()
        for evento_surf in pygame.event.get():
            if evento_surf.type==pygame.QUIT:
                pygame.quit()
            elif evento_surf.type==pygame.KEYDOWN:
                if evento_surf.key==pygame.K_UP:
                    pong.setColoreFrecciaSuperiore(ROSSO)
                    pong.setColoreFrecciaInferiore(VERDE)
                    pong.schermata_pre_gioco(schermata)
                    pygame.display.update()                
                elif evento_surf.key==pygame.K_DOWN:
                    pong.setColoreFrecciaInferiore(ROSSO)
                    pong.setColoreFrecciaSuperiore(VERDE)
                    pong.schermata_pre_gioco(schermata)
                    pygame.display.update()
                if pong.getColoreFrecciaInferiore()==ROSSO:
                    if evento_surf.key==pygame.K_RETURN:                     
                        mod_multigiocatore = True
                        schermata_surf_aperta = False
                elif pong.getColoreFrecciaSuperiore()==ROSSO:
                    if evento_surf.key==pygame.K_RETURN:
                        mod_multigiocatore = False
                        schermata_surf_aperta = False
                    
    schermata = pong.disegna_schermata()
    schermata.fill(ROSA)

    pygame.display.update()
    musica = pygame.mixer.music.load("pong_musica.mp3")
    pygame.mixer.music.play(-1)
    
    #giocatore singolo

    if not mod_multigiocatore:
        gioco_giocatore_singolo_aperto = True
        nessun_vincitore = True
        
        while nessun_vincitore: 
            while gioco_giocatore_singolo_aperto: 
                for evento in pygame.event.get():
                    if evento.type==pygame.QUIT:
                        gioco_giocatore_singolo_aperto = False
                    elif evento.type==pygame.KEYDOWN: #or evento.type==pygame.KEYUP:
                        pong.tasto_premuto_giocatore_singolo(evento.key)
                    elif evento.type==pygame.KEYUP:
                        pong.tasto_lasciato_giocatore_singolo(evento.key)
                pong.movimento_giocatore_singolo(schermata)
                if not gioco_giocatore_singolo_aperto:
                    pygame.quit()
                elif pong.get_punteggio_giocatore_1()==pong.getGoal() or pong.get_punteggio_giocatore_2()==pong.getGoal(): 
                        nessun_vincitore = False  
                        gioco_giocatore_singolo_aperto = False
   
            pong.getOrologio().tick(pong.getFPS())

        x = 0

        if pong.get_punteggio_giocatore_1() == pong.getGoal():
            scelta = pong.mostra_vincitore(schermata, 1)
        elif pong.get_punteggio_giocatore_2() == pong.getGoal():
            scelta = pong.mostra_vincitore(schermata, 2)

        if scelta == "rivincita":
            # Reset punteggi e restart partita
            pong.set_punteggio_giocatore_1(0)
            pong.set_punteggio_giocatore_2(0)
            pong.x_palla, pong.y_palla = pong.LARGHEZZA//2, pong.ALTEZZA//2
            pong.vel_x_palla = random.choice([-pong.vel_xy_palla, pong.vel_xy_palla])
            pong.vel_y_palla = random.choice([-pong.vel_xy_palla, pong.vel_xy_palla])
            # qui potresti richiamare il loop di gioco di nuovo
            schermata_surf_aperta = True
        elif scelta == "esci":
            pygame.quit()
        exit()
    else:  #multigiocatore
        pong.disegna_schermata()
        schermata.fill(ROSA)
        pygame.mixer.music.stop()
        pygame.display.update()
        musica = pygame.mixer.music.load("pong_musica.mp3")
        pygame.mixer.music.play(-1)

        gioco_multigiocatore_aperto = True
        nessun_vincitore = True

        while nessun_vincitore:        
            while gioco_multigiocatore_aperto:
                for evento in pygame.event.get():
                    if evento.type==pygame.QUIT:                
                        gioco_multigiocatore_aperto = False
                    elif evento.type==pygame.KEYDOWN:
                        pong.tasto_premuto_multigiocatore(evento.key)
                    elif evento.type==pygame.KEYUP:             
                        pong.tasto_lasciato_multigiocatore(evento.key)        
                pong.movimento_multigiocatore(schermata)
                if not gioco_multigiocatore_aperto:
                    pygame.quit()
                elif pong.get_punteggio_giocatore_1()==pong.getGoal() or pong.get_punteggio_giocatore_2()==pong.getGoal():
                    nessun_vincitore = False
                    gioco_multigiocatore_aperto = False
        if pong.get_punteggio_giocatore_1() == pong.getGoal():
            scelta = pong.mostra_vincitore(schermata, 1)
        elif pong.get_punteggio_giocatore_2() == pong.getGoal():
            scelta = pong.mostra_vincitore(schermata, 2)

        if scelta == "rivincita":
            # Reset punteggi e restart partita
            pong.set_punteggio_giocatore_1(0)
            pong.set_punteggio_giocatore_2(0)
            pong.x_palla, pong.y_palla = pong.LARGHEZZA//2, pong.ALTEZZA//2
            pong.vel_x_palla = random.choice([-pong.vel_xy_palla, pong.vel_xy_palla])
            pong.vel_y_palla = random.choice([-pong.vel_xy_palla, pong.vel_xy_palla])
            # qui potresti richiamare il loop di gioco di nuovo
        elif scelta == "esci":
            pygame.quit()
            exit()
                        
            pong.getOrologio().tick(pong.getFPS()) 

    finale_aperto = True
    while finale_aperto:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                finale_aperto = False
        pong.getOrologio().tick(pong.getFPS())