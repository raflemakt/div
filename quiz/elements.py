# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import curses
import time

"""
Periodic table quiz for learning the elements by heart.
Written by Gunnar Myhre, October 2020
Keep an eye out for new quizzes at:
https://github.com/raflemakt/div/blob/master/quiz
"""

elements = [
["H" ,  (3,3),      ["Hydrogen"]],
["He",  (3,71),     ["Helium"]],
["Li",  (6,3),      ["Lithium"]],
["Be",  (6,7),      ["Beryllium"]],
["B" ,  (6,51),     ["Boron"]],
["C" ,  (6,55),     ["Carbon"]],
["N" ,  (6,59),     ["Nitrogen"]],
["O" ,  (6,63),     ["Oxygen"]],
["F" ,  (6,67),     ["Fluorine"]],
["Ne",  (6,71),     ["Neon"]],
["Na",  (9,3),      ["Sodium", "Natrium"]],
["Mg",  (9,7),      ["Magnesium"]],
["Al",  (9,51),     ["Aluminum", "Aluminium"]],
["Si",  (9,55),     ["Silicon"]],
["P" ,  (9,59),     ["Phosphorus"]],
["S" ,  (9,63),     ["Sulfur"]],
["Cl",  (9,67),     ["Chlorine"]],
["Ar",  (9,71),     ["Argon"]],
["K" ,  (12,3),     ["Potassium", "Kalium"]],
["Ca",  (12,7),     ["Calcium"]],
["Sc",  (12,11),    ["Scandium"]],
["Ti",  (12,15),    ["Titanium"]],
["V" ,  (12,19),    ["Vanadium"]],
["Cr",  (12,23),    ["Chromium"]],
["Mn",  (12,27),    ["Manganese"]],
["Fe",  (12,31),    ["Iron"]],
["Co",  (12,35),    ["Cobalt"]],
["Ni",  (12,39),    ["Nickel"]],
["Cu",  (12,43),    ["Copper"]],
["Zn",  (12,47),    ["Zinc"]],
["Ga",  (12,51),    ["Gallium"]],
["Ge",  (12,55),    ["Germanium"]],
["As",  (12,59),    ["Arsenic"]],
["Se",  (12,63),    ["Selenium"]],
["Br",  (12,67),    ["Bromine"]],
["Kr",  (12,71),    ["Krypton"]],
["Rb",  (15,3),     ["Rubidium"]],
["Sr",  (15,7),     ["Strontium"]],
["Y" ,  (15,11),    ["Yttrium"]],
["Zr",  (15,15),    ["Zirconium"]],
["Nb",  (15,19),    ["Niobium"]],
["Mo",  (15,23),    ["Molybdenum"]],
["Tc",  (15,27),    ["Technetium"]],
["Ru",  (15,31),    ["Ruthenium"]],
["Rh",  (15,35),    ["Rhodium"]],
["Pd",  (15,39),    ["Palladium"]],
["Ag",  (15,43),    ["Silver"]],
["Cd",  (15,47),    ["Cadmium"]],
["In",  (15,51),    ["Indium"]],
["Sn",  (15,55),    ["Tin"]],
["Sb",  (15,59),    ["Antimony"]],
["Te",  (15,63),    ["Tellurium"]],
["I" ,  (15,67),    ["Iodine"]],
["Xe",  (15,71),    ["Xenon"]],
["Cs",  (18,3),     ["Cesium"]],
["Ba",  (18,7),     ["Barium"]],
["La",  (26,12),    ["Lanthanum"]],
["Ce",  (26,16),    ["Cerium"]],
["Pr",  (26,20),    ["Praseodymium"]],
["Nd",  (26,24),    ["Neodymium"]],
["Pm",  (26,28),    ["Promethium"]],
["Sm",  (26,32),    ["Samarium"]],
["Eu",  (26,36),    ["Europium"]],
["Gd",  (26,40),    ["Gadolinium"]],
["Tb",  (26,44),    ["Terbium"]],
["Dy",  (26,48),    ["Dysprosium"]],
["Ho",  (26,52),    ["Holmium"]],
["Er",  (26,56),    ["Erbium"]],
["Tm",  (26,60),    ["Thulium"]],
["Yb",  (26,64),    ["Ytterbium"]],
["Lu",  (26,68),    ["Lutetium"]],
["Hf",  (18,15),    ["Hafnium"]],
["Ta",  (18,19),    ["Tantalum"]],
["W" ,  (18,23),    ["Tungsten", "Wolfram"]],
["Re",  (18,27),    ["Rhenium"]],
["Os",  (18,31),    ["Osmium"]],
["Ir",  (18,35),    ["Iridium"]],
["Pt",  (18,39),    ["Platinum"]],
["Au",  (18,43),    ["Gold"]],
["Hg",  (18,47),    ["Mercury", "Quicksilver"]],
["Tl",  (18,51),    ["Thallium"]],
["Pb",  (18,55),    ["Lead"]],
["Bi",  (18,59),    ["Bismuth"]],
["Po",  (18,63),    ["Polonium"]],
["At",  (18,67),    ["Astatine"]],
["Rn",  (18,71),    ["Radon"]],
["Fr",  (21,3),     ["Francium"]],
["Ra",  (21,7),     ["Radium"]],
["Ac",  (29,12),    ["Actinium"]],
["Th",  (29,16),    ["Thorium"]],
["Pa",  (29,20),    ["Protactinium"]],
["U" ,  (29,24),    ["Uranium"]],
["Np",  (29,28),    ["Neptunium"]],
["Pu",  (29,32),    ["Plutonium"]],
["Am",  (29,36),    ["Americium"]],
["Cm",  (29,40),    ["Curium"]],
["Bk",  (29,44),    ["Berkelium"]],
["Cf",  (29,48),    ["Californium"]],
["Es",  (29,52),    ["Einsteinium"]],
["Fm",  (29,56),    ["Fermium"]],
["Md",  (29,60),    ["Mendelevium", "Mendeleevium"]],
["No",  (29,64),    ["Nobelium"]],
["Lr",  (29,68),    ["Lawrencium"]],
["Rf",  (21,15),    ["Rutherfordium"]],
["Db",  (21,19),    ["Dubnium"]],
["Sg",  (21,23),    ["Seaborgium"]],
["Bh",  (21,27),    ["Bohrium"]],
["Hs",  (21,31),    ["Hassium"]],
["Mt",  (21,35),    ["Meitnerium"]],
["Ds",  (21,39),    ["Darmstadtium"]],
["Rg",  (21,43),    ["Roentgenium"]],
["Cn",  (21,47),    ["Copernicium"]],
["Nh",  (21,51),    ["Nihonium"]],
["Fl",  (21,55),    ["Flerovium"]],
["Mc",  (21,59),    ["Moscovium"]],
["Lv",  (21,63),    ["Livermorium"]],
["Ts",  (21,67),    ["Tennessine"]],
["Og",  (21,71),    ["Oganesson"]]]

