from flask import Flask
import os 

def create_app():
    app = Flask(__name__)
    # Esto indica a Flask que también busque plantillas en la carpeta 'base_templates'
    app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'base_templates'))
    # Registro de los blueprints (Modulos)
    from app.usuarios.routes import usuarios_bp
    from app.productos.routes import productos_bp
    from app.auth.routes import auth_bp

    from app.admin.routes import admin_bp
    from app.blog.routes import blog_bp
    
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(auth_bp)

    app.register_blueprint(admin_bp)
    app.register_blueprint(blog_bp)
    
    return app