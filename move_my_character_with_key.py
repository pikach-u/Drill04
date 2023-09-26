from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('player.png')

def handle_events():
    global running, dirX, dirY

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: #CLOSED WINDOW
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT: #directionX
                dirX += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_UP: #directionY
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_ESCAPE:  #ESC
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key == SDLK_LEFT:
                dirX += 1
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dirX = 0
dirY = 0

while running:

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if dirY == 0 and dirX == 0:
        character.clip_draw(frame * 48, 48 * 8, 48, 48, x, y, 150, 150)
    elif dirX < 0:
        character.clip_composite_draw(frame * 48, 48 * 5, 48, 48, 0, 'h', x, y, 150, 150)
    elif dirX > 0:
        character.clip_draw(frame * 48, 48 * 5, 48, 48, x, y,150,150)
    if dirY > 0:
        character.clip_draw(frame * 48, 48 * 4, 48, 48, x, y, 150, 150)
    elif dirY < 0:
        character.clip_draw(frame * 48, 48 * 6, 48, 48, x, y, 150, 150)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    x += dirX * 10
    y += dirY * 10
    if x > 1256:
        x = 1256
    elif x < 24:
        x = 24
    if y > 1020:
        y = 1020
    elif y < 60:
        y = 60
    delay(0.1)

close_canvas()



