import pygame
import os
import time
from random import randint, choice
from math import ceil

base_directory = os.path.abspath(os.path.dirname(__file__))
FPS = 144

class Score:

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        high_score_file = open(os.path.join(base_directory, 'resources', 'highscore.txt'), 'r')
        self.high_score = high_score_file.read()
        high_score_file.close()
        self.actual_score = 0
        self.previous_score = 0
        self.point_gain_sound_channel = pygame.mixer.Channel(3)
        self.zero_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', '0.png')).convert_alpha()
        self.one_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', '1.png')).convert_alpha()
        self.two_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', '2.png')).convert_alpha()
        self.three_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', '3.png')).convert_alpha()
        self.four_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', '4.png')).convert_alpha()
        self.five_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', '5.png')).convert_alpha()
        self.six_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', '6.png')).convert_alpha()
        self.seven_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', '7.png')).convert_alpha()
        self.eight_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', '8.png')).convert_alpha()
        self.nine_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', '9.png')).convert_alpha()

        if (pygame.display.Info().current_w > 1280) and (pygame.display.Info().current_h > 720):
            self.zero_image = pygame.transform.scale2x(self.zero_image)
            self.one_image = pygame.transform.scale2x(self.one_image)
            self.two_image = pygame.transform.scale2x(self.two_image)
            self.three_image = pygame.transform.scale2x(self.three_image)
            self.four_image = pygame.transform.scale2x(self.four_image)
            self.five_image = pygame.transform.scale2x(self.five_image)
            self.six_image = pygame.transform.scale2x(self.six_image)
            self.seven_image = pygame.transform.scale2x(self.seven_image)
            self.eight_image = pygame.transform.scale2x(self.eight_image)
            self.nine_image = pygame.transform.scale2x(self.nine_image)
            
    def draw_score(self):
        self.actual_score = int(ceil(self.score/2))
        temp_score = int(ceil(self.score/2))
        temp_score = [int(num) for num in str(temp_score)]
        number_count = []
        
        if len(temp_score)>0:
            for i in temp_score:
                if i == 0:
                    number_count.append(self.zero_image)
                elif i == 1:
                    number_count.append(self.one_image)
                elif i == 2:
                    number_count.append(self.two_image)               
                elif i == 3:
                    number_count.append(self.three_image)
                elif i == 4:
                    number_count.append(self.four_image)
                elif i == 5:
                    number_count.append(self.five_image)
                elif i == 6:
                    number_count.append(self.six_image)
                elif i == 7:
                    number_count.append(self.seven_image)
                elif i == 8:
                    number_count.append(self.eight_image)
                elif i == 9:
                    number_count.append(self.nine_image)

        if len(temp_score) == 1:
            number_rect_1 = number_count[0].get_rect(center=(144,100))
            self.screen.blit(number_count[0], number_rect_1 )

        elif len(temp_score) == 2:
            number_rect_1 = number_count[1].get_rect(midleft=(144,100))
            self.screen.blit(number_count[1], number_rect_1)
            number_rect_2 = number_count[0].get_rect(midright=(144,100))
            self.screen.blit(number_count[0], number_rect_2 )

        if self.previous_score < self.actual_score:
            self.point_gain_sound_play()
            self.previous_score = self.actual_score

    def point_gain_sound_play(self):
        point_sound = pygame.mixer.Sound(os.path.join(base_directory, 'resources', 'audio' ,'point.wav'))
        self.point_gain_sound_channel.set_volume(0.25)
        self.point_gain_sound_channel.play(point_sound)

    def high_score_reader(self):
        current_score = self.actual_score
        file_score = 0
        high_score_file = open(os.path.join(base_directory, 'resources', 'highscore.txt'), 'r')
        file_score = high_score_file.read()
        high_score_file.close()
        if current_score > int(file_score):
            high_score_file = open(os.path.join(base_directory, 'resources', 'highscore.txt'), 'w')
            file_score = high_score_file.write(str(current_score))
            high_score_file.close()

    def draw_high_score(self):
        text = 'Highscore ' + str(self.high_score)
        FONT = pygame.font.Font(os.path.join(base_directory, 'resources', 'font', 'Flappy-Bird.ttf'), 50)
        display_high_score = FONT.render(text, True, (255, 255, 255))
        display_high_score = display_high_score.get_rect(center=(144,256))
        self.screen.blit(FONT.render(text, True, (255, 255, 255)), display_high_score)

