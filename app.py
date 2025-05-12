from flask import Flask, jsonify, request
from utils.profile_faker import generate_profile

app = Flask(__name__)

@app.route('/api/profile-faker')
def api_profile():
    locale = request.args.get('locale', 'en_US')
    return jsonify(generate_profile(locale))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
