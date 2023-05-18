from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
api = Api(app)

cred = credentials.Certificate('./src/dasig-10fad-firebase-adminsdk-n34bd-1d8d189d71.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Users Class that handles GET and POST requests for the users endpoint
class Users(Resource):
    
    def get(self):
        data = []
        users_ref = db.collection('User')
        docs = users_ref.get()
        for doc in docs:
            data.append(doc.to_dict())
        return jsonify(data), 200
    
    def post(self):
        # parses the request
        parser = reqparse.RequestParser()
        parser.add_argument('contact_number', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('fields_of_work', required=True)
        parser.add_argument('first_name', required=True)
        parser.add_argument('last_name', required=True)
        parser.add_argument('location', required=True)
        parser.add_argument('middle_name', required=True)
        parser.add_argument('password', required=True)
        parser.add_argument('prefered_job_locations', required=True)
        parser.add_argument('previous_positions', required=True)
        parser.add_argument('sex', required=True)
        parser.add_argument('skills', required=True)
        args = parser.parse_args()
        
        fields_list = []
        for field in args['fields_of_work'].split(','):
            fields_list.append(field.strip())
        
        pref_loc_list = []
        for loc in args['prefered_job_locations'].split(','):
            pref_loc_list.append(loc.strip())
            
        prev_pos_list = []
        for pos in args['previous_positions'].split(','):
            prev_pos_list.append(pos.strip())
            
        skills_list = []
        for skill in args['skills'].split(','):
            skills_list.append(skill.strip())
            
        # encloses the data into a json/dict
        data = {
            'contact_number': args['contact_number'],
            'email': args['email'],
            'fields_of_work': fields_list,
            'first_name': args['first_name'],
            'last_name': args['last_name'],
            'location': args['location'],
            'middle_name': args['middle_name'],
            'password': args['password'],
            'prefered_job_locations': pref_loc_list,
            'previous_positions': prev_pos_list,
            'sex': args['sex'],
            'skills': skills_list
        }
        
        users_ref = db.collection("Users")
        new_doc_ref = users_ref.document()
        
        new_doc_ref.set(data)
        return data , 201
    
class FieldsOfWork(Resource):
    
    def get(this):
        data = []
        
    
# Add the resource to the api
api.add_resource(Users, '/users/')
api.add_resource(FieldsOfWork, '/field_of_work/')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)