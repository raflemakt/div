# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import curses
import time

"""
US states quiz for learning the states by heart.
Written by Gunnar Myhre, October 2020
Keep an eye out for new quizzes at:
https://github.com/raflemakt/div/blob/master/quiz
"""

us_states = [
["Alabama",         (15,42),    "AL"],
["Alaska",          (1,1),      "\ AK"],
["Arizona",         (14,11),    "Ariz."],
["Arkansas",        (14,34),    "Ark."],
["California",      (11,3),     "Cal"],
["Colorado",        (10,18),    "Colo."],
["Connecticut",     (7, 57),    "Conn"],
["Delaware",        (9, 59),    "(DE)"],
["Florida",         (17,49),    "FL"],
["Georgia",         (15,47),    "GA"],
["Hawaii",          (18,1),     "<---HI"],
["Idaho",           (6,10),     "Ida."],
["Illinois",        (9,38),     "IL"],
["Indiana",         (9,41),     "IN"],
["Iowa",            (8,32),     "Iowa"],
["Kansas",          (11,26),    "Kansas"],
["Kentucky",        (11,43),    "KY"],
["Louisiana",       (17,35),    "LA"],
["Maine",           (3,58),     "ME"],
["Maryland",        (9,56),     "MD"],
["Massachusetts",   (6,60),     "Mass."],
["Michigan",        (4,42),     "Mich."],
["Minnesota",       (4,31),     "Minn"],
["Mississippi",     (15,38),    "MS"],
["Missouri",        (11,34),    "MO"],
["Montana",         (4,15),     "Montana"],
["Nebraska",        (9,26),     "Nebr."],
["Nevada",          (10,7),     "Nev."],
["New Hampshire",   (5,60),     "NH"],
["New Jersey",      (8,56),     "NJ"],
["New Mexico",      (14,17),    "N.Mex"],
["New York",        (5,52),     "NY"],
["North Carolina",  (12,48),    "N Car."],
["North Dakota",    (4,24),     "N Dak"],
["Ohio",            (9,44),     "OH"],
["Oklahoma",        (13,28),    "Okla."],
["Oregon",          (5,3),      "Oregon"],
["Pennsylvania",    (7,49),     "Penn."],
["Rhode Island",    (7,62),     "(RI)"],
["South Carolina",  (14,52),    "S Car."],
["South Dakota",    (6,24),     "S Dak."],
["Tennessee",       (13,40),    "Tenn."],
["Texas",           (17,25),    "Texas"],
["Utah",            (10,12),    "Utah"],
["Vermont",         (3,53),     "VT"],
["Virginia",        (10,51),    "VA"],
["Washington",      (3,5),      "Wash."],
["West Virginia",   (10,47),    "WV"],
["Wisconsin",       (5,36),     "WI"],
["Wyoming",         (7,16),     "Wyoming"]]

stars = [
'* * * * * * * * * * ',
' * * * * * * * * * *',
'* * * * * * * * * * ',
' * * * * * * * * * *',
'* * * * * * * * * * ']

stripes = [
'                                                            ..',
'* * * * * * * * * * $$$$$$$$$$$$$$$$$$$$                 .$$$$.',
' * * * * * * * * * * $$$$$$$$$$$$$$$$$$$$$$$$.          .$$$$$',
'* * * * * * * * * * ::::::::::::::::::::::::::.      .::::::::',
' * * * * * * * * * * $$$$$$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$F',
'* * * * * * * * * * $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$d$$$$$$$"',
'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;',
'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$',
'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$',
':::::::::::::::::::::::::::::::::::::::::::::::::::::::::;',
' ^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"',
'   ^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$',
'     ":::::::::::::::::::::::::::::::::::::::::::::::"',
'       ""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P',
'                   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$L',
' You WON!            ;; ;::::::::::::::::;;    ;;:::.',
'                          $$$$$$"     ""         $$$$$;',
'                           ^$$"                   $$$$',
'                                                    ""']

