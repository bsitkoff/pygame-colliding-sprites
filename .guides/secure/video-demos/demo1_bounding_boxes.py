import pgzrun

WIDTH = 800
HEIGHT = 600

player = Actor('happy')
player.pos = (WIDTH // 2, HEIGHT // 2)

alien = Actor('alien')
alien.pos = (300, 200)

hit = False

def update():
    global hit
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    hit = player.colliderect(alien)

def draw():
    screen.fill((0, 0, 0))

    player.draw()
    alien.draw()

    # Draw bounding boxes
    if hit:
        color = (255, 0, 0)       # Red when overlapping
        label = "colliderect() = True"
    else:
        color = (0, 255, 0)       # Green when apart
        label = "colliderect() = False"

    screen.draw.rect(Rect(player.topleft, (player.width, player.height)), color)
    screen.draw.rect(Rect(alien.topleft, (alien.width, alien.height)), color)

    # Show status
    screen.draw.text(label, center=(WIDTH // 2, 30), fontsize=36, color=color)

pgzrun.go()
