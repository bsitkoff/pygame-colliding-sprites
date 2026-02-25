import pgzrun
import random

WIDTH = 800
HEIGHT = 600

player = Actor('happy')
player.pos = (WIDTH // 2, HEIGHT // 2)

alien = Actor('alien')
alien.pos = (100, 100)

def update():
    if keyboard.left:
        player.x -= 4
    if keyboard.right:
        player.x += 4
    if keyboard.up:
        player.y -= 4
    if keyboard.down:
        player.y += 4

    # Keep player on screen
    player.x = max(0, min(WIDTH, player.x))
    player.y = max(0, min(HEIGHT, player.y))

    # TODO: make alien chase the player

    # TODO: check if player collides with alien (player.colliderect(alien))

def draw():
    screen.fill((0, 0, 0))
    player.draw()
    alien.draw()

pgzrun.go()
