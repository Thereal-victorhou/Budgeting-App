from flask import Flask
from config import Config
from extensions import db, migrate, jwt, cors

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    # Register routes
    from routes.auth_routes import auth_bp
    from routes.account_routes import account_bp
    from routes.transaction_routes import transaction_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(account_bp, url_prefix='/accounts')
    app.register_blueprint(transaction_bp, url_prefix='/transactions')

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
