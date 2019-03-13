import pygame
import time
from game import GameClass 
from notecard import NotecardClass
from stack import StackClass
pygame.init()

#settings

black = (0,0,0)
purple = (120, 90, 200)
l_purple = (160, 140, 230)
green = (107, 142, 35)
l_green = (150, 200, 70)
red = (180, 80, 80)
l_red = (225, 100, 100)
blue = (64, 224, 208)
display_width = 900
display_height = 500
button_down = False   
nc_front = pygame.image.load(r'C:\Users\j51780\Pictures\game\front_of_notecard.png')
nc_back = pygame.image.load(r'C:\Users\j51780\Pictures\game\back_of_notecard.png')
        

def redraw_window():
    win.fill(blue)
    pygame.display.update()

def quitGame():
    exit(0)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text, width, height, size, font):
    largetext = pygame.font.SysFont(font, size)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = ((width/2), (height/2))
    win.blit(TextSurf, TextRect)
    #pygame.display.update()
    return

def welcome_message():
    height_component = .5
    message = "Are you ready to learn \n Russian verbs?"
    message = message.split('\n')
    for text in message:
        message_display(text, display_width, display_height*height_component, 50, "Arial" )
        #largetext = pygame.font.SysFont("Arial", 50)
        #TextSurf, TextRect = text_objects(text, largetext)
        #TextRect.center = ((display_width/2), (display_height/2*height_component))
        height_component += .5
        #win.blit(TextSurf, TextRect)
    pygame.display.update()    
    return

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global button_down
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))

        if click[0] == 1 and action != None and button_down != True:
            action()         
            button_down = True
        elif click[0] == 0:
            button_down = False

    else:
        pygame.draw.rect(win, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)


def start_screen():
    start = True
    redraw_window()    
    welcome_message()
    
    while start:
    #draw rectangles for learn/study, quiz, about
        button("Study",125,400,150,50,green,l_green,study)
        button("Quiz",400,400,150,50,purple,l_purple,quiz)
        button("Quit",650,400,150,50,red,l_red,quitGame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                redraw_window()
                message_display("hi")
                start = False
        pygame.display.update()
    return

def study():
    redraw_window()
    count = 0
    count_max = game.getIncorrectStack().getStackCount() 
    study = True
    front = True
    
    while study:
        if front:            
            win.blit(nc_front, (70,60))
            message_display(game.getCurrentNotecard().getVerb(), display_width, display_height, 100, "Arial")
            pygame.display.update()
        else:
            win.blit(nc_back, (70,60))
            message_display(game.getCurrentNotecard().getDefinition(), display_width, display_height, 100, "Arial")
            pygame.display.update()
        
        if count < count_max:
            button("Next",200,440,100,40,green,l_green, getNextNC)
        button("Back",100,440,100,40,purple,l_purple,getPrevNC)
        button("Exit",680,440,100,40,red,l_red,start_screen)    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
                return
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                front = not front
                pygame.display.update()
            
            elif keys[pygame.K_RIGHT]:
                getNextNC()

def quiz():
    redraw_window()
    count = 0
    count_max = game.getIncorrectStack().getStackCount() 
    quiz = True
    update = False
    answer = ""
    
    while quiz: 
        
        if not update:
            #redraw_window()
            displayQuiz()
            pygame.display.update()
            update = True

        button("Back",125,440,100,40,purple,l_purple,start_screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    checkAnswer(answer)
                    update = False
                    answer = ""
                elif event.key == pygame.K_BACKSPACE:
                    answer = answer[:-1]
                    print(answer)
                    displayAnswer(answer)
                else:
                    answer += event.unicode
                    displayAnswer(answer)
        pygame.display.update()
                

def displayQuiz():
    win.blit(nc_front, (70,60))
    message_display(game.getCurrentNotecard().getVerb(), display_width, display_height/2, 100, "Arial")
    message_display("English: ", display_width/2.5, display_height*1.4, 50, "Arial")
    

def displayAnswer(answer):
    win.fill(blue)
    win.blit(nc_front, (70,60))
    displayQuiz()
    location = (display_width/2.5 + 180)
    for letter in answer: 
        message_display(letter, location , display_height*1.4, 50, "Arial")
        location += 50
    pygame.display.update()

def checkAnswer(answer):
    win.fill(blue)
    win.blit(nc_back, (70,60))
    message_display(game.getCurrentNotecard().getDefinition(), display_width, display_height/2, 100, "Arial")
    if game.checkInput(answer):
        message_display("Correct!", display_width, display_height*1.4, 100, "Arial")
    else:
        message_display("Inorrect", display_width, display_height*1.4, 100, "Arial")
    pygame.display.update()
    getNextRanNC()
    time.sleep(2)

    return

def getNextNC():
    game.getNextNotecard()
    return 

def getNextRanNC():
    game.getNextNotecardRand()
    return

def getPrevNC():
    game.getPreviousNotecard()
    return

if __name__ == '__main__':
    win = pygame.display.set_mode((display_width, display_height))
    win.fill(blue)
    pygame.display.set_caption("Learn Russian")
    message_display("Hello!", display_width, display_height, 100, "Arial")
    pygame.display.update()
    time.sleep(2)
    game = GameClass()
    game.setUp(r'C:\Users\j51780\Documents\Notecards\words.txt')
    
    button_down = False
    run = True
    start = True
    
    while run:
        if start:
            start_screen()
            start = False
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            isFlip = True
            redraw_window()
            message_display("hi",display_width, display_height, 100, "Arial")
        pygame.display.update()

    pygame.quit()

