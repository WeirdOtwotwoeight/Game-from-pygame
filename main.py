import pygame  #Обязательно нужно установить pygame перед использованием его
import time
import random
import mixer

pygame.init()

pygame.mixer.init()


image_pygame = None
our_frame = None
buttcolor = None
qwerty = None
in_the_start=False
in_da_start = False
in_boss_start = False
minus = False
life = 100
rock_hitbox = None
rock_hitbox_two = None
rock_hitbox_three = None
open = 5
close = None
check_key_one = False
check_key_two = False
check_key_three = False
check_key_four = False
check_key_five = False
hero_hitboxes = None
music = None
random_time = 3000
fish_y = random.randint(0, 1024)
fish_x = 0
one_second = 1000
five_seconds = 5000
endless = True
sec = 1000
costume = True
able = True
more_ticks = pygame.time.get_ticks()
fish_last_time = None#Время, когда рыба ушла за экран
fish_delay = 0#Задержка, перед повторным появлением рыбы в миллисекундах
How_many = None
WG_fish_hitboxes = None
Fish_gonna_get_you = True
second_level_in_the_start = False
invisibilaty = True
mask = None
wall_mask = None


time_in_the_start = pygame.time.get_ticks()+sec#Эта переменная хранит в себе количество милисекунд, которые прошли с запуска программы
I_hate_timers = pygame.time.get_ticks()
get = pygame.time.get_ticks()


def draw_mask(mask, surface, color=(255, 0, 0)):
    """
    Отображает маску на заданной поверхности.
    :param mask: Маска уровня (pygame.mask.Mask)
    :param surface: Поверхность для отрисовки (pygame.Surface)
    :param color: Цвет маски
    """
    mask_surface = pygame.Surface(mask.get_size())
    mask_surface.fill((0, 0, 0))  # Залить черным цветом
    mask_outline = mask.outline()  # Получаем контуры маски

    # Рисуем точки контура
    for point in mask_outline:
        mask_surface.set_at(point, color)

    # Отображаем на экране
    surface.blit(mask_surface, (0, 0))



width = 1024
height = 1024

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Окно, созданное на pygame")

color_white = (255, 255, 255)


lasers = [
    pygame.Rect(428, 100, 60, 5),
    pygame.Rect(537, 200, 70, 5),
    pygame.Rect(700, 12, 5, 63),
    pygame.Rect(928, 300, 88, 5),
    pygame.Rect(928, 500, 88, 5)
]
# Начальные координаты героя
hero_x = 425
hero_y = 10
hero_speed = 1# Скорость движения героя
meteorite_x = random.randint(0,924)
meteorite_y = 0
meteorite_witch = 1
meteorite_x_x = random.randint(0, 924)
meteorite_three_x = random.randint(0, 924)
meteorite_four_x = random.randint(0, 924)

brain_image = pygame.image.load("Brain picture/Brain.png").convert_alpha()
pers_image = pygame.image.load("Images_hero/right1 (1) (1).png").convert_alpha()
image_pygame = pygame.image.load("Images_mazes/maze1b.png").convert_alpha()
mainy = pygame.image.load("Images_mazes/main_maze.png").convert_alpha()  # Путь к картинке
qwerty = pygame.image.load("Images_mazes/maze2.png").convert()#convert отключает прозрачность для изображений
bowlleg = pygame.image.load("Images_mazes/maze3c.png").convert_alpha()
key = pygame.image.load("Key image/key.png").convert_alpha()
rock = pygame.image.load("Meteorite image/meteorite3.png").convert_alpha()
mainy = pygame.image.load("Images_mazes/main_maze.png").convert_alpha()
octo = pygame.image.load("enemy/spooky_scary_octopus.png").convert_alpha()
water = pygame.image.load("enemy/water_location.png").convert_alpha()
goofish = pygame.image.load("fish/angry_goofy_fish2.png").convert_alpha()
goofish_two = pygame.image.load("fish/angry_goofy_fish.png").convert_alpha()


#Изменяю размер картинок
goofish = pygame.transform.scale(goofish, (100, 100))
octo = pygame.transform.scale(octo, (100, 100))#Изменил размер картинки
goofish_two = pygame.transform.scale(goofish_two, (100, 100))


#Создание шрифтов для виджетов
comic_sans = pygame.font.Font("Fonts/papyrus.ttf", 50)
minifont = pygame.font.Font("Fonts/papyrus.ttf", 25)
new_font = pygame.font.Font("Fonts/papyrus.ttf", 40)
Back_text = new_font.render("Back to menu", True, (255, 255, 255))
big_new_font = pygame.font.Font("Fonts/papyrus.ttf", 60)

