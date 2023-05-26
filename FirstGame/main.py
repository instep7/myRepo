import pygame as pg
import time
import random

pg.init()

display_width = 800
display_height = 1000

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption("LANE SPLITTER 0.2")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
brown = (150, 75, 0)
green = (0, 255, 0)

car_width = 40
car_height = 80

clock = pg.time.Clock()

carImg = pg.image.load('racecar.png')

road_surface = pg.Surface((600,1000))
road_surface.fill(black)

global HighScoreFile
HighScoreFile = open("HighScore.txt", "r+")
global highScore
highScore = HighScoreFile.read()
highScore = highScore.strip('\x00')
highScore = int(highScore)

global dodged
dodged = 0

def things_dodged(count):
    font = pg.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pg.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 255), white)
    return textSurface, textSurface.get_rect()

def message_display(text1, text2, text3):
    largeText = pg.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text1, largeText)
    TextRect.center = ((display_width/2),(display_height/6))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects(text2, largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects(text3, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pg.display.update()
    time.sleep(5)
    game_loop()

def crash():
    global dodged, highScore
    score = dodged
    if score > highScore:
        HighScoreFile.truncate(0)
        HighScoreFile.write(str(score))
        highScore = score
        message_display("  You Crashed...  ", "  NEW HIGH SCORE: " + str(highScore), "")
    else:
        message_display("  You Crashed...  ", "  SCORE: " + str(score) + "  ", "  Try to beat the HIGH SCORE: " + str(highScore) + "  ")

def game_loop():
    global dodged
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -1000
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    line_startx1 = 390
    line_starty1 = -60
    line_speed1 = 7
    line_width1 = 20
    line_height1 = 60

    line_startx2 = 390
    line_starty2 = -310
    line_speed2 = 7
    line_width2 = 20
    line_height2 = 60

    line_startx3 = 390
    line_starty3 = -560
    line_speed3 = 7
    line_width3 = 20
    line_height3 = 60

    line_startx4 = 390
    line_starty4 = -810
    line_speed4 = 7
    line_width4 = 20
    line_height4 = 60
    
    thingCount = 1

    dodged = 0

    speed = 5

    gameExit = False

    while not gameExit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = speed * -1
                elif event.key == pg.K_RIGHT:
                    x_change = speed
                elif event.key == pg.K_UP:
                    y_change = speed * -1
                elif event.key == pg.K_DOWN:
                    y_change = speed
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_UP or event.key == pg.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(green)
        gameDisplay.blit(road_surface, (100, 0))
        

        # things(thingx, thingy, thingw, thingh, color)
        things(line_startx1, line_starty1, line_width1, line_height1, white)
        line_starty1 += line_speed1
        things(line_startx2, line_starty2, line_width2, line_height2, white)
        line_starty2 += line_speed2
        things(line_startx3, line_starty3, line_width3, line_height3, white)
        line_starty3 += line_speed3
        things(line_startx4, line_starty4, line_width4, line_height4, white)
        line_starty4 += line_speed4
        things(thing_startx, thing_starty, thing_width, thing_height, brown)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if line_starty1 > display_height:
            line_starty1 = 0 - line_height1
            line_speed1 += .05
            line_speed2 += .05
            line_speed3 += .05
            line_speed4 += .05
        if line_starty2 > display_height:
            line_starty2 = 0 - line_height2
            line_speed1 += .05
            line_speed2 += .05
            line_speed3 += .05
            line_speed4 += .05
        if line_starty3 > display_height:
            line_starty3 = 0 - line_height3
            line_speed1 += .05
            line_speed2 += .05
            line_speed3 += .05
            line_speed4 += .05
        if line_starty4 > display_height:
            line_starty4 = 0 - line_height4 
            line_speed1 += .05
            line_speed2 += .05
            line_speed3 += .05
            line_speed4 += .05

        if x > display_width - car_width or x < 0:
            crash()
        if y > display_height - car_height or y < 0:
            crash()

        if x < 100 or x > 760:
            y_change = 3
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -3
                elif event.key == pg.K_RIGHT:
                    x_change = 3
            
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            speed = speed * 1.1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if thing_starty < y and y < thing_starty+thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                crash()

        pg.display.update()
        clock.tick(60)

    

game_loop()
pg.quit()
quit()