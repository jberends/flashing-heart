is_running = 0

def on_button_pressed_a():
    if not (is_running):
        plane_fly_left()
input.on_button_pressed(Button.A, on_button_pressed_a)

def plane_fly_left():
    global is_running
    is_running = 1
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . #
        . . . . .
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . # #
        . . . . #
        . . . # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . # # #
        . . . # .
        . . # . .
        """)
    basic.show_leds("""
        . . . . #
        . . . # #
        . # # # #
        . . # . .
        . # . . .
        """)
    basic.show_leds("""
        . . . # .
        . . # # .
        # # # # .
        . # . . .
        # . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # # . .
        # # # . .
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # . . .
        # # . . .
        # # . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # . . . .
        # . . . .
        # . . . .
        . . . . .
        # . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    is_running = 0

def on_button_pressed_b():
    if not (is_running):
        plane_fly_right()
input.on_button_pressed(Button.B, on_button_pressed_b)

def plane_fly_right():
    global is_running
    is_running = 1
    basic.show_leds("""
        # . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # . . .
        # . . . .
        # # . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # . .
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . # .
        # . # . .
        # # # # .
        . # . . .
        # . . . .
        """)
    basic.show_leds("""
        . . . . #
        . # . # .
        . # # # #
        . . # . .
        . # . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # . #
        . . # # #
        . . . # .
        . . # . .
        """)
    basic.show_leds("""
        . . . . .
        . . . # .
        . . . # #
        . . . . #
        . . . # .
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . #
        . . . . .
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    is_running = 0