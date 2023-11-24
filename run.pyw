import pygame
from pygame.locals import *
import math
from mousetracker import MouseTracker

from key_defs import *

mousetracker = MouseTracker()
mousetracker.start()

# Initialize pygame
pygame.init()

mouse_images = {
    "left": pygame.image.load('images/leftb.png'),
    "right": pygame.image.load('images/rightb.png'),
    "x1": pygame.image.load('images/m4b.png'),
    "x2": pygame.image.load('images/m5b.png'),
    "middle": pygame.image.load('images/sb.png'),
    "middleup": pygame.image.load('images/sub.png'),
    "middledown": pygame.image.load('images/sdb.png'),
}

pressed_mouse_images = {
    "left": pygame.image.load('images/leftbp.png'),
    "right": pygame.image.load('images/rightbp.png'),
    "x1": pygame.image.load('images/m4w.png'),
    "x2": pygame.image.load('images/m5w.png'),
    "middle": pygame.image.load('images/sw.png'),
    "middleup": pygame.image.load('images/suw.png'),
    "middledown": pygame.image.load('images/sdw.png'),
}

mouse_positions = {
    "left": (850, 25),
    "right": (913, 25),
    "x1": (859, 119),
    "x2": (856, 86),
    "middle": (907, 48),
    "middleup": (907, 48),
    "middledown": (907, 67),
}

# Load images
key_images = {
    'key': pygame.image.load('images/keyb.png'),
    'backslash': pygame.image.load('images/backslashb.png'),
    'alt': pygame.image.load('images/altb.png'),
    'tab': pygame.image.load('images/tabb.png'),
    'ctrl': pygame.image.load('images/tabb.png'),
    'back': pygame.image.load('images/backb.png'),
    'caps': pygame.image.load('images/capsb.png'),
    'shift': pygame.image.load('images/shiftb.png'),
    'rshift': pygame.image.load('images/rshiftb.png'),
    'space': pygame.image.load('images/spaceb.png'),
    'special': pygame.image.load('images/keyb.png'),
}

# Load images
pressed_key_images = {
    'key': pygame.image.load('images/keyw.png'),
    'backslash': pygame.image.load('images/backslashw.png'),
    'alt': pygame.image.load('images/altw.png'),
    'tab': pygame.image.load('images/tabw.png'),
    'ctrl': pygame.image.load('images/tabw.png'),
    'back': pygame.image.load('images/backw.png'),
    'caps': pygame.image.load('images/capsw.png'),
    'shift': pygame.image.load('images/shiftw.png'),
    'rshift': pygame.image.load('images/rshiftw.png'),
    'space': pygame.image.load('images/spacew.png'),
    'special': pygame.image.load('images/keyw.png'),
}

key_text_sizes = {
    'key': 24,
    'backslash': 24,
    'alt': 16,
    'tab': 24,
    'ctrl': 16,
    'back': 16,
    'caps': 16,
    'shift': 16,
    'rshift': 16,
    'space': 24,
    'special': 16,
}

image_text_centers = {
    'key': (20, 20),
    'backslash': (30, 20),
    'alt': (25, 20),
    'tab': (30, 20),
    'ctrl': (30, 20),
    'back': (40, 20),
    'caps': (40, 20),
    'shift': (50, 20),
    'rshift': (50, 20),
    'space': (120, 20),
    'special': (20, 20),
}

# Create screen
screen = pygame.display.set_mode((1000, 282))  # Adjust size as needed

# Define positions (simplified for this example)
key_positions = {
    'esc': (5, 5),   'F1': (80, 5), 'F2': (125, 5), 'F3': (170, 5), 'F4': (215, 5),   'F5': (290, 5), 'F6': (335, 5), 'F7': (380, 5), 'F8': (425, 5),   'F9': (500, 5), 'F10': (545, 5), 'F11': (590, 5), 'F12': (635, 5),     'print screen': (700, 5), 'scroll lock': (745, 5), 'pause break': (790, 5),                                 
    '`': (5, 55), '1': (50, 55), '2': (95, 55), '3': (140, 55), '4': (185, 55), '5': (230, 55), '6': (275, 55), '7': (320, 55), '8': (365, 55), '9': (410, 55), '0': (455, 55), '-': (500, 55), '=': (545, 55), "Back Space": (590, 55),      'insert': (700, 55), 'home': (745, 55), 'page up': (790, 55),
    
    'tab': (5, 100), 'q': (75, 100), 'w': (120, 100), 'e': (165, 100), 'r': (210, 100), 't': (255, 100), 'y': (300, 100), 'u': (345, 100), 'i': (390, 100), 'o': (435, 100), 'p': (480, 100), '[': (525, 100), ']': (570, 100), '\\': (615, 100),    'delete': (700, 100), 'end': (745, 100), 'page down': (790, 100),
    'Caps Lock': (5, 145), 'a': (84, 145), 's': (129, 145), 'd': (174, 145), 'f': (219, 145), 'g': (264, 145), 'h': (309, 145), 'j': (354, 145), 'k': (399, 145), 'l': (444, 145), ';': (489, 145), '"': (534, 145), 'Enter': (579, 145),

    'Shift (Left)': (5, 190), 'z': (106, 190), 'x': (151, 190), 'c': (196, 190), 'v': (241, 190), 'b': (286, 190), 'n': (331, 190), 'm': (376, 190), ',': (421, 190), '.': (466, 190), '/': (511, 190), 'Shift (Right)': (556, 190),                          'Up': (745, 190),
    'Ctrl (Left)': (5, 235), 'Win': (75, 235), 'Alt (Left)': (132, 235), 'Space': (189, 235), 'Alt (Right)': (435, 235), 'FN': (492, 235), 'Menu': (549, 235), 'Ctrl (Right)': (606, 235),                                                           'Left': (700, 235), 'Down': (745, 235), 'Right': (790, 235), 
}

