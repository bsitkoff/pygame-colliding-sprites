## Change It

### 📹 **Watch:** Making a Sprite Chase — How it works

<iframe width="720" height="600"
  src="https://app.screencastify.com/watch/SQfsCE4x3IiG7AsAvQuC/embed"
  title="Codio - Colliding Sprites-1 - Screencastify - March 21, 2026 3:17 PM"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
  
---

### 📹 **Watch:** Making a Sprite Chase — but with more math *(optional)*

<iframe width="720" height="600"
  src="https://app.screencastify.com/watch/oe6W3v40edFPb9Dgltar/embed"
  title="Codio - Colliding Sprites-1 - Screencastify - March 21, 2026 3:23 PM"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
  

## 1: Make the Collision Actually Do Something

Right now a collision prints `"Hit!"` and exits. That's not very exciting. Change the `if player.colliderect(alien):` block to do something else — try moving the alien to a random position instead.

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
{Check It!|assessment}(free-text-auto-616170812)