USA = [
"    ,__                                                  _,",
" \~\|  ~~---___              ,                          | \ ",
"  |      / |   ~~~~~~~|~~~~~| ~~---,                  _/,  >",
" /~-_--__| |          |     \     / ~\~~/          /~| ||,'",
" |       /  \         |------|   {    / /~)     __-  ',|_\,",
"/       |    |~~~~~~~~|      \    \   | | '~\  |_____,|~,-'",
"|~~--__ |    |        |____  |~~~~~|--| |__ /_-'     {,~",
"|   |  ~~~|~~|        |    ~~\     /  `-' |`~ |~_____{/",
"|   |     |  '---------,      \----|   |  |  ,' ~/~\,|`",
"',  \     |    |       |~~~~~~~|    \  | ,'~~\  /    |",
" |   \    |    |       |       |     \_-~    /`~___--\ ",
" ',   \  ,-----|-------+-------'_____/__----~~/      /",
"  '_   '\|     |      |~~~|     |    |      _/-,~~-,/",
"    \    |     |      |   |_    |    /~~|~~\    \,/",
"     ~~~-'     |      |     `~~~\___|   |   |    /",
"         '-,_  | _____|          |  /   | ,-'---~\ ",
"             `~'~  \             |  `--,~~~~-~~,  \ ",
"                    \/~\      /~~~`---`         |  \ ",
"                        \    /                   \  |",
"                         \  |                     '/' ",
"                          `~'"]

eagle = [
"           ___----------___",
"        _--                ----__",
"       -                         ---_",
"      -___    ____---_              --_",
"  __---_ .-_--   _ O _-                -",
" -      -_-       ---                   -",
"-   __---------___                       -",
"- _----                                  -",
" -     -_                                 _",
" `      _-                                 _",
"       _                           _-_  _-_ _",
"      _-                   ____    -_  -   --",
"      -   _-__   _    __---    -------       -",
"     _- _-   -_-- -_--                        _",
"     -_-                                       _",
"    _-                                          _",
"    -"]

def win_graphics(stdscr, y, x, elap):
    """Draws an american flag and elapsed time"""
    stdscr.erase()
    #draw stripes
    for line in range(0, len(stripes)):
        if line in [1,2, 4,5, 7,8, 10,11, 13,14, 16,17]:
            stdscr.addstr(y+line, x, stripes[line], curses.color_pair(4))
        else:
            stdscr.addstr(y+line, x, stripes[line], curses.color_pair(1))
    #draw stars
    for line in range(0, len(stars)):
        stdscr.addstr(y+line+1, x, stars[line], curses.color_pair(3))
    stdscr.addstr(21+y, x, "Time elapsed: {} seconds".format(round(elap, 2)))

    stdscr.refresh()
    stdscr.getch()

def print_big_number(stdscr, number, offsy, offsx):
    """Prints a six lines high ASCII-art number at the position (offsy, offsx)"""
    length = [9, 4, 8, 8, 8, 8, 9, 8, 8, 8]
    num_str = str(number)

    num_gfxlist = [
    " ██████╗  ██╗██████╗ ██████╗ ██╗  ██╗███████╗ ██████╗ ███████╗ █████╗  █████╗ ",
    "██╔═████╗███║╚════██╗╚════██╗██║  ██║██╔════╝██╔════╝ ╚════██║██╔══██╗██╔══██╗",
    "██║██╔██║╚██║ █████╔╝ █████╔╝███████║███████╗███████╗     ██╔╝╚█████╔╝╚██████║",
    "████╔╝██║ ██║██╔═══╝  ╚═══██╗╚════██║╚════██║██╔═══██╗   ██╔╝ ██╔══██╗ ╚═══██║",
    "╚██████╔╝ ██║███████╗██████╔╝     ██║███████║╚██████╔╝   ██║  ╚█████╔╝ █████╔╝",
    " ╚═════╝  ╚═╝╚══════╝╚═════╝      ╚═╝╚══════╝ ╚═════╝    ╚═╝   ╚════╝  ╚════╝ "]

    num_offsx = 0
    while len(num_str) != 0:
        if len(num_str) > 1:
            current_num = int(num_str[:-len(num_str)+1])
        else:
            current_num = int(num_str)
        remain = 0
        before = 0
        if current_num > 0:
            for i in range(0, current_num):
                before = before + length[i]
        for num in range(current_num+1, len(length)):
            remain = remain + length[num]
        for i in range(0, 6):
            short = num_gfxlist[i]
            if current_num < 9:
                short = short[:-remain]
            shorter = short[before:]
            spacewait = 0
            for char in shorter:
                stdscr.addstr(offsy+i, offsx + num_offsx, shorter, curses.color_pair(2))
        num_offsx = num_offsx + length[current_num]
        num_str = num_str[1:]

