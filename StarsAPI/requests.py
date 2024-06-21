from flask import Flask, render_template, jsonify, request
from data import data

app = Flask(__name__)
@app.route('/')
def getStarData():
    return jsonify({
        'data': data,
        'message': 'success'
    })

@app.route('/stars')
def getStarDetails():
    star_name = requests.args.get('name')
    star_name = next(item for item in data if item['name'] == star_name)
    return jsonify({
        'data': star_name,
        'message': 'success'
    })