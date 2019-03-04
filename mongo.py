# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'person'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/person'

mongo = PyMongo(app)

@app.route('/person', methods=['GET'])
def get_all_personalities():
  person = mongo.db.person
  output = []
  for s in person.find():
    output.append({'first_name' : s['first_name'], 'last_name' : s['last_name'],'country' : s['country'],'company' : s['company']})
  return jsonify({'result' : output})

@app.route('/person/', methods=['GET'])
def get_one_person(first_name):
  person = mongo.db.person
  s = person.find_one({'first_name' : first_name})
  if s:
    output = {'first_name' : s['first_name'], 'last_name' : s['last_name'],'country' : s['country'],'company' : s['company']}
  else:
    output = "No such person exists in this database"
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)
