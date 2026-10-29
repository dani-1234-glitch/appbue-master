from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, template_folder='templates', url_prefix='/blog')

@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    # Simulamos un título dinámico que responda a la solicitud
    titulo = f"Entrada número {id}"
    return render_template('entrada.html', id=id, titulo=titulo)
