from flask_cors import CORS
from flask import Flask, jsonify
from apimercadopago import gerar_link_pagamento

app = Flask(__name__)
CORS(app)  # Permite requisições de qualquer origem

@app.route("/api/payment-link", methods=["GET"])
def payment_link():
    link_iniciar_pagamento = gerar_link_pagamento()
    return jsonify({"payment_link": link_iniciar_pagamento})

if __name__ == "__main__":
    app.run(debug=True)
