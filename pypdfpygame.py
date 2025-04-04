import pygame
import PyPDF2

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fun Polymers Display')

font = pygame.font.Font(None, 36)
bg_color = (255, 255, 255)  # white
text_color = (0, 100, 200)
formula_color = (0, 102, 204) # blue

def extract_pdf_text(pdf_path, num_pages):
    text_data = []
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for i in range(num_pages):
                page = reader.pages[i]
                text_data.append(page.extract_text())
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text_data

def draw_formulas(screen):
    pygame.draw.line(screen, formula_color, (300, 300), (500, 300), 5)
    pygame.draw.line(screen, formula_color, (400, 200), (400, 400), 5)

def display_text_and_graphics(text_data):
    running = True
    while running:
        screen.fill(bg_color)

        y_offset = 50
        for line in text_data[:5]:
            rendered_text = font.render(line, True, text_color)
            screen.blit(rendered_text, (50, y_offset))
            y_offset += 40
            if y_offset > 550:
                break
        draw_formulas(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()
# run the program
pdf_path = '/Users/amakki/Documents/Coding-Design'\
            '/GitHub/HTML-monomers/UNIT-II-Polymers.pdf'
text_data = extract_pdf_text(pdf_path, 6)
display_text_and_graphics(text_data)

