# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import curses
import time

"""
European countries quiz for learning the countries by heart.
Written by Gunnar Myhre, October 2020
Keep an eye out for new quizzes at:
https://github.com/raflemakt/div/blob/master/quiz

Ascii art credits:
Win screen composed of two pictures from "JGS"
Mountains: Unknown
EU map by myself
"""

countries = [
["Albania",                  (25,37),   "AL."],
["Andorra",                  (23,14),   "And."],
["Austria",                  (19,30),   "AT."],
["Belarus",                  (13,42),   "Belarus"],
["Belgium",                  (17,20),   "Bel."],
["Bosnia and Herzegovina",   (22,33),   "BA"],
["Bulgaria",                 (23,41),   "Bulgaria"],
["Croatia",                  (21,31),   "HR"],
["Cyprus",                   (29,50),   "Cyprus"],
["Czech Republic",           (17,29),   "CZ"],
["Denmark",                  (11,22),   "Denmark"],
["Estonia",                  (9,40),    "Estonia"],
["Finland",                  (6,37),    "Finland"],
["France",                   (20,11),   "France"],
["Germany",                  (15,24),   "Germany"],
["Greece",                   (27,38),   "Greece"],
["Hungary",                  (19,36),   "HU"],
["Iceland",                  (3,10),    "Iceland"],
["Ireland",                  (12,1),    "Ireland"],
["Italy",                    (26,26),   "Italy"],
["Kosovo",                   (23,36),   "Kos."],
["Latvia",                   (10,40),   "Latvia"],
["Liechtenstein",            (19,22),   "Liecht."],
["Lithuania",                (12,38),   "Lithuania"],
["Luxembourg",               (18,21),   "Lux."],
["Malta",                    (29,30),   "Malta"],
["Moldova",                  (18,46),   "Moldova"],
["Monaco",                   (23,20),   "Mon."],
["Montenegro",               (24,35),   "ME"],
["Netherlands",              (14,21),   "NL"],
["North Macedonia",          (24,40),   "MK"],
["Norway",                   (6,24),    "Norway"],
["Poland",                   (13,32),   "Poland"],
["Portugal",                 (24,1),    "Portugal"],
["Romania",                  (20,40),   "Romania"],
["Russia",                   (13,51),   "Russia"],
["San Marino",               (21,26),   "S.M."],
["Serbia",                   (22,37),   "Serb."],
["Slovakia",                 (17,35),   "SK."],
["Slovenia",                 (20,29),   "SL"],
["Spain",                    (26,5),    "Spain"],
["Sweden",                   (8,28),    "Sweden"],
["Switzerland",              (20,20),   "Switz."],
["Turkey",                   (25,48),   "Turkey"],
["Ukraine",                  (16,44),   "Ukraine"],
["United Kingdom",           (14,13),   "UK"],
["Vatican City",             (24,26),   "VA"]]

forfeit = [
"          /\      ",
"         /**\      ",
"        /****\   /\      ",
"       /      \ /**\      ",
"      /  /\    /    \        /\    /\  /\      /\            /\/\/\  /\ ",
"     /  /  \  /      \      /  \/\/  \/  \  /\/  \/\  /\  /\/ / /  \/  \ ",
"    /  /    \/ /\     \    /    \ \  /    \/ /   /  \/  \/  \  /    \   \ ",
"   /  /      \/  \/\   \  /      \    /   /    \ ",
"__/__/_______/___/__\___\__________________________________________________"]



win = [
'                        .',
'                        T                        |',
'                       ( )                       |',
'                       <==>                      A',
'                        FJ                     _/X\_',
'                        ==                     \/X\/',
'                       J||F                     |V|',
'                       F||J                     |A|',
'                      /\/\/\                    |V|',
'                      F++++J                   /XXX\ ',
'                     J{}{}{}F         .        |\/\|',
'                  .  F{}{}{}J         T        |/\/|',
'       .          T J{}{}{}{}F        ;;       |\/\|',
'       T         /|\F \/ \/ \J  .   ,;;;;.     |/\/|',
'      /:\      .`/|7\:========F T ./;;;;;;\    |\/\|',
'    ./:/:/.   ///|||`\`""""""" /x\T\;;;;;;/    |/\/|',
'   //:/:/:/\  \`\`|////..[]...xXXXx.|====|    IIIIIII',
'   \:/:/:/:T7 :.:.:.:.:||[]|/xXXXXXx\|||||    |\/_\/|',
'   ::.:.:.:A. `;:;:;:;`=====\XXXXXXX/=====.  /\// \`/\ ',
'   `;""::/xxx\.|,|,|,| ( )( )| | | |.=..=.|  |/|   |\|',
"    :. :`\ xx/(_)(_)(_) _  _ | | | |`-``-`| /\X/___\X/\ ",
'    :T-`-.:"":|"""""""|/ \/ \|=====|======|IIIIIIIIIIIII ',
'    .A."""||_|| ,. .. || || |/\/\/\/ | | |/`-\/XXXXX\/-`\ ',
':;:////\:::.`.| || || ||-||-|/\/\/\+|+| /`.-`/\|/I\|/\`-.`\ ',
':;;\////::::,=`=======`============/\/\/`\-/_.-"` `"-._ \-/\ ',
'::;""":::::;:|__..,__|===========/||\=/.-`.`           `.`-.\ ',
'::;|=:::;:;::|,;:::::         |===== /`\-/               \-/`\ ',
'::::::::(}:::::;::::::________|===_/`-`/`_               _`\`-`\ ',
'                                     `"""""""`                `""']


