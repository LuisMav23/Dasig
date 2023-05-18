import hashlib

class passwordManager():
    salt = ''
    
    def __init__(self, salt):
        self.salt = salt
    
    def encrypt_password(self, password):
        password += self.salt
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        # Return the hashed password as a string
        return hashed_password
    
    def check_password(self, password, hashed_password):
        password += self.salt
        password = hashlib.sha256(password.encode()).hexdigest()
        # Check if the provided password matches the hashed password
        return True if password == hashed_password else False