#Музыка
pygame.mixer.music.load("Musicy/BOSS_MUSIC.mp3")
pygame.mixer.music.set_volume(0.15)#Изменили громкость музыки в pygame
pygame.mixer.music.play()


Laser_death = pygame.mixer.Sound("Musicy/laser_shot.mp3")


Next_level = pygame.mixer.Sound("Musicy/Welcome.mp3")
Next_level.set_volume(1.0)








our_frame = "menu"

buttcolor = (255, 255, 255)
Redbull = (255, 0, 0)
Ban_on_Twich = (255, 255, 255)
Start_button = pygame.Rect(370, 400, 280, 60)
little_buttons = pygame.Rect(370, 460, 140, 60, )





vidiblasers=True
paradox = time.time()
seconds = 2
def Menu_function():

    screen.blit(mainy, (0, 0))  # Отображаю картинку

    pygame.draw.rect(screen, buttcolor, Start_button, 2)
    pygame.draw.rect(screen, buttcolor, little_buttons, 2)
    pygame.draw.rect(screen, buttcolor, (510, 460, 140, 60), 2)

    comic_sans = pygame.font.Font("Fonts/papyrus.ttf", 50)
    minifont = pygame.font.Font("Fonts/papyrus.ttf", 25)

    start_text = comic_sans.render("Start", True, (255, 255, 255))
    settings_text = minifont.render("Settings", True, (255, 255, 255))
    exit_text = minifont.render("Exit", True, (255, 255, 255))

    screen.blit(start_text, (460, 395))
    screen.blit(settings_text, (395, 480))
    screen.blit(exit_text, (550, 480))


def Maze1_function():
    global image_pygame, hero_hitboxes, pers_image, our_frame, hero_x, hero_y, How_many, in_the_start

    keys = pygame.key.get_pressed()
    hero_speed = 0.36

    hero_hitboxes = pers_image.get_rect(topleft=(hero_x, hero_y))  #Хитбоксы персонажа
    first_hero_mask = pygame.mask.Mask((hero_hitboxes.width, hero_hitboxes.height), True)


    screen.blit(image_pygame, (0, 0))
    screen.blit(pers_image, hero_hitboxes.topleft)  #Отображает персонажа там, где его хитбокс
    screen.blit(brain_image, (10, 10))
    pygame.draw.rect(screen, (255, 0, 0), hero_hitboxes, 2)

    first_mask = pygame.mask.from_threshold(image_pygame, (255, 255, 255), (10, 10, 10))

    pygame.draw.rect(screen, (255, 255, 255), (350, 50, 280, 60,), 2)

    How_many = big_new_font.render(str(life), True, (0,0,0))


    screen.blit(Back_text, (360, 50))
    screen.blit(How_many, (59, 7))

    first_wall_kaboom = (hero_x, hero_y)
    if first_mask.overlap(first_hero_mask, first_wall_kaboom):
        print("Ого, ого всё работает")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            hero_y -= 1
        if keys[pygame.K_UP]:
            hero_y += 1
        if keys[pygame.K_RIGHT]:
            hero_x -= 1
        if keys[pygame.K_LEFT]:
            hero_x += 1

    if keys[pygame.K_DOWN]:
        next_y = hero_y + hero_speed
        if not first_mask.overlap_area(first_hero_mask, (hero_x, next_y)):
            hero_y = next_y
    if keys[pygame.K_UP]:
        next_y = hero_y - hero_speed
        if not first_mask.overlap_area(first_hero_mask, (hero_x, next_y)):
            hero_y = next_y
    if keys[pygame.K_RIGHT]:
        next_x = hero_x + hero_speed
        if not first_mask.overlap_area(first_hero_mask, (next_x, hero_y)):
            hero_x = next_x
    if keys[pygame.K_LEFT]:
        next_x = hero_x - hero_speed
        if not first_mask.overlap_area(first_hero_mask, (next_x, hero_y)):
            hero_x = next_x

    if hero_x >= 453 and hero_x <= 477 and hero_y >= 930 and hero_y <= 972: #Проверяю, находиться ли персонаж в диапозоне финиша
        in_the_start = True
        our_frame = "maze2"
        Next_level.play()

    return(How_many)

