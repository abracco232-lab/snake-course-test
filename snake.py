"""
Classic Snake Game in Python
-----------------------------
Built with Python's standard 'turtle' module.
No third-party packages required — runs out of the box!
"""

import random
import time
import turtle

# ==============================================================================
# GAME CONFIGURATION (Feel free to customize!)
# ==============================================================================
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Speed settings (Lower delay = faster snake)
# 0.14 is relaxed and beginner-friendly ("Easy")
INITIAL_DELAY = 0.14
MIN_DELAY = 0.06           # Maximum speed cap
SPEED_RAMP = 0.0015        # How much delay decreases per food eaten

# Color Palette (Modern Dark Theme)
COLOR_BG = "#1e1e2e"       # Deep slate navy background
COLOR_BORDER = "#475569"   # Slate gray playing field border
COLOR_HEAD = "#4ade80"     # Bright neon green head
COLOR_BODY = "#22c55e"     # Lush green body
COLOR_FOOD = "#f87171"     # Vibrant apple red
COLOR_TEXT = "#f8fafc"     # Crisp white score text
COLOR_OVER = "#ef4444"     # Red game-over text

# Play Area Boundaries (Grid coordinates)
# The playable area sits inside a 560x500 box
GRID_MIN_X = -13  # -260px
GRID_MAX_X = 13   #  260px
GRID_MIN_Y = -13  # -260px
GRID_MAX_Y = 11   #  220px
# ==============================================================================

# Game State
score = 0
high_score = 0
delay = INITIAL_DELAY
is_paused = False
next_direction = "stop"


# ------------------------------------------------------------------------------
# Screen & Window Setup
# ------------------------------------------------------------------------------
window = turtle.Screen()
window.title("Classic Snake Game")
window.bgcolor(COLOR_BG)
window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.tracer(0)  # Disable auto-refresh for smooth, flicker-free rendering


# ------------------------------------------------------------------------------
# Draw Play Area Border
# ------------------------------------------------------------------------------
def draw_border():
    border = turtle.Turtle()
    border.speed(0)
    border.color(COLOR_BORDER)
    border.pensize(3)
    border.penup()
    border.hideturtle()

    # Draw rectangular perimeter around the playable grid
    top_y = GRID_MAX_Y * 20 + 15
    bottom_y = GRID_MIN_Y * 20 - 15
    left_x = GRID_MIN_X * 20 - 15
    right_x = GRID_MAX_X * 20 + 15

    border.goto(left_x, top_y)
    border.pendown()
    border.goto(right_x, top_y)
    border.goto(right_x, bottom_y)
    border.goto(left_x, bottom_y)
    border.goto(left_x, top_y)


draw_border()


# ------------------------------------------------------------------------------
# Game Objects: Head, Food, Segments, Pen
# ------------------------------------------------------------------------------
# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color(COLOR_HEAD)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(COLOR_FOOD)
food.penup()
food.goto(0, 80)

# Body segments list
segments = []

# Scoreboard Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color(COLOR_TEXT)
pen.penup()
pen.hideturtle()
pen.goto(0, 255)


def update_scoreboard():
    """Redraws the score and high-score header."""
    pen.clear()
    pen.write(
        f"Score: {score}   |   High Score: {high_score}",
        align="center",
        font=("Arial", 16, "bold"),
    )


# ------------------------------------------------------------------------------
# Movement & Controls
# ------------------------------------------------------------------------------
def go_up():
    global next_direction
    if head.direction != "down" and next_direction != "down" and not is_paused:
        next_direction = "up"


def go_down():
    global next_direction
    if head.direction != "up" and next_direction != "up" and not is_paused:
        next_direction = "down"


def go_left():
    global next_direction
    if head.direction != "right" and next_direction != "right" and not is_paused:
        next_direction = "left"


def go_right():
    global next_direction
    if head.direction != "left" and next_direction != "left" and not is_paused:
        next_direction = "right"


def toggle_pause():
    """Pauses or resumes the game."""
    global is_paused
    if head.direction == "stop":
        return  # Don't pause before game starts

    is_paused = not is_paused
    if is_paused:
        pen.goto(0, 0)
        pen.color(COLOR_TEXT)
        pen.write("PAUSED (Press Space)", align="center", font=("Arial", 22, "bold"))
        pen.goto(0, 255)
    else:
        update_scoreboard()