class Bird:
    def __init__(self, screen):
        self.current_flap = 0
        self.screen = screen
        self.random_number = randint(0,2)
        self.bird = 0

        if (pygame.display.Info().current_w > 1280) and (pygame.display.Info().current_h > 720):
            if (self.random_number == 0):
                self.bird_top_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'redbird-topflap.png')).convert_alpha()
                self.bird_mid_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'redbird-midflap.png')).convert_alpha()
                self.bird_down_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'redbird-downflap.png')).convert_alpha()

            elif (self.random_number == 1):
                self.bird_top_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'bluebird-topflap.png')).convert_alpha()
                self.bird_mid_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'bluebird-midflap.png')).convert_alpha()
                self.bird_down_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'bluebird-downflap.png')).convert_alpha()

            else:
                self.bird_top_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'yellowbird-topflap.png')).convert_alpha()
                self.bird_mid_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'yellowbird-midflap.png')).convert_alpha()
                self.bird_down_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'yellowbird-downflap.png')).convert_alpha()

            self.bird_top_flap_image = pygame.transform.scale2x(self.bird_top_flap_image)
            self.bird_mid_flap_image = pygame.transform.scale2x(self.bird_mid_flap_image)
            self.bird_down_flap_image = pygame.transform.scale2x(self.bird_down_flap_image)

        else:

            if (self.random_number == 0):
                self.bird_top_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'redbird-upflap.png')).convert_alpha()
                self.bird_mid_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'redbird-midflap.png')).convert_alpha()
                self.bird_down_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'redbird-downflap.png')).convert_alpha()

            elif (self.random_number == 1):
                self.bird_top_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'bluebird-upflap.png')).convert_alpha()
                self.bird_mid_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'bluebird-midflap.png')).convert_alpha()
                self.bird_down_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'bluebird-downflap.png')).convert_alpha()

            else:
                self.bird_top_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'yellowbird-upflap.png')).convert_alpha()
                self.bird_mid_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'yellowbird-midflap.png')).convert_alpha()
                self.bird_down_flap_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'yellowbird-downflap.png')).convert_alpha()
        
        self.bird_rectangle = self.bird_mid_flap_image.get_rect(center=(50, 200))
        self.bird_images_list = [self.bird_top_flap_image, self.bird_mid_flap_image, self.bird_down_flap_image]

    def swinging_bird(self):
        if self.current_flap > 2:
            self.current_flap = 0
        self.bird = self.bird_images_list[self.current_flap]
        self.current_flap += 1

    def rotating_and_drawing_bird(self, angle):
        rotating_bird = pygame.transform.rotozoom(self.bird, -angle*10, 1)
        self.screen.blit(rotating_bird, self.bird_rectangle)

