from flask import Blueprint, render_template

# Definimos el blueprint apuntando a su propia carpeta de plantillas interna
admin_bp = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')

@admin_bp.route('/panel')
def panel():
    return render_template('panel.html')
