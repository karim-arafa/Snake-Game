import random
import curses
from curses import textpad 
#screen configuration
stdscr = curses.initscr()
curses.curs_set(0)
screen_height,screen_width = stdscr.getmaxyx()
window= curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1)
window.timeout(100)

#snake configurations

snake_x = screen_width//4
snake_y = screen_height//2

snake = [
    [snake_y,snake_x],
    [snake_y,snake_x-1],
    [snake_y,snake_x-2]
]

#food configuraton
food = [screen_height//2,screen_width//2]
window.addch(food[0],food[1],curses.ACS_PI)
key = curses.KEY_RIGHT
#game logic
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0,screen_height] or snake[0][1] in [0,screen_width] or snake[0] in snake[1: ]:
        curses.endwin()
        quit()
    new_head = [snake[0][0],snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake.insert(0,new_head)
    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1,screen_height-1),
                random.randint(1,screen_width-1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)






