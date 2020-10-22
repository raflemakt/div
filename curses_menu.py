import curses
from curses import textpad

"""
This file is an example of how to make a menu with python/curses.
The list of items (menu_items) are printed to the screen and you
choose between them with the arrow keys.
Pressing ENTER executes the code block for the current choise.
"""

menu_items = ["Item1", "Item2", "ItemN", "I use arch btw", "Exit"]


def print_menu(stdscr, selected_row_idx):
    stdscr.erase()  #use erase() instead of clear() for less flicker
    h, w = stdscr.getmaxyx()    #gets terminal window dimensions

    #an example of using textpad for making a rectangle
    textpad.rectangle(stdscr, 2, 3, h-2, w-3)

    #draws the menu
    for idx, row in enumerate(menu_items):
        x = w//2 - len(row)//2
        y = h//2 - len(menu_items)//2 + idx
        if idx == selected_row_idx: 
            stdscr.attron(curses.color_pair(1)) #uses the highlight
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))#goes back to default white on black
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def main(stdscr):
    #turns off the terminal cursor
    curses.curs_set(0)

    #initiates a color pair with black letters on white highlight
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0
    print_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()    #waiting for keyboard input

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_items)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            
            #demonstration code:
            stdscr.erase()
            stdscr.addstr(0, 0, "You selected '{}'".format(menu_items[current_row]))
            stdscr.getch()

            #last menu item is in this case exit
            if current_row == len(menu_items)-1:
                break
            #in here you paste your different menu options like this:
            """
            elif current_row_idx == 0:
                function_1()
            elif current_row_idx == 1:
                function_2()
            """
            
        print_menu(stdscr, current_row)


#the wrapper automatically does some things like noecho() and cbreak()
curses.wrapper(main)
