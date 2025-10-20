import pygame
import random
import time #Time module is used for the countdown before the main game loop

def run_game():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Target Clicking")

#Define screen size with relevant factors (added scaling factors when this project is opened with uni laptop)
    scaling_factor = 0.75
    w = 1920 * scaling_factor # =  1440
    h = 1080 * scaling_factor # =  810
    font = pygame.font.SysFont('Arial', 75)
    timer = pygame.time.Clock()

    screen = pygame.display.set_mode((w, h))

#Setting the parameter variables for the targets
    hitbox_x = 50 #Sets the hitbox size for the target, which is currently 50 pixels wide by 50 pixels tall, and the variables beneath are for the second and third targets respectively
    hitbox_y = 50
    hitbox_x2 = 50
    hitbox_y2 = 50
    hitbox_x3 = 50
    hitbox_y3 = 50
    #randomx_quarter = 0.25 #I thought about using these as variables to use in centering or placing my objects to a quarter of the screen, but the way PyGame draws these objects makes it difficult to
    #randomx_quarter3 = 0.75
    #randomy_quarter = 0.25
    #randomy_quarter3 = 0.75
    

    def pre_timer(counter): #Sets the timer to display in a 00:00 format
        if counter > 9: 
            return '0:'
        else:
            return '0:0'

#Setting the reset variables to be used later, alongside the running = True variable that is common in all PyGame game loops
    reset = True #Setting the base reset when the target is clicked
    reset2 = True #Setting the base reset for the second target
    reset3 = True
    running = True

#Setting the player live stats and mouse handling event variables
    score = 0 #Setting the baseline score variable
    score_text = font.render("Points: " + str(score), True, (0, 0, 0))
    base_score = 100
    counter = 60 #Sets the game timer's session to 60 seconds to start
    timer_text = font.render(pre_timer(counter) + str(counter), True, (0, 0, 0))
    hit_counter = 0 #Counts the number of successful hits (will be used in the hitscan coding below)
    miss_counter = 0 #Counts the number of misses (will be used in the else function of the hitscan coding)
    countdown_font = pygame.font.SysFont("Arial", 200) #Sets an independent font variable that uses the pygame.font functions to be used later
    bonus_counter = 0 #bonus counter for multiplier
    multiplier = 1

#Creating the timer event 
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000) #Sets the timer to count down every 1000ms or 1 second, taking guidance from IntegerNumber's video

    def countdown(seconds):
        for i in range(seconds, 0, -1):
            screen.fill("Dark Gray")
            countdown_text = countdown_font.render(str(i), True, (0, 0, 0))  #Black countdown text, using the countdown_font variable above in another variable that determines the countdown's text block itself
            screen.blit(countdown_text, (w/2 - countdown_text.get_width()/2, h/2 - countdown_text.get_height()/2))
            pygame.display.flip()
            time.sleep(1)  #Wait 1 second per countdown number
    

    countdown(3) #Sets a countdown based on the set dimensions above starting from 3 seconds, and decreasing every second before going onto the main game

#Main Game Loop
    while running: 
        timer.tick(60) 
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        accuracy = round(hit_counter / (hit_counter + miss_counter) * 100) if hit_counter > 0 else 0 #Calculates the accuracy percentage based on successful hits divided by total clicks (hit_counter + miss_counter) 
        accuracy_text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 0, 0)) #Renders the accuracy variable as text on the screen with black text
        #The if hit_counter > 0 else 0 accounts for the division by zero error by setting a conditional. If the value of the hit_counter variable is greater than 0, then it takes whatever value is there as true. Otherwise, it is false, and sets it back to 0, meaning it will not accept 0 as a usable integer in the variable. 
#Randomizer element for each target orbs' x and y coordinates
        for event in pygame.event.get():
            if reset is True:
                target_x = random.randint(360, 1080) #Sets the random spawn point for the target on the x-axis to be between 360 and 1440, which is 25% and 75% of the screen width respectively
                target_y = random.randint(203, 608) #Sets the random spawn point for the target on the y-axis to be between 270 and 810, which is 25% and 75% of the screen height respectively
                reset = False
            if reset2 is True:
                target2_x = random.randint(360, 1080)
                target2_y = random.randint(203, 608)
                reset2 = False
            if reset3 is True:
                target3_x = random.randint(360, 1080)
                target3_y = random.randint(203, 608)
                reset3 = False
            if event.type == pygame.QUIT or counter == 1: #Ends the session if the timer reaches 1, as putting 0 will make the timer go into a negative number. However, because the tick setting is 1, it will end at 0 regardless.
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Ends the session if the Escape key is pressed
                    running = False

