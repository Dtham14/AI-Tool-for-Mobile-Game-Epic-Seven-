from flask import Flask, render_template, send_file, request, jsonify
import json
import pandas as pd
from model import getModel
from draft_logic import draft_response

app = Flask(__name__)
# model = getModel()
# python app.py

@app.route('/')
def homepage():
    with open('e7_data/herocodes.json', 'r') as file:
        data = json.load(file)
    return render_template('homepage.html', hero_list =data)

@app.route('/image')
def get_vs():
    filename = 'VS.png'  # Name of the image file
    return send_file('images/' + filename)
 
@app.route('/updateDraftPick', methods=['POST'])
def updateDraftPick():
    data = request.json  # Read JSON data sent from client
    # Process the data here
    # print(data)
    draft_list = list(data.values())
        
    print(draft_list)
        
    res = draft_response(draft_list[0], draft_list[1], draft_list[2], draft_list[3], draft_list[4],
                   draft_list[5], draft_list[6], draft_list[7], draft_list[8], draft_list[9],
                   draft_list[10], draft_list[11], draft_list[12], draft_list[13])    

    draft_response_vals = res 
    print(res)
    return draft_response_vals

@app.route('/calculateWin', methods=['POST'])
def calculateWin():
    data = request.json  # Read JSON data sent from client
    # Process the data here
    draft_list = list(data.values()) 
    
    print(draft_list)
    pred = getModel(draft_list)
    print(pred[0])
    return {'res':int(pred[0])}

if __name__ == '__main__':
    app.run()