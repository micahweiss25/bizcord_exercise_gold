import pgpy
from flask import Flask

app = Flask(__name__)

# Dictionary contains:
# msgId: String,
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

def get(msgId):
    callsign = messageDB[msgId].callsign
    enc_message = messageDB[msgId].message
    dir = callsignMap[callsign]
    private_file = dir + 'private'
    public_file = dir + 'public'

    key, _ = PGPKey.from_file(private_file)
    decrypt_message = key.decrypt(enc_message).message

    return decrypt_message

def post(msg, callsign):
    raise NotImplementedError()


if __name__ == "__main__"":
    app.run(debug=True)
