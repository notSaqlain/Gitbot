from flask import Flask, request
import pandas as pd

app = Flask(__name__)

"""
@app.route("/")
def api_test():
    return "TEST1"
"""

@app.route("/webhook", methods=["POST"])
def gitlab_webhook():
    data = request.json
    print("Received webhook:", data)
    
    # Salva dati in un file JSON
    dati = pd.DataFrame([data])
    dati.to_json("data.json", orient="records", lines=True, mode='a')

    
    return "Webhook received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)