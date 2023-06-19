from flask_app import app
from flask import render_template, redirect, request, session


from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


@app.route('/')
def Home():

    all_dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = all_dojos)
    

@app.route('/dojos')
def ninja_form():
    
    all_dojos = Dojo.get_all()
    return render_template('add_ninja_form.html', all_dojos = all_dojos)


@app.route('/add_new_dojo', methods=['POST'])
def add_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/')




@app.route('/dojos/<int:id>')
def show_data(id):

    return render_template('ninjas.html', dojos = Dojo.get_one({'id' : id}), ninjas = Ninja.get_all({'id' : id}) )





