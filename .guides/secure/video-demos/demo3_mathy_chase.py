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

    # Math-y chase: direction from difference
    if player.x != alien.x:
        alien.x += (player.x - alien.x) / abs(player.x - alien.x)
    if player.y != alien.y:
        alien.y += (player.y - alien.y) / abs(player.y - alien.y)

    if player.colliderect(alien):
        print("Hit!")
        exit()

def draw():
    screen.fill((0, 0, 0))
    player.draw()
    alien.draw()

pgzrun.go()