table = [
"╔═══╗                                                               ╔═══╗",
"║1  ║                                                               ║2  ║",
"║   ║                                                               ║   ║",
"╠═══╬═══╗                                       ╔═══╦═══╦═══╦═══╦═══╬═══╣",
"║3  ║4  ║                                       ║5  ║6  ║7  ║8  ║9  ║10 ║",
"║   ║   ║                                       ║   ║   ║   ║   ║   ║   ║",
"╠═══╬═══╣                                       ╠═══╬═══╬═══╬═══╬═══╬═══╣",
"║11 ║12 ║                                       ║13 ║14 ║15 ║16 ║17 ║18 ║",
"║   ║   ║                                       ║   ║   ║   ║   ║   ║   ║",
"╠═══╬═══╬═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╬═══╬═══╬═══╬═══╬═══╬═══╣",
"║19 ║20 ║21 ║22 ║23 ║24 ║25 ║26 ║27 ║28 ║29 ║30 ║31 ║32 ║33 ║34 ║35 ║36 ║",
"║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║",
"╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣",
"║37 ║38 ║39 ║40 ║41 ║42 ║43 ║44 ║45 ║46 ║47 ║48 ║49 ║50 ║51 ║52 ║53 ║54 ║",
"║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║",
"╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣",
"║55 ║56 ║57-║72 ║73 ║74 ║75 ║76 ║77 ║78 ║79 ║80 ║81 ║82 ║83 ║84 ║85 ║86 ║",
"║   ║   ║ 71║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║",
"╠═══╬═══╣   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣",
"║87 ║88 ║89-║104║105║106║107║108║109║110║111║112║113║114║115║116║117║118║",
"║   ║   ║103║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║",
"╚═══╩═══╝   ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝",
"",
"         ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗",
"         ║57 ║58 ║59 ║60 ║61 ║62 ║63 ║64 ║65 ║66 ║67 ║68 ║69 ║70 ║71 ║",
"         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║",
"         ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣",
"         ║89 ║90 ║91 ║92 ║93 ║94 ║95 ║96 ║97 ║98 ║99 ║100║101║102║103║",
"         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║   ║",
"         ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝"]

bunsen = [
"                               __              []",
"                               ||              []",
"                               ||              []",
"                               ||              []",
"                            __ ||              []",
"                            || ||              []",
"                          .-||-||-.            []  /\ ",
"                         _\_______/_===========[]=(-o)",
"                          )\_____/(            []  \/",
"                         /     ||  \           []",
"                        /      ||   \          []",
"                       /       ||    \         []",
"                      /~~~~~~~~~~~~~~~\        []",
"                     /         ::      \       []",
"                    (          ::       )      []",
"    You guessed      `-----------------'       []",
"    all 118 elements.        )                 []",
"    Good job!              (   )               []",
"                             )( . (            []",
"                          .) @@)   )           []",
"                       ` ) @@(@@)@             []",
"                         (@@(@@)@              []",
"                          @(@.@)@@             []",
"                        ` (@{__}@)`            []",
"                            :__;               []",
"        ___                  {}+               []",
"       ( = )             .---'`---.            []",
"        | |_            /          \   ________[]____",
"    ____| |_|==========(____________)_/______________\ "]

