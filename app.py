from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route("/")
def api_test():
    return "TEST1"

@app.route("/webhook", methods=["POST"])
def gitlab_webhook():
    data = request.json
    print("Received webhook:", data)
    
    # Salva dati in un file JSON
    with open("webhook_data.json", "a") as json_file:
        json.dump(data, json_file)
        json_file.write("\n")
    
    return "Webhook received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)