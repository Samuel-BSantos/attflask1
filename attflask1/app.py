from flask import *
from classe import *

app = Flask(__name__)

menu = []

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/criar', methods=['POST']) 
def create():
    comida_atual = prato()
    comida_atual.setNome(request.form['nome'])
    comida_atual.setPreco(request.form['preco'])
    comida_atual.setDesc(request.form['descricao'])
    menu.append(comida_atual)
    return redirect('/')

@app.route('/alterar', methods=['POST']) # Rota /alterar
def update():
    old_name = request.form['old_name']
    new_name = request.form['new_name']
    new_price = request.form['new_price']
    new_desc = request.form['new_desc']
    for i in menu:
        if i.getNome() == old_name:
            i.setNome(new_name)
            i.setPreco(new_price)
            i.setDesc(new_desc)
    return redirect('/')

@app.route('/apagar', methods=['POST']) # Rota /apagar
def delete():
    nome = request.form['nome']
    for i in menu:
        if i.getNome() == nome:
            menu.remove(i)
            return redirect('/')
    else:
        return "prato não encontrado"
if __name__ == '__main__':
    app.run(debug=True)