from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images/uploads/'

app.secret_key = "yashashree"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/men')
def men():
    return render_template('men.html')


@app.route('/men1')
def men1():
    return render_template('men1.html')


@app.route('/women')
def women():
    return render_template('women.html')


@app.route('/women1')
def women1():
    return render_template('women1.html')


@app.route('/popup')
def popup():
    return render_template('popup.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload_image():
    if 'file1' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file1 = request.files['file1']
    if file1.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file1 and allowed_file(file1.filename):
        filename = secure_filename(file1.filename)
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('men1.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)


@app.route('/uploadwomen', methods=['POST', 'GET'])
def upload_image_women():
    if 'file2' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file2 = request.files['file2']
    if file2.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file2 and allowed_file(file2.filename):
        filename = secure_filename(file2.filename)
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('women.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='images/uploads/' + filename), code=301)


@app.route('/guidelines')
def guidelines():
    return render_template('guidelines.html')

if __name__ == "__main__":
    app.run(debug=True)
