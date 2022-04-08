from re import U
from flask import Flask,jsonify,request
app=Flask(__name__)
data=[
    {
        'id': 1,
        'name': 'Elizabeth',
        'contact': '0987654321',
        'done':False
    },
    {
        'id': 2,
        'name': 'William',
        'contact': '1234567890',
        'done':False
    }
]


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': data[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    data.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)


