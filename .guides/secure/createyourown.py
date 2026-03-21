import pgzrun
import random

WIDTH = 800
HEIGHT = 600

score = 0
alien_speed = 1

player = Actor('knight')
player.pos = (WIDTH // 2, HEIGHT // 2)

alien = Actor('dragon')
alien.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

cookie = Actor('gem')
cookie.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))


def update():
    global score, alien_speed

    # Player movement
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # Keep player on screen
    player.x = max(0, min(WIDTH, player.x))
    player.y = max(0, min(HEIGHT, player.y))

    # Alien chases the player
    if player.x > alien.x:
        alien.x += alien_speed
    elif player.x < alien.x:
        alien.x -= alien_speed
    if player.y > alien.y:
        alien.y += alien_speed
    elif player.y < alien.y:
        alien.y -= alien_speed

    # Collision with cookie — move to new random position
    if player.colliderect(cookie):
        score += 1
        cookie.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        alien_speed += 0.5
        print("Score: " + str(score))

    # Collision with alien — game over
    if player.colliderect(alien):
        print("Game Over! Final Score: " + str(score))
        exit()


def draw():
    screen.fill((0, 0, 0))
    player.draw()
    alien.draw()
    cookie.draw()
    screen.draw.text("Score: " + str(score), topleft=(10, 10), fontsize=30)


pgzrun.go()
