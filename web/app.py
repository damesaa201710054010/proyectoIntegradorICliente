from flask import Flask
from flask_cors import CORS
from datetime import date
from datetime import datetime
from flask import request, Response, jsonify, render_template
import requests

app = Flask(__name__, template_folder='templates')
CORS(app)

#participantes_List = [
#    {'cedula':1041151979, 'nombre':'Daniel', 
 #   'actividad':'Comercio', 'estrato':'2', 
 #   'foto':'https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwibq7n21cnkAhXFtVkKHb2YAPsQjRx6BAgBEAQ&url=https%3A%2F%2Fpixabay.com%2Fes%2Fimages%2Fsearch%2Fatardecer%2F&psig=AOvVaw3ZRGt6kL2hYLUASfsrhP7i&ust=1568322277268281'}
#]

actividades_List = ['Agricultura', 'Comercio',
'Investigación', 'Insumos', 'Transporte']

@app.route('/formulario', methods = ['GET'])
def formulario():
    return render_template('formulario.html', actividades = actividades_List)

@app.route('/guardarParticipante', methods = ['POST'])
def guardarParticipante():
    participantes = dict(request.values)
    participantes['cedula'] = int(participantes['cedula'])
    requests.post('https://api-evergreen-979.azurewebsites.net/mediciones/addValue', json = participantes)
    return (listar())

@app.route('/listar', methods = ['GET'])
def listar():
    participantes_List = requests.get('https://api-evergreen-979.azurewebsites.net/listarMediciones').json()
    return render_template('listar.html', list = participantes_List)
