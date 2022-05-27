from flask import Blueprint

epwm = Blueprint(
    'epwm_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)