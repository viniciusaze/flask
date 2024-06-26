from flask import Flask

app = Flask(__name__)

# Testando rota
@app.route("/<int: numero>", methods=['GET','POST'])
def hello_world(numero):
    return f"Olá, mundo! {numero}"

if __name__ == "__main__":
    app.run(debug=True)