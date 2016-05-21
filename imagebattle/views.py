from flask import render_template
from imagebattle import app
from imagebattle.model import Image 
from random import sample

@app.route('/', methods=['GET'])
def index():
	images = Image.query.all()
	random_images = sample(list(images), 2)
	return render_template('index.html',left=random_images[0],right=random_images[1])

@app.route('/leading', methods=['GET'])
def leading():
    images = Image.query.all()
    return render_template('leading.html', battlers=images)