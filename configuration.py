from app.routes.home import home_route
from app.routes.cliente import cliente_route
from app.database.database import db
from app.database.models.data_cliente import Cliente


def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(home_route)

    app.register_blueprint(cliente_route, url_prefix='/cliente')


def configure_db():
    db.connect()
    db.create_tables([Cliente])
