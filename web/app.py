import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import sys
import wikipedia
sys.path.insert(0, '../src')
from parser import readFiles, wordToElements
from PeriodicTable import table
app = Flask(__name__)
filePath = os.path.join(app.root_path, 'files')

wikipedia.set_lang("pt")


def format_word(word):
    elements = word.split('-')
    wiki = zip (elements, map(lambda x: wikipedia.summary(table[x]["nome"] +' '+x ,sentences=1), elements))
    return render_template('word.html',
        word=''.join(elements).lower().title(),
        content=word,
        elements = wiki)


@app.route('/word/<word>', methods = ['GET'])
def word(word):
    return format_word(word)

@app.route('/word', methods = ['POST'])
def word_post():
    tableKeys = list(map(lambda x: x.lower(), table.keys()))
    word = request.form['word']
    print(word)
    word = wordToElements(word, tableKeys)

    return     format_word(word)

@app.route('/file/<filename>')
def file(filename):
    file = os.path.join(filePath, filename)
    readFiles([file])
    text = open(file +'.elem', 'r+')
    content = text.read().splitlines()
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
