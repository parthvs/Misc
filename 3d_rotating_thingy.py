import pygame
import math



print("PRESS Q ANYTIME TO EXIT\n")


choice = input("PRESS Y TO START")

pygame.init()

# Set up the screen
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))

running = True

side = 180
clock = pygame.time.Clock()

# Initial square vertices with z-coordinates, centered around (0, 0, 0)
square = [
    [-side, -side, 0],
    [side, -side, 0],
    [-side, side, 0],
    [side, side, 0]
]

# Function to draw a 3D square
def draw_3d_sq(square,color):
    projected_pts = []
    
    for point in square:
        x, y, z = point
        # Apply perspective scaling based on z-coordinate
        scale = 1 + z / side
        x_proj = x * scale + width // 2
        y_proj = y * scale + height // 2
        projected_pts.append((x_proj, y_proj))

    # Draw the square by connecting the points
    pygame.draw.line(screen, color, projected_pts[0], projected_pts[1], 3)
    pygame.draw.line(screen, color, projected_pts[1], projected_pts[3], 3)
    pygame.draw.line(screen, color, projected_pts[3], projected_pts[2], 3)
    pygame.draw.line(screen, color, projected_pts[2], projected_pts[0], )

# Function to rotate the square around the y-axis
def rotate_y(square, theta,color):
    rotated_square = []
    
    for point in square:
        x, y, z = point
        # Rotate around the y-axis
        x_new = x * math.cos(theta) - z * math.sin(theta)
        z_new = z * math.cos(theta) + x * math.sin(theta)
        rotated_square.append([x_new, y, z_new])
    draw_3d_sq(rotated_square,color)
    return rotated_square

theta = 0 # Rotation angle per frame (1 degree)

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Rotate the square around the y-axis
    square = rotate_y(square, theta,(255,255,255))
    # Draw the rotated 3D square
    angles = [
 
        (theta + math.pi / 18, (0, 255, 0)),
        (theta +2 * math.pi / 18, (0, 0, 255)),
        (theta +3 * math.pi / 18, (255, 255, 0)),
        (theta +4 * math.pi / 18, (255, 0, 255)),
        (theta +5 * math.pi / 18, (0, 255, 255)),
        (theta +6 * math.pi / 18, (128, 0, 0)),
        (theta +7 * math.pi / 18, (0, 128, 0)),
        (theta +8 * math.pi / 18, (0, 0, 128)),
        (theta +9 * math.pi / 18, (128, 128, 0)),
        (theta +10 * math.pi / 18, (128, 0, 128)),
        (theta +11 * math.pi / 18, (0, 128, 128)),
        (theta +12 * math.pi / 18, (192, 192, 192)),
        (theta +13 * math.pi / 18, (128, 128, 128)),
        (theta +14 * math.pi / 18, (255, 165, 0)),
        (theta +15 * math.pi / 18, (255, 192, 203)),
        (theta +16 * math.pi / 18, (255, 20, 147)),
        (theta +17 * math.pi / 18, (0, 255, 127)),
        (theta +18 * math.pi / 18, (255, 105, 180)),
        (theta +19 * math.pi / 18, (255, 140, 0)),
        (theta +20 * math.pi / 18, (50, 205, 50)),
        (theta +21 * math.pi / 18, (186, 85, 211)),
        (theta +22 * math.pi / 18, (147, 112, 219)),
        (theta +23 * math.pi / 18, (0, 139, 139)),
        (theta +24 * math.pi / 18, (255, 69, 0)),
        (theta +25 * math.pi / 18, (0, 191, 255)),
        (theta +26 * math.pi / 18, (255, 160, 122)),
        (theta +27 * math.pi / 18, (32, 178, 170)),
        (theta +28 * math.pi / 18, (135, 206, 250)),
        (theta +29 * math.pi / 18, (255, 215, 0)),
        (theta +30 * math.pi / 18, (64, 224, 208)),
        (theta +31 * math.pi / 18, (255, 228, 196)),
        (theta +32 * math.pi / 18, (70, 130, 180)),
        (theta +33 * math.pi / 18, (255, 240, 245)),
        (theta +34 * math.pi / 18, (240, 248, 255)),
        (theta +35 * math.pi / 18, (255, 240, 245))
    ]
    
    for angle, color in angles:
        temp_square = rotate_y(square, angle,color)

    # Update the display
    pygame.display.flip()
    clock.tick(60)
    theta += 0.001

pygame.quit()
