from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__, template_folder='template')
app.config['SECRET_KEY']= 'vanshika'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app) 

from routes import *

if __name__ == '__main__':
    app.run(debug=True)