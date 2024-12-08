from app.models import Category, Product, User
from flask_admin import Admin
from app import app, db
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name='eCommerce Admin', template_mode='bootstrap4')


class CategoryView(ModelView):
    column_list = ['name', 'products']


class ProductView(ModelView):
    column_list = ['id', 'name', 'price']
    column_searchable_list = ['name']
    column_filters = ['id', 'name', 'price']
    column_editable_list = ['name']
    can_export = True


admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(ModelView(User, db.session))
