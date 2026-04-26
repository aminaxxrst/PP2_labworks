import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 800))
WHITE = (255, 255, 255)
CLOCK_CENTER = (400, 400)

bg = pygame.image.load('images/clock.png')
body = pygame.image.load('images/mickey_body.png')
hand_s_img = pygame.image.load('images/hand_second.png')
hand_m_img = pygame.image.load('images/hand_minute.png')

bg = pygame.transform.scale(bg, (700, 700)) 
body = pygame.transform.scale(body, (300, 300))

def make_hand_surface(image, width, height):
    temp_surface = pygame.Surface((width, height*2), pygame.SRCALPHA) 
    resized_hand = pygame.transform.scale(image, (width, height)) 
    temp_surface.blit(resized_hand, (0, 0))
    return temp_surface

hand_s_base = make_hand_surface(hand_s_img, 70, 220)
hand_m_base = make_hand_surface(hand_m_img, 85, 190)

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    s = now.second
    m = now.minute

    s_angle = -(s * 6)
    m_angle = -(m * 6 + s * 0.1)

    rot_s = pygame.transform.rotate(hand_s_base, s_angle)
    rot_m = pygame.transform.rotate(hand_m_base, m_angle)

    rect_s = rot_s.get_rect(center=CLOCK_CENTER)
    rect_m = rot_m.get_rect(center=CLOCK_CENTER)

    screen.fill(WHITE)
    
    screen.blit(bg, bg.get_rect(center=CLOCK_CENTER))
    screen.blit(body, body.get_rect(center=CLOCK_CENTER))
    
    screen.blit(rot_s, rect_s)
    screen.blit(rot_m, rect_m)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()