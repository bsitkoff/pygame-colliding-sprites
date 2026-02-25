import pgzrun
import random

WIDTH = 800
HEIGHT = 600

class Player:
    def __init__(self, x, y):
        self.image = "happy"
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40

class Enemy:
    def __init__(self, x, y):
        self.image = "alien"
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40

class Collectible:
    def __init__(self, x, y):
        self.image = "cookie"
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30

player = Player(WIDTH // 2, HEIGHT // 2)
enemy = Enemy(100, 100)
cookie = Collectible(300, 300)

def update():
    # Move enemy toward player
    if player.x > enemy.x:
        enemy.x += 1
    elif player.x < enemy.x:
        enemy.x -= 1
    
    if player.y > enemy.y:
        enemy.y += 1
    elif player.y < enemy.y:
        enemy.y -= 1

def draw():
    screen.clear((0, 0, 0))
    screen.blit(player.image, (player.x, player.y))
    screen.blit(enemy.image, (enemy.x, enemy.y))
    screen.blit(cookie.image, (cookie.x, cookie.y))

def on_key_down(key):
    if key == keys.UP:
        player.y -= 10
    elif key == keys.DOWN:
        player.y += 10
    elif key == keys.LEFT:
        player.x -= 10
    elif key == keys.RIGHT:
        player.x += 10
    
    # Wrap around screen
    if player.x < 0:
        player.x = WIDTH
    elif player.x > WIDTH:
        player.x = 0
    if player.y < 0:
        player.y = HEIGHT
    elif player.y > HEIGHT:
        player.y = 0

pgzrun.go()
