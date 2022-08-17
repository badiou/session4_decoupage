from models import db,Etudiant,app
from flask_migrate import Migrate

migrate=Migrate(app,db)

@app.route('/')
def home():
    return 'Bonjour'


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)