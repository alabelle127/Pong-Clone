import pygame as pg
import time

# Display Width and Display Height
dw = 800
dh = 600

gameDisplay = pg.display.set_mode((dw,dh))
pg.display.set_caption("Pong")
pg.init()

paddle = pg.mixer.Sound("paddle.wav")
ground = pg.mixer.Sound("ground.wav")
scores = pg.mixer.Sound("score.wav")

white = (255,255,255)
black = (0,0,0)

# Paddle Height and Paddle Width
ph = 60
pw = 10

def ball(x,y):
    pg.draw.rect(gameDisplay, white, (x, y, 10, 10))

def paddle1(x,y):
    pg.draw.rect(gameDisplay, white, (x,y,pw,ph))

def paddle2(x,y):
    pg.draw.rect(gameDisplay, white, (x,y,pw,ph))

# Speed of the Paddles
speed = s = 10

xP1, yP1 = 10, dh/2
xP2, yP2 = 780, dh/2
xb, yb = dw/2, dh/2

xChange, yChange = xcb, ycb = 5,2

p1Score = 0
p2Score = 0

playing = True

clock = pg.time.Clock()

score = False

win = 0

font = pg.font.SysFont(None, 100)

def displayText(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameDisplay.blit(screen_text, [x,y])

while playing:

    if score:
        time.sleep(1)
        score = False

    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    # Paddles

    if keys[pg.K_UP]:
        yP2 += s * -1
    if keys[pg.K_DOWN]:
        yP2 += s
    if keys[pg.K_w]:
        yP1 += s * -1
    if keys[pg.K_s]:
        yP1 += s

    # This enables the computer to basically cheat and go to where the ball is. I used it to test my program
    #yP1 = yb-ph//2

    # Ball

    if yb <= 0:
        pg.mixer.Sound.play(ground)
        ycb = -ycb
    if yb >= dh:
        pg.mixer.Sound.play(ground)
        ycb = -ycb
    if abs(xb) == xP2 and abs(yb) <= yP2 + ph and abs(yb) >= yP2:
        pg.mixer.Sound.play(paddle)
        xcb = -xcb
    if abs(xb) == xP1 and abs(yb) <= yP1 + ph and abs(yb) >= yP1:
        pg.mixer.Sound.play(paddle)
        xcb = -xcb

    #####################

    xb += xcb
    yb += ycb

    gameDisplay.fill(black)

    if xb >= dw:
        pg.mixer.Sound.play(scores)
        p1Score += 1
        score = True
    if xb <= 0:
        pg.mixer.Sound.play(scores)
        p2Score += 1
        score = True

    if score:
        xb, yb = dw//2, dh//2
        yP1, yP2 = dh//2, dh//2

    ball(xb, yb)
    paddle1(xP1, yP1)
    paddle2(xP2, yP2)

    displayText(str(p1Score), white, dw//4, dh//4)
    displayText(str(p2Score), white, dw - dw//4, dh//4)

    if p1Score == 11:
        win = 0
        playing = False
    if p2Score == 11:
        win = 1
        playing = False

    clock.tick(60)
    pg.display.update()

if win == 0:
    displayText("Player 1 Wins!", white, dw // 2, dh // 2)
    time.sleep(2)
if win == 1:
    displayText("Player 2 Wins!", white, dw // 2, dh // 2)
    time.sleep(2)
pg.quit()
quit()




