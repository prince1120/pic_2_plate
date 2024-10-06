# from flask import render_template ,url_for,flash,redirect,request
# from Foodimg2Ing import app
# from Foodimg2Ing.output import output
# import os


# @app.route('/',methods=['GET'])
# def home():
#     return render_template('home.html')

# @app.route('/about',methods=['GET'])
# def about():
#     return render_template('about.html')

# @app.route('/',methods=['POST','GET'])
# def predict():
#     imagefile=request.files['imagefile']
#     image_path=os.path.join(app.root_path,'static\\images\\demo_imgs',imagefile.filename)
#     imagefile.save(image_path)
#     img="/images/demo_imgs/"+imagefile.filename
#     title,ingredients,recipe = output(image_path)
#     return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)

# @app.route('/<samplefoodname>')
# def predictsample(samplefoodname):
#     imagefile=os.path.join(app.root_path,'static\\images',str(samplefoodname)+".jpg")
#     img="/images/"+str(samplefoodname)+".jpg"
#     title,ingredients,recipe = output(imagefile)
#     return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)


from flask import render_template, url_for, flash, redirect, request
from Foodimg2Ing import app
from Foodimg2Ing.output import output
import os

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/', methods=['POST'])
def predict():
    # Check if the 'imagefile' is part of the request
    if 'imagefile' not in request.files:
        flash('No file part')
        return redirect(request.url)

    imagefile = request.files['imagefile']

    # Check if the user actually selected a file
    if imagefile.filename == '':
        flash('No selected file')
        return redirect(request.url)

    # Create the path to save the image
    demo_imgs_path = os.path.join(app.root_path, 'static', 'images', 'demo_imgs')
    
    # Create the directory if it does not exist
    if not os.path.exists(demo_imgs_path):
        os.makedirs(demo_imgs_path)

    # Save the image file
    image_path = os.path.join(demo_imgs_path, imagefile.filename)
    imagefile.save(image_path)

    # Prepare the path for rendering the image in the template
    img = "/images/demo_imgs/" + imagefile.filename

    # Generate output using the image
    title, ingredients, recipe = output(image_path)

    return render_template('predict.html', title=title, ingredients=ingredients, recipe=recipe, img=img)

@app.route('/<samplefoodname>')
def predictsample(samplefoodname):
    imagefile = os.path.join(app.root_path, 'static', 'images', str(samplefoodname) + ".jpg")
    img = "/images/" + str(samplefoodname) + ".jpg"
    
    # Generate output using the sample image
    title, ingredients, recipe = output(imagefile)

    return render_template('predict.html', title=title, ingredients=ingredients, recipe=recipe, img=img)
