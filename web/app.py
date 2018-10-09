import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import sys
sys.path.insert(0, '../src')
from parser import readFiles
app = Flask(__name__)
filePath = os.path.join(app.root_path, 'files')


@app.route('/file/<filename>')
def file(filename):
    file = os.path.join(filePath, filename)
    readFiles([file])
    text = open(file +'.elem', 'r+')
    content = text.read()
    text.close()
    return render_template('file.html', text=content)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(filePath, filename))
      return redirect(url_for('file', filename = filename))

   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)

