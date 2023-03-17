# LineEstimation.py
import pygame
import random
from time import sleep

WIDTH = 500
HEIGHT = 300
BACKGROUND = (255, 255, 255)

class Scoreboard:

    def __init__(self, p1, p2) :
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 120)

        # Scoreboard 1
        self.label = "Scoreboard"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0))
        self.TextRect = self.TextLabel.get_rect(center=(WIDTH//2, HEIGHT//8))  

        # Player 1
        self.playerOneLabel = "Player 1"
        self.playerOneTextLabel = self.font.render(str(self.playerOneLabel), True, (0,0,0))
        self.playerOneTextRect = self.playerOneTextLabel.get_rect(center=(WIDTH//4, HEIGHT//8 * 3))
        self.playerOneScore = p1
        self.playerOneScoreText = self.font.render(str(self.playerOneScore), True, (0,0,0))           
        self.playerOneScoreRect = self.playerOneScoreText.get_rect(center=(WIDTH//4, HEIGHT//8 * 5))

        # LINE
        self.divider = "|"
        self.divider = self.font1.render(str(self.divider), True, (0,0,0))
        self.dividerRect = self.divider.get_rect(center=(WIDTH//2, HEIGHT//2))
        
        # Player 2
        self.playerTwoLabel = "Player 2"
        self.playerTwoTextLabel = self.font.render(str(self.playerTwoLabel), True, (0,0,0))
        self.playerTwoTextRect = self.playerTwoTextLabel.get_rect(center=(WIDTH//4*3, HEIGHT//8 * 3))
        self.playerTwoScore = p2
        self.playerTwoScoreText = self.font.render(str(self.playerTwoScore), True, (0,0,0))   
        self.playerTwoScoreRect = self.playerTwoScoreText.get_rect(center=(WIDTH//4*3, HEIGHT//8 * 5))


class Ready:

    def __init__(self, seconds, n, l):
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 24)
        
        # Player Turn
        self.player = f"P{n}"
        if n == 1:
            self.player = self.font1.render(str(self.player), True, (255,0,0), (255, 255, 255))
            self.playerRect = self.player.get_rect(center=(WIDTH-30, 30))  
        elif n == 2:
            self.player = self.font1.render(str(self.player), True, (0,0,255), (255, 255, 255))
            self.playerRect = self.player.get_rect(center=(WIDTH-30, 30))  

        # Level
        self.level = f"Level {l}"
        self.level = self.font1.render(str(self.level), True, (0,0,0), (255, 255, 255))
        self.levelRect = self.level.get_rect(center=(60, 30))

        # Ready
        self.label = f"Ready in {seconds}"
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), (255,255,255))
        self.TextRect = self.TextLabel.get_rect(center=(WIDTH//2, 125))  


class Answer:

    def __init__(self, screen, user_text, n, q, total):
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 24)
        self.font2 = pygame.font.Font('freesansbold.ttf', 14)


        # Counter 
        self.nLabel = f"{n}"
        self.nLabel = self.font1.render(str(self.nLabel), True, (0,0,0), (255, 255, 255))
        self.nRect = self.nLabel.get_rect(center=(WIDTH-30, 30))

        # User_Text Input
        self.userText = f"{user_text}"
        self.userText = self.font.render(str(self.userText), True, (0,0,0), (255,255,255))
        self.userTextRect = self.userText.get_rect(center=(WIDTH//2, 225))  


         # Text 
        self.nLabel0 = "Make an Estimate!"
        self.nLabel0 = self.font1.render(str(self.nLabel0), True, (0,0,0), (255, 255, 255))
        self.nRect0 = self.nLabel0.get_rect(center=(WIDTH//2,HEIGHT//4))


        self.nLabel1 = "0"
        self.nLabel1 = self.font2.render(str(self.nLabel1), True, (0,0,0), (255, 255, 255))
        self.nRect1 = self.nLabel1.get_rect(center=(WIDTH//3-20,HEIGHT//2+10))

        self.nLabel2 = "100"
        self.nLabel2 = self.font2.render(str(self.nLabel2), True, (0,0,0), (255, 255, 255))
        self.nRect2 = self.nLabel2.get_rect(center=(WIDTH//3*2+20,HEIGHT//2+10))


        # Bargraph
        total = 100
        max_length = WIDTH//3
        pygame.draw.rect(screen,(255,0,0),( (WIDTH//3,HEIGHT//2) ,(int(max_length*q/total),20) )) # Fill
        pygame.draw.rect(screen,(0,0,0),( (WIDTH//3,HEIGHT//2),(max_length, 20) ),4) # Border

        

class Result:

    def __init__(self, state):
        self.font0 = pygame.font.Font('freesansbold.ttf', 60)  
        self.font = pygame.font.Font('freesansbold.ttf', 120)
        
        if state:
        # Score
            self.text = "That's correct"
        else:
            self.text = "Try again"
        self.text = self.font0.render(str(self.text), True, (0,0,0), (255,255,255))           
        self.textRect = self.text.get_rect(center=(WIDTH//2, HEIGHT//2))

class Winner:

    def __init__(self, p1,p2):
        self.font0 = pygame.font.Font('freesansbold.ttf', 60)  
        self.font = pygame.font.Font('freesansbold.ttf', 120)
        
        if p1 > p2:
        # Score
            self.text = "Player 1 Wins"
        elif p2 > p1:
            self.text = "Player 2 Wins"
        else:
            self.text = "Draw"
        self.text = self.font0.render(str(self.text), True, (0,0,0), (255,255,255))           
        self.textRect = self.text.get_rect(center=(WIDTH//2, HEIGHT//2))

def generateNumber(n):
    from random import randint
    return (int("".join([str(randint(1,9)) for i in range(n)])))

def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    count = 5

    countdown = {
        1: 7,
        2: 6,
        3: 5,
    }
    user_text = ''
    # Player Scores
    Player1 = 0
    Player2 = 0
    # Current Player Turn 
    player_turn = 0    # 0 -> Player 1 | 1 -> Player 2 
    # Current Level 
    level = 1
    max_level = 3
    # Current State of Game
    state = 0
    # Current Runtime
    run = True
    # Max
    total = 100
    while run:
        screen.fill(BACKGROUND)

        # EVENTS 
        for event in pygame.event.get():
            if state == 0:      # SCOREBOARD
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    state = 1
                    count = 5
                elif pygame.key.get_pressed()[pygame.K_q]:
                    run = False
            elif state == 1:    # READY
                pass
            elif state == 2:    # ANSWER
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_SPACE:
                        state = 3
                    else:
                        user_text += event.unicode
                        print(user_text)
            elif state == 3:    # LOGIC 
                print("q =", q)
                try:
                    if int(user_text) <= int(q) + 5 and int(user_text) >= int(q) - 5:
                        s = 1
                    else:
                        s = 0
                except:
                    s = 0
                    print("E")
            elif state == 4:
                pass
            elif state == 5:    # WINNER
                if pygame.key.get_pressed()[pygame.K_q]:
                    run = False

               

        # STATE
        if state == 0:
            pass
           
        elif state == 1:          # SCOREBOARD
            count -= 0.1 
            sleep(0.1)
            if count < 0: 
                q = random.randint(30, 80)
                state = 2
                user_text = ''
                count0 = countdown[level]
                count1 = 5
            
        elif state == 2:        # READY
            count0 -= 0.1 
            sleep(0.1)
            if count0 < 0:
                state = 3
                s = 0
                
        elif state == 3:        # RESULT
            count1 -= 1
            sleep(0.1)
            if count1 < 0: 
                state = 4
                
        
        elif state == 4:        # COMPUTE
            # Update the player turn
            if player_turn == 0:
                Player1 += s
                player_turn = 1
            
            elif player_turn == 1:
                Player2 += s
                player_turn = 0
                level += 1
            
            if level > max_level: 
                state = 5
            else:
                state = 0
        
        elif state == 5:        # Winner
            pass
        
       # UPDATING SCREEN
        if state == 0: # SCOREBOARD
            screen1 = Scoreboard(Player1, Player2)
            screen.blit(screen1.TextLabel, screen1.TextRect)
            screen.blit(screen1.playerOneTextLabel, screen1.playerOneTextRect)
            screen.blit(screen1.playerOneScoreText, screen1.playerOneScoreRect)
            screen.blit(screen1.divider, screen1.dividerRect)
            screen.blit(screen1.playerTwoTextLabel, screen1.playerTwoTextRect)
            screen.blit(screen1.playerTwoScoreText, screen1.playerTwoScoreRect)

        elif state == 1: # READY
            screen2 = Ready( "{}".format(int(count)), player_turn+1, level)
            screen.blit(screen2.level, screen2.levelRect)
            screen.blit(screen2.player, screen2.playerRect)
            screen.blit(screen2.TextLabel, screen2.TextRect)
            
        elif state == 2:  # ANSWER 
            screen3 = Answer(screen, user_text, "{}".format(int(count0)), q, total)
            screen.blit(screen3.userText, screen3.userTextRect)
            screen.blit(screen3.nLabel, screen3.nRect)
            screen.blit(screen3.nLabel0, screen3.nRect0)
            screen.blit(screen3.nLabel1, screen3.nRect1)
            screen.blit(screen3.nLabel2, screen3.nRect2)

        elif state == 3: # RESULT
            screen4 = Result(s)
            screen.blit(screen4.text, screen4.textRect)
        
        elif state == 4:
            pass
    
        elif state == 5:
            screen5 = Winner(Player1, Player2)
            screen.blit(screen5.text, screen5.textRect)

        pygame.display.flip() 
        clock.tick(60)

if __name__ == "__main__":
    main()