original_qwerty = None
def Maze2_function():
    global hero_x, hero_y, qwerty, original_qwerty, pers_image, hero_hitboxes, wall_mask, second_level_in_the_start, our_frame

    # Инициализация уровня
    if not second_level_in_the_start:
        hero_x = 450
        hero_y = 10
        second_level_in_the_start = True
        # Загружаем изображение карты и создаём маску для стен
        original_qwerty = pygame.image.load("Images_mazes/maze2.png").convert()
        wall_mask = pygame.mask.from_threshold(original_qwerty, (255, 255, 255), (10, 10, 10))  # Белые стены


    # Определяем хитбокс героя
    hero_hitboxes = pers_image.get_rect(topleft=(hero_x, hero_y))
    hero_mask = pygame.mask.Mask((hero_hitboxes.width, hero_hitboxes.height), True)#В перенную сохранили каждый пиксель уровня и определили, какие из них белые

    # Проверка столкновений с белыми стенами
    wall_offset = (hero_x, hero_y)
    if wall_mask.overlap(hero_mask, wall_offset):  # Если герой касается белой стены
        print("Герой коснулся белой стены!")
        # Отталкиваем героя обратно
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            hero_y -= 1
        if keys[pygame.K_UP]:
            hero_y += 1
        if keys[pygame.K_RIGHT]:
            hero_x -= 1
        if keys[pygame.K_LEFT]:
            hero_x += 1

    # Отрисовка уровня
    screen.fill((0, 0, 0))
    screen.blit(original_qwerty, (0, 0))  # Отображаем карту
    screen.blit(pers_image, (hero_x, hero_y))  # Отображаем героя
    pygame.draw.rect(screen, (255, 0, 0), hero_hitboxes, 2)  # Отображаем хитбокс героя

    # Обработка движения персонажа
    keys = pygame.key.get_pressed()
    hero_speed = 0.36

    # Проверяем движение с учётом белых стен
    if keys[pygame.K_DOWN]:
        next_y = hero_y + hero_speed
        if not wall_mask.overlap_area(hero_mask, (hero_x, next_y)):
            hero_y = next_y
    if keys[pygame.K_UP]:
        next_y = hero_y - hero_speed
        if not wall_mask.overlap_area(hero_mask, (hero_x, next_y)):
            hero_y = next_y
    if keys[pygame.K_RIGHT]:
        next_x = hero_x + hero_speed
        if not wall_mask.overlap_area(hero_mask, (next_x, hero_y)):
            hero_x = next_x
    if keys[pygame.K_LEFT]:
        next_x = hero_x - hero_speed
        if not wall_mask.overlap_area(hero_mask, (next_x, hero_y)):
            hero_x = next_x

    pygame.display.flip()

    if hero_x >= 577 and hero_x <= 607 and hero_y >= 902 and hero_y <= 968:
        our_frame = "maze3"


hit_detected = False  # Глобальная переменная для отслеживания столкновения

def Meteorites():
    global meteorite_y, meteorite_x, meteorite_x_x, meteorite_three_x
    global rock_hitbox, rock_hitbox_two, rock_hitbox_three

    if rock:  # Убедимся, что изображение загружено
        if isinstance(meteorite_x, (int, float)) and isinstance(meteorite_y, (int, float)):
            rock_hitbox = rock.get_rect(topleft=(meteorite_x, meteorite_y))
            rock_hitbox_two = rock.get_rect(topleft=(meteorite_x_x, meteorite_y))
            rock_hitbox_three = rock.get_rect(topleft=(meteorite_three_x, meteorite_y))
        else:
            print("Ошибка: некорректные координаты для метеоритов")

        # Отрисовка метеоритов
        screen.blit(rock, (meteorite_x, meteorite_y))
        screen.blit(rock, (meteorite_x_x, meteorite_y))
        screen.blit(rock, (meteorite_three_x, meteorite_y))

        # Движение метеоритов
        if meteorite_y < 1024:
            meteorite_y += 0.5
        else:
            meteorite_y = 0
            meteorite_x = random.randint(0, 924)
            meteorite_x_x = random.randint(0, 924)
            meteorite_three_x = random.randint(0, 924)
    else:
        print("Ошибка: изображение метеорита не загружено")


hit_detected = False  # Глобальная переменная для отслеживания столкновения

