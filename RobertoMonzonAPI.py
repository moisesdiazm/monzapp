from flask import Flask, jsonify
from peers import Peer
from mson import Mson
from emailSender import Email

app = Flask(__name__) #local instance is the name for the app

@app.route('/')
def root():
    return "hello world"


@app.route('/peers/create/<email_in>/<int:phone_in>/<namein>')
def create_peers(email_in,phone_in,namein):
    Peer.create(name = namein,
    phone = phone_in,
    email = email_in
    )

    return "Peer created"

@app.route('/peers/get')
def get_peers():
    retobj = Mson.to_json(Peer.select())
    return jsonify(retobj)

@app.route('/peers/delete/<email>')
def delete_peers(email):
    peer_instance = Peer.get(Peer.email==email)
    peer_instance.delete_instance()

    return "Peer deleted"

@app.route('/peers/sendEmail/<email>')
def send_email(email):
    peer_instance = Peer.get(Peer.email==email)
    emailAPI.send_email(peer_instance.email)
    return "Email call retrieved"


if __name__=="__main__":
    emailAPI = Email()
    app.run(debug=True, host='0.0.0.0', port=5000)
