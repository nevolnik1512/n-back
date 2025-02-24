# Example file showing a basic pygame "game loop"
import random
import pygame

 

# pygame setup
pygame.init()
fps=60
screen = pygame.display.set_mode((1280, 720))
cx=screen.get_width()/2#screen center x position
cy=screen.get_height()/2#screen center y position
clock = pygame.time.Clock()
running = True
pause=True
pausecldwn=10
bullet_pos=pygame.Vector2(screen.get_width()/3,screen.get_height()/3)
theme_font = pygame.font.SysFont('DejaVu Sans Mono', 30)
mess_font = pygame.font.SysFont('DejaVu Sans Mono', 50)
messx=700
messy=300




#game set up
theme_color="white"
cell_size=150#one side size
back=3#steps back to remember
queue=[i for i in range(back)]#history of positions
press=False
round=fps * 2 # seconds
tleft=round
score=0
health=5




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    keys = pygame.key.get_pressed()

    if tleft == round:# new round 
        press = False#zeroing press
        for i in range(len(queue),-1,-1):
            
            if i < len(queue)-1:#shifting all elements to the right on one
                queue[i+1]=queue[i]
        if random.randint(0,3)==0:
            queue[0]=queue[-1]
        else:
            while queue [0]==queue[-1]:
                queue[0]=random.randint(0,8)
            

    #rendering grid
    


    messages=['N='+str(back-1),
            'Score='+str(score),
            'Health='+str(health),
            '',
            'To pause press p',
            'To escape press ESC',
            'To catch a ball',
            'press Space']
    for i in range(len(messages)):
        text_surface = theme_font.render(messages[i], False, (255, 255, 255))
        screen.blit(text_surface, (0,30*i))

    pygame.draw.line(screen,color=theme_color,start_pos=(cx+0.5*cell_size,cy+1.5*cell_size),end_pos=(cx+0.5*cell_size,cy-1.5*cell_size),width=5)
    pygame.draw.line(screen,color=theme_color,start_pos=(cx-0.5*cell_size,cy+1.5*cell_size),end_pos=(cx-0.5*cell_size,cy-1.5*cell_size),width=5)
    pygame.draw.line(screen,color=theme_color,start_pos=(cx+1.5*cell_size,cy+0.5*cell_size),end_pos=(cx-1.5*cell_size,cy+0.5*cell_size),width=5)
    pygame.draw.line(screen,color=theme_color,start_pos=(cx+1.5*cell_size,cy-0.5*cell_size),end_pos=(cx-1.5*cell_size,cy-0.5*cell_size),width=5)

    pygame.draw.line(screen,color=theme_color,start_pos=(cx+1.5*cell_size,cy+1.5*cell_size),end_pos=(cx+1.5*cell_size,cy-1.5*cell_size),width=5)
    pygame.draw.line(screen,color=theme_color,start_pos=(cx-1.5*cell_size,cy+1.5*cell_size),end_pos=(cx-1.5*cell_size,cy-1.5*cell_size),width=5)
    pygame.draw.line(screen,color=theme_color,start_pos=(cx+1.5*cell_size,cy+1.5*cell_size),end_pos=(cx-1.5*cell_size,cy+1.5*cell_size),width=5)
    pygame.draw.line(screen,color=theme_color,start_pos=(cx+1.5*cell_size,cy-1.5*cell_size),end_pos=(cx-1.5*cell_size,cy-1.5*cell_size),width=5)
    

    #line of time
    leng=4*cell_size*tleft/round
    pygame.draw.line(screen,color=theme_color,start_pos=(cx+leng/2,cy+2*cell_size),end_pos=(cx-leng/2,cy+2*cell_size),width=5)


    #rendering posiion of bullet
    if round - tleft > 10: # this is a little blink of bullet at each new round
        bx=cx+(queue[0]%3)*cell_size-cell_size
        by=cy+(queue[0]//3)*cell_size-cell_size
        bullet_pos=pygame.Vector2(bx,by)
        bullet_color=""
        if press:
            if queue[0]==queue[back-1]:
                bullet_color="green"
            else:
                bullet_color="red"
        else:
            bullet_color="white"
            
        pygame.draw.circle(screen, bullet_color, bullet_pos, 40)

    #rendering message
    if pause:
        pygame.draw.rect(screen,"white",(cx-messx/2,cy-messy/2,messx,messy))
        pygame.draw.rect(screen,"black",(cx-(messx-10)/2,cy-(messy-10)/2,messx-10,messy-10))

        text_surface = mess_font.render("Paused", False, (255, 255, 255))
        screen.blit(text_surface, (cx-len("Paused")/2*28,cy-80))
        text_surface = mess_font.render("Press p to resume", False, (255, 255, 255))
        screen.blit(text_surface, (cx-len("Press p to resume")/2*28,cy))


    #getting users pressions
    
    if not press:#if key is not already pressed
        if keys[pygame.K_SPACE]:
            if queue[0]==queue[back-1]:
                score+=1
            else:
                health -=1
            press=True
        if keys[pygame.K_p] and pausecldwn<=0:
            pause=not pause
            pausecldwn=10
    if keys[pygame.K_ESCAPE]:
        running=False

    if health <= 0:
        running=False
    
    if not pause:
        tleft-=1
    if tleft <= 0:
        tleft = round

    pausecldwn-=1


    

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(fps)  # limits FPS to 60






pygame.quit()