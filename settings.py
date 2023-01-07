import pygame

WINDOW_NAME = "Catch Red envelope"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 700

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
RED_ENVELOPES_SIZES = (50, 38)
RED_ENVELOPE_SIZE_RANDOMIZE = (1,2) # for each new red_envelope, it will multiply the size with an random value beteewn X and Y
CAT_SIZES = (50, 50)
CAT_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
DRAW_HITBOX = False # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.08 # the frame of the insects will change every X sec

# difficulty
GAME_DURATION = 30 # the game will last X sec
RED_ENVELOPES_SPAWN_TIME = 1
RED_ENVELOPES_MOVE_SPEED = {"min": 1, "max": 5}
CAT_PENALITY = 2 # will remove X of the score of the player (if he kills a cat)

# colors
COLORS = {"title": (38, 61, 39), "score": (255, 2, 3), "timer": (255, 10, 39),
            "buttons": {"default": (255, 184, 0), "second":  (255, 184, 50),
                        "text": (255, 255, 255), "shadow": (255, 184, 50)}} # second is the color when the mouse is on the button

# sounds / music
MUSIC_VOLUME = 0.16 # value between 0 and 1
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
