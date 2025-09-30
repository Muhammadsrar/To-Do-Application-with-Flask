import mongoengine as me

# Student Model
class Task(me.Document):
    name = me.StringField(required=True) 
    title = me.StringField(required=True,unique=True)   
    description = me.StringField(required=True)  
    category = me.StringField(required=True)
    deadline = me.DateTimeField(required=True)

    meta = {
        'indexes': [
            {'fields': ['name', 'title'], 'unique': True}  # compound unique index
        ]
    }