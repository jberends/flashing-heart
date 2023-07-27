let is_running = 0
input.onButtonPressed(Button.A, function () {
    if (!(is_running)) {
        plane_fly_left()
    }
})
function plane_fly_left () {
    is_running = 1
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . #
        . . . . .
        . . . . #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . # #
        . . . . #
        . . . # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . #
        . . # # #
        . . . # .
        . . # . .
        `)
    basic.showLeds(`
        . . . . #
        . . . # #
        . # # # #
        . . # . .
        . # . . .
        `)
    basic.showLeds(`
        . . . # .
        . . # # .
        # # # # .
        . # . . .
        # . . . .
        `)
    basic.showLeds(`
        . . # . .
        . # # . .
        # # # . .
        # . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # . . .
        # # . . .
        # # . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # . . . .
        # . . . .
        # . . . .
        . . . . .
        # . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    is_running = 0
}
input.onButtonPressed(Button.B, function () {
    if (!(is_running)) {
        plane_fly_right()
    }
})
function plane_fly_right () {
    is_running = 1
    basic.showLeds(`
        # . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # . . .
        # . . . .
        # # . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . # . .
        . # . . .
        # # # . .
        # . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . # .
        # . # . .
        # # # # .
        . # . . .
        # . . . .
        `)
    basic.showLeds(`
        . . . . #
        . # . # .
        . # # # #
        . . # . .
        . # . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # . #
        . . # # #
        . . . # .
        . . # . .
        `)
    basic.showLeds(`
        . . . . .
        . . . # .
        . . . # #
        . . . . #
        . . . # .
        `)
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . . #
        . . . . .
        . . . . #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    is_running = 0
}
