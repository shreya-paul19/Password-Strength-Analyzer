from flask import Flask, render_template, request, jsonify

from password_checker import analyze_password
from entropy import calculate_entropy
from crack_time import estimate_crack_time
from password_generator import generate_password
from policy_checker import check_policy
from breach_checker import check_breach

from database import (
    create_db,
    save_result,
    get_statistics
)

app = Flask(__name__)

create_db()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    data = request.get_json()

    password = data.get('password', '')

    result = analyze_password(password)

    entropy = calculate_entropy(password)

    result["entropy"] = entropy
    result["crack_time"] = estimate_crack_time(entropy)
    result["policy"] = check_policy(password)
    result["breach"] = check_breach(password)

    save_result(
        result["score"],
        result["strength"],
        entropy
    )

    return jsonify(result)


@app.route('/generate', methods=['GET'])
def generate():

    password = generate_password()

    return jsonify({
        "password": password
    })


@app.route('/dashboard')
def dashboard():

    stats = get_statistics()

    return render_template(
        'dashboard.html',
        stats=stats
    )


if __name__ == '__main__':
    app.run(debug=True)