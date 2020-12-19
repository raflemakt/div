# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import curses
import time

"""
Geological time quiz for learning the periods by heart.
Written by Gunnar Myhre, December 2020
Keep an eye out for new quizzes at:
https://github.com/raflemakt/div/blob/master/quiz

Ascii art credits:
3D Globe - Unknown
Moon     - Unknown
"""


game_screen = [
"Eon  Era  Period       Epoch        Age         Years     Events, occurances",
"╔═══╦═══╦════════════╦════════════════════════╗",
"║ P ║ C ║            ║                        ║",
"║ h ║ e ║            ╠════════════════════════╣",
"║ a ║ n ║            ║                        ║",
"║ n ║ o ╠════════════╬════════════════════════╣",
"║ e ║ z ║            ║                        ║",
"║ r ║ o ║            ║                        ║",
"║ o ║ i ║            ╠════════════════════════╣",
"║ z ║ c ║            ║                        ║",
"║ o ║   ║            ║                        ║",
"║ i ║   ║            ║                        ║",
"║ c ╠═══╬════════════╩═══╦════════════════════╝",
"║   ║ M ║                ║",
"║   ║ e ║                ║",
"║   ║ s ╠════════════════╣",
"║   ║ o ║                ║",
"║   ║ z ║                ║",
"║   ║ o ╠════════════════╣",
"║   ║ i ║                ║",
"║   ║ c ║                ║",
"║   ╠═══╬════════════════╣",
"║   ║ P ║                ║",
"║   ║ a ╠════════════════╣",
"║   ║ l ║                ║",
"║   ║ e ╠════════════════╣",
"║   ║ o ║                ║",
"║   ║ z ╠════════════════╣",
"║   ║ o ║                ║",
"║   ║ i ╠════════════════╣",
"║   ║ c ║                ║",
"║   ║   ╠════════════════╣",
"║   ║   ║                ║",
"╠═══╬═══╩═══════════╦════╝",
"║ P ║               ║",
"║ r ║               ║",
"║ e ║               ║",
"║ c ╠═══════════════╣",
"║ a ║               ║",
"║ m ║               ║",
"║ b ║               ║",
"║ r ╠═══════════════╣",
"║ i ║               ║",
"║ a ║               ║",
"║ n ║               ║",
"╚═══╩═══════════════╝"]

epoch_list = [
        [["Hadean"],          [
                            [(44,8),    5,  "Hadean"],
                            [(43,39),   5,  "Earliest water"],
                            [(44,39),   5,  "Earth's crust solidifies"],
                            [(45,39),   5,  "Formation of the Moon"],
                            [(46,26),   2,  "4600 Ma"]]],
        [["Archean"],         [
                            [(40,8),    5,  "Archean"],
                            [(39,39),   5,  "Earliest oxygen, photosynthesis"],
                            [(40,39),   5,  "Late Heavy Bombardement (LHB) ends"],
                            [(41,39),   5,  "Earliest life"],
                            [(42,26),   2,  "3875 Ma"]]],
        [["Proterozoic"],     [
                            [(36,8),    5,  "Proterozoic"],
                            [(35,39),   5,  "Global ice ages, Rodinia supercontinent"],
                            [(36,39),   5,  "Eukaryotes, multicellular life"],
                            [(37,39),   5,  "Oxygen Crisis (GOE)"],
                            [(38,26),   2,  "2500 Ma"]]],
        [["Cambrian"],        [
                            [(33,12),   5,  "Cambrian"],
                            [(33,39),   5,  "First evolution of eyes"],
                            [(34,39),   3,  "Cambrian Explosion"],
                            [(34,29),   2,  "541 Ma"]]],
        [["Ordovician"],      [
                            [(31,12),   5,  "Ordovician"],
                            [(31,39),   5,  "First land plant spores"],
                            [(32,29),   2,  "485 Ma"]]],
        [["Silurian"],        [
                            [(29,12),   5,  "Silurian"],
                            [(29,39),   5,  "Moss forests, land arthropods"],
                            [(30,39),   4,  "O-S Extinction events"],
                            [(30,29),   2,  "444 Ma"]]],
        [["Devonian"],        [
                            [(27,12),   5,  "Devonian"],
                            [(27,39),   5,  "Land vertebrates"],
                            [(28,29),   2,  "419 Ma"]]],
        [["Carboniferous"],   [
                            [(25,12),   5,  "Carboniferous"],
                            [(25,39),   5,  "Pangaea assembles"],
                            [(26,39),   4,  "Late Devonian Extinction"],
                            [(26,29),   2,  "359 Ma"]]],
        [["Permian"],         [
                            [(23,12),   5,  "Permian"],
                            [(23,39),   5,  "Large archosaurs and therapsids"],
                            [(24,29),   2,  "299 Ma"]]],
        [["Triassic"],        [
                            [(20,12),   5,  "Triassic"],
                            [(20,39),   5,  "First dinosaurs and mammals"],
                            [(21,39),   5,  "Acidic dysaerobic conditions (Coal Gap)"],
                            [(22,39),   4,  "P-Tr Extinction (the Great Dying)"],
                            [(22,29),   2,  "252 Ma"]]],
        [["Jurassic"],        [
                            [(17,12),   5,  "Jurassic"],
                            [(17,39),   5,  "Pangaea drifts apart"],
                            [(18,39),   5,  "Dinosaurs dominate the land"],
                            [(19,39),   4,  "Tr-J Extinction"],
                            [(19,29),   2,  "201 Ma"]]],
        [["Cretaceous"],      [
                            [(14,12),   5,  "Cretaceous"],
                            [(14,39),   5,  "Angiosperms (flowering plants)"],
                            [(15,39),   5,  "Dinosaurs continue their reign"],
                            [(16,29),   2,  "145 Ma"]]],
        [["Tertiary"],        [
                            [(7,11),    5,  "Tertiary"]]],
        [["Paleogene"],       [
                            [(10,24),   5,  "Paleogene"]]],
        [["Paleocene"],       [
                            [(12,37),   5,  "Paleocene"],
                            [(12,59),   5,  "Polar forests"],
                            [(13,59),   4,  "K-Pg Extinction"],
                            [(13,49),   2,  "66 Ma"]]],
        [["Eocene"],          [
                            [(11,37),   5,  "Eocene"],
                            [(11,49),   2,  "56 Ma"],
                            [(11,59),   5,  "P-E Thermal Maximum"]]],
        [["Oligocene"],       [
                            [(10,37),   5,  "Oligocene"],
                            [(10,49),   2,  "34 Ma"],
                            [(10,59),   5,  "Antarctic ice sheets"]]],
        [["Neogene"],         [
                            [(7,24),    5,  "Neogene"]]],
        [["Miocene"],         [
                            [(8,37),    5,  "Miocene"],
                            [(8,49),    2,  "23 Ma"],
                            [(8,59),    5,  "Himalayas rise"]]],
        [["Pliocene"],        [
                            [(7,37),    5,  "Pliocene"],
                            [(7,49),    2,  "5.3 Ma"],
                            [(7,59),    5,  "Bipedal apes, tools"]]],
        [["Quaternary"],      [
                            [(3,11),    5,  "Quaternary"]]],
        [["Pleistocene"],     [
                            [(5,24),    5,  "Pleistocene"],
                            [(5,49),    2,  "2.6 Ma"],
                            [(5,59),    5,  "Ice Age, genus Homo"]]],
        [["Holocene"],        [
                            [(3,24),    5,  "Holocene"],
                            [(3,49),    2,  "11,700 years ago"],
                            [(3,67),    5,  "Ice Age ends"]]]]