def move():
    """Moves the snake head one step in the active direction."""
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)


def reposition_food():
    """Places food at a random grid point not occupied by the snake."""
    while True:
        rand_x = random.randint(GRID_MIN_X, GRID_MAX_X) * 20
        rand_y = random.randint(GRID_MIN_Y, GRID_MAX_Y) * 20

        # Verify new spot doesn't clash with snake head or any segment
        clash = (head.xcor() == rand_x and head.ycor() == rand_y) or any(
            seg.xcor() == rand_x and seg.ycor() == rand_y for seg in segments
        )
        if not clash:
            food.goto(rand_x, rand_y)
            break


def trigger_game_over():
    """Displays game over animation and resets the board."""
    global score, delay, next_direction

    # Show Game Over Banner
    pen.goto(0, 0)
    pen.color(COLOR_OVER)
    pen.write("GAME OVER!", align="center", font=("Arial", 26, "bold"))
    window.update()
    time.sleep(0.9)

    # Clean up segments
    for segment in segments:
        segment.goto(2000, 2000)
    segments.clear()

    # Reset position and state
    head.goto(0, 0)
    head.direction = "stop"
    next_direction = "stop"
    score = 0
    delay = INITIAL_DELAY

    # Restore pen & scoreboard
    pen.color(COLOR_TEXT)
    pen.goto(0, 255)
    update_scoreboard()


# ------------------------------------------------------------------------------
# Key Bindings
# ------------------------------------------------------------------------------
window.listen()

# Arrow keys
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# WASD keys (lowercase and uppercase for CapsLock tolerance)
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(go_up, "W")
window.onkeypress(go_down, "S")
window.onkeypress(go_left, "A")
window.onkeypress(go_right, "D")

# Spacebar for Pause
window.onkeypress(toggle_pause, "space")


# ------------------------------------------------------------------------------
# Main Game Loop
# ------------------------------------------------------------------------------
def main():
    global score, high_score, delay, next_direction

    update_scoreboard()

    # Display introductory start hint
    pen.goto(0, -30)
    pen.write("Use Arrow Keys or WASD to start", align="center", font=("Arial", 12, "italic"))
    pen.goto(0, 255)

    try:
        while True:
            window.update()

            if is_paused:
                time.sleep(0.05)
                continue

            # Clear start hint once movement begins
            if head.direction == "stop" and next_direction != "stop":
                head.direction = next_direction
                update_scoreboard()
            elif head.direction != "stop":
                head.direction = next_direction

            # Only process gameplay if snake is moving
            if head.direction != "stop":
                # 1. Check Wall Collisions
                limit_x = GRID_MAX_X * 20
                limit_y_top = GRID_MAX_Y * 20
                limit_y_bottom = GRID_MIN_Y * 20

                if (
                    head.xcor() > limit_x
                    or head.xcor() < -limit_x
                    or head.ycor() > limit_y_top
                    or head.ycor() < limit_y_bottom
                ):
                    trigger_game_over()
                    continue

                # 2. Check Food Collision
                if head.distance(food) < 18:
                    reposition_food()

                    # Create & attach new body segment
                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape("square")
                    new_segment.color(COLOR_BODY)
                    new_segment.penup()
                    segments.append(new_segment)

                    # Update scores
                    score += 10
                    if score > high_score:
                        high_score = score
                    update_scoreboard()

                    # Gentle speed increment
                    delay = max(MIN_DELAY, delay - SPEED_RAMP)

                # 3. Move trailing body segments in reverse order
                for i in range(len(segments) - 1, 0, -1):
                    x = segments[i - 1].xcor()
                    y = segments[i - 1].ycor()
                    segments[i].goto(x, y)

                # Move segment 0 to old head location
                if len(segments) > 0:
                    segments[0].goto(head.xcor(), head.ycor())

                # 4. Move head forward
                move()

                # 5. Check Self-Collision
                collision = False
                for segment in segments:
                    if segment.distance(head) < 12:
                        collision = True
                        break

                if collision:
                    trigger_game_over()
                    continue

            time.sleep(delay)

    except (turtle.Terminator, turtle.TK.TclError):
        # Gracefully handle window close without error tracebacks
        pass


if __name__ == "__main__":
    main()
