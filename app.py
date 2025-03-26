from flask import Flask, render_template, jsonify, send_file
import subprocess
import os
app = Flask(__name__)
def create_image():
    """Create an image with shapes using Pygame and save it to the static directory."""
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    screen.fill((255, 255, 255))  # Fill the screen with white
    pygame.draw.circle(screen, (255, 0, 0), (320, 240), 100)  # Red circle
    pygame.draw.rect(screen, (0, 255, 0), (50, 50, 100, 50))  # Green rectangle
    pygame.image.save(screen, 'static/image.png')


# Sample data with practical applications
data = {
    "epoxy": {
        "description": "Epoxy is a type of adhesive that is strong and sticky. Epoxy resin is made from a combination of epoxide compounds and hardeners.",
        "chemical_composition": "Typically involves bisphenol A and epichlorohydrin.",
        "image": "static/epoxy.png",
        "applications": {
            "1": "Bonding and sealing in construction.",
            "2": "Protective coatings for floors and surfaces.",
            "3": "Strong adhesives in automotive repairs.",
            "4": "Encapsulation of electronic components.",
            "5": "Composite materials for aerospace."
        }
    },
    "polyurethane": {
        "description": "Polyurethane foam is created by the reaction of polyols and diisocyanates.",
        "chemical_composition": "Involves a mix of polyols and isocyanates.",
        "image": "static/polyurethane.png",
        "applications": {
            "1": "Insulation panels for buildings.",
            "2": "Cushioning in furniture and mattresses.",
            "3": "Durable coatings for wooden surfaces.",
            "4": "Elastomers for wheels and industrial belts.",
            "5": "Thermal and acoustic insulation in vehicles."
        }
    }
}
elements_dict = {
    "Hydrogen": {
        "symbol": "H",
        "atomic_number": 1,
        "atomic_mass": 1.008,
        "atomic_weight": 1.008,
        "number_of_protons": 1,
        "number_of_neutrons": 0,
        "number_of_electrons": 1,
        "nuclear_density": 0.074,
        "number_of_quarks": 3,
        "electron_configuration": "1s¹"
    },
    "Helium": {
        "symbol": "He",
        "atomic_number": 2,
        "atomic_mass": 4.0026,
        "atomic_weight": 4.0026,
        "number_of_protons": 2,
        "number_of_neutrons": 2,
        "number_of_electrons": 2,
        "nuclear_density": 0.125,
        "number_of_quarks": 6,
        "electron_configuration": "1s²"
    },
    "Lithium": {
        "symbol": "Li",
        "atomic_number": 3,
        "atomic_mass": 6.94,
        "atomic_weight": 6.94,
        "number_of_protons": 3,
        "number_of_neutrons": 4,
        "number_of_electrons": 3,
        "nuclear_density": 0.53,
        "number_of_quarks": 9,
        "electron_configuration": "[He] 2s¹"
    },
    "Beryllium": {
        "symbol": "Be",
        "atomic_number": 4,
        "atomic_mass": 9.0122,
        "atomic_weight": 9.0122,
        "number_of_protons": 4,
        "number_of_neutrons": 5,
        "number_of_electrons": 4,
        "nuclear_density": 1.85,
        "number_of_quarks": 12,
        "electron_configuration": "[He] 2s²"
    },
    "Boron": {
        "symbol": "B",
        "atomic_number": 5,
        "atomic_mass": 10.81,
        "atomic_weight": 10.81,
        "number_of_protons": 5,
        "number_of_neutrons": 5,
        "number_of_electrons": 5,
        "nuclear_density": 2.34,
        "number_of_quarks": 15,
        "electron_configuration": "[He] 2s² 2p¹"
    },
    "Carbon": {
        "symbol": "C",
        "atomic_number": 6,
        "atomic_mass": 12.011,
        "atomic_weight": 12.011,
        "number_of_protons": 6,
        "number_of_neutrons": 6,
        "number_of_electrons": 6,
        "nuclear_density": 2.26,
        "number_of_quarks": 18,
        "electron_configuration": "[He] 2s² 2p²"
    },
    "Nitrogen": {
        "symbol": "N",
        "atomic_number": 7,
        "atomic_mass": 14.007,
        "atomic_weight": 14.007,
        "number_of_protons": 7,
        "number_of_neutrons": 7,
        "number_of_electrons": 7,
        "nuclear_density": 0.97,
        "number_of_quarks": 21,
        "electron_configuration": "[He] 2s² 2p³"
    },
    "Oxygen": {
        "symbol": "O",
        "atomic_number": 8,
        "atomic_mass": 15.999,
        "atomic_weight": 15.999,
        "number_of_protons": 8,
        "number_of_neutrons": 8,
        "number_of_electrons": 8,
        "nuclear_density": 0.83,
        "number_of_quarks": 24,
        "electron_configuration": "[He] 2s² 2p⁴"
    },
    "Fluorine": {
        "symbol": "F",
        "atomic_number": 9,
        "atomic_mass": 18.998,
        "atomic_weight": 18.998,
        "number_of_protons": 9,
        "number_of_neutrons": 10,
        "number_of_electrons": 9,
        "nuclear_density": 1.70,
        "number_of_quarks": 27,
        "electron_configuration": "[He] 2s² 2p⁵"
    },
    "Neon": {
        "symbol": "Ne",
        "atomic_number": 10,
        "atomic_mass": 20.180,
        "atomic_weight": 20.180,
        "number_of_protons": 10,
        "number_of_neutrons": 10,
        "number_of_electrons": 10,
        "nuclear_density": 0.90,
        "number_of_quarks": 30,
        "electron_configuration": "[He] 2s² 2p⁶"
    }
}
@app.route('/')
   def index():
       """Render the main page and generate the image."""
       subprocess.run(["python3", "image_generator.py"])  # Call the image generator script
       return render_template('template.html')  # Render the HTML template
   @app.route('/data/<material>')
   def get_data(material):
       """Return the specific material's data or an empty dictionary if not found."""
       return jsonify(data.get(material, {}))
   @app.route('/image')
   def image():
       """Serve the generated image."""
       return send_file('static/image.png')  # Return the generated image file
   if __name__ == '__main__':
       app.run(debug=True)