earth = [
"""
               _-o#&&*''*'?d:>b\_
          _o/"`''  '',, dMF9MMMMMHo_
       .o&#'        `"MbHMMMMMMMMMMMHo.
     .o"" '         vodM*$&&HMMMMMMMMMM?.
    ,'              $M&ood,~'`(&##MMMMMMH)
   /               ,MMMMMMM#b?#bobMMMMHMMML
  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
 ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
]MMH#             ""*""*"*#MMMMMMMMMMMMM'    -
MMMMMb_                   |MMMMMMMMMMMP'     :
HMMMMMMMHo                 `MMMMMMMMMT       .
?MMMMMMMMP                  9MMMMMMMM}       -
-?MMMMMMM                  |MMMMMMMMM?,d-    '
 :|MMMMMM-                 `MMMMMMMT .M|.   :
  .9MMM[                    &MMMMM*' `'    .
   :9MMk                    `MMM#"        -
     &M}                     `          .-
      `&.                             .
        `~,   .                     ./
            . _                  .-
              '`--._,dd###pp=""'
""",
"""
              _v->#H#P? "':o<>\_
          .,dP` `''  "'-o.+H6&MMMHo_
        oHMH9'         `?&bHMHMMMMMMHo.
      oMP"' '           ooMP*#&HMMMMMMM?.
    ,M*          -     `*MSdob//`^&##MMMH)
   d*'                .,MMMMMMH#o>#ooMMMMMb
  HM-                :HMMMMMMMMMMMMMMM&HM[R)
 d"Z\.               9MMMMMMMMMMMMMMMMM[HMM|:
-H    -              MMMMMMMMMMMMMMMMMMMbMP' :
:??Mb#               `9MMMMMMMMMMMMMMMMMMH#! .
: MMMMH#,              "*""*"`#HMMMMMMMMMMH  -
||MMMMMM6\.                    {MMMMMMMMMH'  :
:|MMMMMMMMMMHo                 `9MMMMMMMM'   .
. HMMMMMMMMMMP'                 !MMMMMMMM    `
- `#MMMMMMMMM                   HMMMMMMM*,/  :
 :  ?MMMMMMMF                   HMMMMMM',P' :
  .  HMMMMR'                    {MMMMP' ^' -
   : `HMMMT                     iMMH'     .'
    -.`HMH                               .
      -:*H                            . '
        -`\,,    .                  .-
          ' .  _                 .-`
              '`~\.__,obb#q==~*''
""",
"""
              .ovr:HMM#?:`' >b\_
          .,:&Hi' `'   "' )\|&bSMHo_
        oHMMM#*}          `?&dMMMMMMHo.
     .dMMMH"'*''           ,oHH*&&9MMMM?.
    ,MMM*'                 `*M)bd<|"*&#MH)
   dHH?'                   :MMMMMM#bd#odMML
  H' |\                  `dMMMMMMMMMMMMMM9Mk
 JL/"7+,.                `MMMMMMMMMMMMMMMH9ML
-`Hp     '               |MMMMMMMMMMMMMMMMHH|:
:  )\#M#d?                `HMMMMMMMMMMMMMMMMH.
.   JMMMMM##,              ``*""'"*#MMMMMMMMH
-. ,MMMMMMMM6o_                    |MMMMMMMM':
:  |MMMMMMMMMMMMMb\                 TMMMMMMT :
.   ?MMMMMMMMMMMMM'                 :MMMMMM|.`
-    ?HMMMMMMMMMM:                  HMMMMMM\|:
 :     9MMMMMMMMH'                 `MMMMMP.P.
  .    `MMMMMMT''                   HMMM*''-
   -    TMMMMM'                     MM*'  -
    '.   HMM#                            -
      -. `9M:                          .'
        -. `b,,    .                . '
          '-\   .,               .-`
              '-:b~7\_,oddq==--"
""",
"""
              _oo##'9MMHb':'-,o_
          .oH":HH$' ""'  "' -)7*R&o_
       .oHMMMHMH#9:          ")bMMMMHo.
      dMMMMMM*""'`'           .oHM"H9MM?.
    ,MMMMMM'                   "HLbd<|?&H)
   JMMH#H'                     |MMMMM#b>bHb
  :MH  ."\                   `|MMMMMMMMMMMM&
 .:M:d-"|:b..                 9MMMMMMMMMMMMM+
:  "*H|      -                &MMMMMMMMMMMMMH:
.    `LvdHH#d?                `?MMMMMMMMMMMMMb
:      iMMMMMMH#b               `"*"'"#HMMMMMM
.   . ,MMMMMMMMMMb\.                   {MMMMMH
-     |MMMMMMMMMMMMMMHb,               `MMMMM|
:      |MMMMMMMMMMMMMMH'                &MMMM,
-       `#MMMMMMMMMMMM                 |MMMM6-
 :        `MMMMMMMMMM+                 ]MMMT/
  .       `MMMMMMMP"                   HMM*`
   -       |MMMMMH'                   ,M#'-
    '.     :MMMH|                       .-
      .     |MM                        -
       ` .   `#?..    .             ..'
           -.     _.             .-
              '-|.#qo__,,ob=~~-''
""",
"""
              _ooppH[`MMMD::--\_
          _oHMR":&M&. ""'  "'  /&)\_
        oHMMMMMHMMH#9,         `"<MMHo.
      oHMMMMMMMM*""'``           .dMP#M?.
    .dMMMMMMMM*                   `H\do?&)
   -iMMMHH#H'                      &MMMHb#?
  : ZMM'   7-.                   `{MMMMMMMMH
 .  .M6_d|"`$|v..                 9MMMMMMMMML
-    `'*H#       :                |MMMMMMMMMM:
:        *(7dHM#dd.                ?MMMMMMMMMb
-          |MMMMMMM##\              `"*""?HMMM
:      .  |MMMMMMMMMMMo\.                 {MMM
.         {MMMMMMMMMMMMMMMHo.             `MMM
-          ?MMMMMMMMMMMMMMM*'             -MMP
:           `#MMMMMMMMMMMMT               dMM'
 -            |MMMMMMMMMMH'              -MMT
  :           `MMMMMMMM"'                JMP
   -           MMMMMMH'                 ,H?
    '.         HMMM#'                    :
      .        ?MM-                   . '
        -.      *M:..               .-
           - .      _.           .-
              '-.~-dHb__\ov+~~-`
""",
"""
              _ooppH[`MMMD::--\_
          .oHMMMR:"&MZ\ `"'  "  |$-_
       ..dMMMMMMMMdMMM#9\        `'HHo.
     . ,dMMMMMMMMMMM"`' `           ?MP?.
    . |MMMMMMMMMMM'                 `"$b&)
   -  |MMMMHH##M'                     HMMH?
  -   TTMM|    >..                   \MMMMMH
 :     |MM\,#-""$~b\.                `MMMMMM+
.       ``"H&#        -               &MMMMMM|
:            *7v,#MHddc.              `9MMMMMb
.               MMMMMMMM##\             `"":HM
-          .  .HMMMMMMMMMMRo_.              |M
:             |MMMMMMMMMMMMMMMM#\           :M
-              `HMMMMMMMMMMMMMMM'           |T
:               `*HMMMMMMMMMMMM'            H'
 :                 MMMMMMMMMMM|            |T
  .                MMMMMMMM?'             ./
  `.               MMMMMMH'              ./
    -.            |MMMH#'                .
      .           `MM*                . '
        -.         #M: .    .       .-
          ` .         .,         .-
              '-.-~ooHH__,,v~--`
""",
"""
              _ood>H&H&Z?#M#b-\.
          .\HMMMMMR?`\M6b."`' ''``v.
       .. .MMMMMMMMMMHMMM#&.      ``~o.
     .   ,HMMMMMMMMMMMM*"'-`          &b.
    .   .MMMMMMMMMMMMH'               `"&)
   -     RMMMMM#H##R'                   4Mb
  -      |7MMM'    ?::                 `|MMb
 /         HMM__#|`"\>?v..              `MMML
.           `"'#Hd|       `              9MMM:
-                |\,\?HH#bbL             `9MMb
:                   !MMMMMMMH#b,          `""T
.              .   ,MMMMMMMMMMMbo.           |
:                  4MMMMMMMMMMMMMMMHo        |
:                   ?MMMMMMMMMMMMMMM?        :
-.                   `#MMMMMMMMMMMM:        .-
 :                     |MMMMMMMMMM?         .
  -                    JMMMMMMMT'          :
  `.                   MMMMMMH'           -
    -.                |MMM#*`            -
      .               HMH'            . '
        -.            #H:.          .-
          ` .           .\       .-
              '-..-+oodHL_,--/-`
""",
"""
              _,\?dZkMHF&$*q#b..
          .//9MMMMMMM?:'HM))"`-''`..
       ..`  :MMMMMMMMMMHMMMMH?_    `-)
     .     .dMMMMMMMMMMMMMM'"'"       `\.
    .      |MMMMMMMMMMMMMR              ))
   -        T9MMMMMHH##M"                `?
  :          (9MMM'    !':.               &k
 .:            HMM\_?p "":-b\.            `ML
-                "'"H&#,       :           |M|
:                     ?\,\dMH#b#.           9b
:                        |MMMMMMM##,        `*
:                   .   +MMMMMMMMMMMo_       -
:                       HMMMMMMMMMMMMMM#,    :
:                        9MMMMMMMMMMMMMH'    .
: .                       *HMMMMMMMMMMP     .'
 :                          MMMMMMMMMH'     .
  -                        :MMMMMMM'`      .
  `.                       9MMMMM*'       -
    -.                    {MMM#'         :
      -                  |MM"          .'
       `.                &M'..  .   ..'
          ' .             ._     .-
              '-. -voboo#&:,-.-`
""",
"""
              _oo:7bk99M[<$$+b\.
           .$*"MMMMMMMM[:"\Mb\?^" .
       . '`    HMMMMMMMMMMHMMMM+?.  `.
     .        .HMMMMMMMMMMMMMMP"''     .
    .         `MMMMMMMMMMMMMM|         -`.
   -           `&MMMMMMHH##H:             :
  :             `(*MMM}    `|\             |
 : `-              ?MMb__#|""`|+v..         )
.                    `''*H#b       -        :|
:                         `*7v,#M#b#,        )
.                             9MMMMMMHb.     :
:                        .   #MMMMMMMMMb\    -
-                           .HMMMMMMMMMMMMb  :
:                            `MMMMMMMMMMMMH  .
-:  .                         `#MMMMMMMMMP   '
 :                              ]MMMMMMMH'  :
  -                            ,MMMMMM?'   .
  `:                           HMMMMH"    -
    -.                       .HMM#*     .-
     `.                     .HH*'     .
       `-.                  &R".    .-
           -.               ._   .-
              '-. .voodoodc?..-`
""",
"""
              _\oo\?ddk9MRbS>v\_
          ..:>*""MMMMMMMMM:?|H?$?-.
       ..- -     "HMMMMMMMMMMHMMMH\_-.
     .            dMMMMMMMMMMMMMMT"    .
    .             TMMMMMMMMMMMMMM       `.
   -               `&HMMMMMM#H#H:         .
  -                 `)7HMMH     |\.        .
 :    `                 HMM\_?c`""+?\..     :
-                         "``#&#|      .     -
:                              `?,\#MHdb.    .
:                                 |MMMMMH#.  :
:                            .   ,HMMMMMMMb, -
: '                              4MMMMMMMMMMH`
:   .                             9MMMMMMMMMT-
:.`                               `#MMMMMMMH '
 :      '                           HMMMMMH':
  -                                |MMMMH" -
  `:                              |MMMH*' .'
    '?                           dMM#'   .
      \.                       .dH"    .'
        -.                    ,M'-  ..'
          ` .                .. ..-`
              '-. .\ooooboo<^.-`
""",
"""
              _o,:o?\?dM&MHcc~,.
          ..^':&#""HMMMMMMMM$:?&&?.
        .`  -`      'HMMMMMMMMMHMMMp\.
     . '             |MMMMMMMMMMMMMM"' .
    .                `9MMMMMMMMMMMMM    -.
   -                   `*9MMMMMHH##[      .
  -                     `\Z9MMM    `~\     .
 :       '|                 ?MMb_?p""-?v..  :
-                             `"'*&#,    -   .
:                                  `?,oHH#?  .
--                                    |MMMMH,:
:                                 .  |MMMMMM6,
:   -                                |MMMMMMMM
?                                     HMMMMMMP
-- . '                                |HMMMMM'
 :.`     .  '                          JMMMM+
  \                                   ,MMMP:
   :                                 |MMH?:
    -:\.                            dM#" .
       \                          ,H*' .'
        -.                       d':..'
          ` .                  .,.-
              '-.. .\oooodov~^-`
""",
"""
              _o\:,??\??MR9#cb\_
          .v/'*':&#""#HMMMMMMM$?*d\.
       ..~' - -`      `"#MMMMMMMMMMMHv.
     .-'                 HMMMMMMMMMMMR!.
    :                    `9MMMMMMMMMMM| -.
   .                       `*9MMMMMH##|   .
  -                          `(#MMH   `:,  .
 :           '|                 `HMb_>/"|\,.:
.'                                `"'#&b   - .
:                                      ?\oHH?.
:                                        !MMM&
:  .                                  .  HMMMM
/.      -                               -MMMMM
\`.                                      9MMMP
:. .  . -                                |MMM'
 \... '                                  .MMT
  &.                                    .dMP
   \,                                  .HM*
    \. `\.                            ,H&'
     `- `| -                        ,&':
       `.                         ,/\ '
          '-..                  _.-
              "---.._\o,oov+--'"
""",
"""
              _,d?,:?o?:?HM>#b\_
          ..H*"''`'H#*"**MMMMMM6$$v_
        v//"   - ``      `'#MMMMMMMMHo.
      /"`                   |MMMMMMMMMM:.
    ,>                       `HMMMMMMMMH:.
   :                           `#HMMMMHH\ -
  '                              `Z#MM,  `,:
 :               '\                 ?HH_>:`\,
:                                     "'*&| `:
.                                         <\Hb
:                                           MM
:                                        . iMM
Mb\.                                       {MM
::.`-       -                              !MP
`&.   .  .  -                              :M'
 9H,  \  '                                 |T
  HM?                                     ,P
   *ML                                   ??
    :&.   `o                           .d'
      ':  |T                          /"
        -.                         .<''
          `...                  ..-
              "`-=.,_,,,oov-~.-`
""",
"""
              _,oc>?_:b?o?HH#b\_
          .v/99*"*" '*H#""*HMMMMMZ,_
        oH* /"   -   '      "`#MMMMM#o.
     ./*>-                     `MMMMMMMb
    ,b/'                        `#MMMMMMM)
   :'                             ``HMMMMb:
  /-                                `|&MH `)
 /                   `-.               |Hb??)
,-  '                                    "`&,.
1                                           \}
!.                                           T
$,.                                        . 1
?`M??.                                       M
?.::| '\        -                            ?
 M?&.    .   .  -                           ,'
 9MMH\   ..  '           `                  .
  HMMM#.                                   :'
   9#MMb                                 ..
    -:"#     `b.                        .-
      . `    {!                        /
        -                           ,-'
          ' .                    .-
             ```^==\_.,,,ov--\-`
""",
"""
              _\o##??,:io??$#b\_
          .oH#"H9*""* "`#H*"*#MMMHo_
        oHMM- -'    -  ''     ``*HMMHo.
      dM#S>-`                     ?MMMM?.
    ,&&,/'                         "#MMMH)
   d?-"                              `*HMMb
  H?                                   "ZHb:
 /:                        \              H?L
|:|   .                                    `*:
:?:                                          )
>"                                           :
M|\,_                                        |
!|":HH?-'.                                   :
:^'_:?"\ `--         -                       .
- |ML?b      .   ..  -                       -
 :HMMMMH\    \               `              :
  >MMMMMM#.                                .
   ^M*HMMM|                               -
    `. `"#+     `?v                     .`
      .   `-    +?'                    -
       ` .                          ..'
           - .                   .-
              "`)b=p?.._\)vv---`
""",
"""
              _,o#bH\??::?o?cbo_
          .o#MH#**SH""' "`*H#"*#MHo_
        oHMMMH^  ^"    -  `      '*HHo.
     .dMMM#">>-                     `HM?.
    ,MH:R_o/                         `*MH)
   dMM' '                               "ML
  HMR! '                                 `#k
 d&'.                          -.          `L
:M ::     `                                 `-
/| !|                                        -
k.$-"                                        :
}9R:!,,_.                                    .
\::)':`*M#\-'.                               -
: "''..:"!`\  '-          -                  `
-   ,HMb.H|      .    _   -                 .'
 : ,MMMMMMMb.    ..                         .
  .`HMMMMMMMM?                             .
  `.`9M#*HMMMM                            :
    -.'   "##*      `b,                  .
      .      `     ,/'                 .'
       ` .                          ..'
           - .                  ..-
              "`*#d##c.._)v----`
""",
"""
              _,o#&oHb?\o::d?>\_
          .oHHMMM#**$M""` "`*HH"#&o_
        oHMMMMMMD' .''    -  '    ``bo.
     .dMMMMMH*'/|-                   `)b.
    ,MMMM?T|_o/                        `))
   dMMMMP  ''                            `|
  HMMMH& -                                `)
 /MH7' :                          --        :
-:MM  {.      .                              .
:i?' .!&                                     .
:{, o| '                                     :
-T?9M\:-'o,_                                 .
: \?::``"`?9MHo./..                          -
.  '"`'^ _.`"!"^.  `-         -              `
-      ,bMM?.M\       .    .  -      .      .'
 :   .oMMMMMMMMb.    ..   `                 .
  .  `HMMMMMMMMMMb                         -
   -   9MH*#HMMMMH                        .'
    '.  '   `"*##'      `b.              :
      .         `     .d''             .'
        -.                          . '
           -.                    .-`
              "`*##H###:._\--.-`
""",
"""
              _oo#H&d#b?)b:_>>\_
          .oHMMMMMMH*"*9R"'-``*#P\-_
        oHMMMMMMMMM$  ."       '   `^-
     .dMMMMMMMMH*",?-                 '\.
    ,MMMMMMM:?}.,d'                     `.
   dMMMMMMMH  /''                         :
  HMMMMMMM&' -                             -
 dPTMMP>' :                           -.    :
|? -MM}  .\                                  .
J' ::*'  -$L                                 .
:  ?b .,H- '                                 :
-  |6.&MP:: !.,_.                            -
:   `\:: "' "`:"MM#,-^,            -         :
-     ````:' _.:"?``\   `-                   .
:         .?bMML.]#        -   _  `      .  .'
 -      .o#MMMMMMMMH\     \.          .     .
  -     `HMMMMMMMMMMMH                     :
  `.     `HMM#*#MMMMMH'                   -
    -.     '    ``##*'      i+           :
      -            `'     v/'          .'
       `-                           ..'
          ' .                    .-
              "`*##HMH##:__,-.-`
""",
"""
              _oo##Mbb&bo??o_>\_
          .oHMMMMMMMMM**#?M*' "?*&..
        oHMMMMMMMMMMMM4  `"      -  `.
     .dMMMMMMMMMMMM#"\?.-              .
    ,MMMMMMMMMM}"9:_,d'                 -.
   dMMMMMMMMMMM|  ^''                     .
  &MMMMMMMMMMH\  -                         .
 :{M*"MMMPT"' :                         `-. :
.'M'  'MMM.  -T,       .                     .
- k   i:?''  -|&                             .
: `  -o&  .,H- "                             :
-     `M:`HMP|:'!.o._.                       .
:      "<:::'<^ '"``9MH#,-^ .                -
-         '*'``''._.`"?`^|   ^        -      :
:              ?#dMM_.M?       .   .  -    ..'
 :          ,ddMMMMMMMMMb.    ..   '        .
  .         TMMMMMMMMMMMMM,                :
   -         ?MMH**#MMMMMH'               :
    '.        '     "`##*'      &.       :
      -.               `'    ,~"       .'
        -.                          ..'
          ` .                    .-
             ```*##HMMMH#<:,..-`
""",
"""
              _,dd#HMb&dHo?\?:\_
          .oHMMMMMMMMMMMH***9P'`")v.
        oHMMMMMMMMMMMMMMM>  `'      -.
     .dMMMMMMMMMMMMMMMH*'|~-'          .
    ,MMMMMMMMMMMMM6>`H._,&              -.
   dMMMMMMMMMMMMMMM|  `"                  .
  H*MMMMMMMMMMMMMH&. -                     .
 d' HMM""&MMMPT'' :.                      `.-
,'  MP   `TMMM,   |:        .                -
|   #:    ? *"   : &L                        :
!   `'   /?H   ,#r `'                        :
.         ?M: HMM^<~->,o._                   :
:          `9:::'`*-``':`9MHb,|-,         '  :
.             `"'*':' :_ ""!"^.  `|          :
`.                 _dbHM6_|H.      .   . '  .'
 \              _odHMMMMMMMMH,    ..  `     :
 `-             |MMMMMMMMMMMMM|            :
  `.             9MMH**#MMMMMH'           :
    -.            '     "?##"      d     :
      .                    '    ,/"    .'
       `..                          ..'
          `  .                   .-
              '`"#HHMMMMM#<>..-`
""",
"""
              _oo##bHMb&d#bd,>\_
          .oHMMMMMMMMMMMMMM***9R"-..
        oHMMMMMMMMMMMMMMMMMH\  ?   `-.
     .dMMMMMMMMMMMMMMMMMMM#".}-'       .
    ,MMMMMMMMMMMMMMMMM6/`H _o}          -.
   dMMMMMMMMMMMMMMMMMMML  `''             .
  HbP*HMMMMMMMMMMMMMMM*: -                 ,
 dMH' `MMMP'"HMMMR'T"  :                    :
|H'   -MR'   `?MMMb    P,       .            .
1&     *|     |.`*"  .-`&|                   .
M'      "    |\&|  .,#~ "'                   :
T             :HL.|HMH\c~`|v,\_              :
|              `"|:::':`-`` '"MM#\-'.       -:
%                 ``'``'`' :_ '?'`| ``.      :
||,                     ,#dMM?.M?      .  .` -
 ?\                 .,odMMMMMMMMM?    \  `  :
  /                 |MMMMMMMMMMMMM:        .'
  `.                 TMMH#*9MMMMM*        :
    -.               `      "*#*'    ,:  .
      .                       `   .v'' .'
       `.                           ..'
          '- .                   .-
              "`\+HHMMMMMMHr~.-`
""",
"""
              _,,>#b&HMHd&&bb>\_
          _oHMMMMMMMMMMMMMMMMH**H:.
        oHMMMMMMMMMMMMMMMMMMMM#v`?  `.
     .dMMMMMMMMMMMMMMMMMMMMMMH*`+|     .
    ,MMMMMMMMMMMMMMMMMMMMMb|?+.,H       -.
   ddHMMMMMMMMMMMMMMMMMMMMMb  `'          .
  HMMkZ**HMMMMMMMMMMMMMMMMH\  -   .        :
 dTMMM*  `9MMMP'"*MMMMPT"` ..               :
|M6H''    4MP'   `"HMMM|   !|.      .        .
1MHp'      #L      $ *"'  .-:&.              .
MMM'        "     q:H.  .o#-``'              :
MM'                ?H?.|MMH::::-o,_.         -
M[                  `*?:::'|` `"`:9MH\~-.    `
&M.                     ""'`'^'.:.`?'`. '|  -:
`M|d,                       .dbHM[.1?     .. :
 9||| .                  _obMMMMMMMMH,   .  :
  H.^                    MMMMMMMMMMMM}     -
   \                     |MMH#*HMMMMH'    .'
    .                    `      `#*'   ,:-
     `                           '' .-'.
       `.                           .-
          '- .                   .-`
              '`)bqHMMMMMMHHb--`
""",
"""
              .,:,#&6dHHHb&##o\_
          .oHHMMMMMMMMMMMMMMMMMH*\,.
        oHMMMMMMMMMMMMMMMMMMMMMMHb:'-.
     .dMMMMMMMMMMMMMMMMMMMMMMMMMH|\/'  .
    ,&HMMMMMMMMMMMMMMMMMMMMMMM/"&.,d.   -.
   dboMMHMMMMMMMMMMMMMMMMMMMMMML `'       .
  HMHMMM$Z***MMMMMMMMMMMMMMMMMM|.-         .
 dMM}MMMM#'  `9MMMH?"`MMMMR'T'  _           :
|MMMbM#''     |MM"    ``MMMH.   <_           .
dMMMM#&        *&.     .?`*"   .'&:          .
MMMMMH-         `'    -v/H   .dD "'  '       :
MMMM*                  `*M: 4MM*::-!v,_      :
MMMM                     `*?::" "'``"?9Mb::. :
&MMM,                       `"'"'|"._ "?`| - :
`MMM}.H                          ,#dM[_H   ..:
 9MMi`M: .                   .ooHMMMMMMM,  ..
  9Mb `-                     1MMMMMMMMMM|  :
   ?M                        |MM#*#MMMM*  .
    -.                       `     |#"' ,'
      .                            -" v`
        -.                          .-
           - .                   . `
              '-*#d#HHMMMMHH#"-'
""",
"""
              _,<_:&S6dHHHb&bb\_
          .odHMMMMMMMMMMMMMMMMMMM}-_
       .oHMMMMMMMMMMMMMMMMMMMMMMMM#d:.
      ?9MMMMMMMMMMMMMMMMMMMMMMMMMMMH-$ .
    ,::dHMMMMMMMMMMMMMMMMMMMMMMMMH:\.?? -.
   dMdboHMMHMMMMMMMMMMMMMMMMMMMMMMH, '    .
  HMMMM7MMMb$R***MMMMMMMMMMMMMMMMMH\ -     .
 dMMMMM/MMMMM*   `$MMMM*'"*MMMM?&'  .       :
|MMMMMMb1H*'       HMP'    '9MMM|   &.    .  .
dMMMMMMM##~`       `#\      |.`*"  .-9.      :
9MMMMMMMM*           `     |v7?  .,H `' `    :
SMMMMMMH'                   '9M_-MMH::-)v_   :
:HMMMMM                       `\_:"'|'`':9Mv\.
-|MMMMM,                         ""`'`':.`?\ )
`:MMMMM}.d}                         .?bM6,|  |
 :?MMM6  M|  .                   .,oHMMMMM| /
  .?MMM- `'                      &MMMMMMMM|.
   -`HM-                         HMH#*MMM?:
    '.                           '   `#*:`
      -                              -'/
       ` .                          . '
          ` .                    . `
              '--##HH#HMMMHH#""`
""",
"""
              _o,d_?dZdoHHHb#b\_
          .vdMMMMMMMMMMMMMMMMMMMMH\.
       .,HHMMMMMMMMMMMMMMMMMMMMMMMMH&,.
      /?RMMMMMMMMMMMMMMMMMMMMMMMMMMMMH|..
    ,\?>`T#RMMMMMMMMMMMMMMMMMMMMMMMM6`\|/
   dMMbd#ooHMMMHMMMMMMMMMMMMMMMMMMMMMH,`' '
  HMMMMMMMTMMMMb$ZP**HMMMMMMMMMMMMMMMM|.   :
 dMMMMMMMM}$MMMMMH'   `HMMMH?"`MMMM?T' .    :
|MMMMMMMMMMoMH*''      `MM?    ``MMM|  +\    .
1MMMMMMMMMMMb#/         ?#?      |`#"  -T:   :
*'HMMMMMMMMMM*'           "     ~?&  .?} ' ' .
- 4MMMMMMMMP"                    `M? HMTc:)\.:
: `MMMMMMM[                       "#:::`>`"?M{
.  |MMMMMMH.                        ``'``'_`:-
-  |MMMMMMM|.dD                         ,#Mb)'
 :  *MMMMM: iM|  .                   _oHMMMM:
  .  ?MMMM'  "'                     ,MMMMMMP
   :  `HMH                          JM#*MMT
    -.  '                           `   #'
      .                                /
        -.            -              .'
           -.                    . `
              '--=&&MH##HMHH#"*"
""",
"""
              .-:?,Z?:&$dHH##b\_
           ,:bqRMMMMMMMMMMMMMMMMMHo.
        .?HHHMMMMMMMMMMMMMMMMMMMMMMMHo.
      -o/*M9MMMMMMMMMMMMMMMMMMMMMMMMMMMv
    .:H7b7'|?#HHMMMMMMMMMMMMMMMMMMMMMM6?Z)
   .?MMMHbdbbodMMMMHMMMMMMMMMMMMMMMMMMMM)':
  :MMMMMMMMMMM7MMMMb?6P**#MMMMMMMMMMMMMMM_ :
 \MMMMMMMMMMMMb^MMMMMM?   `*MMMM*"`MMMR<' . -
.1MMMMMMMMMMMMMb]M#""       9MR'   `?MMb  \. :
-MMMMMMMMMMMMMMMH##|`        *&.     |`*' .\ .
-?""*MMMMMMMMMMMMM'            '    |?b  ,}" :
:    MMMMMMMMMMH'                    `M_|M}r\?
.    `MMMMMMMMM'                      `$_:`'"H
-     TMMMMMMMM,                        '"``::
:     {MMMMMMMM| oH|                      .#M-
 :    `9MMMMMM' .MP   .                 ,oMMT
  .     HMMMMP'  `'                    ,MMMP
   -     `MMH'                         HH9*
    '.    `                           ` .'
      -                               . '
       ` .               -          .-
          ` .                    .-
              ' -==pHMMH##HH#"*"
""",
"""
              _..-:b&::&?&&##bo_
          ...?-#&9MMMMMMMMMMMMMMMHo_
       .. .1&#MMHMMMMMMMMMMMMMMMMMMMHo.
     .  .o/##R9MMMMMMMMMMMMMMMMMMMMMMMM?.
    .- |MSd?|'`$?#HMMMMMMMMMMMMMMMMMMMMMH)
   -  dMMMMHbd##oodMMMM#MMMMMMMMMMMMMMMMMH:
  - JMMMMMMMMMMMMM7HMMMH$SR***MMMMMMMMMMMMb>
 : {MMMMMMMMMMMMMMM`9MMMMMH'  ``HMMM?"*MM[| :
- |MMMMMMMMMMMMMMMMM<MH*''      `MM'   'HM? |.
: `MMMMMMMMMMMMMMMMMM##H-'       `#,  ` |`? /|
.  ?"*"?HMMMMMMMMMMMMMH'           "    v& .}?
-       |MMMMMMMMMMMP'                  `H:&H&
i       `9MMMMMMMMMT                     `|?"?
:         MMMMMMMMMH                       "`|
:         MMMMMMMMMH-.dH                    ,|
 :        ?MMMMMMM?  {M' .                .dT
  .        ?MMMMMR'  `'                  ,MP
   -        `HMM#'                      .&*
    '.        '                         `.
      -                               . '
       `..                          .-
           -.                    .-
              '-.==p##HMMHp&#"*"
""",
"""
              _v---:?&?:?&?&#b\_
          ..' i: #M$MMMMMMMMMMMMMHo_
       ..   -]M#HMHMMMMMMMMMMMMMMMMMHo.
     .     ooP*&6&MMMMMMMMMMMMMMMMMMMMM?.
    . -   &Rbbd-/`?:##HMMMMMMMMMMMMMMMMMH?
   -    ,HMMMMM#od#boodMMMMHMMMMMMMMMMMMMMb
  -   iMMMMMMMMMMMMMMM[*MMMH&$R***MMMMMMMMMb
 :   |MMMMMMMMMMMMMMMMML"MMMMMM'  ``MMMP"HMM:
.    HMMMMMMMMMMMMMMMMMMb/MH""      `MR   *M,|
:    TMMMMMMMMMMMMMMMMMMMMd#&`       `D.   ?|)
.     `*"'"*HMMMMMMMMMMMMMMP'          '  -d,J
:           |MMMMMMMMMMMMP'                ||M
M,           ?MMMMMMMMMM|                  `\?
&|            HMMMMMMMMM}                   ``
`L           .MMMMMMMMMMP ,d|                :
 *.           ?MMMMMMMF' .MP                /
  |            TMMMMMM'  `"'               /
  `.            `MMMP'                   ./
    -.           `                       .
      .                               . '
        - .                         .-
           -\                   ..-
              '-..=p####HMH&="*"
""",
"""
              _vo~^'':&b::d,#b)_
          ..`" `:v +9P]MMMMMMMMMMHo_
        ,-     ?Mb#MMMMMMMMMMMMMMMMMHo.
     . "     ,ooM*&&&HMMMMMMMMMMMMMMMMHb.
    .   -    99Soo?|'`*?##HMMMMMMMMMMMMMH)
   -       .HMMMMMM#od#boodMMMMHMMMMMMMMMMb
  -      :MMMMMMMMMMMMMMMM67HMMH&$R**HMMMMMb
 :      .MMMMMMMMMMMMMMMMMMM/HMMMMM|  `9MM'HL
:       {MMMMMMMMMMMMMMMMMMMM\MM*''    `H[ `9|
|       `HMMMMMMMMMMMMMMMMMMMMb##|      `F. :?
H        `"*"'"`#MMMMMMMMMMMMMMM?         '  k
M.               MMMMMMMMMMMMM"'             H
MMH.             `HMMMMMMMMMM:               |
&MM|              `MMMMMMMMMM,               -
`MM|              dMMMMMMMMMM|.oH            :
 9ML              `HMMMMMMM?  dH'           -
  Hi               |MMMMMMP   "'           .'
   T.               `MMM#'                -
    `.               `                  .`
     `                                 -
       `.. .                        ..'
           ...                   .-
              '-. //######M#b~""
""",
"""
              _ooq=""''$b$_&?b\_
          .-`^"  "'o |&M:MMMMMMMMHo_
        o/'      -$Mb#MMMMMMMMMMMMMMHo.
      /'        .ooHP*&R&MMMMMMMMMMMMMM?.
    .'          `MRbod?|'`+?##9MMMMMMMMMH)
  .`          .,MMMMMMH#od##obdMMMMHMMMMMMb
  -          ?MMMMMMMMMMMMMMMMM$HMMH$ZP*HMMb
 ?          |MMMMMMMMMMMMMMMMMMM|9MMMMP  "M6)
.-          dMMMMMMMMMMMMMMMMMMMMb]M*'    |R |
1|          `HMMMMMMMMMMMMMMMMMMMMMd#|     ?,:
MH,          ``*""'"*#MMMMMMMMMMMMMM*       '`
MM6_                 |MMMMMMMMMMMMH"         :
MMMMMb.               "MMMMMMMMMMT           -
&MMMMM'                |MMMMMMMMMH           `
!MMMMb                .HMMMMMMMMM+.?&        :
 TMMMM                 *MMMMMMMP  dH' .     :
  9MM'                 `MMMMMMP'  "'       .
   9ML                  `MMM#'            -
    `H                   `               :
     `\.                               .'
       `-\  .                       .-
          ' ._                   .-`
              '-\. ,b#####p&**^`
"""]

