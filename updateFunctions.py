from constants import *

def screenWrapEntity(position):
    newPosition = position
    if position.x < 0:
        newPosition.x = SCREEN_WIDTH
    if position.x > SCREEN_WIDTH:
        newPosition.x = 0
    if position.y < 0:
        newPosition.y = SCREEN_HEIGHT
    if position.y > SCREEN_HEIGHT:
        newPosition.y = 0
    return position