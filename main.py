from flask import Flask, request, send_file
from flasgger import Swagger
app = Flask(__name__)
app.config['SWAGGER'] = {
    "title": "My API",
    "description": "My API",
    "version": "1.0.2",
    "termsOfService": "",
    "hide_top_bar": True
}
CORS(app)
Swagger(app)

app = Flask(__name__)

@app.route('/hello-world', methods=['GET'])
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)