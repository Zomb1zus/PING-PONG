from pygame import *
from random import *
from time import sleep
import time as pytime
from pygame.sprite import collide_rect

mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_player1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 407:
            self.rect.y += self.speed

    def update_player2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 407:
            self.rect.y += self.speed



def score_draw(scor_image, x, y):
        num = transform.scale(image.load(scor_image), (200, 200))
        window.blit(num, (x, y))


window = display.set_mode((500,500))
display.set_caption('Ping Pong')
game = True
background = transform.scale(image.load("Images/map.png"), (500, 500))

player1 = Player('Images/racket_red.png', 455, 216, 7, 36, 90)
player2 = Player('Images/racket_blue.png', 10, 216, 7, 36, 90)

management_red = GameSprite('Images/management_red.png', 265, 60, 6, 196, 196)
management_blue = GameSprite('Images/management_blue.png', 25, 60, 6, 196, 196)

ball = GameSprite('Images/ball.png', 250, 250, 6, 30, 30)


kick = 0 #счётчик столкновений с ракетками
stoper = 0 #курирующий счётчик для ограничений ускорения

score1 = 0
score2 = 0
begin = True
clock = time.Clock()

# ____скорость мяча вначале____
ran_x = randint(1, 2)
if ran_x == 1:
    speed_x = -2
    ran_y = randint(1, 2)
    if ran_y == 1:
        speed_y = -2
    else:
        speed_y = 2
if ran_x == 2:
    speed_x = 2
    ran_y = randint(1, 2)
    if ran_y == 1:
        speed_y = -2
    else:
        speed_y = 2
