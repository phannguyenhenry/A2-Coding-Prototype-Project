import pygame
import random
import time 

def run_game2(): #Structure is copied from Target Clicking for base elements like points scoring, countdown, timers, and pre-game foundations
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Decision Making")

#Defining the screen size of the game
    w = 1920 * 0.75
    h = 1080 * 0.75

    font = pygame.font.SysFont('Arial', 75)
    timer = pygame.time.Clock()
    screen = pygame.display.set_mode((w, h))

    def pre_timer(counter):
        if counter > 9:
            return '0:'
        else:
            return '0:0'

#Setting the player's live stats and mouse handling event variables
    running = True
    score = 0
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    base_score = 100
    bonus_counter = 0 #bonus counter for multiplier
    multiplier = 1
    counter = 60
    timer_text = font.render(pre_timer(counter) + str(counter), True, (0, 0, 0))
    hit_counter = 0
    miss_counter = 0
    countdown_font = pygame.font.SysFont("Arial", 200)

#Creating the positional reset variables for each shape
    rect_reset = True
    triangle_reset = True
    ellipse_reset = True

#Setting the game state for the correct shape to spawn in the center of the screen
    mode = "center" #Setting a center mode with a "center" string that could be used later to check if the shape is in the "correct mode"
    correct_shape = None #The use of none means there is no value assigned to this variable yet, and will be amended later in the game logic
    center_shape = None
    center_x = w / 2 - 50
    center_y = h / 2 - 50

#Setting the center origin point of each shape's x and y coordinates
    rect_x = 0
    rect_y = 0
    triangle_x = 0
    triangle_y = 0
    ellipse_x = 0
    ellipse_y = 0

#Hitboxes per shape, and is a universal value that could be added to each shape when coding the hitscan mechanism
    hitbox_x = 100
    hitbox_y = 100

    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)

#Setting the countdown screen, porting the same code from Target Clicking
    def countdown(seconds):
        for i in range(seconds,0,-1):
            screen.fill("Dark Gray")
            countdown_text = countdown_font.render(str(i), True, (0,0,0))
            screen.blit(countdown_text,(w/2 - countdown_text.get_width()/2, h/2 - countdown_text.get_height()/2))
            pygame.display.flip()
            time.sleep(1)

    countdown(3)

#Main Game Loop
    while running:
        timer.tick(60)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        accuracy = round(hit_counter / (hit_counter + miss_counter) * 100) if hit_counter > 0 else 0 #Accuracy checker still works the same way as the clicking on the "correct" target would only add points and hit_counter
        accuracy_text = font.render("Accuracy: " + str(accuracy) + "%", True, (0,0,0))

#Setting the logic for quit events (either by exiting the window, pressing Esc, or the timer running out from 60)
        for event in pygame.event.get(): #Creating the quit event based on ESC, and interactions around the mouse with quitting events
            if event.type == pygame.QUIT or counter <= 0:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == timer_event:
                counter -= 1
                timer_text = font.render(pre_timer(counter) + str(counter), True, (0,0,0))
                if counter <= 0:
                    running = False

            if mode == "center" and center_shape is None: #Randomizes the random shape in the center if there is none on screen
                center_shape = random.choice(["Rect","Triangle","Ellipse"]) #Uses the choice function of the random module instead of integer to choose between three choices in a list

#Setting the hitscanning logic when the game is in "center" mode
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mode == "center" and center_shape is not None:
                    if center_shape == "Rect": #A conditional that if the center shape variable is equivalent to a Rect 
                        if (mouse[0] < center_x + hitbox_x and mouse[0] > center_x) and (mouse[1] < center_y + hitbox_y and mouse[1] > center_y): #Matches Target Clicking hitscan logic exactly
                            click == True
                            correct_shape = "Rect"
                            mode = "randomized" #Allows the hitscan mechanism of the mouse to work when the shape is clicked while the event mode is randomized, determining that the correct shape that matches with the set string is the one that gives players points
                            #score = score + base_score * multiplier
                            hit_counter += 1
                            rect_reset = True 
                    elif center_shape == "Triangle":
                        if (mouse[0] < center_x + hitbox_x and mouse[0] > center_x) and (mouse[1] < center_y + hitbox_y and mouse[1] > center_y):
                            click == True
                            correct_shape = "Triangle"
                            mode = "randomized"
                            #score = score + base_score * multiplier
                            hit_counter += 1
                            triangle_reset = True
                    elif center_shape == "Ellipse":
                        if (mouse[0] < center_x + hitbox_x and mouse[0] > center_x) and (mouse[1] < center_y + hitbox_y and mouse[1] > center_y):
                            click == True
                            correct_shape = "Ellipse"
                            mode = "randomized"
                            #score = score + base_score * multiplier
                            hit_counter += 1
                            ellipse_reset = True
                    #else: #No longer needed because it will be a redundant function when the hitscan logic below can apply the multiplier
                        #score = score - 50
                        #miss_counter += 1
                        #bonus_counter = 0
                        #multiplier = 1