def Maze3_function():
    global hit_detected, life, our_frame, hero_x, hero_y, in_the_start, in_da_start

    # Проверка столкновения с метеоритами
    if (rock_hitbox and rock_hitbox_two and rock_hitbox_three and
            (hero_hitboxes.colliderect(rock_hitbox) or
             hero_hitboxes.colliderect(rock_hitbox_two) or
             hero_hitboxes.colliderect(rock_hitbox_three))):
        if not hit_detected:  # Проверяем, не было ли уже столкновения
            life -= 1
            print(f"Осталось жизней: {life}")
            hit_detected = True  # Устанавливаем флаг столкновения
            if life == 0:  # Если жизней не осталось
                screen.fill((0, 0, 0))
                game_over_text = big_new_font.render("Game Over", True, (255, 0, 0))
                screen.blit(game_over_text, (400, 500))
                pygame.display.flip()
                pygame.time.wait(2000)  # Ожидание 2 секунды
                our_frame = "maze1"
                hero_x = 450
                hero_y = 10
                in_the_start = False
                in_da_start = False
                life = 3  # Сбрасываем жизни
            else:
                pygame.time.wait(1000)  # Задержка перед продолжением
    else:
        hit_detected = False  # Сбрасываем флаг, если больше нет столкновения




def Keys():
    print(hero_x, hero_y)
    global open, close, check_key_one, check_key_two, check_key_three, check_key_four, check_key_five, our_frame
    if check_key_one == False:
        screen.blit(key, (105, 105))
    if check_key_two == False:
        screen.blit(key, (870, 440))
    if check_key_three == False:
        screen.blit(key, (900, 30))
    if check_key_four == False:
        screen.blit(key, (450, 500))
    if check_key_five == False:
        screen.blit(key, (750, 860))
    if check_key_one == False:
       if hero_x>=85 and hero_x<= 125 and hero_y >= 85 and hero_y<= 125:
           open-=1
           check_key_one = True
           print(open)
    if check_key_two == False:
       if hero_x>=850 and hero_x<= 890 and hero_y >= 420 and hero_y<= 460:
           open-=1
           check_key_two = True
           print(open)
    if check_key_three == False:
        if hero_x >= 880 and hero_x <= 920 and hero_y >= 10 and hero_y <= 50:
            open-=1
            check_key_three = True
            print(open)
    if check_key_four == False:
        if hero_x>=430 and hero_x<=470 and hero_y>=480 and hero_y<=520:
            open-=1
            check_key_four = True
            print(open)
    if check_key_five == False:
        if hero_x>=730 and hero_x<=770 and hero_y>=840 and hero_y<= 880:
            open-=1
            check_key_five = True
            print(open)
    if hero_x >= 520 and hero_x <= 580 and hero_y>= 940 and hero_y<= 980:
        if open == 0:
            our_frame = "BOSS"






def BOSS():
    global hero_hitboxes, hero_y, hero_x, in_boss_start, fish_y, fish_x, get, more_ticks, fish_last_time, fish_delay, How_many, WG_fish_hitboxes, life
    screen.blit(water, (0,0))
    hero_hitboxes = pers_image.get_rect(topleft=(hero_x, hero_y))
    WG_fish_hitboxes = goofish.get_rect(topleft = (fish_x, fish_y))
    screen.blit(pers_image, hero_hitboxes.topleft)  # Отображает персонажа там, где его хитбокс
    pygame.draw.rect(screen, (255, 0, 0), hero_hitboxes, 2)
    pygame.draw.rect(screen, (255, 0, 0), WG_fish_hitboxes, 2)
    screen.blit(brain_image, (10, 10))


    How_many = big_new_font.render(str(life), True, (255, 255, 255))
    screen.blit(How_many, (60, 10))



    if fish_x <= 1024:
        fish_x+=1
    else:
        if fish_last_time == None:
            fish_last_time = pygame.time.get_ticks()
            fish_delay = random.randint(500, 1000)
        else:
            fish_x=0
            now = pygame.time.get_ticks()
            if now - fish_last_time >= fish_delay:
                fish_y = random.randint(0, 1024)
                fish_x = 0
                fish_last_time = None
    if costume == True:
        screen.blit(goofish, (fish_x, fish_y))
    else:
        screen.blit(goofish_two, (fish_x, fish_y))







    if in_boss_start == False:
        hero_y = 950
        hero_x = 450
        in_boss_start = True




running = True




while running:  #while running и while running==True - это одно и то же, можно писать и так, и так








    for event in pygame.event.get():  #Проверяем все события в игре

        if event.type == pygame.QUIT:  #Если событие - это закрытие окна...
            running = False  #...то тогда переменная running меняется на False и игровой цикл прекращается

        if event.type == pygame.MOUSEBUTTONDOWN:  #Если событие - нажатие на экран...
            if our_frame == "menu" and Start_button.collidepoint(event.pos):
                our_frame = "maze1"
    keys = pygame.key.get_pressed()

    if our_frame == "menu":  #Если то, где мы находимся(тоесть переменная our_frame) - это меню...

        Menu_function()  #...то запускается функция Menu_function, котора рисует все нужные нам в меню виджеты

