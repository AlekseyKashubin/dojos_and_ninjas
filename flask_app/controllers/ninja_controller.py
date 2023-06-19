from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.ninja_model import Ninja


@app.route('/submit_ninja_form', methods=['POST'])
def submit_ninja_form():
    
    Ninja.add_ninja(request.form)
    dojo_id = request.form['dojo_id']

    return redirect(f'/dojos/{dojo_id}')





