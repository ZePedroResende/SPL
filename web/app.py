import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)
filePath = os.path.join(app.root_path, 'files')


@app.route('/file')
def file(filename):
    print(file_Path)
    text = open(os.path.join(filePath, f.filename), 'r+')
    content = text.read()
    text.close()
    return render_template('file.html', text=content)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(filePath, f.filename))
      redirect(url_for('file', filename = f.filename))

   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)

