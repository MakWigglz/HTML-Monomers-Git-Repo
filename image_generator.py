import pygame
   def create_image():
       width, height = 800, 600
       pygame.init()
       screen = pygame.display.set_mode((width, height))
       # Your drawing code here
       pygame.image.save(screen, "static/image.png")  # Save the image
       pygame.quit()