#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:21:13 2021

@author: hantswilliams
"""

from flask import Flask, request, render_template

import os
import openai
from dotenv import dotenv_values

os.chdir('/Users/hantswilliams/Documents/development/python_projects/openAI-exploration-flask')
config = dotenv_values("./.env") 
openapikey = config["apikey"]
openai.api_key = config["apikey"]



### Examples: use first paragraph: https://www.nytimes.com/2021/05/06/us/arizona-vote-count-republicans.html 


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    
    text_response = request.form['text']
    text_ending = "\n\ntl;dr:"
    response = openai.Completion.create(
    engine="davinci",
    prompt=text_response + text_ending,
    temperature=0,
    max_tokens=10,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n\n"])

    print(response)
    
    

    return response


