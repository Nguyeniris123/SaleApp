from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    cates = dao.load_categories()
    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    pruds = dao.load_products(cate_id=cate_id, kw=kw) # cách lấy dữ liệu phổ biến
    return render_template('index.html', categories=cates, products=pruds)


if __name__ == '__main__':
    app.run(debug=True)
