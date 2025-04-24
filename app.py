from flask import Flask, request , render_template
import os
from.parser.parse_resume import parse_and_score
UPLOAD_FOLDER='uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(_name_)
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        file=request.files['resume']

        if file and file.file.name:
            file_path=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file.path)

            score, feedback = parse_and_score(file_path)

            return render_template('index.html')
if _name_=='_main_':
    app.run(debug=True)