start = True
while game:

    '''ОБРАТНЫЙ ОТСЧЕТ'''
    if begin:
        mixer.music.load('Sounds/begin.mp3')
        mixer.music.play()
        a = 3
        for i in range(3):
            for w in event.get():
                if w.type == QUIT:
                    game = False
            ball.rect.x = 250
            ball.rect.y = 250

            a = str(a)
            countdown = 'Images/Countdown/countdown_' + a + '.png'
            a = int(a)
            i += 1
            a -= i
            if a == 0:
                a = 1
            countdown_imag = transform.scale(image.load(countdown), (300, 300))

            window.fill((0, 0, 0))
            window.blit(background, (0, 0))
            player1.reset()
            player2.reset()
            ball.reset()
            window.blit(countdown_imag, (110, 100))
            display.update()

            sleep(1)
        mixer.music.load('Sounds/whistle_begin.mp3')
        mixer.music.play()
        begin = False

    for i in event.get():
        if i.type == QUIT:
            game = False


    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    management_red.reset()
    management_blue.reset()
    '''ОТРИСОВКА ОЧКОВ'''
    point_str1 = str(score1)
    point_str1 = 'Images/numbers/' + point_str1 + '.png'
    score_draw(point_str1, 50, 250)

    point_str2 = str(score2)
    point_str2 = 'Images/numbers/' + point_str2 + '.png'
    score_draw(point_str2, 250, 250)




    '''ОТСКОК ОТ ПЕРВОГО'''
    if collide_rect(ball, player1):
        mixer.music.load('Sounds/rebound.mp3')
        mixer.music.play()
        kick += 1
        speed_x *= -1


    '''ОТСКОК ОТ ВТОРОГО'''
    if collide_rect(ball, player2):
        mixer.music.load('Sounds/rebound.mp3')
        mixer.music.play()
        kick += 1

        speed_x *= -1


    '''___________ОСКОРИТЕЛИ_______________'''
    if kick == 1 and stoper == 0:
        if speed_x < 0:
            speed_x = -4
        else:
            speed_x = 4

        if speed_y < 0:
            speed_y = -4
        else:
            speed_y = 4

        stoper = 1

    if kick == 4 and stoper == 1:
        speed_x_cur = uniform(4.1, 4.9)
        speed_y_cur = uniform(4.1, 4.9)
        if speed_x < 0:
            speed_x = -speed_x_cur
        else:
            speed_x = speed_x_cur

        if speed_y < 0:
            speed_y = -speed_y_cur
        else:
            speed_y = speed_y_cur

        stoper = 2

    if kick == 10 and stoper == 2:
        speed_x_cur = uniform(5.1, 5.9)
        speed_y_cur = uniform(5.1, 5.9)
        if speed_x < 0:
            speed_x = -speed_x_cur
        else:
            speed_x = speed_x_cur

        if speed_y < 0:
            speed_y = -speed_y_cur
        else:
            speed_y = speed_y_cur

        stoper = 3

    if kick == 16 and stoper == 3:
        speed_x_cur = uniform(6.1, 6.9)
        speed_y_cur = uniform(6.1, 6.9)
        if speed_x < 0:
            speed_x = -speed_x_cur
        else:
            speed_x = speed_x_cur

        if speed_y < 0:
            speed_y = -speed_y_cur
        else:
            speed_y = speed_y_cur

        stoper = 4

    if kick == 22 and stoper == 4:
        speed_x_cur = uniform(7.1, 7.9)
        speed_y_cur = uniform(7.1, 7.9)
        if speed_x < 0:
            speed_x = -speed_x_cur
        else:
            speed_x = speed_x_cur

        if speed_y < 0:
            speed_y = -speed_y_cur
        else:
            speed_y = speed_y_cur

        stoper = 5

    if kick == 28 and stoper ==5:
        speed_x_cur = uniform(8.1, 8.9)
        speed_y_cur = uniform(8.1, 8.9)
        if speed_x < 0:
            speed_x = -speed_x_cur
        else:
            speed_x = speed_x_cur

        if speed_y < 0:
            speed_y = -speed_y_cur
        else:
            speed_y = speed_y_cur

        stoper = 5


    '''ОТСКОКИ МЯЧА'''
    if ball.rect.y <= 0 or ball.rect.y >= 470:
        mixer.music.load('Sounds/rebound.mp3')
        mixer.music.play()
        speed_y *=-1

    ball.reset()

    player1.update_player2()
    player1.reset()

    player2.update_player1()
    player2.reset()






    # второй забивает
    if ball.rect.x <= -50:
        mixer.music.load('Sounds/goal_whistle.mp3')
        mixer.music.play()
        start = False
        kick = 0
        stoper = 0
        score2 += 1

        if score2 == 12:
            sleep(0.5)
            exit_not = True
            cup = GameSprite('Images/win.png', 0, 0, 0, 256, 256)
            mixer.music.load('Sounds/end_whistle.mp3')
            mixer.music.play()
            mixer.Sound('Sounds/applause_end.mp3').play()
            while exit_not:
                window.fill((0, 0, 0))
                window.blit(background, (0, 0))
                ball.kill()
                cup.rect.x = 265
                cup.rect.y = 100
                cup.reset()

                for i in event.get():
                    if i.type == QUIT:
                        game = False
                        exit_not = False

                clock.tick(60)
                display.update()
        else:
            window.fill((0, 0, 0))
            window.blit(background, (0, 0))
            management_red.reset()
            management_blue.reset()
            '''ОТРИСОВКА ОЧКОВ'''
            point_str1 = str(score1)
            point_str1 = 'Images/numbers/' + point_str1 + '.png'
            score_draw(point_str1, 50, 250)

            point_str2 = str(score2)
            point_str2 = 'Images/numbers/' + point_str2 + '.png'
            score_draw(point_str2, 250, 250)
            sleep(1)
            player1.rect.y = 216
            player2.rect.y = 216
            player1.reset()
            player2.reset()
            ball.rect.x = 240
            ball.rect.y = 240
            ball.reset()
            display.update()
            mixer.music.load('Sounds/whistle_begin.mp3')
            mixer.music.play()
            sleep(0.5)



    # первый забивает
    if ball.rect.x >= 500:
        mixer.music.load('Sounds/goal_whistle.mp3')
        mixer.music.play()

        start = False
        kick = 0
        stoper = 0
        score1 += 1

        if score1 == 12:
            sleep(0.5)
            exit_not = True
            mixer.music.load('Sounds/end_whistle.mp3')
            mixer.music.play()
            mixer.Sound('Sounds/applause_end.mp3').play()
            cup = GameSprite('Images/win.png', 0, 0, 0, 256, 256)
            while exit_not:
                window.fill((0, 0, 0))
                window.blit(background, (0, 0))
                ball.kill()
                cup.rect.x = 2
                cup.rect.y = 100
                cup.reset()
                for i in event.get():
                    if i.type == QUIT:
                        game = False
                        exit_not = False

                clock.tick(60)
                display.update()
        else:
            window.fill((0, 0, 0))
            window.blit(background, (0, 0))
            management_red.reset()
            management_blue.reset()
            '''ОТРИСОВКА ОЧКОВ'''
            point_str1 = str(score1)
            point_str1 = 'Images/numbers/' + point_str1 + '.png'
            score_draw(point_str1, 50, 250)

            point_str2 = str(score2)
            point_str2 = 'Images/numbers/' + point_str2 + '.png'
            score_draw(point_str2, 250, 250)
            sleep(1)
            player1.rect.y = 216
            player2.rect.y = 216
            player1.reset()
            player2.reset()
            ball.rect.x = 240
            ball.rect.y = 240
            ball.reset()
            display.update()
            mixer.music.load('Sounds/whistle_begin.mp3')
            mixer.music.play()
            sleep(0.5)





    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if kick == 0 and not start:
        # ____скорость мяча вначале____
        ran_x = randint(1, 2)
        if ran_x == 1:
            speed_x = -2
            ran_y = randint(1, 2)
            if ran_y == 1:
                speed_y = -2
            else:
                speed_y = 2
        if ran_x == 2:
            speed_x = 2
            ran_y = randint(1, 2)
            if ran_y == 1:
                speed_y = -2
            else:
                speed_y = 2

        start = True
    clock.tick(60)
    display.update()





