from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('app.config.Config')
    
    # Register Blueprints
    from app.api.routes import tasks
    app.register_blueprint(tasks, url_prefix='/api')
    
    return app