#Hitscan mechanism for all three targets           
            if event.type == pygame.MOUSEBUTTONDOWN: #Setting the primary control with an event where a mouse button is clicked
                if (mouse[0] < target_x + hitbox_x) and (mouse[0] > target_x) and (mouse[1] < target_y + hitbox_y) and (mouse[1] > target_y) and event.button == 1: #This checks if the mouse position is within the target's spawnpoint with target_x added with hitbox_x, and same for target_y and hitbox_y.
                    click == True
                    if bonus_counter >= 3: #Setting the bonus streak to activate when 3 consecutive accurate clicks are done
                        multiplier = 2 #Using the if logic, the base multiplier of 1 now becomes 2 for double points
                    score = score + base_score * multiplier #Calculates the score based on score + a base increase of 100, subject to a multiplier. Initially coded with print("HIT!") to verify that the hitbox detection mechanism was working properly, and can now be replaced by points increasing
                    score_text = font.render("Score: " + str(score), True, (0, 0, 0)) #This renders the score variable as text on the screen with black text. Takes guidance from IntegerNumber's video.
                    hit_counter = hit_counter + 1 #Registers this click as a successful hit, thus adding to the hit counter variable
                    bonus_counter = bonus_counter + 1
                    reset = True
                elif (mouse[0] < target2_x + hitbox_x2) and (mouse[0] > target2_x) and (mouse[1] < target2_y + hitbox_y2) and (mouse[1] > target2_y) and event.button == 1:
                    click == True
                    if bonus_counter >= 3: 
                        multiplier = 2
                    score = score + base_score * multiplier 
                    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
                    hit_counter = hit_counter + 1
                    bonus_counter = bonus_counter + 1
                    reset2 = True
                elif (mouse[0] < target3_x + hitbox_x3) and (mouse[0] > target3_x) and (mouse[1] < target3_y + hitbox_y3) and (mouse[1] > target3_y) and event.button == 1:
                    click == True
                    if bonus_counter >= 3:
                        multiplier = 2
                    score = score + base_score * multiplier 
                    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
                    hit_counter = hit_counter + 1
                    bonus_counter = bonus_counter + 1
                    reset3 = True
                else:
                    score = score - 50 #Subtracts 50 points for a misclick
                    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
                    miss_counter = miss_counter + 1 #Registers this click as a miss, thus adding to the miss counter variable
                    bonus_counter = 0
                    multiplier = 1

            if event.type == timer_event:
                counter = counter - 1
                timer_text = font.render(pre_timer(counter) + str(counter), True, (0, 0, 0)) #Renders the timer variable as text on the screen with black text
        
            if not pygame.display.get_surface():
                break

#Drawing the background color and targets onto the game's screen
        screen.fill(("Dark Gray"))
        pygame.draw.ellipse(screen, ("Red"), (target_x, target_y, hitbox_x, hitbox_y)) #Renders the target on the screen, in red, at a random position from 0 to 1440 on the x-axis and 0 to 810 on the y-axis + an extended hitbox size of 50 pixels by 50 pixels
        pygame.draw.ellipse(screen, ("Red"), (target2_x, target2_y, hitbox_x2, hitbox_y2))
        pygame.draw.ellipse(screen, ("Red"), (target3_x, target3_y, hitbox_x3, hitbox_y3))

        analytics_box = pygame.Rect(w - w, h - h, 1600, 100) #Sets a variable for a pygame drawing function, and this will be for the score, timer, and accuracy text to be printed upon a white box
        pygame.draw.rect(screen, "White", analytics_box)

        screen.blit(score_text, (w / 10 + 20, 10)) #This places the score text at the top left of the screen, with a 10 pixel offset from both the x and y axis
        screen.blit(timer_text, (w / 2 - 50, 10)) #This places the timer text at the center of the screen
        screen.blit(accuracy_text, (w / 10 + 800, 10)) #This places the accuracy text at the top right of the screen, with a 10 pixel offset from the y axis and 600 pixel offset from the x axis to account for the text width
        
        pygame.display.flip() #Updates the blitted score, timer, and accuracy text to the window screen while the game session is active

#Points display
    print ("Final Score: " + str(score)) #Prints the final score to the console after the game window is closed
    print("Accuracy Score: " + str(accuracy) + "%") #Prints the final accuracy percentage to the console after the game window is closed

if __name__ == "__main__": #Allows Target Clicking to run as a standalone file for easier testing, taking guidance from Martin Breuss' article
    run_game()