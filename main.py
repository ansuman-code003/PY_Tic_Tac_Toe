import pygame as pg

# pygame setup
pg.init()
screen = pg.display.set_mode((500,500))
surface_width = 100
surface_height = 100

game_font=pg.font.Font("Roboto-Light.ttf",68)

text_content = [
	"0",
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8"
]

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (255, 255, 0), (255, 165, 0), (255, 255, 255),
          (0, 255, 255), (128, 0, 128), (255, 192, 203)]

surfaces = []
texts = []

for txt in text_content:
    elem = game_font.render(txt,True,(55,215,168)) 
    texts.append(elem)
    
    
for color in colors:
    surface = pg.Surface((surface_width, surface_height))
    surface.fill(color)
    surfaces.append(surface)



clock = pg.time.Clock()
running = True

while running:
    # poll the events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    pg.display.set_caption("AI TIC-TAC-TOE")
    screen.fill("grey")
    
    # Rendering the game   
    # Render all surfaces
    for i in range(9):
        row = i // 3
        col = i % 3
        x = row * (surface_width + 10) + 100
        y = col * (surface_height + 10) + 80
        screen.blit(surfaces[i], (x,y))
        screen.blit(texts[i], (x+40,y+24)) 
       
    
   # flip() to update screen
    pg.display.flip()
    clock.tick(60)


pg.quit()



