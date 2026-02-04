from mongoengine import connect, Document, StringField

connect(host = "mongodb://localhost:27017/my_database")

class User(Document):
    name = StringField(required = True)
    email = StringField(unique = True)

newUser = User(name = 'Virat', email = 'virat@india.com')
newUser.save()

for user in User.objects:
    print(f"Found user: {user.name}")