# Define a function to determine key type
def determine_key_type(key):
    if key == "tab":
        return 'tab'
    elif key == "Ctrl (Left)" or key == "Ctrl (Right)":
        return "ctrl"
    elif key == "\\":
        return 'backslash'
    elif key == "Caps Lock":
        return "caps"
    elif key == "Back Space":
        return "back"
    elif key == "Win" or key == "Alt (Left)" or key == "Alt (Right)" or key == "FN" or key == "Menu":
        return "alt"
    elif key == "Shift (Left)" or key == "Enter":
        return "shift"
    elif key == "Shift (Right)":
        return "rshift"
    elif key == "Space":
        return "space"
    elif len(key) == 1:
        return 'key'
    return 'special'


def draw_text(screen, text, x, y, font, color=(255, 255, 255)):
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

def draw_multiline_text(screen, text, x, y, font, color=(255, 255, 255)):
    lines = text.split(' ')
    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        text_rect = line_surface.get_rect(center=(x, y + i * font.get_height()))
        screen.blit(line_surface, text_rect.topleft)


# Circle settings
circle_center = (913, 230)
circle_radius = 50
circle_width = 5
inner_circle_radius = 5

def draw_wedge(center, radius, dx, dy, color):
    angle = math.atan2(dy, dx)
    wedge_radius = math.sqrt(dx**2 + dy**2)
    wedge_radius = min(wedge_radius, radius)

    # Calculate the two endpoints by adjusting the angle slightly
    angle1 = angle - math.radians(5)  # Subtracting 5 degrees
    angle2 = angle + math.radians(5)  # Adding 5 degrees
    
    end_x1 = center[0] + wedge_radius * math.cos(angle1)
    end_y1 = center[1] + wedge_radius * math.sin(angle1)
    end_x2 = center[0] + wedge_radius * math.cos(angle2)
    end_y2 = center[1] + wedge_radius * math.sin(angle2)
    
    pygame.draw.polygon(screen, color, [center, (end_x1, end_y1), (end_x2, end_y2)])


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            break
    if running == False:
        break


    screen.fill((0, 255, 0))  # Fill screen with green

    # Draw keys
    for key, position in key_positions.items():
        key_type = determine_key_type(key)
        key_text_color = (255, 255, 255)
        if key != "FN" and is_key_pressed(key):
            key_text_color = (0, 0, 0)
            screen.blit(pressed_key_images[key_type], position)
        else:
            screen.blit(key_images[key_type], position)

        # Render text
        if key == "Lshift" or key == "Rshift":
            key = "shift"
        if key == "LAlt" or key == "RAlt":
            key = "alt"

        if " " in key:
            font = pygame.font.Font(None, key_text_sizes[key_type])
            draw_multiline_text(screen, key, position[0] + image_text_centers[key_type][0], position[1] + (image_text_centers[key_type][1] - 5), font, key_text_color)
        else:
            font = pygame.font.Font(None, key_text_sizes[key_type])
            draw_text(screen, key, position[0] + image_text_centers[key_type][0], position[1] + image_text_centers[key_type][1], font, key_text_color)

    # First, draw the default state for all buttons
    for mouse, position in mouse_positions.items():
        screen.blit(mouse_images[mouse], position)

    # Then, draw the pressed state for any pressed button
    for mouse, position in mouse_positions.items():
        if mousetracker.is_button_pressed(mouse):
            screen.blit(pressed_mouse_images[mouse], position)

    # Finally, handle the scroll count
    scroll_count = mousetracker.get_scroll_count()
    font = pygame.font.Font(None, 16)
    if scroll_count > 0:
        screen.blit(pressed_mouse_images["middleup"], mouse_positions["middleup"])
        draw_text(screen, str(abs(scroll_count)), mouse_positions["middleup"][0] + 6, mouse_positions["middleup"][1] + 10, font, (0, 0, 0))
    elif scroll_count < 0:
        screen.blit(pressed_mouse_images["middledown"], mouse_positions["middledown"])
        draw_text(screen, str(abs(scroll_count)), mouse_positions["middledown"][0] + 6, mouse_positions["middledown"][1] + 10, font, (0, 0, 0))
        
            

    
    # Draw the wedge inside the hollow circle
    (dx, dy) = mousetracker.get_deltas()
    dx, dy = dx / 15, dy / 15
    draw_wedge(circle_center, circle_radius, dx, dy, (200, 200, 200))

    # Draw hollow circle
    pygame.draw.circle(screen, (200, 200, 200), circle_center, circle_radius, circle_width)

    # Draw a smaller circle on the circumference of the hollow circle based on dx and dy
    angle = math.atan2(dy, dx)
    dot_x = circle_center[0] + (circle_radius * math.cos(angle))
    dot_y = circle_center[1] + (circle_radius * math.sin(angle))
    pygame.draw.circle(screen, (200, 200, 200), (int(dot_x), int(dot_y)), inner_circle_radius)

    pygame.display.flip()
    pygame.time.Clock().tick(144)  # Limit to 144 FPS


mousetracker.stop()
pygame.quit()
