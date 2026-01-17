from flask import Flask
from database import db, init_db
from models import MedicinalPlant

def initialize_database():
    """Initialize database with medicinal plants data."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical_plants.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    init_db(app)
    
    with app.app_context():
        # Check if plants already exist
        if MedicinalPlant.query.first() is not None:
            print("Database already initialized with plant data.")
            return
        
        # Medicinal plants data
        plants_data = [
            {
                'common_name': 'Aloe Vera',
                'scientific_name': 'Aloe barbadensis miller',
                'description': 'Aloe Vera is a succulent plant with thick, fleshy leaves containing a clear gel. It has been used for centuries for its medicinal properties and is widely known for its skin healing benefits.',
                'medical_properties': [
                    'Anti-inflammatory',
                    'Wound healing',
                    'Digestive aid',
                    'Skin moisturizer',
                    'Antioxidant'
                ],
                'usage_instructions': {
                    'topical': 'Apply gel directly to skin burns, wounds, or dry skin',
                    'oral': 'Consume 1-2 tablespoons of aloe juice daily for digestive health',
                    'hair': 'Apply gel to scalp and hair for 30 minutes before washing'
                },
                'dosage': 'Topical: Apply as needed. Oral: 1-2 tablespoons of juice daily. Start with small amounts to test tolerance.',
                'warnings': [
                    'May cause allergic reactions in some people',
                    'Oral consumption may cause diarrhea or cramping',
                    'Not recommended during pregnancy',
                    'May interact with diabetes medications'
                ],
                'season': 'Year-round (grows in warm climates)',
                'regions': 'Tropical and subtropical regions worldwide'
            },
            {
                'common_name': 'Tulsi (Holy Basil)',
                'scientific_name': 'Ocimum sanctum',
                'description': 'Tulsi, also known as Holy Basil, is a sacred plant in Hindu tradition and a powerful adaptogen. It has been used in Ayurvedic medicine for thousands of years to promote overall health and well-being.',
                'medical_properties': [
                    'Immune system booster',
                    'Stress reliever',
                    'Respiratory health',
                    'Adaptogenic',
                    'Antibacterial'
                ],
                'usage_instructions': {
                    'tea': 'Steep 5-7 fresh leaves in hot water for 10 minutes',
                    'raw': 'Chew 2-3 fresh leaves daily on empty stomach',
                    'powder': 'Mix 1/2 teaspoon dried tulsi powder in warm water'
                },
                'dosage': 'Tea: 2-3 cups daily. Fresh leaves: 2-3 leaves daily. Powder: 1/2 teaspoon twice daily.',
                'warnings': [
                    'May affect blood clotting',
                    'May lower blood sugar levels',
                    'Not recommended during pregnancy',
                    'May interact with blood thinning medications'
                ],
                'season': 'Summer (monsoon in tropical regions)',
                'regions': 'Indian subcontinent, Southeast Asia'
            },
            {
                'common_name': 'Neem',
                'scientific_name': 'Azadirachta indica',
                'description': 'Neem is known as the "village pharmacy" in India due to its wide range of medicinal uses. Every part of the neem tree - leaves, bark, flowers, and seeds - has therapeutic properties.',
                'medical_properties': [
                    'Antibacterial',
                    'Antifungal',
                    'Skin disease treatment',
                    'Dental health',
                    'Blood purifier'
                ],
                'usage_instructions': {
                    'topical': 'Apply neem paste to affected skin areas',
                    'oral': 'Chew fresh leaves or consume neem juice',
                    'dental': 'Use neem twigs as natural toothbrush or neem-based toothpaste'
                },
                'dosage': 'Topical: Apply paste 2-3 times daily. Oral: 2-3 leaves or 1 tablespoon juice daily. Dental: Use neem products as directed.',
                'warnings': [
                    'Bitter taste may be unpleasant',
                    'May cause nausea if taken in large quantities',
                    'Not recommended for infants and young children',
                    'May affect fertility in high doses'
                ],
                'season': 'Year-round in tropical climates',
                'regions': 'Indian subcontinent, tropical Africa, Southeast Asia'
            },
            {
                'common_name': 'Turmeric',
                'scientific_name': 'Curcuma longa',
                'description': 'Turmeric is a golden-yellow spice derived from the rhizome of the Curcuma longa plant. It contains curcumin, a powerful anti-inflammatory compound used extensively in traditional medicine.',
                'medical_properties': [
                    'Anti-inflammatory',
                    'Antioxidant',
                    'Pain relief',
                    'Wound healing',
                    'Digestive aid'
                ],
                'usage_instructions': {
                    'oral': 'Mix 1/2 teaspoon turmeric powder in warm milk (golden milk)',
                    'topical': 'Make paste with water and apply to wounds or skin inflammations',
                    'cooking': 'Add to daily cooking for health benefits'
                },
                'dosage': 'Oral: 1/2 to 1 teaspoon daily with black pepper for better absorption. Topical: Apply paste as needed.',
                'warnings': [
                    'May increase bleeding risk',
                    'May worsen gallbladder problems',
                    'High doses may cause digestive upset',
                    'May interact with blood thinners'
                ],
                'season': 'Harvested in winter months',
                'regions': 'India, Southeast Asia, tropical regions'
            },
            {
                'common_name': 'Ginger',
                'scientific_name': 'Zingiber officinale',
                'description': 'Ginger is a flowering plant whose rhizome is widely used as a spice and traditional medicine. It has a distinctive spicy flavor and numerous health benefits, particularly for digestive issues.',
                'medical_properties': [
                    'Nausea relief',
                    'Digestive aid',
                    'Anti-inflammatory',
                    'Cold and flu relief',
                    'Pain relief'
                ],
                'usage_instructions': {
                    'tea': 'Steep fresh ginger slices in hot water for 10 minutes',
                    'raw': 'Chew small piece of fresh ginger',
                    'cooking': 'Add to meals for flavor and health benefits'
                },
                'dosage': 'Tea: 2-3 cups daily. Fresh: 1-2 grams daily. Powder: 1/4 to 1/2 teaspoon up to 3 times daily.',
                'warnings': [
                    'May increase bleeding risk',
                    'May cause heartburn in some people',
                    'Consult doctor if taking blood thinners',
                    'Large doses may interact with diabetes medications'
                ],
                'season': 'Year-round availability, harvested after 8-10 months',
                'regions': 'Tropical and subtropical regions worldwide'
            },
            {
                'common_name': 'Peppermint',
                'scientific_name': 'Mentha × piperita',
                'description': 'Peppermint is a hybrid mint plant with a refreshing aroma and cooling sensation. It has been used for centuries to treat digestive issues and is known for its menthol content.',
                'medical_properties': [
                    'Digestive relief',
                    'Headache relief',
                    'Respiratory support',
                    'Muscle pain relief',
                    'Mental clarity'
                ],
                'usage_instructions': {
                    'tea': 'Steep fresh or dried leaves in hot water for 5-10 minutes',
                    'oil': 'Apply diluted peppermint oil to temples for headaches',
                    'steam': 'Inhale peppermint steam for respiratory relief'
                },
                'dosage': 'Tea: 2-3 cups daily. Essential oil: 1-2 drops diluted in carrier oil. Avoid ingesting essential oil.',
                'warnings': [
                    'May worsen acid reflux in some people',
                    'Essential oil should be diluted before topical use',
                    'Not recommended for infants and young children',
                    'May interact with certain medications'
                ],
                'season': 'Summer months',
                'regions': 'Europe, North America, temperate regions'
            },
            {
                'common_name': 'Lavender',
                'scientific_name': 'Lavandula angustifolia',
                'description': 'Lavender is an aromatic flowering plant with purple blooms known for its calming properties. It has been used traditionally for relaxation, sleep improvement, and skin care.',
                'medical_properties': [
                    'Anxiety relief',
                    'Sleep aid',
                    'Skin healing',
                    'Pain relief',
                    'Antimicrobial'
                ],
                'usage_instructions': {
                    'aromatherapy': 'Use essential oil in diffuser or apply to pillow',
                    'tea': 'Steep dried lavender flowers in hot water',
                    'topical': 'Apply diluted oil to skin for burns or irritations'
                },
                'dosage': 'Tea: 1 cup before bedtime. Essential oil: 2-3 drops in diffuser. Topical: 1-2 drops diluted in carrier oil.',
                'warnings': [
                    'May cause drowsiness',
                    'Essential oil should be diluted before skin application',
                    'May cause allergic reactions in some people',
                    'Not recommended for young boys (hormonal effects)'
                ],
                'season': 'Summer months',
                'regions': 'Mediterranean, temperate climates worldwide'
            },
            {
                'common_name': 'Chamomile',
                'scientific_name': 'Matricaria chamomilla',
                'description': 'Chamomile is a daisy-like flowering plant traditionally used as a calming tea. It has mild sedative properties and is widely used for relaxation and digestive comfort.',
                'medical_properties': [
                    'Sleep aid',
                    'Digestive support',
                    'Anti-inflammatory',
                    'Anxiety relief',
                    'Skin soothing'
                ],
                'usage_instructions': {
                    'tea': 'Steep dried chamomile flowers in hot water for 5-10 minutes',
                    'topical': 'Apply cooled chamomile tea to skin irritations',
                    'compress': 'Use chamomile-soaked cloth as compress for inflammation'
                },
                'dosage': 'Tea: 1-4 cups daily, especially before bedtime. Topical: Apply as needed.',
                'warnings': [
                    'May cause allergic reactions in people allergic to ragweed',
                    'May interact with blood thinners',
                    'May cause drowsiness',
                    'Consult doctor if taking sedative medications'
                ],
                'season': 'Late spring to early summer',
                'regions': 'Europe, North America, temperate regions'
            }
        ]
        
        # Add plants to database
        for plant_data in plants_data:
            plant = MedicinalPlant(**plant_data)
            db.session.add(plant)
        
        db.session.commit()
        print(f"Successfully initialized database with {len(plants_data)} medicinal plants.")


if __name__ == '__main__':
    initialize_database()
