from flask import Flask, jsonify

app = Flask(__name__)

names = [ { 'name' : "Kalyan G",
             'Role' : "DevOps Engineer",
             'employeeid' : "1"
},
{ 'name' : "Ryan J",
             'Role' : "HR",
             'employeeid' : "2"
},
{ 'name' : "John C",
             'Role' : "DevOps Engineer",
             'employeeid' : "3"
},
{ 'name' : "Joe A",
             'Role' : "DevOps Engineer",
             'employeeid' : "4"
},
{ 'name' : "Sidhu G",
             'Role' : "DevOps Engineer",
             'employeeid' : "5"
}
]

@app.route('/')
def index():
    return "Welcome to the reading API"

@app.route("/names", methods = ['GET'])
def get():
    return jsonify({'names':names})

@app.route("/names", methods = ['POST'])
def create():
    name = { "name" : "Shiva ",
            "Role" : "Manager",
            'employeeid' : "6"
    }
    names.append(name)
    return jsonify({'Created': name})

@app.route("/names/<int:employeeid>", methods=['PUT'])
def names_update(employeeid):
    names[employeeid]['Role'] = 'Lead'
    return jsonify({'names': names[employeeid]})

@app.route("/names/<int:employeeid>", methods=['DELETE'])
def delete(employeeid):
    names.remove(names[employeeid])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run('0.0.0.0',5000,debug=True)