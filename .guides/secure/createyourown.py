import pgzrun
import random

WIDTH = 800
HEIGHT = 600

score = 0
predator_speed = 1

# Ecosystem: ocean — fish avoids shark, collects plankton
fish = Actor('fish')
fish.pos = (WIDTH // 2, HEIGHT // 2)

shark = Actor('shark')
shark.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

plankton = Actor('plankton')
plankton.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))


def update():
    global score, predator_speed

    # Creature movement
    if keyboard.left:
        fish.x -= 5
    if keyboard.right:
        fish.x += 5
    if keyboard.up:
        fish.y -= 5
    if keyboard.down:
        fish.y += 5

    # Keep creature on screen
    fish.x = max(0, min(WIDTH, fish.x))
    fish.y = max(0, min(HEIGHT, fish.y))

    # Predator chases the creature
    if fish.x > shark.x:
        shark.x += predator_speed
    elif fish.x < shark.x:
        shark.x -= predator_speed
    if fish.y > shark.y:
        shark.y += predator_speed
    elif fish.y < shark.y:
        shark.y -= predator_speed

    # Collision with resource — move to new random position
    if fish.colliderect(plankton):
        score += 1
        plankton.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        predator_speed += 0.5
        print("Score: " + str(score))

    # Collision with predator — game over
    if fish.colliderect(shark):
        print("Game Over! Final Score: " + str(score))
        exit()


def draw():
    screen.fill((0, 0, 0))
    fish.draw()
    shark.draw()
    plankton.draw()
    screen.draw.text("Score: " + str(score), topleft=(10, 10), fontsize=30)


pgzrun.go()
