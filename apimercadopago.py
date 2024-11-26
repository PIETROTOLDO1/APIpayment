import mercadopago

def gerar_link_pagamento():
    sdk = mercadopago.SDK("APP_USR-7886720796801836-111622-38a0b04f1a0c725744be66d3538884be-2102915636")

    request_options = mercadopago.config.RequestOptions()
    request_options.custom_headers = {
        'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
    }

    payment_data = {
        "items":[
            {"id":"1", "tittle": "Cachaca", "quantity":1, "currency_id": "BRL", "unit_price": 84},
        ],
        "back_urls": {
            "success": "http://127.0.0.1:5000/compracerta",
            "failure": "http://127.0.0.1:5000/compraerrada",
            "pending": "http://127.0.0.1:5000/compraerrada",
        },
        "auto_return": "all",
    }
    result = sdk.preference().create(payment_data, request_options)
    payment = result["response"]
    link_iniciar_pagamento = payment["init_point"]
    return link_iniciar_pagamento