from mollie.api.client import Client

mollie_client = Client()
mollie_client.set_api_key("live_dHar4XY7LxsDOtmnkVtjNVWXLSlXsM")

payment = mollie_client.payments.create({
    "amount": {
        "currency": "EUR",
        "value": "10.00",
    },
    "description": "Order #12345",
    "redirectUrl": "https://webshop.example.org/order/12345/",
    "webhookUrl": "https://webshop.example.org/payments/webhook/",
    "metadata": {
        "order_id": "12345",
    }
})

from mollie.api.client import Client

mollie_client = Client()
mollie_client.set_api_key("live_dHar4XY7LxsDOtmnkVtjNVWXLSlXsM")

payments = mollie_client.payments.list()

# Get the next page
next_payments = payments.get_next()

from mollie.api.client import Client

mollie_client = Client()
mollie_client.set_api_key("live_dHar4XY7LxsDOtmnkVtjNVWXLSlXsM")

payment = mollie_client.payments.get(
    "tr_5B8cwPMGnU6qLbRvo7qEZo",
    embed="refunds,chargebacks",
    include="details.qrCode"
)

from mollie.api.client import Client

mollie_client = Client()
mollie_client.set_api_key("live_dHar4XY7LxsDOtmnkVtjNVWXLSlXsM")

payment = mollie_client.payments.update(
    "tr_5B8cwPMGnU6qLbRvo7qEZo",
    {
        "description": "Order #98765",
        "redirectUrl": "https://webshop.example.org/order/98765/",
        "webhookUrl": "https://webshop.example.org/payments/webhook/",
        "metadata": {
            "order_id": "98765",
        }
    }
)

from mollie.api.client import Client

mollie_client = Client()
mollie_client.set_api_key("live_dHar4XY7LxsDOtmnkVtjNVWXLSlXsM")

canceled_payment = mollie_client.payments.delete("tr_WDqYK6vllg")

def start_payment():
    # Implement payment processing logic here
    print('Payment processing started')