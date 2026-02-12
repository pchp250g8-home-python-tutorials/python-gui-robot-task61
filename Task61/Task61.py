from robot import *

while is_free_right() and is_wall_up():
    move_right()
while is_free_down():
    move_down()
while is_free_right() and is_wall_down():
    move_right()
while is_free_up() and is_wall_right():
    move_up()
while is_free_right() and is_wall_up():
    move_right()