## Change It

> 📹 **Watch:** Making a Sprite Chase — Math Lite
> *Record in Screencastify — show the if/elif pattern for moving toward a target*
> *Objective: I can write code that moves one sprite toward another.*
> **[ADD VIDEO URL WHEN RECORDED]**

> 📹 **Watch:** Making a Sprite Chase — Math-y Version *(optional)*
> *Record in Screencastify — same result using subtraction and sign; for students who want the math explanation*
> **[ADD VIDEO URL WHEN RECORDED]**

---

Don't worry — you can't break anything permanently!

## 1: Make the Collision Actually Do Something

Right now a collision prints "Hit!" and exits. That's not very satisfying. Change the `if player.colliderect(alien):` block to do something else — try moving the alien to a random position instead.

```python
import random
# inside the if block:
alien.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
```

## 2: Make the Alien Chase the Player

Add code in `update()` to move the alien toward the player. Use the pattern from the video:

```python
if alien.x < player.x:
    alien.x += 1
elif alien.x > player.x:
    alien.x -= 1
```

Do the same for `y`. Run the game — can you outrun the alien?

## 3: Add a Collectible

Add a `cookie = Actor('cookie')` and make something happen when the player collides with it (move it to a new random spot, for starters).

---

> *[TODO: insert free-text-auto assessment — "What changes did you make? Describe what your game does now."]*
