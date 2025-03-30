import pygame
from math import sqrt
def main():

    # initializing
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    baseLayer = pygame.Surface((640, 480))
    clock = pygame.time.Clock()

    # main coordinates
    prevX = 0
    prevY = 0

    # support coordinates
    prevX1 = -1
    prevY1 = -1
    currentX1 = -1
    currentY1 = -1

    color = (255, 255, 255)
    screen.fill((0, 0, 0))
    isMouseDown = False

    while True:

        pressed = pygame.key.get_pressed() # very important parameter
        currentX = prevX
        currentY = prevY
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN: # if lmb is currently pressed
                if event.button == 1: 
                    isMouseDown = True
            if event.type == pygame.MOUSEBUTTONUP: # if lmb is currently not pressed
                if event.button == 1:
                    isMouseDown = False
            if event.type == pygame.MOUSEMOTION: # if mouse is doing something
                currentX = event.pos[0]
                currentY = event.pos[1]
            
            if event.type == pygame.MOUSEBUTTONDOWN: # if lmb is currently pressed (for figure drawing)
                if event.button == 1:
                    isMouseDown = True  
                    currentX1 = event.pos[0]
                    currentY1 = event.pos[1]
                    prevX1 = event.pos[0]
                    prevY1 = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))
            if event.type == pygame.MOUSEMOTION: 
                if isMouseDown:
                    currentX1 =  event.pos[0]
                    currentY1 =  event.pos[1]
            if event.type == pygame.KEYDOWN: # colors
                if event.key == pygame.K_r: # red
                    color = (255, 0, 0)
                elif event.key == pygame.K_g: # green
                    color = (0, 255, 0)
                elif event.key == pygame.K_b: # blue
                    color = (0, 0, 255)
                elif event.key == pygame.K_w: # white
                    color = (255, 255, 255)
        if isMouseDown:
            pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))
        
        if pressed[pygame.K_1]: # rectangle
         if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
            screen.blit(baseLayer, (0, 0))
            r = calculateRect(prevX1, prevY1, currentX1, currentY1)
            pygame.draw.rect(screen, color, pygame.Rect(r), 1)
        if pressed[pygame.K_2]: # circle
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1: 
                screen.blit(baseLayer, (0, 0))
                c = centerCirc(prevX1, prevY1, currentX1, currentY1) 
                ra = radiusCirc(prevX1, prevY1, currentX1, currentY1) 
                pygame.draw.circle(screen, color, c, ra, 1)
        if pressed[pygame.K_3]: # eraser
            if isMouseDown:
                pygame.draw.line(screen, (0, 0, 0), (prevX, prevY), (currentX, currentY), 20)
        if pressed[pygame.K_4]: # square
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                square = calculatesquare(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.rect(screen, color,pygame.Rect(square), 1)
        if pressed[pygame.K_5]: # ravnostoronnii treugolnik
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                triangle = equilateraltriangle(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color,triangle, 1)
        if pressed[pygame.K_6]: # right triangle
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                rtriangle = calculateRtriangle(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color,rtriangle, 1)
        if pressed[pygame.K_7]: # rombik
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                romb = calcRomb(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color,romb, 1)

        
        prevX = currentX
        prevY = currentY

        pygame.display.flip()
        clock.tick(60)

def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
def centerCirc(x1, y1, x2, y2): 
    return abs(x1 - x2) / 2 + min(x1, x2), abs(y1 - y2) / 2 + min(y1, y2)
def radiusCirc(x1, y1, x2, y2): 
    return sqrt((((abs(x1 - x2) / 2) ** 2) + (abs(y1 - y2) / 2) ** 2))
def calculatesquare(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    return min(x1,x2),min(y1,y2),a,a
def calculateRtriangle(x1, y1, x2, y2): 
    return [(min(x1, x2), min(y1, y2)), (min(x1, x2), abs(y1 - y2) + min(y1, y2)), (abs(x1 - x2) + min(x1, x2), abs(y1 - y2) + min(y1, y2))]
def equilateraltriangle(x1, y1, x2, y2):
    side = min(abs(x2-x1), abs(y2-y1))
    height = round(side * 0.866) 
    x = 1
    y = 1
    if (x2 > x1):
        x = -1
    if (y2 > y1):
        y = -1
    pnt1 = (x2 + round(side/2)*x, y2)
    pnt2 = (x2, y2 + height*y)
    pnt3 = (x2 + side*x, y2 + height*y)
    return (pnt1, pnt2, pnt3)
def calcRomb(x1, y1, x2, y2):
    a, b = abs(x2-x1),abs(y2-y1)
    return (x1,y1+b),(x1+a,y1),(x1,y1-b),(x1-a,y1)

main()

'''
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
'''
        