europe = [
'                               _i-*L\___      /                   ',
'         ___                  /_AH/ \   """| p                    ',
'       /"iiii                //   \  \ t""""/                     ',
'       \__/*               _//   -YY  \ ""\_\                     ',
'                          / ?    | /   \                          ',
'             O         ,/J |   U" |     >                         ',
'                     %"    |   |  \  __/_                         ',
'                %    |     /    \¤ \/&--|                         ',
'           ,-=<      |   /A    /*   U_ _|                         ',
'           t */       "-_.\    |¤  |--* \                         ',
'       __--t =|        / # |  /    |=T--/***\                     ',
'      / \_/p= \        |_Y¤?-" ___/__T  |    \,                   ',
'     ,7 _/ _/  |,   _ _| \/t\_/       \y      >__                 ',
'     """ ,/     /  / |       |        |_______|  |_____           ',
'        ,-7____|__/_./       |         |               |          ',
'        """ _ _| \  |       /A\__     _|               |          ',
'        ---" "    \_O_     |_    /----|    ___        _/          ',
'        ""\          /      /---x  _r-K___/\_ \ __   / |          ',
'           \        /*-\---t    r-/   /      |// *\  >t-"=__      ',
'           /       /_AA_>"""T--T\____/       |//   \/       \     ',
' .-=__    /         |     /"|-7_---| \_      _|             /     ',
' |t-, ""--y         t:-\  |_ "\9_  |.  T----" |    _-------/      ',
' |  |      ""\_T""\-" _.|   \  "-../|/\T     _T___/               ',
' / /        __-H      || "\  \_    \/T"_\=--/_==t                 ',
'|  /       /         -p,   "\ _"--. |"T _E" "6                    ',
'| /       | . o `    T |     ""tp\| \/  7_   |        ___         ',
' t\  _  _-"          \/    _   /P    "T   \   "-_ ,--"_  |        ',
'  "="_""   ______         |_\-|"      \__|"      ""  /_7 |        ',
'  "Y"  T--/      ""--t""-   "?u           -===-      "   |        ']


def win_graphics(stdscr, y, x, elap):
    """Draws the win graphics and elapsed time"""
    stdscr.erase()
    for line in range(0, len(win)):
        stdscr.addstr(y+line, x, win[line], curses.color_pair(5))
    stdscr.addstr(30+y, x, "Time elapsed: {} seconds".format(round(elap, 2)))
    stdscr.addstr(6+y, 7+x, "You WON!")
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
                stdscr.addstr(offsy+i, offsx + num_offsx, shorter, curses.color_pair(3))
        num_offsx = num_offsx + length[current_num]
        num_str = num_str[1:]

def curses_init(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
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
    print_big_number(stdscr, 47, 5, 48)
    stdscr.addstr(31,4,"Guess the countries:")
    stdscr.addstr(0, 0, "write 'quit' to exit", curses.color_pair(5))
    stdscr.refresh()

    starttime = time.time()

    #game loop, while guessed countries are fewer than 47
    while len(guessed) < 47:
        check_term_minsize(stdscr, min_h, min_w)

        try:
            #fetch a key and add it to "text"
            key = stdscr.getch()
            c = chr(key)
            if ("A" <= c <= "z") or c == " ":
                if len(text) <= 25:
                    text += c

            #if ENTER is pressed, check if "text" is either a correctly
            #spelled country or "quit". Case insensitive
            elif key == curses.KEY_ENTER or key in [10,13]:
                if text.lower() == "quit":
                    stdscr.erase()
                    s = "You forfeit. Better luck next time."
                    for line in range(0, len(forfeit)):
                        stdscr.addstr(3+line, 5, forfeit[line][:-5], curses.color_pair(3))
                    for line in range(0, len(forfeit)):
                        stdscr.addstr(5+line, 0, forfeit[line])
                    stdscr.addstr(19, w//2-len(s)//2, s)
                    stdscr.refresh
                    stdscr.getch()
                    return
                i = 0
                #check if answer is correct, and add the country coordinates
                #and string (shortened name) to "gfx_add"
                while i < len(countries):
                    if text.lower() == countries[i][0].lower():
                        gfx_add.append([countries[i][1], countries[i][2]])
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
            draw_EU(stdscr, 0, 0, gfx_add)
            stdscr.addstr(31,4,"Guess the countries:")
            stdscr.addstr(31,25,text)
            print_big_number(stdscr, 47-len(guessed), 5, 48)
            stdscr.addstr(0, 0, "write 'quit' to exit", curses.color_pair(5))
            stdscr.refresh()
        except:
            check_term_minsize(stdscr, min_h, min_w)

    #if you reach this point you've guessed 47 countries and won the game
    endtime = time.time()
    elap = endtime - starttime
    win_graphics(stdscr, 0,0, elap)


def draw_EU(stdscr, y, x, gfx_add):
    """draws the game map and all countries that are already guessed"""
    for line in range(0, len(europe)):
        stdscr.addstr(line+y+1, x, europe[line])
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
    curses_init(stdscr)
    min_h, min_w = 32, 66
    check_term_minsize(stdscr, min_h, min_w)

    try:
        draw_EU(stdscr, 0, 0, [])
        quiz_loop(stdscr, min_h, min_w)
    except:
        stdscr.erase()
        res = "Failed to draw to the screen"
        stdscr.getch()
    return 0

curses.wrapper(main)
