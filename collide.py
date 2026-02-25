import pgzrun
import random

WIDTH = 800
HEIGHT = 600

player = Actor('happy')
player.pos = (WIDTH // 2, HEIGHT // 2)

alien = Actor('alien')
alien.pos = (100, 100)

cookie = Actor('cookie')
cookie.pos = (300, 300)


def update():
    # Player movement
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # Wrap around screen
    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y > HEIGHT:
        player.y = 0
    if player.y < 0:
        player.y = HEIGHT

    # Alien slowly chases player
    if player.x > alien.x:
        alien.x += 1
    elif player.x < alien.x:
        alien.x -= 1
    if player.y > alien.y:
        alien.y += 1
    elif player.y < alien.y:
        alien.y -= 1

    # Check collision with cookie — colliderect() returns True if they overlap
    if player.colliderect(cookie):
        print("Got it!")
        cookie.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    # Check collision with alien
    if player.colliderect(alien):
        print("Caught!")
        exit()


def draw():
    screen.fill((0, 0, 0))
    player.draw()
    alien.draw()
    cookie.draw()


pgzrun.go()
