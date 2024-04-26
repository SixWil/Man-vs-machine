# # # prompt 1

# # använder pygame i stället för Pysimplegui som jag gjorde
import pygame
import time
import random

pygame.init()
##

# # rgb värden
# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
##

# Window dimensions
display_width = 800
display_height = 600

# Snake block size
block_size = 20

# Speed of the snake
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont(None, 50)

# Function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [display_width / 6, display_height / 3])

# # använder också listor för att hålla vart masken vart
# Function to draw the snake
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, black, [x[0], x[1], block_size, block_size])
##
        
# Function to the main game loop
def gameLoop():
    # # använder också en boolean för att spara om spelet kör eller inte
    game_over = False
    ##
    game_close = False
    
    # # använder också x y värden men inte på samma sätt
    # Starting position of the snake
    x1 = display_width / 2
    y1 = display_height / 2
    ##

    # # använder också förändrings riktning i x y
    # Change in position of the snake
    x1_change = 0
    y1_change = 0
    ##

    # # använder också lista för visualiseringen och int för poäng
    # Snake body
    snake_list = []
    length_of_snake = 1
    ##

    # #  använder också random för att placera ut frukt, men inte på samma sätt(?)
    # Position of food
    foodx = round(random.randrange(0, display_width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, display_height - block_size) / block_size) * block_size
    ##

    # # typ exakt så som jag håller koll på om rundan kör som i mitt spel
    while not game_over:
    ##
        
        # # väldigt likt
        while game_close == True:
            gameDisplay.fill(white)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()
        ##
            # # använder event lite likt som man kan med knapparna i PySimpleGui
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                # # K_ = KEYDOWN?
                    # # ?
                    if event.key == pygame.K_q:
                    ##
                        
                    # # räknas som avslut men stänger inte sidan
                        game_over = True
                        game_close = False
                    ##
                        
                    # # ?    
                    if event.key == pygame.K_c:
                        # # starta om
                        gameLoop()
                        ##
                    ##
                ##
            ##
                        
        # # använder event lite likt som man kan med knapparna i PySimpleGui
        for event in pygame.event.get():

            # # om event = quit, avsluta spelet?
            if event.type == pygame.QUIT:
                game_over = True
            ##
                
            # # piltangenterna ändrar riktnings värdena, liknar så jag gjorde mitt spel
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0
            ##
                    
        ##

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        # # förändrar maskens platts baserat på riktning x y's värden.
        x1 += x1_change
        y1 += y1_change
        ##
        gameDisplay.fill(blue)
        pygame.draw.rect(gameDisplay, green, [foodx, foody, block_size, block_size])
        # # uppdaterar masken baserat på dess platsdata
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        ##

        # # tar bort sista svansen av masken
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        ##
        # # för alla utom sista, om mask huvud beter det att du har kraschat
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        ##
                
        # # kör mask funktionen med två data
        our_snake(block_size, snake_list)
        ##

        # # uppdaterar rutan precis som i PySimpleGui
        pygame.display.update()
        ##

        # # om du träffar en frukt placera ut en ny frukt och ge ett poäng
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, display_height - block_size) / block_size) * block_size
            length_of_snake += 1
        ##

        # # EXAKT så som jag gjorde hastighet i mitt spel, jag kallade det bokstavligen 'tick' i min kommentar
        clock.tick(snake_speed)
        ##

    # # stäng av allt(?)
    pygame.quit()
    quit()
    ##

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# # dra igång
gameLoop()
##