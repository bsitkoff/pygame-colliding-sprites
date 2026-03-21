import pgzrun

WIDTH = 800
HEIGHT = 600

player = Actor('happy')
player.pos = (WIDTH // 2, HEIGHT // 2)

alien = Actor('alien')
alien.pos = (200, 150)

def update():
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # Alien chases the player
    if alien.x < player.x:
        alien.x += 1
    elif alien.x > player.x:
        alien.x -= 1

    if alien.y < player.y:
        alien.y += 1
    elif alien.y > player.y:
        alien.y -= 1

    if player.colliderect(alien):
        print("Hit!")
        exit()

def draw():
    screen.fill((0, 0, 0))
    player.draw()
    alien.draw()

pgzrun.go()
