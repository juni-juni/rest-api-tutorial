from flask import Flask, jsonify, request
app = Flask(__name__)

#127.0.0.1:5000/
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit hi there"
    
@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    #Get x,y from the posted data
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    #Add z=x+y
    z = x+y
    #Prepare a JSON
    retJSON = {
        'z' : z
    }
    #return jsonify(map_prepared)
    return jsonify(retJSON), 200
@app.route('/bye')
def bye():
    age= 2* 14
    retJson = {
        'Name' : 'Juni-Juni',
        'Age' : age,
        'phones':[
            {
                'phone_type' : 'samsung s9',
                'phone_number' : 000000000
            },
            {
                'phone_type' : 'iphone',
                'phone_number' : 111111111
            }
        ]
    }
    return jsonify(retJson)

if __name__=='main':
    #app.run(host="127.0.0.1", port=80)
    app.run(debug=True)


"""
runing on terminal:

    export FLASK_APP=app.py
    flask run

"""
"""
Web service:
    return JSON
        ex)
            retJson = {
                'field' : 'abc'
                'field' : 'def'
            }
Web application:
    return page(index.html)
"""
