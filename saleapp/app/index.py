import math
from flask import render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user, logout_user

from app.dao import get_user_by_id


@app.route("/")
def index():
    cates = dao.load_categories()
    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    page = request.args.get('page', 1)
    prods = dao.load_products(cate_id=cate_id, kw=kw, page=int(page)) # cách lấy dữ liệu phổ biến

    page_size = app.config.get('PAGE_SIZE', 8)
    total = dao.count_products()
    return render_template('index.html', categories=cates, products=prods, pages=math.ceil(total/page_size))

@app.route("/login", methods = ['get', 'post'])
def login_process():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        u = dao.auth_user(username=username, password=password)
        if u:
            login_user(u)
            return redirect('/') #dieu huong ve trang chu
    return render_template('login.html')

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

@app.route("/logout")
def logout_process():
    logout_user()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
