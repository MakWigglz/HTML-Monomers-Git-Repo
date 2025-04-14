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


def display_text_and_graphics(text_data):
    running = True
    while running:
        screen.fill(bg_color)
# run the program
pdf_path = '/Users/amakki/Documents/Coding-Design'\
            '/GitHub/HTML-monomers/UNIT-II-Polymers.pdf'
text_data = extract_pdf_text(pdf_path, 2)
display_text_and_graphics(text_data)

