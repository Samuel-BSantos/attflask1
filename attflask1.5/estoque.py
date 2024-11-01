from flask import *
from cest import *

app = Flask(__name__)

est = []


@app.route('/')
def esto():
    return render_template('estoque.html', est=est)

@app.route('/index')
def menu():
    return render_template('index.html')


@app.route('/adicionar', methods=['POST']) 
def create():
    produto_atual = estoque()
    produto_atual.setNome(request.form['nome'])
    produto_atual.setQtd(request.form['qtd'])
    produto_atual.setPreco(request.form['preco'])
    produto_atual.setData(request.form['data'])
    produto_atual.setValidade(request.form['validade'])
    est.append(produto_atual)
    return redirect('/')

@app.route('/alterar', methods=['POST']) # Rota /alterar
def update():
    name = request.form['nome']
    new_qtd = request.form['new_qtd']
    new_price = request.form['new_price']
    new_date = request.form['new_date']
    new_vali = request.form['new_vali']
    for i in est:
        if i.getNome() == name:
            i.setQtd(new_qtd)
            i.setPreco(new_price)
            i.setData(new_date)
            i.setValidade(new_vali)
    return redirect('/')

@app.route('/apagar', methods=['POST']) # Rota /apagar
def delete():
    nome = request.form['nome']
    for i in est:
        if i.getNome() == nome:
            est.remove(i)
            return redirect('/')
    else:
        return "produto não encontrado"
if __name__ == '__main__':
    app.run(debug=True)