def all():   
    import pygame
    import time
    import threading
    import os
    import random
    pygame.init()
    background_colour = (255 ,255, 255)
    font_color = (0, 0, 0)
    FPS = 480
    CPS = 0
    timer = 6
    clicks = 0
    #PLEASE CHANGE THE RESOLUTION OCCORDING TO YOUR DEVICE DOWN BELOW
    #     |
    #     |
    #     |
    #   \ | /
    #    \ /
    #     V           (Don't change the resolution below than this. It might cause problems)
    (width, height) = (1366, 768)
    screen = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont('comicsans', 32)
    pygame.display.set_caption('Clicker game')
    screen.fill(background_colour)
    thread_started = False
    def display():
        welcome_msg = font.render("This is a clicker game, click as fast as you can anywhere!              CPS = Clicks Per Second                 Try to find hidden messages", False, font_color)
        screen.blit(welcome_msg, (10, 722))
        pygame.display.update()
    def main(thread_started, clicks):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicks = clicks + 1
                        if clicks == 100:
                            sequence = random.randrange(1,4,1)
                            if sequence == 1:
                                gud_msg1 = font.render("Bulling is bad as it troubles people and makes them insecure, we should start many campains set against bullying", False, font_color)
                                screen.blit(gud_msg1, (90, 100))
                            if sequence == 2:
                                gud_msg2 = font.render("My favorite food is pizza because love the texture of the base and the taste of cheese", False, font_color)
                                screen.blit(gud_msg2, (250, 100))
                            if sequence == 3:
                                gud_msg3 = font.render("Yes, Covid-19 was beneficial for the environment because not many people went outside which reduced the C02 emmisions", False, font_color)
                                screen.blit(gud_msg3, (40, 100))
                        def countdown():
                            timer = 6
                            for i in range(timer):
                                timer = timer - 1
                                timer_dis = font.render("Time remaining: " + str(timer), False, font_color)
                                screen.blit(timer_dis, (50, 20))
                                time.sleep(1)
                                pygame.draw.rect(screen, background_colour, pygame.Rect(220, 20, 60, 60))
                                if timer == 0:
                                    timer_dis = font.render("Time remaining: " + str(timer), False, font_color)
                                    screen.blit(timer_dis, (50, 20))
                                    CPS = clicks/6
                                    CPS_dis = font.render("CPS = " + str(round(CPS, 2)), False, font_color)
                                    pygame.draw.rect(screen, background_colour, pygame.Rect(1200, 20, 120, 60))
                                    screen.blit(CPS_dis, (1100, 20))
                                    CPS = round(CPS, 0)
                                    if CPS == 0 or CPS == 1 or CPS == 2or CPS == 3:
                                        turtle = pygame.image.load(os.path.join('Assets', 'Turtle.png'))
                                        screen.blit(turtle, (460, 280))
                                        turtle_msg = font.render("I eat faster than your clicking speed", False, font_color)
                                        screen.blit(turtle_msg, (510, 550))
                                    elif CPS == 4 or CPS == 5 or CPS == 6 or CPS == 7 or CPS == 8:
                                        rabbit = pygame.image.load(os.path.join('Assets', 'Rabbit.jpeg'))
                                        rabbit = pygame.transform.scale(rabbit, (400, 240))
                                        screen.blit(rabbit, (500, 280))
                                        rabbit_msg = font.render("Flicker your finger even faster, you are close to being the best", False, font_color)
                                        screen.blit(rabbit_msg, (380, 550))
                                    elif CPS == 9 or CPS == 10 or CPS == 11 or CPS == 12 or CPS == 13 or CPS == 14 or CPS == 15 or CPS == 16 or CPS == 17 or CPS == 18 or CPS == 19:
                                        cheetah = pygame.image.load(os.path.join('Assets', 'Cheetah.jpg'))
                                        screen.blit(cheetah, (350, 200))
                                        cheetah_msg = font.render("Your fingers snap at blistering speed, hail to the king of clicking", False, font_color)
                                        screen.blit(cheetah_msg, (370, 550))
                                    else:
                                        cheater = font.render("Cheater", False, font_color)
                                        screen.blit(cheater, (640, 370))
                        countdown_thread = threading.Thread(target = countdown)
                        click_surface = font.render('Clicks - ' + str(clicks), False, font_color)
                        pygame.draw.rect(screen, background_colour, pygame.Rect(640, 20, 120, 60))
                        screen.blit(click_surface, (630, 20))
                        if not thread_started:
                            countdown_thread.start()
                            thread_started = True
                    if clicks == -1:
                        clicks = clicks + 1
                        click_surface = font.render('Clicks - ' + str(clicks), False, font_color)
                        pygame.draw.rect(screen, background_colour, pygame.Rect(700, 20, 120, 60))
                        screen.blit(click_surface, (580, 20))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        #program closed
            display()
    main(thread_started, clicks)
all()