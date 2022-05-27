from flask import request,render_template,jsonify,redirect,make_response,current_app
from app.epwm import epwm
from app.epwm.forms import UploadFile
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import os
from shutil import rmtree
import pandas as pd
import numpy as np
@epwm.get("/upload")
def upload():
  upload = UploadFile(request.form)
  return render_template('upload.html',form=upload)
  
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
        df.columns =['cadena', 'col1', 'col2', 'col3','col4','col5','col5']
        df.to_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'),index = False)
      else:
        print("no existe ya el charts")
        df=pd.read_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))  
        df = df.fillna(0)
        df.columns =['cadena', 'col1', 'col2', 'col3','col4','col5','col5']
        df.to_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'),index = False)
      res = make_response(jsonify({"message":"recibido"}),200)
    else:
      print("Creamos el archivo entrante ya que no existe")
      f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
      df=pd.read_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))   
      df = df.fillna(0)
      df.columns =['cadena', 'col1', 'col2', 'col3','col4','col5','col5']
      df.to_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'),index = False)
      res = make_response(jsonify({"message":"recibido"}),200)
  return res

@cross_origin
@epwm.get("/barchart")
def barchart():
  años=[]
  if(os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'))):
    dfn=pd.read_excel(os.path.join(current_app.config['UPLOAD_FOLDER'], 'charts.xlsx'))
    titulo=dfn.iloc[0]['cadena'].lstrip().rstrip()
    res = make_response(jsonify({
    "title":titulo,
    "anios":[50000,50000,150000,248000,792000]
    }),200)
  else:
    res = make_response(jsonify({
    "encabezado":"Sin datos",
    "title":"Sin datos"
    "anios":[50000,50000,150000,248000,792000]
    }),200)
  return res

@cross_origin
@epwm.get("/linechart")
def linechart():
  res = make_response(jsonify({
    "title":"Ingresos",
    "title2":"Gastos",
    "ingresos_anios":[0,50000,150000,248000,792000],
    "gasto_anios":[ '45,441.33',27330.00,94250.00,107300.00,117300.00]
    }),200)
  return res