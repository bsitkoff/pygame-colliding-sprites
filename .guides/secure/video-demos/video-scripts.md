# Video Scripts — Colliding Sprites

---

## Video 1: How colliderect() Works

**Page:** Try It Out
**Length:** ~3 minutes
**Objective:** I can use colliderect() to detect when two sprites touch.

### Script

**[Screen: Open `video-demos/demo1_bounding_boxes.py` and run it.]**

Hey everyone — so today we're going to learn how to make sprites react when they touch each other. The tool we'll use is called `colliderect()`.

So we've got two sprites here — a player and an alien. They each have a position on the screen, and Pygame Zero draws an invisible rectangle around each one. That rectangle is called a **bounding box** — it's basically a box that tightly fits around the image.

**[Move the player around, staying away from the alien. Point out the green boxes and "colliderect() = False" text at the top.]**

See the green rectangles? Those are the bounding boxes. Right now they're not overlapping, so `colliderect()` returns `False`. Nothing happens.

**[Move the player so the boxes just barely overlap. They turn red and the text changes to "colliderect() = True".]**

But the moment any part of these rectangles overlaps — even just a tiny corner — boom, red. `colliderect()` returns `True`. That's it. It's checking: "Do these two boxes overlap right now?"

**[Stop the game. Open `collide.py` and highlight the if statement:]**
```python
if player.colliderect(alien):
    print("Hit!")
    exit()
```

So in the real code, every single frame — 60 times a second — we're asking: "Is the player's box overlapping the alien's box?" If yes, we print "Hit!" and the game exits.

**[Run `collide.py`. Move the player around, then deliberately collide with the alien.]**

Watch — I'll move into the alien... and there it is. "Hit!" in the terminal, game over.

**[Point to terminal output]**

Notice it doesn't matter WHERE they touch — top, side, corner — any overlap counts. That's because `colliderect()` is just checking rectangles, not the actual pixel shapes. For most games, that's close enough.

**[Back to code]**

The pattern is always the same: `sprite1.colliderect(sprite2)`. You put it in an `if` statement, and then you decide what happens — print a message, move a sprite, end the game, whatever you want.

OK, your turn — run the code and see it for yourself. Then we'll start changing what happens on collision.

---

## Video 2: Making a Sprite Chase — Math Lite

**Page:** Change It
**Length:** ~3 minutes
**Objective:** I can write code that moves one sprite toward another.

### Script

**[Screen: Open `video-demos/demo2_no_chase.py`. Run it — move around, show the alien just sitting there.]**

So right now the alien just sits there. Not much of a challenge. Let's make it chase the player.

**[Stop the game. Scroll to the comment in `update()` that says "Add chase code during recording".]**

The idea is simple. Every frame, we ask: "Is the alien to the LEFT of the player? Then move it right a little. Is the alien to the RIGHT? Move it left." Same thing for up and down.

**[Switch to `video-demos/demo2_with_chase.py`. Highlight the chase code:]**
```python
if alien.x < player.x:
    alien.x += 1
elif alien.x > player.x:
    alien.x -= 1
```

Here's what that looks like. Let's read it out loud. If the alien's x is less than the player's x — meaning the alien is further left — we add 1 to the alien's x. That nudges it to the right, toward the player. If the alien is further right, we subtract 1. Nudge it left.

**[Highlight the y block:]**
```python
if alien.y < player.y:
    alien.y += 1
elif alien.y > player.y:
    alien.y -= 1
```

Same thing for y. If the alien is above the player, move it down. If it's below, move it up.

**[Run `demo2_with_chase.py`]**

And look — the alien is creeping toward us. It's slow because we're only moving 1 pixel per frame, but it never stops.

**[Move player around, show alien following]**

See how it follows? It's not very smart — it just moves in a straight-ish line toward wherever you are right now. But it works, and it makes the game way more interesting.

**[Collide with alien on purpose]**

And when it catches you — boom, collision detected, game over.

The number you use — that `1` — is the speed. Want a faster alien? Change it to `2` or `3`. Want it really terrifying? Try `4`. You'll experiment with that in a minute.

---

## Video 3: Making a Sprite Chase — Math-y Version (Optional)

**Page:** Change It
**Length:** ~2 minutes
**Objective:** Understand the math behind sprite chasing (for curious students).

### Script

**[Screen: Open `video-demos/demo3_mathy_chase.py`. Don't run it yet.]**

OK so this one's optional — if you're curious about WHY the if/elif pattern works, or you just like math, this is for you. If not, totally fine to skip.

**[Scroll to the chase code in demo3]**

So in the last video we wrote that pattern with `if` and `elif` — check if alien is left of player, move right, and vice versa. This file does the same thing, but in a completely different way. Look at this:

```python
if player.x != alien.x:
    alien.x += (player.x - alien.x) / abs(player.x - alien.x)
```

Whoa — that looks scary. Let's break it down.

**[Highlight `player.x - alien.x`]**

`player.x - alien.x` — that's the distance between them on the x axis. If the player is to the RIGHT, this number is positive. If the player is to the LEFT, it's negative.

We divide by the absolute value — that just gives us +1 or -1. Positive means "move right," negative means "move left." That's the same thing our if/elif was doing, just in one line.

**[Run it — show that it behaves identically to demo2_with_chase.py]**

See? Same behavior. The alien chases, you get caught, game over.

**[Stop the game]**

Honestly? The if/elif version is easier to read and does the same thing. I'm showing you this because in more advanced game programming, you'll see this kind of math a lot — calculating direction from a difference. It's the same idea behind homing missiles, AI pathfinding, all sorts of stuff.

For now, use whichever version makes sense to you. They both work.
