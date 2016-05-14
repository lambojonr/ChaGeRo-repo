from imagebattle import app

if __name__ == '__main__':
    app.run(debug=True)

from imagebattle import db 
db.create_all()