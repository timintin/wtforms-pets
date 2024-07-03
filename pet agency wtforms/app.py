from flask import Flask, render_template, redirect, url_for, flash
from models import db, Pet
from forms import AddPetForm, EditPetForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data,
            available=True
        )
        db.session.add(pet)
        db.session.commit()
        flash('Pet added successfully!')
        return redirect(url_for('home'))
    return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash('Pet updated successfully!')
        return redirect(url_for('home'))
    return render_template('edit_pet.html', form=form, pet=pet)

if __name__ == '__main__':
    app.run(debug=True)