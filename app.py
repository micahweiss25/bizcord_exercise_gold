import json
import pgpy
import uuid

from flask import Flask

app = Flask(__name__)

# Dictionary contains:
# messageId: String,
# { 
#   callsign: String
#   message: String 
# }
messageDB = {}

# Callsigns to Directory
callsignMap = {
    "goose": "~/goose/",
    "firefly": "~/firefly/",
    "mouse": "~/mouse/"
}

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

def get():
    messageId = request.args.get("messageId")
    try:
        uuid.UUID(str(messageId))
    except ValueError:
        return 400
    callsign = messageDB[messageId].callsign
    enc_message = messageDB[messageId].message
    dir = callsignMap[callsign]
    private_file = dir + 'private'

    key, _ = PGPKey.from_file(private_file)
    decrypt_message = key.decrypt(enc_message).message

    return decrypt_message

def post(message, callsign):
    # Need to create messageId from message -> add to messageDB along with callSign and Message.
    messageId = uuid.UUID(msg) # In the form of UUID-4
    messageDB[messageId] = {'callsign': callsign, 'message': message} # Updated internal messageDB

    # Need to encrypt Message
    dir = callsignMap[callsign]
    public_file = dir + 'public'
    public_key, _ = PGPKey.from_file(public_file)
    encryptedMessage = public_key.encrypt(message)
    
    json_string = json.loads(f'{{"messageId": {messageId}, "encryptedMessage": {encryptedMessage}}}')

    return json_string


if __name__ == "__main__"":
    app.run(debug=True)
