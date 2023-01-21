# Complete your game here
import pygame
import random


class MyGame:
    def __init__(self):
        pygame.init()

        self.load_images()

        self.window = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("MONEY HUNT")
        
        self.x = 900-self.robot.get_width()
        self.y = 700-self.robot.get_height()
        self.m = 0
        self.n = 700-self.ghost.get_height()

        self.to_right = False
        self.to_left = False
        self.to_up = False
        self.to_down = False
        self.d = False
        self.a = False
        self.w = False
        self.s = False

        self.speed = 4
        self.list_coordinates = []
        self.coin_generator = True

        self.robot_points = 0
        self.ghost_points = 0

        self.clock = pygame.time.Clock()

        self.intro()

    def load_images(self):
        self.robot = pygame.image.load("robot.png")
        self.ghost = pygame.image.load("monster.png")
        self.coin = pygame.image.load("coin.png")

    def main_loop(self):
        while True:
            self.check_events()
            self.robot_movement()
            self.ghost_movement()
            self.collecting_coins()
            self.draw_window()
            self.clock.tick(60)
            if self.robot_points == 10 or self.ghost_points == 10:
                break
        self.outro()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                if event.key == pygame.K_UP:
                    self.to_up = True
                if event.key == pygame.K_DOWN:
                    self.to_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
                if event.key == pygame.K_UP:
                    self.to_up = False
                if event.key == pygame.K_DOWN:
                    self.to_down = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.a = True
                if event.key == pygame.K_d:
                    self.d = True
                if event.key == pygame.K_w:
                    self.w = True
                if event.key == pygame.K_s:
                    self.s = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.a = False
                if event.key == pygame.K_d:
                    self.d = False
                if event.key == pygame.K_w:
                    self.w = False
                if event.key == pygame.K_s:
                    self.s = False

    def robot_movement(self):
        if self.to_right:
            self.x += self.speed
            if self.x+self.robot.get_width() >= 900:
                self.to_right = False

        if self.to_left:
            self.x -= self.speed
            if self.x <= 0:
                self.to_left = False

        if self.to_up:
            self.y -= self.speed
            if self.y <= 0:
                self.to_up = False

        if self.to_down:
            self.y += self.speed
            if self.y+self.robot.get_height() >= 700:
                self.to_down = False
        
        self.robot_coordinates = (self.x, self.y)
    
    def ghost_movement(self):
        if self.d:
            self.m += 4
            if self.m+self.ghost.get_width() >= 900:
                self.d = False

        if self.a:
            self.m -= 4
            if self.m <= 0:
                self.a = False

        if self.w:
            self.n -= 4
            if self.n <= 0:
                self.w = False

        if self.s:
            self.n += 4
            if self.n+self.ghost.get_height() >= 700:
                self.s = False
        
        self.ghost_coordinates = (self.m, self.n)

    def draw_clouds(self):
        #cloud1
        pygame.draw.circle(self.window, (255, 255, 255), (150, 100), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (230, 100), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (110, 140), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (190, 150), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (270, 140), 50)

        #sun
        pygame.draw.circle(self.window, (255,215,0), (500, 200), 70)

        #cloud2
        pygame.draw.circle(self.window, (255, 255, 255), (650, 200), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (730, 200), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (610, 240), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (690, 250), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (770, 240), 50)

        
        #cloud3
        pygame.draw.circle(self.window, (255, 255, 255), (550, 270), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (630, 270), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (510, 310), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (590, 320), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (670, 310), 50)

        #cloud4
        pygame.draw.circle(self.window, (255, 255, 255), (220, 400), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (300, 400), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (180, 440), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (260, 450), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (340, 440), 50)

        #cloud5
        pygame.draw.circle(self.window, (255, 255, 255), (720, 500), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (800, 500), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (680, 540), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (760, 550), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (840, 540), 50)

        #cloud6
        pygame.draw.circle(self.window, (255, 255, 255), (420, 660), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (500, 660), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (380, 700), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (460, 710), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (540, 700), 50)
        
        #cloud7
        pygame.draw.circle(self.window, (255, 255, 255), (40, 560), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (120, 560), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (0, 600), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (60, 610), 50)
        pygame.draw.circle(self.window, (255, 255, 255), (145, 600), 50)
        

    def draw_window(self):
        self.window.fill((100, 255, 255))
        self.draw_clouds()

        self.coins_generator()
        self.window.blit(self.robot, (self.robot_coordinates))
        self.window.blit(self.ghost, (self.ghost_coordinates))

        game_font = pygame.font.SysFont("Hack", 20)
        
        text_r = game_font.render(f"Robot's money: {self.robot_points}€", True, (255, 0, 0))
        text_g = game_font.render(f"Ghost's money: {self.ghost_points}€", True, (255, 0, 0))
        
        self.window.blit(text_g, (30, 10))
        self.window.blit(text_r, (680, 10))

        pygame.display.flip()

    def coins_generator(self):

        if self.coin_generator:
            x = random.randint(0, 900-self.coin.get_width())
            y = random.randint(40, 700-self.coin.get_height())
            self.coin_generator = False
            self.coin_coordinates = (x, y)
            self.list_coordinates.append(self.coin_coordinates)

        self.window.blit(self.coin, self.coin_coordinates)

    def collecting_coins(self):
        if len(self.list_coordinates) > 0:
            coordinates = self.list_coordinates[-1]
            x = coordinates[0]
            y = coordinates[1]
            
            if self.x <= x <= self.x+self.robot.get_width() or self.x <= x+self.coin.get_width() <= self.x+self.robot.get_width():
                if self.y <= y <= self.y+self.robot.get_height() or self.y <= y+self.coin.get_height() <= self.y+self.robot.get_height():
                    self.robot_points += 1
                    self.coin_generator = True

            if self.m <= x <= self.m+self.ghost.get_width() or self.m <= x+self.coin.get_width() <= self.m+self.ghost.get_width():
                if self.n <= y <= self.n+self.ghost.get_height() or self.n <= y+self.coin.get_height() <= self.n+self.ghost.get_height():
                    self.ghost_points += 1
                    self.coin_generator = True
                  
    def intro(self):
        while True:
            for event in pygame.event.get():    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]

                    if 550 <= mouse_x <= 770 and 550 <= mouse_y <= 650:
                        self.main_loop()
                
                if event.type == pygame.QUIT:
                    exit()
            
            self.window.fill((100, 225, 225))
            pygame.draw.rect(self.window, (255, 255, 255), (80, 180, 320, 210))
            pygame.draw.rect(self.window, (255, 255, 255), (530, 180, 320, 210))

            hello_font = pygame.font.SysFont("Hack", 50)
            player_font = pygame.font.SysFont("Hack", 30)
            moves_font = pygame.font.SysFont("Hack", 15)
            ins_font = pygame.font.SysFont("Hack", 20)

            hello = hello_font.render("Hello!", True, (0, 0, 0))
            p1 = player_font.render("Player 1: GHOST", True, (255, 0, 0))
            p1_moves = moves_font.render("Press A, W, S, D to move", True, (255, 0, 0))
            p2 = player_font.render("Player 2: ROBOT", True, (255, 0, 0))
            p2_moves = moves_font.render("Press arrows to move", True, (255, 0, 0))
            ins1 = ins_font.render("Instructions:", True, (0, 0, 0))
            ins2 = ins_font.render("Run to collect money.", True, (0, 0, 0))
            ins3 = ins_font.render("Player who collects 10€ wins!", True, (0, 0, 0))
            ins4 = ins_font.render("Press play to start:", True, (0, 0, 0))
            play = player_font.render("PLAY!", True, (0, 0, 0))

            self.window.blit(hello, (350, 80))
            self.window.blit(p1, (100, 200))
            self.window.blit(self.ghost, (200, 250))
            self.window.blit(p1_moves, (130, 350))
            self.window.blit(p2, (550, 200))
            self.window.blit(self.robot, (660, 250))
            self.window.blit(p2_moves, (590, 350))

            self.window.blit(ins1, (80, 470))
            self.window.blit(ins2, (90, 510))
            self.window.blit(ins3, (90, 535))
            self.window.blit(ins4, (550, 500))

            pygame.draw.rect(self.window, (225, 0, 0), (550, 550, 250, 100))
            self.window.blit(play, (630, 580))

            pygame.display.flip()

            self.clock.tick(60)

    def outro(self):
        while True:
            for event in pygame.event.get():    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]

                    if 220 <= mouse_x <= 370 and 550 <= mouse_y <= 630:
                        self.robot_points = 0
                        self.ghost_points = 0
                        self.to_right = False
                        self.to_left = False
                        self.to_up = False
                        self.to_down = False
                        self.d = False
                        self.a = False
                        self.w = False
                        self.s = False
                        self.main_loop()
                    
                    if 570 <= mouse_x <= 720 and 550 <= mouse_y <= 630:
                        exit()
                
                if event.type == pygame.QUIT:
                    exit()
            
            self.window.fill((100, 225, 225))
            self.draw_clouds()

            font_winner = pygame.font.SysFont("Hack", 70)
            font_replay = pygame.font.SysFont("Hack", 30)

            replay = font_replay.render("Replay", True, (0, 0, 0))
            ext = font_replay.render("Exit", True, (0, 0, 0))

            if self.robot_points == 10:
                winner = font_winner.render("ROBOT won!", True, (255, 0, 0))
                self.window.blit(self.robot, (400, 270))
            if self.ghost_points == 10:
                winner = font_winner.render("GHOST won!", True, (255, 0, 0))
                self.window.blit(self.ghost, (400, 270))

            pygame.draw.rect(self.window, (0, 0, 0), (0, 400, 900, 300))
            pygame.draw.rect(self.window, (225, 0, 0), (200, 530, 150, 80))
            pygame.draw.rect(self.window, (225, 0, 0), (530, 530, 150, 80))

            self.window.blit(winner, (225, 130))
            self.window.blit(replay, (220, 550))
            self.window.blit(ext, (570, 550))
        
            pygame.display.flip()

            self.clock.tick(60)

if __name__ == "__main__":
    MyGame()