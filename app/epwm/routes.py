from flask import request,render_template,jsonify,redirect,make_response,current_app
from app.epwm import epwm
from app.epwm.forms import UploadFile
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import os
from shutil import rmtree
import pandas as pd
import numpy as np

@cross_origin
@epwm.post("/recibe")
def recibe():
  if not 'file'in request.files:
    print('no viene el archivo')
    res = make_response(jsonify({"message":"vacio"}),200)
  else:
    f=request.files['file']

    filename = secure_filename(f.filename)
    if(os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))):
      print("Borraremos el archivo entrante")
      os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
      print("Creamos el archivo entrante")
      f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
      
      if(os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'))):
        print("existe ya el charts")
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'))
        df=pd.read_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))  
        df = df.fillna(0)
        df.columns =['cadena', 'col1', 'col2', 'col3','col4','col5','col6']
        df.to_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'),index = False)
      else:
        print("no existe ya el charts")
        df=pd.read_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))  
        df = df.fillna(0)
        df.columns =['cadena', 'col1', 'col2', 'col3','col4','col5','col6']
        df.to_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'),index = False)
      res = make_response(jsonify({"message":"recibido"}),200)
    else:
      print("Creamos el archivo entrante ya que no existe")
      f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
      df=pd.read_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))   
      df = df.fillna(0)
      df.columns =['cadena', 'col1', 'col2', 'col3','col4','col5','col6']
      df.to_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'),index = False)
      res = make_response(jsonify({"message":"recibido"}),200)
  return res

