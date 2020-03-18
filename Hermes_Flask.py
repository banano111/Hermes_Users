from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")
    
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alta_user', methods=["GET", "POST"])
def altas():
    if request.method == "GET":
        return render_template('alta_user.html')        
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug = True, port=8000)

