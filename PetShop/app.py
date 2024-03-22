from flask import Flask, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from form import AddPetForm, EditPetForm

# Create the Flask app instance
app = Flask(__name__)

# Configure Flask app and SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "yobananaboy"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Initialize SQLAlchemy and connect to the app
connect_db(app)

# Enable Flask Debug Toolbar
debug = DebugToolbarExtension(app)

@app.route('/', methods=["GET", 'POST'])
def home():
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo.data,
            age=form.age.data,
            notes=form.notes.data
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('home'))  # Updated redirection to stay on the same page (home) on successful form submission
    pets = Pet.query.all()
    return render_template('adopt_home.html', pets=pets, form=form)


@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        # Handle form submission
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo.data,
            age=form.age.data,
            notes=form.notes.data
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('home'))  # Redirect to home page if form is valid
    # If form is not valid or it's a GET request, render the add_pet.html template
    return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>')
def pet_details(pet_id):
    # Fetch the pet details based on the pet_id
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)

@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def pet_details_edit(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)  # Load existing pet data into the form

    if form.validate_on_submit():
        # Update the pet details based on form data
        pet.name = form.name.data
        pet.age = form.age.data
        pet.species = form.species.data
        pet.notes = form.notes.data

        db.session.commit()  # Commit the changes to the database
        return redirect(url_for('pet_details', pet_id=pet_id))  # Redirect to pet details page

    return render_template('pet_details_edit.html', pet=pet, form=form)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
