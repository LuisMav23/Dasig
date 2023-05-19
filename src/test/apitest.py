import requests

url = 'http://127.0.0.1:5000/users/lmlgabriel20321@plm.edu.ph/pogi123'
data = {
        'contact_number': '09334565717',
        'email': 'lmlgabriel20321@plm.edu.ph',
        'fields_of_work': 'Technology, Science',
        'first_name': 'Earl John',
        'last_name': 'Pulido',
        'location': 'Cavite City',
        'middle_name': 'Narvaza',
        'password': 'pogi123',
        'prefered_job_locations': 'Manila City, Cavite City',
        'previous_positions': 'Data Analyst, Data Scientist',
        'sex': 'Male',
        'skills': 'java, python'
}

headers = {'Content-Type': 'application/json'}
response = requests.get(url, headers=headers)
# response = requests.post(url, json=data, headers=headers)
print(response.text)
