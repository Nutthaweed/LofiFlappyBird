import random
import pygame

def base_movement(screen, base_img, var_x):
    screen.blit(base_img, (var_x, 720 - 12))
    screen.blit(base_img, (var_x+720, 720 - 12))


def bird_movement(screen, bird_img, bird_rect):
    screen.blit(bird_img, bird_rect)

def pipe_movement(screen, pipes, pipe_img):
    
    for pipe in pipes:
        pipe.centerx -= 7

    for pipe in pipes:
        screen.blit(pipe_img, pipe)

def collision(pipes, bird_rect):
    for pipe in pipes:
        if pipe.colliderect( bird_rect):
            print("collided")
    if bird_rect.top <= -10:
        print("exceed upper limit")
    if bird_rect.bottom >= 512-75:
        print("exceed lower limit")

def game_build():
  pygame.init()
  screen =pygame.display.set_mode((1280, 720))


  pygame.mixer.init()
  pygame.mixer.music.load("resources\\music.mp3")
  pygame.mixer.music.set_volume(0.5)
  pygame.mixer.music.play()
    

  bkg_img = pygame.image.load("resources\\maxresdefault.jpg")

  base_img = pygame.image.load("resources\\base.png")
  var_x =  0

  bird_img = pygame.image.load("resources\\flappybird.png")
  bird_rect = bird_img.get_rect(center = (75, 500/2))
  g_force= 2
  bird_new_position = 0

  pipe_img = pygame.image.load("resources\\pipe.png")
  list_of_pipe = []

  TIMER = pygame.USEREVENT
  pygame.time.set_timer(TIMER, 1200)

  clock = pygame.time.Clock()
  running = True
  while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird_new_position = 0
                bird_new_position -= 8

        if event.type == TIMER:
            random_pipe_height = [ 400, 500,600]
            pipes = pipe_img.get_rect(midtop = (500/2, random.choice(random_pipe_height)))
            list_of_pipe.append(pipes)
    
    screen.blit(bkg_img, (0,0))

    collision(list_of_pipe, bird_rect)

    pipe_movement(screen, list_of_pipe, pipe_img)

    var_x = -1
    base_movement(screen, base_img, var_x)
    if var_x <= -500:
        var_x = 0
    
    bird_new_position += g_force
    bird_rect.centery = bird_new_position
    bird_movement(screen, bird_img, bird_rect)


    clock.tick(60)
    pygame.display.update()

  pygame.quit()


if __name__ == "__main__":
    game_build()