@cross_origin
@epwm.get("/barchart")
def barchart():
  anio=[]
  scores=[]
  if(os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'))):
    dfn=pd.read_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'))
    titulo=dfn.iloc[0]['cadena'].lstrip().rstrip()
    
    
    if '*' in str(dfn.iloc[13]['col2']):
      uno = dfn.iloc[13]['col2']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col2'])

    if '*' in str(dfn.iloc[13]['col3']):
      uno = dfn.iloc[13]['col3']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col3'])

    if '*' in str(dfn.iloc[13]['col4']):
      uno = dfn.iloc[13]['col4']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col4'])

    if '*' in str(dfn.iloc[13]['col5']):
      uno = dfn.iloc[13]['col5']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col5'])

    if '*' in str(dfn.iloc[13]['col6']):
      uno = dfn.iloc[13]['col6']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(int(dfn.iloc[13]['col6']))
    anio.sort()
    
    scores.append(int(dfn.iloc[17]['col2'])*int(dfn.iloc[18]['col2']))
    scores.append(int(dfn.iloc[17]['col3'])*int(dfn.iloc[18]['col3']))
    scores.append(int(dfn.iloc[17]['col4'])*int(dfn.iloc[18]['col4']))
    scores.append(int(dfn.iloc[17]['col5'])*int(dfn.iloc[18]['col5']))
    scores.append(int(dfn.iloc[17]['col6'])*int(dfn.iloc[18]['col6']))

    print(scores)

    res = make_response(jsonify({
    "title":titulo,
    "anios":anio,
    "scores":scores
    }),200)
  else:
    res = make_response(jsonify({
    "encabezado":"Sin datos",
    "title":"Sin datos",
    "anios":"Sin datos"
    }),200)
  return res

@cross_origin
@epwm.get("/linechart")
def linechart():
  anio=[]
  scores=[]
  gastos=[]
  if(os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'))):
    dfn=pd.read_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'))
    titulo=dfn.iloc[0]['cadena'].lstrip().rstrip()

    if '*' in str(dfn.iloc[13]['col2']):
      uno = dfn.iloc[13]['col2']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col2'])

    if '*' in str(dfn.iloc[13]['col3']):
      uno = dfn.iloc[13]['col3']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col3'])

    if '*' in str(dfn.iloc[13]['col4']):
      uno = dfn.iloc[13]['col4']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col4'])

    if '*' in str(dfn.iloc[13]['col5']):
      uno = dfn.iloc[13]['col5']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col5'])

    if '*' in str(dfn.iloc[13]['col6']):
      uno = dfn.iloc[13]['col6']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(int(dfn.iloc[13]['col6']))
    anio.sort()
    
    scores.append(int(dfn.iloc[17]['col2'])*int(dfn.iloc[18]['col2']))
    scores.append(int(dfn.iloc[17]['col3'])*int(dfn.iloc[18]['col3']))
    scores.append(int(dfn.iloc[17]['col4'])*int(dfn.iloc[18]['col4']))
    scores.append(int(dfn.iloc[17]['col5'])*int(dfn.iloc[18]['col5']))
    scores.append(int(dfn.iloc[17]['col6'])*int(dfn.iloc[18]['col6']))
    
    gastos.append(float(dfn.iloc[30]['col2'])+float(dfn.iloc[31]['col2'])+float(dfn.iloc[32]['col2'])+float(dfn.iloc[33]['col2'])+float(dfn.iloc[34]['col2'])+float(dfn.iloc[35]['col2'])+float(dfn.iloc[36]['col2'])+float(dfn.iloc[37]['col2'])+float(dfn.iloc[38]['col2'])+float(dfn.iloc[39]['col2'])+float(dfn.iloc[40]['col2'])+float(dfn.iloc[41]['col2'])+float(dfn.iloc[42]['col2'])+float(dfn.iloc[43]['col2'])+float(dfn.iloc[44]['col2'])+float(dfn.iloc[45]['col2'])+float(dfn.iloc[46]['col2']))
    gastos.append(float(dfn.iloc[30]['col3'])+float(dfn.iloc[31]['col3'])+float(dfn.iloc[32]['col3'])+float(dfn.iloc[33]['col3'])+float(dfn.iloc[34]['col3'])+float(dfn.iloc[35]['col3'])+float(dfn.iloc[36]['col3'])+float(dfn.iloc[37]['col3'])+float(dfn.iloc[38]['col3'])+float(dfn.iloc[39]['col3'])+float(dfn.iloc[40]['col3'])+float(dfn.iloc[41]['col3'])+float(dfn.iloc[42]['col3'])+float(dfn.iloc[43]['col3'])+float(dfn.iloc[44]['col3'])+float(dfn.iloc[45]['col3'])+float(dfn.iloc[46]['col3']))
    gastos.append(float(dfn.iloc[30]['col4'])+float(dfn.iloc[31]['col4'])+float(dfn.iloc[32]['col4'])+float(dfn.iloc[33]['col4'])+float(dfn.iloc[34]['col4'])+float(dfn.iloc[35]['col4'])+float(dfn.iloc[36]['col4'])+float(dfn.iloc[37]['col4'])+float(dfn.iloc[38]['col4'])+float(dfn.iloc[39]['col4'])+float(dfn.iloc[40]['col4'])+float(dfn.iloc[41]['col4'])+float(dfn.iloc[42]['col4'])+float(dfn.iloc[43]['col4'])+float(dfn.iloc[44]['col4'])+float(dfn.iloc[45]['col4'])+float(dfn.iloc[46]['col4']))
    gastos.append(float(dfn.iloc[30]['col5'])+float(dfn.iloc[31]['col5'])+float(dfn.iloc[32]['col5'])+float(dfn.iloc[33]['col5'])+float(dfn.iloc[34]['col5'])+float(dfn.iloc[35]['col5'])+float(dfn.iloc[36]['col5'])+float(dfn.iloc[37]['col5'])+float(dfn.iloc[38]['col5'])+float(dfn.iloc[39]['col5'])+float(dfn.iloc[40]['col5'])+float(dfn.iloc[41]['col5'])+float(dfn.iloc[42]['col5'])+float(dfn.iloc[43]['col5'])+float(dfn.iloc[44]['col5'])+float(dfn.iloc[45]['col5'])+float(dfn.iloc[46]['col5']))
    gastos.append(float(dfn.iloc[30]['col6'])+float(dfn.iloc[31]['col6'])+float(dfn.iloc[32]['col6'])+float(dfn.iloc[33]['col6'])+float(dfn.iloc[34]['col6'])+float(dfn.iloc[35]['col6'])+float(dfn.iloc[36]['col6'])+float(dfn.iloc[37]['col6'])+float(dfn.iloc[38]['col6'])+float(dfn.iloc[39]['col6'])+float(dfn.iloc[40]['col6'])+float(dfn.iloc[41]['col6'])+float(dfn.iloc[42]['col6'])+float(dfn.iloc[43]['col6'])+float(dfn.iloc[44]['col6'])+float(dfn.iloc[45]['col6'])+float(dfn.iloc[46]['col6']))
    
    print(gastos)
    res = make_response(jsonify({
    "title":"Ingresos",
    "title2":"Gastos",
    "ingresos_anios":scores,
    "gasto_anios":gastos
    }),200)
  else:
    res = make_response(jsonify({
    "title":"Sin Datos",
    "title2":"Sin Datos",
    "ingresos_anios":"Sin Datos",
    "gasto_anios":"Sin Datos"
    }),200)
  return res

@cross_origin
@epwm.get("/doughnutchart")
def doughnutchart():
  anio=[]
  disponible=[]
  if(os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'))):
    dfn=pd.read_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'))
    titulo=dfn.iloc[0]['cadena'].lstrip().rstrip()
    
    if '*' in str(dfn.iloc[13]['col2']):
      uno = dfn.iloc[13]['col2']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col2'])

    if '*' in str(dfn.iloc[13]['col3']):
      uno = dfn.iloc[13]['col3']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col3'])

    if '*' in str(dfn.iloc[13]['col4']):
      uno = dfn.iloc[13]['col4']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col4'])

    if '*' in str(dfn.iloc[13]['col5']):
      uno = dfn.iloc[13]['col5']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(dfn.iloc[13]['col5'])

    if '*' in str(dfn.iloc[13]['col6']):
      uno = dfn.iloc[13]['col6']
      anio.append(int(uno.split('*')[0]))
    else:
      anio.append(int(dfn.iloc[13]['col6']))
    anio.sort()

    disponible.append(dfn.iloc[59]['col2'])
    disponible.append(dfn.iloc[59]['col3'])
    disponible.append(dfn.iloc[59]['col4'])
    disponible.append(dfn.iloc[59]['col5'])
    disponible.append(dfn.iloc[59]['col6'])

    res = make_response(jsonify({
    "labels":anio,
    "disponible":disponible
    }),200)
  else:
    res = make_response(jsonify({
    "labels":labels,
    "gasto_anios":"Sin Datos"
    }),200)
  return res