#
    elif our_frame == "maze1":
        Maze1_function()

    elif our_frame == "maze2":
        Maze2_function()

    elif our_frame == "maze3":
        Maze3_function()
        if keys[pygame.K_DOWN]:  # Если стрелка вниз нажата
            if (bowlleg.get_at((hero_hitboxes.centerx, int(hero_hitboxes.bottom + hero_speed))) != Ban_on_Twich and #if (qwerty.get_at((hero_hitboxes.centerx, hero_hitboxes.bottom + hero_speed)) == Redbull or
                    bowlleg.get_at((hero_hitboxes.left, int(hero_hitboxes.bottom + hero_speed))) != Ban_on_Twich and
                    bowlleg.get_at((hero_hitboxes.right, int(hero_hitboxes.bottom + hero_speed))) != Ban_on_Twich):
                hero_y += 0.36  # Увеличиваем игрек персонажа

        if keys[pygame.K_UP]:# Если стрелка вверх нажата

            if (bowlleg.get_at((int(hero_hitboxes.centerx), int(hero_hitboxes.top - hero_speed))) != Ban_on_Twich and
                    bowlleg.get_at((int(hero_hitboxes.left), int(hero_hitboxes.top - hero_speed))) != Ban_on_Twich and
                    bowlleg.get_at((int(hero_hitboxes.right), int(hero_hitboxes.top - hero_speed))) != Ban_on_Twich):
                hero_y -= 0.36 # Уменьшаем игрек персонажа

        if keys[pygame.K_RIGHT]:  # Если стрелка вправо нажата
            if (bowlleg.get_at((int(hero_hitboxes.right + hero_speed), int(hero_hitboxes.centery))) != Ban_on_Twich and
                    bowlleg.get_at((int(hero_hitboxes.right + hero_speed), int(hero_hitboxes.top))) != Ban_on_Twich and
                    bowlleg.get_at((int(hero_hitboxes.right + hero_speed), int(hero_hitboxes.bottom))) != Ban_on_Twich):
                hero_x += 0.36  # Увеличиваем икс персонажа

        if keys[pygame.K_LEFT]:  # Если стрелка влево нажата
            if (bowlleg.get_at((int(hero_hitboxes.left - hero_speed), int(hero_hitboxes.centery))) != Ban_on_Twich and
                    bowlleg.get_at((int(hero_hitboxes.left - hero_speed), int(hero_hitboxes.top))) != Ban_on_Twich and
                    bowlleg.get_at((int(hero_hitboxes.left - hero_speed), int(hero_hitboxes.bottom))) != Ban_on_Twich):
                hero_x -= 0.36  # Уменьшаем икс персонажа
        if hero_hitboxes.colliderect(rock_hitbox) or hero_hitboxes.colliderect(rock_hitbox_two) or hero_hitboxes.colliderect(rock_hitbox_three):#Проверяем, столкновение-колизию двух прямоугольников
            life-=1
            if life == 0:
                pygame.time.wait(1000)
                minus = True
        if minus:
            our_frame="maze1"
            hero_x=450
            hero_y=10
            in_the_start = False
            in_da_start = False
            minus = False
            life = 3
    elif our_frame == "BOSS":
        BOSS()
        get = pygame.time.get_ticks()
        if keys[pygame.K_DOWN] and hero_y<= 950:  # Если стрелка вниз нажата:
            hero_y += 0.2  # Увеличиваем игрек персонажа

        if keys[pygame.K_UP] and hero_y>=0:  # Если стрелка вверх нажата
                hero_y -= 0.2  # Уменьшаем игрек персонажа

        if keys[pygame.K_RIGHT] and hero_x<=950:# Если стрелка вправо нажата
            hero_x += 0.2  # Увеличиваем икс персонажа

        if keys[pygame.K_LEFT] and hero_x>=0:  # Если стрелка влево нажата
            hero_x -= 0.2  # Уменьшаем икс персонажа


        HWTIT = pygame.time.get_ticks()
        if HWTIT >= I_hate_timers:
            costume = not costume
            I_hate_timers = pygame.time.get_ticks()+sec


        if hero_hitboxes.colliderect(WG_fish_hitboxes):
            life-=0.1
            print("аааа тебя рыба сожрала ужас")
        






    pygame.display.flip()  #Благодаря этой строчке мы сразу видим изменения на экране, если они будут происходить

pygame.quit()
#Следующий шаг - сделать проверку нажата ли клавиша стрелка вниз.
#Если нажата, то мы должны уменьшить y героя.