nuke = [
"                          ________________",
"                     ____/ (  (    )   )  \___",
"                    /( (  (  )   _    ))  )   )\ ",
"                  ((     (   )(    )  )   (   )  )",
"                ((/  ( _(   )   (   _) ) (  () )  )",
"               ( (  ( (_)   ((    (   )  .((_ ) .  )_",
"              ( (  )    (      (  )    )   ) . ) (   )",
"             (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )",
"             ( (  (   ) (  )   (  ))     ) _)(   )  )  )",
"            ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )",
"             (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )",
"            ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )",
"             ((  (   )(    (     _    )   _) _(_ (  (_ )",
"              (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)",
"              ((__)        \ ||lll|l||///          \_))",
"                       (   /(/ (  )  ) )\   )",
"                     (    ( ( ( | | ) ) )\   )",
"                      (   /(| / ( )) ) ) )) )",
"                    (     ( ((((_(|)_)))))     )",
"                     (      ||\(|(|)|/||     )",
"                   (        |(||(||)||||        )",
"                     (     //|/l|||)||\ \     )",
"                   (/ / //  /|//|||||\  \ \  \ _)",
"---------------------------------------------------------------------"]

def win_graphics(stdscr, y, x, elap):
    """Draws the win graphics and elapsed time"""
    stdscr.erase()
    for line in range(0, len(bunsen)):
        stdscr.addstr(y+line, x+13, bunsen[line], curses.color_pair(1))
    elap_str = "Time elapsed: {} seconds".format(round(elap, 2))
    stdscr.addstr(30+y, x+7, elap_str, curses.color_pair(5))
    stdscr.addstr(31+y, x+7, "Press 'q' to exit", curses.color_pair(1))
    stdscr.refresh()
    k = stdscr.getch()
    while k != ord("q"):
        k = stdscr.getch()
    return

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
                stdscr.addstr(offsy+i, offsx + num_offsx, shorter, curses.color_pair(4))
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
    print_big_number(stdscr, 118-len(guessed), 2, 15)
    stdscr.addstr(8, 15, "remaining")
    stdscr.addstr(32,4,"Guess the elements:")
    stdscr.addstr(0, 28, "write 'quit' to exit", curses.color_pair(5))
    stdscr.refresh()

    starttime = time.time()

    #game loop, while guessed elements are fewer than 118
    while len(guessed) < 118:
        check_term_minsize(stdscr, min_h, min_w)

        try:
            #fetch a key and add it to "text"
            key = stdscr.getch()
            c = chr(key)
            if ("A" <= c <= "z") or c == " ":
                if len(text) <= 16:
                    text += c

            #if ENTER is pressed, check if "text" is either a correctly
            #spelled element or "quit". Case insensitive
            elif key == curses.KEY_ENTER or key in [10,13]:
                if text.lower() == "quit":
                    stdscr.erase()
                    s = "You FAILED chemistry!"
                    for line in range(0, len(nuke)):
                        stdscr.addstr(3+line, w//2-35, nuke[line], curses.color_pair(5))
                    stdscr.addstr(19, w//2-len(s)//2-1, s)
                    stdscr.refresh
                    stdscr.getch()
                    return
                i = 0
                #check if answer is correct, and add the element coordinates
                #and string (chemical symbol) to "gfx_add"
                while i < len(elements):
                    if text.title() in elements[i][2]:
                        stdscr.addstr(7, 27, "\u262D", curses.color_pair(4))
                        gfx_add.append([elements[i][0], elements[i][1]])
                        if i not in guessed:
                            guessed.append(i)
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
            draw_table(stdscr, 0, 0, gfx_add)
            stdscr.addstr(32,4,"Guess the elements:")
            stdscr.addstr(32,24,text)
            print_big_number(stdscr, 118-len(guessed), 2, 15)
            stdscr.addstr(8, 15, "remaining")
            stdscr.addstr(0, 28, "write 'quit' to exit", curses.color_pair(5))
            stdscr.refresh()
        except:
            check_term_minsize(stdscr, min_h, min_w)

    #if you reach this point you've guessed 118 elements and won the game
    endtime = time.time()
    elap = endtime - starttime
    win_graphics(stdscr, 2,1, elap)


def draw_table(stdscr, y, x, gfx_add):
    """draws the table and all elements that are already guessed"""
    for line in range(0, len(table)):
        stdscr.addstr(line+y+1, x, table[line])
    for item in gfx_add:
        stdscr.addstr(item[1][0], item[1][1]-1, item[0], curses.color_pair(2))

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
    min_h, min_w = 34, 73
    check_term_minsize(stdscr, min_h, min_w)

    try:
        draw_table(stdscr, 0, 0, [])
        quiz_loop(stdscr, min_h, min_w)
    except:
        stdscr.erase()
        res = "Failed to draw to the screen"
        stdscr.getch()
    return 0

curses.wrapper(main)
