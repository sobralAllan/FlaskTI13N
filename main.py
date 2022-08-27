from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)#Referência ao objeto FLASK, criando uma variável APP que guarda os elementos do Flask

@app.route("/")#Página Index - Primeira Página de Qualquer Site
def homepage():
    return render_template("index.html")

@app.route("/soma", methods=['POST','GET'])
def soma():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)


