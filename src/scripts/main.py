#import flask modules
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

#import firebase modules
import firebase_admin
from firebase_admin import credentials, firestore

#import custom modules
from password_manager import passwordManager
from job_scraping import JobSearch

#==================================================================

#initialize API
app = Flask(__name__)
api = Api(app)

#initilialize firebase access
cred = credentials.Certificate('./src/scripts/dasig-10fad-firebase-adminsdk-n34bd-1d8d189d71.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

#encryption shts
salt = "jF4kT6m9sL2zA8qW15$#v3!p@9&r*"

#==================================================================
# Users Class that handles GET and POST requests
class Users(Resource):
    
    def get(self, email, password):
        users_ref = db.collection('Users')
        user = users_ref.where("email", "==", email).get()
        pmanager = passwordManager(salt)
        user_dict = user[0].to_dict();
        if pmanager.check_password(password, user_dict['password']):
            return user_dict , 200
        else:
            return "Invalid Credentials", 401
        
        
    
    def post(self, email, password):
        # parses the request
        users_ref = db.collection('Users')
        user = users_ref.where("email", "==", email).get()
        
        if len(user) > 0:
            return "User already exists", 400
        
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
            
        pmanager = passwordManager(salt)
            
        # encloses the data into a json/dict
        data = {
            'contact_number': args['contact_number'],
            'email': args['email'],
            'fields_of_work': fields_list,
            'first_name': args['first_name'],
            'last_name': args['last_name'],
            'location': args['location'],
            'middle_name': args['middle_name'],
            'password': pmanager.encrypt_password(str(args['password'])),
            'prefered_job_locations': pref_loc_list,
            'previous_positions': prev_pos_list,
            'sex': args['sex'],
            'skills': skills_list
        }
        
        users_ref = db.collection("Users")
        new_doc_ref = users_ref.document()
        
        new_doc_ref.set(data)
        return data , 201
    
# Jobs Class that handles GET requests
class Jobs (Resource):
    
    def get(self, search, limit):
        jobScraping = JobSearch()
        jobs_list = jobScraping.search(search, int(limit))
        return jobs_list, 200
    

    
# Add the resource to the api
api.add_resource(Users, '/users/<email>/<password>')
api.add_resource(Jobs, '/jobs/<search>/<limit>')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)