#Setting the hitscanning logic when the game is in "randomized" mode
                elif mode == "randomized": #Mirroring the hitscan mechanism when the game event mode is in "randomized". There is no scoring variable in here because the center shape is meant to set the player with a specific target.
                    clicked_shape = None
                    if (mouse[0] < rect_x + hitbox_x and mouse[0] > rect_x) and (mouse[1] < rect_y + hitbox_y and mouse[1] > rect_y): #Using Target Clicking's hitscan coding as a guide, I did exactly the same to check. 
                        clicked_shape = "Rect"
                        rect_reset = False
                    elif (mouse[0] < triangle_x + hitbox_x and mouse[0] > triangle_x) and (mouse[1] < triangle_y + hitbox_y and mouse[1] > triangle_y):
                        clicked_shape = "Triangle"
                        triangle_reset = False
                    elif (mouse[0] < ellipse_x + hitbox_x and mouse[0] > ellipse_x) and (mouse[1] < ellipse_y + hitbox_y and mouse[1] > ellipse_y):
                        clicked_shape = "Ellipse"
                        ellipse_reset = False
                    else:
                        clicked_shape = None

                    if clicked_shape == correct_shape: #This is the fundamental logic that checks if the clicked shape is the shape set to the correct state, thus points scoring will go under here
                        if bonus_counter >= 3: #Setting the streak counter to activate when it reaches 3 consecutive accurate clicks, identical to Target Clicking's
                            multiplier = 2
                        score = score + base_score * multiplier         
                        hit_counter += 1
                        bonus_counter += 1
                        mode = "center"
                        center_shape = None
                    else:
                        score = score - 50
                        miss_counter += 1
                        bonus_counter = 0
                        multiplier = 1

                    score_text = font.render("Score: " + str(score), True, (0,0,0))

#Creating the randomizing logic for the shapes when the game is in "randomized" mode, porting the same coding logic from Target Clicking
        if mode == "randomized": #This randomizes the grid shape positions on the grid after the initial target has been clicked on
            if rect_reset:
                rect_x = random.randint(360, 1080)
                rect_y = random.randint(203, 608)
                rect_reset = False
            if triangle_reset:
                triangle_x = random.randint(360, 1080)
                triangle_y = random.randint(203, 608)
                triangle_reset = False
            if ellipse_reset:
                ellipse_x = random.randint(360, 1080)
                ellipse_y = random.randint(203, 608)
                ellipse_reset = False

#Drawing out the background color and the shapes
        screen.fill("Dark Gray")

        if mode == "center" and center_shape is not None:
            if center_shape == "Rect": #Red is assigned with red
                pygame.draw.rect(screen,"Red",(center_x, center_y, 100, 100)) 
            elif center_shape == "Triangle": #Triangle is assigned with blue
                pygame.draw.polygon(screen,"Blue",[(center_x + 50, center_y),(center_x, center_y + 100),(center_x +100, center_y + 100)])
            elif center_shape == "Ellipse": #Ellipse is assigned with green
                pygame.draw.ellipse(screen,"Green",(center_x , center_y, 100, 100)) 

        elif mode == "randomized": #This is where the rectangle, triangle, and circle targets are drawn onto the canvas
            pygame.draw.rect(screen,"Red",(rect_x, rect_y,100,100)) 
            pygame.draw.ellipse(screen,"Green",(ellipse_x, ellipse_y,100,100))
            pygame.draw.polygon(screen,"Blue",[(triangle_x + 50, triangle_y),(triangle_x, triangle_y+ 100),(triangle_x + 100, triangle_y + 100)]) 
        
        analytics_box = pygame.Rect(w - w, h - h, 2000, 100) 
        pygame.draw.rect(screen,"White",analytics_box)
        screen.blit(score_text, (w / 10 + 20, 10)) 
        screen.blit(timer_text, (w / 2 - 50, 10))
        screen.blit(accuracy_text, (w / 10 + 800, 10))

        pygame.display.flip() #Updates the shapes onto the canvas

#Points display
    print("Final Score:",score) #Prints the player's results onto the console 
    print("Accuracy:",accuracy,"%")

if __name__ == "__main__": #Allows Decision Making to run as a standalone program
    run_game2()