class Pipes:
    def __init__(self, screen):
        self.screen = screen
        self.random_number = randint(0,1)
        self.pipes_list = []
        self.pipe_heights =  [350, 300, 250, 200, 150]
 
        if (pygame.display.Info().current_w > 1280) and (pygame.display.Info().current_h > 720):
            if (self.random_number == 0):
                self.pipe_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'pipe-green.png')).convert_alpha()
                self.flipped_pipe_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'pipe-green-revert.png')).convert_alpha()
            else:
                self.floor_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'pipe-red.png')).convert_alpha()
                self.flipped_pipe_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'pipe-red-revert.png')).convert_alpha()

            self.pipe_image = pygame.transform.scale2x(self.pipe_image)
            self.flipped_pipe_image = pygame.transform.scale2x(self.flipped_pipe_image)

        else:
            if (self.random_number == 0):
                self.pipe_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'pipe-green.png')).convert_alpha()
                self.flipped_pipe_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'pipe-green-revert.png')).convert_alpha()

            else:
                self.pipe_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'pipe-red.png')).convert_alpha()
                self.flipped_pipe_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'pipe-red-revert.png')).convert_alpha()
            
    def create_pipe(self):
        y_position = choice(self.pipe_heights)
        bottom_pipe = self.pipe_image.get_rect(midtop=(400, y_position))
        top_pipe = self.pipe_image.get_rect(midbottom=(400, y_position -100))

        return bottom_pipe, top_pipe

    def draw_pipe(self):
        for current_pipe in self.pipes_list:
            if current_pipe.bottom > 460:
                self.screen.blit(self.pipe_image, current_pipe)
            else:
                self.screen.blit(self.flipped_pipe_image, current_pipe)
                
    def move_pipe(self):
        for current_pipe in self.pipes_list:
            current_pipe.centerx -= 1

    def remove_useless_pipe(self, score):
        for current_pipe in self.pipes_list:
            if current_pipe.centerx < -20:
                score += 1
                self.pipes_list.remove(current_pipe)
        return score
   
class Floor:

    def __init__(self, screen):
        self.screen = screen

        if (pygame.display.Info().current_w > 1280) and (pygame.display.Info().current_h > 720):
            self.floor_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'floor.png')).convert_alpha()
            self.floor_image = pygame.transform.scale2x(self.floor_image)
            self.floor_y = 800
        else:
            self.floor_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'floor.png')).convert_alpha()
            self.floor_y = 400
    
    def moving_floor(self, moving_x):
        self.screen.blit(self.floor_image, (moving_x, self.floor_y))
        self.screen.blit(self.floor_image, (moving_x + 336, self.floor_y))