moon = [
["___---___", 9],
[".--         --.", 6],
["./   ()      .-. \.", 4],
["/   o    .   (   )  )", 3],
["/ .            '-'    )", 2],
["| ()    .  O         .  |", 1],
["|                         |", 0],
["|    o           ()       |", 0],
["|       .--.          O   |", 0],
["| .   |    |            |", 1],
["\    `.__.'    o   .  /", 2],
["\                   /", 3],
["`\  o    ()      /'", 4],
["`--___   ___--'", 6],
["---", 12]]


def win_graphics(stdscr, y, x, elap, min_h, min_w):
    """Draws the win graphics and elapsed time"""
    stars = [(3,17), (21,60), (18,80), (8,44), (35,11), (41,27)]
    day_counter = 24
    while True:
        for frame in range(0, 3*len(earth)):
            check_term_minsize(stdscr, min_h, min_w)
            stdscr.erase()
            #rotating Earth
            stdscr.addstr(y+8, x, earth[frame//3], curses.color_pair(3))

            #stars
            for s in range(0, len(stars)):
                stdscr.addstr(stars[s][0], stars[s][1], "*", curses.color_pair(5))

            #far Moon on the 13th day
            if day_counter == 12:
                stdscr.addstr(23, 75 - frame//6, "@", curses.color_pair(1))
            if day_counter == 13:
                stdscr.addstr(23, 60 - frame//6, "@", curses.color_pair(1))
            #near Moon on the 27th day
            for row in range(0, len(moon)):
                if day_counter == 26:
                    stdscr.addstr(5+row, 0 + frame//2 + moon[row][1], moon[row][0], curses.color_pair(1))
                if day_counter == 27 and frame <= 32:
                    stdscr.addstr(5+row, 45 + frame//2 + moon[row][1], moon[row][0], curses.color_pair(1))

            elap_str = "You won! Time elapsed: {} seconds".format(round(elap, 2))
            stdscr.addstr(30+y, x+47, elap_str, curses.color_pair(5))
            stdscr.addstr(31+y, x+47, "Press 'ctrl+C' to exit", curses.color_pair(1))
            stdscr.refresh()
            time.sleep(0.06)

        #moon orbits every 27 days
        day_counter += 1
        if day_counter > 27:
            day_counter = 0
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
                stdscr.addstr(offsy+i, offsx + num_offsx, shorter, curses.color_pair(5))
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
    print_big_number(stdscr, 23-len(guessed), 40, 73)
    stdscr.addstr(38, 73, "remaining:")
    stdscr.addstr(46,53,"Guess the periods:")
    stdscr.addstr(0, 28, "write 'quit' to exit", curses.color_pair(5))
    stdscr.refresh()

    starttime = time.time()

    #game loop, while guessed periods are fewer than 23
    while len(guessed) < 23:
        check_term_minsize(stdscr, min_h, min_w)

        try:
            #fetch a key and add it to "text"
            key = stdscr.getch()
            c = chr(key)
            if ("A" <= c <= "z") or c == " ":
                if len(text) <= 16:
                    text += c

            #if ENTER is pressed, check if "text" is either a correctly
            #spelled answer or "quit". Case insensitive
            elif key == curses.KEY_ENTER or key in [10,13]:
                if text.lower() == "quit":
                    stdscr.erase()
                    s = "EPOCH FAIL!"
                    stdscr.addstr(19, w//2-len(s)//2-1, s)
                    stdscr.refresh
                    stdscr.getch()
                    return
                i = 0
                #check if answer is correct, and add the graphics coordinates
                #and graphics elements to "gfx_add"
                while i < len(epoch_list):
                    if text.title() in epoch_list[i][0]:
                        gfx_add.append(epoch_list[i])
                        if i not in guessed:
                            guessed.append(i)
                    i += 1
                #either way, "text" will be reset when ENTER is pressed
                text = ""

            #if backspace is pressed, remove last character from "text"
            elif key == (curses.KEY_BACKSPACE or 127 or ord("\b")):
                if len(text) > 0:
                    text = text[:-1]
                    stdscr.erase()

            #redraw the screen
            stdscr.erase()
            draw_table(stdscr, 0, 0, gfx_add)
            stdscr.addstr(46,53,"Guess the periods:")
            stdscr.addstr(46,73,text)
            print_big_number(stdscr, 23-len(guessed), 40, 73)
            stdscr.addstr(38, 73, "remaining:")
            stdscr.addstr(0, 28, "write 'quit' to exit", curses.color_pair(5))
            stdscr.refresh()
        except:
            check_term_minsize(stdscr, min_h, min_w)

    #if you reach this point you've guessed 23 geological periods and won the game
    endtime = time.time()
    elap = endtime - starttime
    win_graphics(stdscr, 2,1, elap, min_h, min_w)


def draw_table(stdscr, y, x, gfx_add):
    """draws the game table and all periods that are already guessed"""
    for line in range(0, len(game_screen)):
        stdscr.addstr(line+y+1, x, game_screen[line])
    for entry in range(0, len(gfx_add)):
        for item in gfx_add[entry][1]:
            stdscr.addstr(item[0][0], item[0][1]-1, item[2], curses.color_pair(item[1]))

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
    min_h, min_w = 48, 90
    check_term_minsize(stdscr, min_h, min_w)

    try:
        draw_table(stdscr, 0, 0, [])
        quiz_loop(stdscr, min_h, min_w)
    except:
        return 1
    return 0

curses.wrapper(main)
