# Configurations

LENGUAGES_PATH = "/home/mxbg/Activities/Sucrabble.activity/letters"
DICTIONARIES_PATH = "path_to_dictionaries_directory"
DEFAULT_LENGUAGE = "es"
DEFAULT_AMOUNT_LETTERS = 7
DEFAULT_BOARD_SIZE = 15


# Tile Constants
A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
H = 7
I = 8
J = 9
K = 10
L = 11
M = 12
N = 13
O = 14

TILE_LETTER          = 0
TILE_CENTER          = 5
TILE_NORMAL          = 1
TILE_DOUBLE_LETTER   = 2
TILE_TRIPLE_LETTER   = 3
TILE_DOUBLE_WORD     = 4
TILE_TRIPLE_WORD     = 6

LETTER_MODIFIERS     = [TILE_DOUBLE_LETTER, TILE_TRIPLE_LETTER]
WORD_MODIFIERS       = [TILE_DOUBLE_WORD, TILE_TRIPLE_WORD]
CENTER_MODIFIER      = [TILE_DOUBLE_LETTER]

TILE_COLORS = { 
                TILE_NORMAL            : "#FFFFFF", # White
                TILE_DOUBLE_LETTER     : "#CCCFFF", # Light Blue
                TILE_TRIPLE_LETTER     : "#3300CC", # Dark Blue
                TILE_DOUBLE_WORD       : "#FFCCFF", # Pink
                TILE_TRIPLE_WORD       : "#FF0300", # Red
                TILE_CENTER            : "#000000", # Black
                TILE_LETTER            : "#FFCC99"  # "Wood" 
               }

# Locations of special tiles 15X15 board
DOUBLE_LETTERS     = [(D,0), (L,0), (G,2), (I,2), (A,3), (H,3), (O,3), (G,6), (I,6), (C,6), (M,6), (D,7), (L,7), (C,8), (G,8), (I,8), (M,8), (A,11), (H,11), (O,11), (G,12), (I,12), (D,14), (L,14)]
TRIPLE_LETTERS     = [(F,1), (J,1), (B,5), (F,5), (J,5), (N,5), (B,9), (F,9), (J,9), (N,9), (F,13), (J,13)]
DOUBLE_WORDS       = [(B,1), (C,2), (D,3), (E,5), (K,4), (L,3), (M,2), (N,1), (B,13), (C,12), (D,11), (E,10), (K,10), (L,11), (M,12), (N,13)]
TRIPLE_WORDS       = [(A,0), (H,0), (O,0), (A,7), (O,7), (A,14), (H,14), (O,14)]
CENTER             = [(H, 7)]


