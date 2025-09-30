import mongoengine as me
from werkzeug.security import generate_password_hash, check_password_hash

class User(me.Document):
    username = me.StringField(required=True)
    email = me.StringField(required=True, )
    password_hash = me.StringField(required=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)