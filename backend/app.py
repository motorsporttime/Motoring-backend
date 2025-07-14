from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/schedule')
def schedule():
    return jsonify([])

@app.route('/api/results')
def results():
    return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)