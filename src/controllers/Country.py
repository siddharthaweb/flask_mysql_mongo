# -*- coding: utf-8 -*-
from src import app
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

@app.route('/', methods=['GET', 'POST'])
def index():    
        #from src.models.Country import DataList
        #datalist = DataList()
        #print(datalist)
        return render_template('view/index.html')
        
