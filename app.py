from flask import Flask, render_template,redirect,url_for,request
from hikaku import hikaku
app = Flask(__name__,static_folder='./templates/images')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shindan')
def shindan():
    return render_template('shindan.html')

@app.route('/result',methods=['POST'])
def result():
    a1=int(request.form['question1'])
    a2=int(request.form['question2'])
    a3=int(request.form['question3'])
    a4=int(request.form['question4'])
    a5=int(request.form['question5'])
    a6=int(request.form['question6'])
    a7=int(request.form['question7'])
    a8=int(request.form['question8'])
    a9=int(request.form['question9'])
    a10=int(request.form['question10'])
    l=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    k=[1,1,1,1,1,1,1,1,1,1]
    print(l)
    wariai=hikaku(l,k)
    return render_template('kekka.html',wariai=wariai)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')