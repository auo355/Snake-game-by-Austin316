import pygame
import time
import random

#### initialize game #######
block_size = 10
screen_size_x = 80*block_size
screen_size_y = 60*block_size
speed = 5
black = (0,0,0)
white = (255,255,255)
red   = (255, 0, 0)
green = (0,255,0)
blue  = (0, 0, 255)
yellow = (255, 255, 0)
pygame.init()
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
pygame.display.set_caption('snake game by austin 3:16')
game_clock = pygame.time.Clock()
score_increase_per_food = 10
####################################################

def direction_of_snake(previous_direction):
    new_direction = previous_direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if previous_direction == 'down':
                    new_direction = 'down'
                else:
                    new_direction = 'up'
            if event.key == pygame.K_DOWN:
                if previous_direction == 'up':
                    new_direction = 'up'
                else:
                    new_direction = 'down'
            if event.key == pygame.K_LEFT:
                if previous_direction == 'right':
                    new_direction = 'right'
                else:
                    new_direction = 'left'
            if event.key == pygame.K_RIGHT:
                if previous_direction == 'left':
                    new_direction = 'left'
                else:
                    new_direction = 'right'
    return new_direction

def new_position_of_snake(previous_position, direction):
    new_position = previous_position
    if direction == 'up':
        new_position[1] = new_position[1]-block_size
    if direction == 'down':
        new_position[1] = new_position[1]+block_size
    if direction == 'left':
        new_position[0] = new_position[0]-block_size
    if direction == 'right':
        new_position[0] = new_position[0]+block_size
    return new_position

def is_fruit_eating(position_of_snake_head, position_of_fruit):
    if position_of_snake_head[0] == position_of_fruit[0] and position_of_snake_head[1] == position_of_fruit[1]:
        decision = True
    else:
        decision = False
    return decision

def grow_snake(snake_structure, snake_head):
    snake_structure.insert(0,list(snake_head))

def draw_snake_and_fruit(snake_structure, fruit_position):
    screen.fill(blue)
    pygame.draw.circle(screen, white, (snake_structure[0][0]+block_size/2, snake_structure[0][1]+block_size/2),block_size/2, block_size)
    for position in snake_structure[1:]:
        pygame.draw.rect(screen, white, pygame.Rect(position[0], position[1], block_size, block_size ))
    pygame.draw.rect(screen, green, pygame.Rect(fruit_position[0], fruit_position[1], block_size, block_size))

def did_snake_head_touch_border(position):
    if position[0]>=screen_size_x or position[0]<=0 or position[1]>=screen_size_y or position[1]<=0:
        return True
    else:
        return False
    

def did_snake_bite_body(snake_head, snake_body):
    if snake_head in snake_body[1:]:
        return True
    else:
        return False


def display_text_on_screen(caption, colour, position_x, position_y, font, size):
    display_font = pygame.font.SysFont(font, size)
    display_surface = display_font.render(caption,True, colour)
    display_rectangle = display_surface.get_rect()
    ##display_rectangle.midtop(position_x, position_y)
    screen.blit(display_surface, display_rectangle)

def to_continue_game(score):
    screen.fill(blue)
    display_text_on_screen(" GAME OVER. Your score is {}. press Q to quit or P to play a new game".format(score), yellow, screen_size_x/2 , screen_size_x/2, "times new roman", 25)
    pygame.display.update()
    keep_loop = True
    while keep_loop:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    decision = False
                    keep_loop = False
                if event.key == pygame.K_p:
                    decision = True
                    keep_loop = False
    return decision


def snake_game_loop():
    snake_head_position = [screen_size_x/2, screen_size_y/2]
    snake_structure = []
    snake_structure.append(snake_head_position)
    snake_direction = 'up'
    food_position = [block_size*random.randrange(1, screen_size_x/block_size - 1), block_size*random.randrange(1, screen_size_y/block_size - 1) ]

    score = 0
    game_on = True
    while game_on:
        draw_snake_and_fruit(snake_structure, food_position)
        snake_direction = direction_of_snake(snake_direction)
        snake_head_position = new_position_of_snake(snake_head_position, snake_direction)
        grow_snake(snake_structure, snake_head_position)
        
        if snake_head_position == food_position:
            score += score_increase_per_food
            food_position = [block_size*random.randrange(1, screen_size_x/block_size - 1), block_size*random.randrange(1, screen_size_y/block_size - 1) ]
        else:
            del(snake_structure[-1])

        check1 = did_snake_head_touch_border(snake_head_position)
        check2 = did_snake_bite_body(snake_head_position, snake_structure)

        if (check1 == True or check2 == True):
            check3 = to_continue_game(score)
            if check3 == False:
                game_on = False   
            if check3 == True:
                snake_game_loop()
        display_text_on_screen(" your score is {}".format(score), yellow, 0,0, "times new roman", 25)
        pygame.display.update()

        game_clock.tick(speed)




    pygame.quit()
    quit()


snake_game_loop()
    

















