from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def webhook():
  if request.method == "GET":
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token:
      if mode == "subscribe" and token == "whatsapp076":
        return challenge, 200
      else:
        return "Forbidden", 403
    return "Hello World", 200

  elif request.method == "POST":
    data = request.json
    print(data)
    return "EVENT_RECEIVED", 200


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)
