from flask import Blueprint
from flask import request

sms_bp = Blueprint(
    'sms_bp',
    __name__
)

@sms_bp.route('/receive-sms',
              methods=['POST'])
def receive_sms():

    sms = request.form.get("Body")

    print("SMS:", sms)

    return "OK"