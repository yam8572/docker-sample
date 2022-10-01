from flask import Flask, request, send_file
from flasgger import Swagger
app = Flask(__name__)
app.config['SWAGGER'] = {
    "title": "Sample API",
    "description": "Sample API",
    "version": "1.0.0",
    "termsOfService": "",
    "hide_top_bar": True
}
Swagger(app)

@app.route('/hello-world', methods=['GET'])
def hello_world():
  """
    Return Hello World 
    ---
    tags:
      - Node APIs
    produces: application/json,
    responses:
      200:
        description: Return Hello World 
        examples:
          "Hello World"
  """
  return "Hello World"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
