import pygame as pg

# Game variable setup
# O = 0 and X = 1
# Computer will play with O
# User will play with X
# Win=False 
turn = 1 # User plays first
win_combo = [
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,4,8],
    [2,4,6]
]


# pygame setup
pg.init()
screen = pg.display.set_mode((500, 500))
surface_width = 100
surface_height = 100

# dialog box setup
box_width = 400
box_height = 200
button_width = 100
button_height = 50
dialog_box_x = (screen.get_width() - box_width) // 2
dialog_box_y = (screen.get_height() - box_height) // 2



game_font = pg.font.Font("Roboto-Light.ttf", 68)

# Text content represents each cell in the grid (initially all '0')
text_content = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

color = (255,0,0)


surfaces = []
texts = []
rects = []

# Create text and surfaces
for txt in text_content:
    elem = game_font.render(txt, True, (55, 215, 168))
    texts.append(elem)

# Create colored surfaces and their corresponding rectangles
for x in range(9):
    surface = pg.Surface((surface_width, surface_height))
    surface.fill(color)
    surfaces.append(surface)

# Create a list of rectangles to track the positions of the surfaces
for i in range(9):
    row = i // 3
    col = i % 3
    x = row * (surface_width + 10) + 100
    y = col * (surface_height + 10) + 80
    rects.append(pg.Rect(x, y, surface_width, surface_height))

clock = pg.time.Clock()
running = True






def showEndDialogue(message):
    print(message)

def gameValidation(win_combo):
    for combo in win_combo:
        if text_content[combo[0]] == text_content[combo[1]] and text_content[combo[1]] == text_content[combo[2]] and text_content[combo[0]] == text_content[combo[2]]:
            tmp = text_content[combo[0]]
            if tmp == 'X':
                showEndDialogue("You Won!!!!!")
                return True
            elif tmp == 'O':
                showEndDialogue("AI Won!!!!!!")
                return True
            else:
                return False


while running:
    # Poll the events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Check if the click is inside any of the surfaces
            for i, rect in enumerate(rects):
                if rect.collidepoint(mouse_x, mouse_y):
                    if text_content[i] == ' ' and turn == 1:
                        text_content[i] = 'X'
                        turn = 0
                    elif text_content[i] == ' ' and turn == 0:
                        text_content[i] = 'O'
                        turn=1
                    break;

    pg.display.set_caption("AI TIC-TAC-TOE")
    screen.fill("grey")

    # Rendering the game   
    # Render all surfaces and texts
    for i in range(9):
        row = i // 3
        col = i % 3
        x = row * (surface_width + 10) + 100
        y = col * (surface_height + 10) + 80
        screen.blit(surfaces[i], (x, y))
        
        # Update the text rendering for each surface based on the text_content array
        texts[i] = game_font.render(text_content[i], True, (55, 215, 168))
        screen.blit(texts[i], (x + 40, y + 24))
    
    #Check for game winning situation
    if gameValidation(win_combo):
        break


    # Flip the display to update the screen
    pg.display.flip()
    clock.tick(60)

pg.quit()


