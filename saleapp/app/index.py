import math
from flask import render_template, request
import dao
from app import app


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

@app.route("/login")
def login_process():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
