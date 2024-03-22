from models import db, Pet

# Define the sample data using the name 'pet_list'
pet_list = [
    {"name": "Aspen", "species": "Cat", "age": 2, "available": True},
    {"name": "Wendy", "species": "Dog", "age": 13, "available": True},
    {"name": "J.Banana", "species": "Cat", "age": 10, "available": True}
]

def seed_database(app):
    with app.app_context():
        # Check if sample data exists
        if not Pet.query.first():
            # Loop through the 'pet_list' data and create Pet objects
            for pet_data in pet_list:
                pet = Pet(**pet_data)  # Use dictionary unpacking to create Pet object
                db.session.add(pet)  # Add each Pet object to the session
            db.session.commit()  # Commit all changes to the database

if __name__ == "__main__":
    seed_database(app)
