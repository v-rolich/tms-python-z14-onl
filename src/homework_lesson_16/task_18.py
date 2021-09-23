# 1.Написать сайт. Сайт предоставляет полный CRUD для работы с продуктами.
# Модель продукта состоит из id, name, price, amount, comment.
# На главной странице отображена краткая информация(id, name, price, amount) по всем продуктам.
# При нажатии на продукт происходит перенаправление на детализированную информацию по продукту.
# На детализированной странице продукта есть кнопки позволяющие отредактировать и удалить продукт.
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

DB_USER = 'postgres'
DB_PASSWORD = '2332'
DB_NAME = 'product_base.db'
DB_ECHO = True

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    comment = db.Column(db.Text)

    def __init__(self, name, price, amount, comment):
        self.name = name
        self.price = price
        self.amount = amount
        self.comment = comment

    def __repr__(self):
        return f"{self.name} Price:{self.price} Amount:{self.amount}"


if not database_exists(db.engine.url):
    create_database(db.engine.url)
db.create_all()
db.session.commit()


@app.route('/')
def index():
    item = Product.query.all()
    return render_template('home.html', data=item)


@app.route('/details/<int:id>', methods=['POST', 'GET'])
def details(id):
    item = Product.query.filter_by(id=id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.price = request.form['price']
        item.amount = request.form['amount']
        item.comment = request.form['comment']

        try:
            db.session.commit()
            return redirect('/')

        except ValueError:
            return 'Something wrong'
    else:
        return render_template('details.html', info=item)


@app.route('/add product', methods=['POST', 'GET'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        amount = request.form['amount']
        comment = request.form['comment']
        product = Product(name=name, price=price, amount=amount, comment=comment)
        try:
            db.session.add(product)
            db.session.commit()
            return redirect('/')
        except ValueError:
            return 'Error'

    else:
        return render_template('add product.html')


if __name__ == '__main__':
    app.run(debug=True)
