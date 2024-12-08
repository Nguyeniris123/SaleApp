import math
from flask import render_template, request, redirect, request_started
import dao
from app import app, login
from flask_login import login_user, logout_user
from app.models import UserRole

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

@app.route("/login-admin", methods=['post'])
def login_admin_process():
    username = request.form.get('username')
    password = request.form.get('password')
    u = dao.auth_user(username=username, password=password, role=UserRole.ADMIN)
    if u:
        login_user(u)
        return redirect('/admin')  # dieu huong ve trang chu


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

@app.route("/logout")
def logout_process():
    logout_user()
    return redirect('/login')

@app.route("/register", methods = ['get', 'post'])
def register_process():
    err_msg = None
    if request.method.__eq__('POST'):
        confirm = request.form.get('confirm')
        password = request.form.get('password')
        if password.__eq__(confirm):
            data = request.form.copy()
            del data['confirm']
            avatar = request.files.get('avatar')
            dao.add_user(avatar=avatar, **data) #deserializer
            return redirect('/login')
        else:
            err_msg = 'Mật khẩu không khớp!'
    return render_template('register.html', err_msg=err_msg)

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
