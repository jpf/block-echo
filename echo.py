import os
import json
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'OPTIONS'])
def hello():
    if request.method == 'GET':
        return "Run this command: 'curl -v -X OPTIONS " + request.url + "'"
    if request.method == 'POST':
        return post(request)
    if request.method == 'OPTIONS':
        return options()


def post(request):
    data = json.loads(request.data)
    return json.dumps({"outputs":
                       [{"out": data['inputs'][0]['in']}]
                       }, indent=4)


def options():
    out = {"name": "Echo",
           "description": "An example WebPipe block echo service.",
           "inputs": [
               {"name": "in",
                "type": "string",
                "description": "String to echo"}],
           "outputs": [
               {"name": "out",
                "type": "string",
                "description": "Echoed string"}]}
    return json.dumps(out, indent=4)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
