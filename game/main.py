
# TANGUY WAS HIER !!!!!! 

'blablabla'



import pygame;

#initialize pygmae
pygame.init();

#set window size
screen = pygame.display.set_mode((800,600))

#initial pos
x = 0
y = 0
#create a bool to keep the window running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if(x < 750):
            x += 1
    elif keys[pygame.K_LEFT]:
        if(x > -1):
            x -= 1
    elif keys[pygame.K_UP]:
        if(y > -1):
            y -= 1
    elif keys[pygame.K_DOWN]:
        if(y < 550):
            y += 1
    screen.fill((255,0,0))
    pygame.draw.rect(screen,(255,255,255),(x,y,50,50))
    pygame.display.update()

pygame.quit();