def curses_init(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)
    stdscr.erase()

def quiz_loop(stdscr, min_h, min_w):
    """All the game logic is put in here"""
    h, w = stdscr.getmaxyx()
    text = ""
    guessed, gfx_add = [], []

    #draw the screen
    print_big_number(stdscr, 50, 19, 31)
    stdscr.addstr(20,4,"Guess the states:")
    stdscr.addstr(0, 28, "write 'quit' to exit", curses.color_pair(5))
    stdscr.refresh()

    starttime = time.time()

    #game loop, while guessed states are fewer than 50
    while len(guessed) < 50:
        check_term_minsize(stdscr, min_h, min_w)

        try:
            #fetch a key and add it to "text"
            key = stdscr.getch()
            c = chr(key)
            if ("A" <= c <= "z") or c == " ":
                if len(text) <= 16:
                    text += c

            #if ENTER is pressed, check if "text" is either a correctly
            #spelled state or "quit". Case insensitive
            elif key == curses.KEY_ENTER or key in [10,13]:
                if text.lower() == "quit":
                    stdscr.erase()
                    s = "You FAILED America!"
                    for line in range(0, len(eagle)):
                        stdscr.addstr(3+line, 8, eagle[line])
                    stdscr.addstr(7, 27, "\u262D", curses.color_pair(4))
                    stdscr.addstr(19, w//2-len(s)//2, s)
                    stdscr.refresh
                    stdscr.getch()
                    return
                i = 0
                #check if answer is correct, and add the state coordinates
                #and string (shortened name) to "gfx_add"
                while i < len(us_states):
                    if text.lower() == us_states[i][0].lower():
                        gfx_add.append([us_states[i][1], us_states[i][2]])
                        if text.lower() not in guessed:
                            guessed.append(text.lower())
                    i += 1
                #either way, "text" will be reset when ENTER is pressed
                text = ""

            #if backspace is pressed, remove last character from "text"
            elif key == (curses.KEY_BACKSPACE or 127):
                if len(text) > 0:
                    text = text[:-1]
                    stdscr.erase()

            #redraw the screen
            stdscr.erase()
            draw_USA(stdscr, 0, 0, gfx_add)
            stdscr.addstr(20,4,"Guess the states:")
            stdscr.addstr(21,9,text)
            print_big_number(stdscr, 50-len(guessed), 19, 31)
            stdscr.addstr(0, 28, "write 'quit' to exit", curses.color_pair(5))
            stdscr.refresh()
        except:
            check_term_minsize(stdscr, min_h, min_w)

    #if you reach this point you've guessed 50 states and won the game
    endtime = time.time()
    elap = endtime - starttime
    win_graphics(stdscr, 0,1, elap)


def draw_USA(stdscr, y, x, gfx_add):
    """draws the game map and all states that are already guessed"""
    for line in range(0, len(USA)):
        stdscr.addstr(line+y+1, x, USA[line])
    for item in gfx_add:
        stdscr.addstr(item[0][0], item[0][1]-1, item[1], curses.color_pair(2))

def check_term_minsize(stdscr, min_h, min_w):
    while True:
        h, w = stdscr.getmaxyx()
        if (h < min_h) or (w < min_w):
            stdscr.erase()
            if h < min_h:
                red_h_bar = str("V" * (w-1))
                stdscr.addstr(h-1, 0, red_h_bar, curses.color_pair(6))
            if w < min_w:
                for l in range(0, h):
                    stdscr.addstr(l, w-2, ">", curses.color_pair(6))
            res = "Terminal too small!"
            stdscr.addstr(h//2, w//2-len(res)//2, res)
        stdscr.refresh()
        if (h >= min_h) and (w >= min_w):
            break
        time.sleep(.10)


def main(stdscr):
    l = us_states
    curses_init(stdscr)
    min_h, min_w = 25, 65
    check_term_minsize(stdscr, min_h, min_w)

    try:
        draw_USA(stdscr, 0, 0, [])
        quiz_loop(stdscr, min_h, min_w)
    except:
        stdscr.erase()
        res = "Failed to draw to the screen"
        stdscr.getch()
    return 0

curses.wrapper(main)