class Game:
    def __init__(self):
        pygame.init()
        _, _, _, self.hour, _ = map(int, time.strftime("%Y %m %d %H %M").split())
        self.displacement = 0
        self.moving_x = 0
        self.game_activity = False
        self.initiated_game = True
        self.game_over_screen = False
        self.bird_crash_sound_channel = pygame.mixer.Channel(0)
        self.bird_wings_sound_channel = pygame.mixer.Channel(1)
        self.swoosh_sound_channel = pygame.mixer.Channel(2)
        game_icon = pygame.image.load(os.path.join(base_directory, "resources", "images", "icon.png"))
        pygame.display.set_icon(game_icon)
        pygame.display.set_caption('Flappy Bird   ---dsp')

        if (pygame.display.Info().current_w > 1280) and (pygame.display.Info().current_h > 720):
            self.down_fall = 0.07
            self.game_screen = pygame.display.set_mode((576, 1024))
            if (6<self.hour<19):
                self.background_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'background-day.png')).convert_alpha()
            else:
                self.background_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'background-night.png')).convert_alpha()

            self.background_image = pygame.transform.scale2x(self.background_image)
        
        else:
            self.game_screen = pygame.display.set_mode((288,512))
            self.down_fall = 0.07
            self.game_over = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'gameover.png')).convert_alpha()
            self.message = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'message.png')).convert_alpha()

            if (6<self.hour<19):
                self.background_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'background-day.png')).convert_alpha()
            else:
                self.background_image = pygame.image.load(os.path.join(base_directory, 'resources', 'images', 'background-night.png')).convert_alpha()
        
        self.bird = Bird(self.game_screen)
        self.pipe = Pipes(self.game_screen)
        self.floor = Floor(self.game_screen)
        self.scoreboard = Score(self.game_screen)
    
    def wings_sound_play(self):
        wings_sound = pygame.mixer.Sound(os.path.join(base_directory, 'resources', 'audio' ,'wing.wav'))
        self.bird_wings_sound_channel.set_volume(0.25)
        self.bird_wings_sound_channel.play(wings_sound)

    def swoosh_sound_play(self):
        swoosh_sound = pygame.mixer.Sound(os.path.join(base_directory, 'resources', 'audio' ,'swoosh.wav'))
        self.swoosh_sound_channel.set_volume(0.25)
        self.swoosh_sound_channel.play(swoosh_sound)

    def hit_sound_play(self):
        hit_sound = pygame.mixer.Sound(os.path.join(base_directory, 'resources', 'audio' ,'hit.wav'))
        self.bird_crash_sound_channel.set_volume(0.25)
        self.bird_crash_sound_channel.play(hit_sound)

    def collision_detector(self): 
        for current_pipe in self.pipe.pipes_list:
            if current_pipe.colliderect(self.bird.bird_rectangle):
                self.hit_sound_play()
                raise "Bird collided with the pipe"

            if current_pipe.midtop[1] < 0:
                if self.bird.bird_rectangle.bottom < current_pipe.midtop[1]:
                    self.hit_sound_play()
                    raise "Bird escaped the game space"
        
        if self.bird.bird_rectangle.bottomright[1] >= 400:
            self.hit_sound_play()
            raise "Bird collided with the floor"

    def start_game(self):
        SPAWN_NEW_PIPE = pygame.USEREVENT
        pygame.time.set_timer(SPAWN_NEW_PIPE, 1500)

        while True:

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    exit()

                if (event.type == SPAWN_NEW_PIPE) and self.game_activity:
                    self.pipe.pipes_list.extend(self.pipe.create_pipe())
            
                if event.type == pygame.KEYDOWN :
                    if ((event.key == pygame.K_q) or (event.key == pygame.K_ESCAPE)) and not self.game_activity:
                        pygame.quit()
                        exit()

                    if (event.key == pygame.K_SPACE) and self.game_activity:
                        self.wings_sound_play()
                        self.displacement = 0
                        self.displacement = -1

                    if (event.key == pygame.K_RETURN) and not self.game_activity and self.initiated_game:
                        self.swoosh_sound_play()
                        self.initiated_game = False
                        self.game_activity = True

                    if (event.key == pygame.K_RETURN) and self.game_over_screen:
                        self.swoosh_sound_play()
                        self.game_over_screen = False
                        self.initiated_game = True

            try:
                if self.initiated_game and not self.game_over_screen:
                    self.game_screen.blit(self.background_image, (0,0))
                    message_rect = self.message.get_rect(center=(144,256))
                    self.game_screen.blit(self.message, message_rect)


                if self.game_activity and not self.initiated_game and not self.game_over_screen:

                    self.displacement += self.down_fall
                    self.bird.bird_rectangle.centery += self.displacement
                    self.game_screen.blit(self.background_image, (0, 0))
                    
                    self.bird.swinging_bird()
                    self.bird.rotating_and_drawing_bird(self.displacement)
                    self.pipe.move_pipe()
                    self.pipe.draw_pipe()
                    self.floor.moving_floor(self.moving_x)

                    if self.moving_x < -336:
                        self.moving_x = 0
                    
                    self.moving_x -= 1
                    self.collision_detector()
                    self.scoreboard.score = self.pipe.remove_useless_pipe(self.scoreboard.score)
                    self.scoreboard.draw_score()
                    self.scoreboard.high_score_reader()

            except:
                self.game_over_screen = True
                self.game_activity = False
                self.initiated_game = False
                self.pipe.pipes_list.clear()
                self.bird.bird_rectangle.centery = 50
                self.scoreboard.score = 0
                self.displacement = 0
                self.scoreboard.previous_score = 0
                self.game_screen.blit(self.background_image, (0,0))
                self.game_screen.blit(self.game_over, (48,100))
                self.scoreboard.draw_high_score()

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.start_game()