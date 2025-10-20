import pygame
import sys #Allows Visual Studio Code to use local computer-based functions such as retrieving files from the same project folder or directory
from gamemodes import target_clicking #These two import codes specifies where the IDE could retrieve files with specific names
from gamemodes import decision_making


mainClock = pygame.time.Clock()
from pygame.locals import * #Imports local constants such as time, mouse, and keyboard control
pygame.init()
pygame.display.set_caption('Main Menu')
menu_width = 1920 * 0.75
menu_height = 1080 * 0.75
screen = pygame.display.set_mode((menu_width, menu_height)) #Setting the main menu window screen, following the same principles as the previous two game scenarios
 
font = pygame.font.SysFont("Arial", 100, bold = True) #This variable is used with pygame's font commands, specifically SysFont to access the local computer's package of Window fonts
font2 = pygame.font.SysFont("Arial", 50) #Used later in drawing multiple text blocks onto the screen

def draw_text(text, font, color, surface, x, y): #Defining a function with custom parameters, from DaFluffyPotato's tutorial video
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_text2(text, font, color, surface, x, y): #Duplicated from above for the secondary text element on the screen later
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
 
def main_menu(): #The Main Menu loop, operating under a define function
    while True:
        screen.fill("White")
        #draw_text('Main Menu - Select the gamemode to start', font, ("Blue"), screen, 300, 300)
        
        screen.fill("White")
        draw_text("Mindex Benchmark", font, ("Blue"), screen, menu_width / 2 - 350, 150) #Game title text, using the variable parameters defined above to create the text element
        draw_text2("Press ESC to exit gamemode and game", font2, ("Black"), screen, menu_width / 2 - 350, 700) #Instructional text on how to use ESC

        mouse_x, mouse_y = pygame.mouse.get_pos() #Setting the mouse positional variables for the main menu screen
 
        button_font = pygame.font.SysFont ("Arial", 30) #Setting a variable for the button's fonts, used for accessing the two different gamemodes
        button_1 = pygame.Rect(menu_width / 2 - 80, 500, 200, 50) #Setting variables that use the PyGame's.Rect object string to plot two rectangles according to the specified x and y coordinates, and width and heights
        button_2 = pygame.Rect(menu_width / 2 - 80, 600, 200, 50)
        if button_1.collidepoint((mouse_x, mouse_y)): #The collidepoint uses PyGame's point collision mechanism
            if click:
                target_clicking.run_game()
        if button_2.collidepoint((mouse_x, mouse_y)):
            if click:
                decision_making.run_game2()
        pygame.draw.rect(screen, ("Black"), button_1)
        pygame.draw.rect(screen, ("Black"), button_2)
 

        game1text = button_font.render("Target Clicking", True, "White")
        game2text = button_font.render("Decision Making", True, "White")
        screen.blit(game1text, (button_1.centerx - game1text.get_width()/2, button_1.centery - game1text.get_height()/2)) #The centerx and centery string works to center the display blit to according to the x and y's of the screen
        screen.blit(game2text, (button_2.centerx - game2text.get_width()/2, button_2.centery - game2text.get_height()/2))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #The main menu will now handle the escape event handling instead of within Target Clicking with Escape
            if event.type == KEYDOWN: 
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game1(): 
    target_clicking.run_game()
 
def game2():
    decision_making.run_game2()
 
main_menu()