from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def index():
    return 'Hello, World!'

@app.route('/api/data')
def get_data():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
