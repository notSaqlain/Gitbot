from flask import Flask, request
import pandas as pd
import json
import os

app = Flask(__name__)

@app.route("/")
def api_test():
    return "TEST1"

@app.route("/webhook", methods=["POST"])
def gitlab_webhook():
    data = request._cached_json
    print("Received webhook:", data)

    # Salva i dati in un file JSON
    with open("webhook_data.json", "a") as json_file:
        json.dump(data, json_file)
        json_file.write("\n")

    # Salva i dati in un file CSV
    df = pd.DataFrame([data])
    if not os.path.isfile("webhook_data.csv"):
        df.to_csv("webhook_data.csv", mode="w", index=False) 
    else:
        df.to_csv("webhook_data.csv", mode="a", header=False, index=False)

    return "Webhook received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
