from flask import Flask, redirect, request
from keycloak import KeycloakOpenID

app = Flask(__name__)

keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/",
    client_id="flask-app",
    realm_name="infotact",
    client_secret_key="aIaFMI05BK2LxmaDfPw8FqpCLMp11TPP"
)

@app.route("/")
def index():
    return '<a href="/login">Login with Keycloak</a>'

@app.route("/login")
def login():
    return redirect(
        keycloak_openid.auth_url(
            redirect_uri="http://localhost:5000/callback"
        )
    )

@app.route("/callback")
def callback():
    code = request.args.get("code")
    token = keycloak_openid.token(
        grant_type="authorization_code",
        code=code,
        redirect_uri="http://localhost:5000/callback"
    )
    return token

if __name__ == "__main__":
    app.run(debug=True)
