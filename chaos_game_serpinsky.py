import pygame
import random
import math

pygame.init()

# Set up the screen
width,height = 1000,800
screen = pygame.display.set_mode((width, height))

running = True

equi_side = 500

limit = 99999999999

def draw_equi(side):
    # Random starting point for the first vertex
    x1, y1 = random.randint(1, width), random.randint(1, height)
    
    # Random angle to determine the direction of the second vertex
    temp_angle = random.uniform(0, math.pi * 2)
    x2 = int(x1 + side * math.cos(temp_angle))
    y2 = int(y1 + side * math.sin(temp_angle))
    
    # Calculate the third vertex using a 60-degree (π/3 radians) offset
    x3 = int(x1 + side * math.cos(temp_angle + math.pi / 3))
    y3 = int(y1 + side * math.sin(temp_angle + math.pi / 3))
    
    # Ensure all points are within the screen boundaries
    if x1 > width or x2 > width or x3 > width or y1 > height or y2 > height or y3 > height or x1 < 0 or x2 < 0 or x3 < 0 or y1 < 0 or y2 < 0:
        return draw_equi(side)  # Retry if out of bounds by returning the recursive call
    else:
        return (x1, y1, x2, y2, x3, y3)  # Return the correct points

# Get the triangle vertices
def draw_triangle():
    
    x1, y1 = random.randint(1, width), random.randint(1, height)
    x2, y2 = random.randint(1, width), random.randint(1, height)
    x3, y3 = random.randint(1, width), random.randint(1, height)
    if x1 > width or x2 > width or x3 > width or y1 > height or y2 > height or y3 > height or x1 < 0 or x2 < 0 or x3 < 0 or y1 < 0 or y2 < 0:
        return draw_equi(side)  # Retry if out of bounds by returning the recursive call
    else:
        return (x1, y1, x2, y2, x3, y3)  # Return the correct points
    
x1, y1, x2, y2, x3, y3 = draw_equi(equi_side)
#x1, y1, x2, y2, x3, y3 = draw_triangle()



def random_point_in_triangle(x1, y1, x2, y2, x3, y3):
    # Generate two random numbers
    r1 = random.random()
    r2 = random.random()

    # Adjust to ensure the point is inside the triangle
    if r1 + r2 > 1:
        r1 = 1 - r1
        r2 = 1 - r2

    # Compute the random point using barycentric coordinates
    x = r1 * x1 + r2 * x2 + (1 - r1 - r2) * x3
    y = r1 * y1 + r2 * y2 + (1 - r1 - r2) * y3
    
    return (x, y)
iterations = 0

draw_mode = 1
# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # Clear the screen
    #screen.fill((0, 0, 0))
    if draw_mode == 1:
        random_pt = random_point_in_triangle(x1, y1, x2, y2, x3, y3)
        xt,yt = random.choice([(x1,y1),(x2,y2),(x3,y3)])
        x,y = random_pt
        random_pt = ((x + xt)/2 , (y + yt)/2)
        pygame.draw.circle(screen,(255,255,255),random_pt,1)
        # Draw the equilateral triangle
        '''pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 5)
        pygame.draw.line(screen, (255, 255, 255), (x2, y2), (x3, y3), 5)
        pygame.draw.line(screen, (255, 255, 255), (x3, y3), (x1, y1), 5)
        
        pygame.draw.circle(screen,(0,255,0),random_pt,5)'''
        iterations += 1
    if iterations%limit== 0:
        draw_mode *= -1
        iterations += 1
    pygame.display.flip()

pygame.quit()
