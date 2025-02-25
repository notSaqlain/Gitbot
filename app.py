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
    data = request.json  # Get webhook payload
    print("Received webhook:", data)  # Print for debugging

    # Save data to JSON file
    with open("webhook_data.json", "a") as json_file:
        json.dump(data, json_file)
        json_file.write("\n")  # Add newline to separate entries

    # Save data to CSV file
    df = pd.DataFrame([data])  # Convert dict to DataFrame
    if not os.path.isfile("webhook_data.csv"):
        df.to_csv("webhook_data.csv", mode="w", index=False)  # Create new file
    else:
        df.to_csv("webhook_data.csv", mode="a", header=False, index=False)  # Append to file

    return "Webhook received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
