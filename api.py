from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [ 
    { 
        'id': 1, 
        'Name': u'Corona Virus', 
        'Contact': u'108', 
        'done': False 
        }, 
    {   'id': 1, 
        'Name': u'Sars virus', 
        'Contact': u'911', 
        'done': False 
        } 
        ]
@app.route('/add-data', methods = ["POST"])
def add_task():
    if not request.json: 
        return jsonify({ "status":"error", "message": "Please provide the data!" },400)

    task = { 'id': tasks[-1]['id'] + 1, 
    'Name': request.json['Name'], 
    'Contact': request.json.get('Contact', ""), 
    'done': False }
    
    tasks.append(task)
    return jsonify({"status":"Success!", "message":"Task added Successfully."})

@app.route('/get-data')
def get_task():
    return jsonify({"data":tasks})

if(__name__ == "__main__"):
    app.run(debug = True)