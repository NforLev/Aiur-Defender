import pygame
import random
import math
from pygame import mixer
from pathlib import Path


rute=Path.cwd()



"""some misc variables"""
# inicializar pygame
pygame.init()
#pantalla
wind= pygame.display.set_mode((800, 600))
#icono, titulo y fondo
pygame.display.set_caption("Aiur defender")
icono= pygame.image.load(rute/"./img/pylon.png")
pygame.display.set_icon(icono)
fondo=pygame.image.load(rute/"./img/fondo.jpg")
#music
mixer.music.load(rute/"./sounds/main theme.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(-1)


#Classes
"""bellow this lines we can see the diferent class constructors"""
class Probe():
    minerals=mixer.Sound(rute/"./sounds/Alert_ProtossNeedMoreMinerals.mp3")
    minerals.set_volume(0.3)
    img=pygame.image.load(rute/"./img/probe.png")
    def __init__(self, x, y, x_movement):
        self.x=x
        self.y=y
        self.x_movement=x_movement

    def create_probe(self):
        wind.blit(self.img,(self.x,self.y))
        #movimiento
        self.x+=self.x_movement
        #limite de pantalla
        if self.x<=0:
            self.x=0
        elif self.x>=736:
            self.x=736

player=Probe(368, 500, 0)


class Projectiles():
    img=pygame.image.load(rute/"./img/shoot.png")
    def __init__(self, x, y, y_movement):
        self.x=x
        self.y=y
        self.y_movement=y_movement
    
    def draw_projectile(self):
        wind.blit(self.img, (self.x+16, self.y+10))
           

class Enemy():
    def __init__(self, x, y, x_movement, y_movement):
        self.x=x
        self.y=y
        self.x_movement=x_movement
        self.y_movement=y_movement 
    
    def colision(self, x1,y1,x2,y2):
        distance= math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
        if distance<30:
            return True
        else:
            return False


class Zergling(Enemy):
    img=pygame.image.load(rute/"./img/pikazergling.png")
    sound=mixer.Sound(rute/"./sounds/ZerglingDeath.wav")
    sound.set_volume(0.2)
    def create_zergling(self):
        wind.blit(self.img,(self.x,self.y))
        #movimiento
        self.x+=self.x_movement
        #limite de pantalla
        if self.x<=0:
            self.x_movement=0.20
            self.y+=self.y_movement
        elif self.x>=736:
            self.x_movement=-0.20
            self.y+=self.y_movement


class Zergling2(Enemy):
    img=pygame.image.load(rute/"./img/zergling.png")
    sound=mixer.Sound(rute/"./sounds/ZerglingDeath.wav")
    sound.set_volume(0.2)
    def create_zergling(self):
        wind.blit(self.img,(self.x,self.y))
        #movimiento
        self.x+=self.x_movement
        #limite de pantalla
        if self.x<=0:
            self.x_movement=0.35
            self.y+=self.y_movement
        elif self.x>=736:
            self.x_movement=-0.35
            self.y+=self.y_movement


class Marine(Enemy):
    img=pygame.image.load(rute/"./img/marine.png")
    sound=mixer.Sound(rute/"./sounds/MarineDeath.mp3")
    sound.set_volume(0.2)
    soundrdy=mixer.Sound(rute/"./sounds/Marine_Ready00.mp3")
    soundrdy.set_volume(0.3)
    def create_marine(self):
        wind.blit(self.img,(self.x,self.y))
        #movimiento
        self.x+=self.x_movement
        #limite de pantalla
        if self.x<=0:
            self.x_movement=0.10
            self.y+=self.y_movement
        elif self.x>=736:
            self.x_movement=-0.10
            self.y+=self.y_movement


class Zealot(Enemy):
    img=pygame.image.load(rute/"./img/zealot.png")
    sound=mixer.Sound(rute/"./sounds/ZealotDeath.mp3")
    sound.set_volume(0.2)
    def create_zealot(self):
        wind.blit(self.img,(self.x,self.y))
        #movimiento
        self.x+=self.x_movement
        #limite de pantalla
        if self.x<=0:
            self.x_movement=0.15
            self.y+=self.y_movement
        elif self.x>=736:
            self.x_movement=-0.15
            self.y+=self.y_movement


class Reaper(Enemy):
    img=pygame.image.load(rute/"./img/reaper.png")
    sound=mixer.Sound(rute/"./sounds/Marine_Death2.mp3")
    sound.set_volume(0.2)
    def create_reaper(self):
        wind.blit(self.img,(self.x,self.y))
        #movimiento
        self.x+=self.x_movement
        #limite de pantalla
        if self.x<=0:
            self.x_movement=0.35
            self.y+=self.y_movement
        elif self.x>=736:
            self.x_movement=-0.35
            self.y+=self.y_movement


pikazergling=Zergling(random.randint(0,736), random.randint(50,200), 0.22, 30)
marines=Marine(random.randint(0,736), random.randint(50,200), 0.15, 50)
zealots=Zealot(random.randint(0,736), random.randint(50,200), 0.20, 70)
fast_zergling=Zergling2(random.randint(0,736), random.randint(50,200), 0.35, 35)
reapers=Reaper(random.randint(0,736), random.randint(50,200), 0.30, 60)
fast_zergling2=Zergling2(random.randint(0,736), random.randint(50,200), 0.40, 35)
fast_zergling3=Zergling2(random.randint(0,736), random.randint(50,200), 0.45, 35)



#stats, score, and functions
"""global variables to be used in later functions"""
start_app= True
player.minerals.play()
score=0
show_score= pygame.font.Font("Starcraft.ttf", 25)
bullets=[]
endgame=False
end_message= pygame.font.Font("Starcraft.ttf", 40)
thanks=pygame.font.Font("Starcraft.ttf",25)
tutorial_text=pygame.font.Font("Starcraft.ttf",25)

#simple 4sec tutorial on screen
def tutorial():
    wind.blit(fondo,(0,0))
    text1=tutorial_text.render("Use arrow keys to move the probe", True, (255,255,255))
    text2=tutorial_text.render("Use spacebar to shoot", True, (255,255,255))
    text3=tutorial_text.render("Collect minerals for Aiur", True, (255,255,255))
    text4=tutorial_text.render("Don't let enemys reach the probe line", True, (255,255,255))
    wind.blit(text1,(90, 140))
    wind.blit(text2,(210, 220))
    wind.blit(text3,(190, 300))
    wind.blit(text4,(60, 380))
    pygame.display.update()
    pygame.time.delay(4000)

#score function
"""used to draw score on each iteration of redraw_window"""
def draw_score():
    text=show_score.render(f"Minerals: {score}", True, (255,255,255))
    wind.blit(text, (10,10))

#function to keep game window updated
"""used in the main game loop to refresh the screen"""
def redraw_window(score):
    wind.blit(fondo,(0,0))
    player.create_probe()
    draw_score()
    for bullet in bullets:
        bullet.draw_projectile()
    #each score milestown will spawn a new enemy class with diferent atributes
    pikazergling.create_zergling()
    if score>4:
        marines.create_marine()
    if score>15:
        zealots.create_zealot()
    if score>30:
        fast_zergling.create_zergling()
    if score>60:
        reapers.create_reaper()
    if score>250:
        fast_zergling2.create_zergling()
        fast_zergling3.create_zergling()
    
     
    #check if endgame condition is met
    """if endgame is true it will show ending message and end the game"""
    if endgame:
        text1=end_message.render("Aiur has fallen because", True, (255,255,255))
        text2=end_message.render(" not enough minerals", True, (255,255,255))
        text3=thanks.render("Thanks for playing, game closing now   ", True, (255,255,255))
        wind.blit(text1,(80,160))
        wind.blit(text2,(80,300))
        wind.blit(text3,(65,450))
        pygame.display.update()
        pygame.time.wait(6000)
        pygame.quit()

    pygame.display.update()
    

tutorial()
#main game loop
"""first check if any of the enemys is bellow threshold
    if an enemy is found move all enemys out of sight and call
    endgame true
"""
while start_app:
    if (pikazergling.y>510 and pikazergling.y<600) or (pikazergling.colision(pikazergling.x,pikazergling.y,player.x-20,player.y-20) == True):
        endgame=True
        pikazergling.y=1000
    elif (marines.y>510 and marines.y<600) or (marines.colision(marines.x,marines.y,player.x-20,player.y-20) == True):
        endgame=True
        pikazergling.y=1000
        marines.y=1000
    elif (zealots.y>510 and zealots.y<600) or (zealots.colision(zealots.x,zealots.y,player.x-20,player.y-20) == True):
        endgame=True
        pikazergling.y=1000
        marines.y=1000
        zealots.y=1000
    elif (fast_zergling.y>510 and fast_zergling.y<600) or (fast_zergling.colision(fast_zergling.x,fast_zergling.y,player.x-20,player.y-20) == True):
        endgame=True
        pikazergling.y=1000
        marines.y=1000
        zealots.y=1000
        fast_zergling.y=1000
    elif (reapers.y>510 and reapers.y<600) or (reapers.colision(reapers.x,reapers.y,player.x-20,player.y-20) == True):
        endgame=True
        pikazergling.y=1000
        marines.y=1000
        zealots.y=1000
        fast_zergling.y=1000
        reapers.y=1000
    elif (fast_zergling2.y>510 and fast_zergling2.y<600) or (fast_zergling2.colision(fast_zergling2.x,fast_zergling2.y,player.x-20,player.y-20) == True):
        endgame=True
        pikazergling.y=1000
        marines.y=1000
        zealots.y=1000
        fast_zergling.y=1000
        reapers.y=1000
        fast_zergling2.y=1000
    elif (fast_zergling3.y>510 and fast_zergling3.y<600) or (fast_zergling3.colision(fast_zergling3.x,fast_zergling3.y,player.x-20,player.y-20) == True):
        endgame=True
        pikazergling.y=1000
        marines.y=1000
        zealots.y=1000
        fast_zergling.y=1000
        reapers.y=1000
        fast_zergling2.y=1000
        fast_zergling3.y=1000
    

    """bellow loop checks for collition with diferent clases"""
    for bullet in bullets:
        #check colisions with zergling
        pikacol= pikazergling.colision(pikazergling.x,pikazergling.y,bullet.x,bullet.y)
        if pikacol:
            pikazergling.sound.play()
            bullets.pop(bullets.index(bullet))
            score+=1
            pikazergling=Zergling(random.randint(0,736), random.randint(50,200), 0.20, 30)
        #check colisions with marine
        if score>4:
            marinecol= marines.colision(marines.x,marines.y,bullet.x,bullet.y)
            if marinecol:
                marines.sound.play()
                bullets.pop(bullets.index(bullet))
                score+=2
                marines=Marine(random.randint(0,736), random.randint(50,200), 0.20, 50)
        #check colisions with zealot
        if score>15:
            zealotcol= zealots.colision(zealots.x,zealots.y,bullet.x,bullet.y)
            if zealotcol:
                zealots.sound.play()
                bullets.pop(bullets.index(bullet))
                score+=3
                zealots=Zealot(random.randint(0,736), random.randint(50,200), 0.25, 70)
        #check colisions with fast zergling
        if score>30:
            zerglingcol=fast_zergling.colision(fast_zergling.x,fast_zergling.y, bullet.x, bullet.y)
            if zerglingcol:
                pikazergling.sound.play()
                bullets.pop(bullets.index(bullet))
                score+=5
                fast_zergling=Zergling2(random.randint(0,736), random.randint(50,200), 0.35, 35)
        #check colisions with reaper
        if score>60:
            reapercol=reapers.colision(reapers.x,reapers.y,bullet.x,bullet.y)
            if reapercol:
                reapers.sound.play()
                bullets.pop(bullets.index(bullet))
                score+=7
                reapers=Reaper(random.randint(0,736), random.randint(50,200), 0.40, 60)
        #last round for the tryhards
        if score>250:
            zerglingcol2=fast_zergling2.colision(fast_zergling2.x,fast_zergling2.y,bullet.x,bullet.y)
            if zerglingcol2:
                fast_zergling.sound.play()
                bullets.pop(bullets.index(bullet))
                score+=7
                fast_zergling2=Zergling2(random.randint(0,736), random.randint(50,200), 0.40, 35)
            zerglingcol3=fast_zergling3.colision(fast_zergling3.x,fast_zergling3.y,bullet.x,bullet.y)
            if zerglingcol3:
                fast_zergling.sound.play()
                bullets.pop(bullets.index(bullet))
                score+=7
                fast_zergling3=Zergling2(random.randint(0,736), random.randint(50,200), 0.40 , 35)

        #move bullets
        if bullet.y<600 and bullet.y>0:
            bullet.y-=bullet.y_movement
        else:
            bullets.pop(bullets.index(bullet))
            
    #keybinds and events
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            start_app=False
        #movement
        if evento.type==pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player.x_movement=-0.2
            if evento.key == pygame.K_RIGHT:
                player.x_movement=0.2
        if evento.type==pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    player.x_movement=0
                if evento.key == pygame.K_RIGHT:
                    player.x_movement=0
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_SPACE:
                if len(bullets)<4:
                    shoot_sound=mixer.Sound(rute/"./sounds/shoot.wav")
                    shoot_sound.set_volume(0.2)
                    shoot_sound.play()
                    bullets.append(Projectiles(player.x, player.y, 0.20))

    redraw_window(score)

