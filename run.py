from flask import Flask
from flask_cors import CORS,cross_origin
from app.epwm.routes import epwm
import os
app = Flask(__name__,static_folder='app/epwm/static')
CORS(app,resources={r'/recibe','/barchart','/linechart'})
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(epwm)
app.secret_key = 'S#perS3crEt_007'

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if __name__=='__main__':
  app.run(debug=True,port="5000",host="0.0.0.0")