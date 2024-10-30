import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = f"sqlite:///{(os.path.join(project_dir,"bookdatabase.db"))}"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =  database_file

db = SQLAlchemy(app)

class Book(db.model):
    title = db.Column(db.string(80), unique=True, nullable=False, primary_key=True)

    def _repr_(self):
        return f"<Title: {self.title}>"

@app.route('/', methods=["GET","POST"])
def home():
    books = None
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commmit()
        except Exception as e:
            print("Erro em registrar livro")
            print(e)
    books = Book.query.all()
    return render_template("index.html", books=books)

@app.route("/update", methods=["POST"])
def update():
    try:
        novotitulo = request.form.get("novotitulo")
        tituloantigo = request.form.get("tituloantigo")
        book = Book.query.filter_by(title=tituloantigo).first()
        book.title = novotitulo
        db.session.commit()
    except Exception as e:
        print("não pude atualzar o livro")
        print(e)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)