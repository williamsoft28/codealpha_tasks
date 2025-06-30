from flask import Flask, request, redirect, jsonify, render_template
import random
import string

app = Flask(__name__)

url_mapping = {}

def generate_short_code(num_chars=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    # Si la requête vient du formulaire HTML
    if request.content_type == 'application/x-www-form-urlencoded':
        long_url = request.form.get('url')
        if not long_url:
            return render_template('index.html', short_url=None)

        short_code = generate_short_code()
        url_mapping[short_code] = long_url
        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)

    # Si la requête vient d'un JSON (API)
    if request.is_json:
        data = request.get_json()
        long_url = data.get('url')
        if not long_url:
            return jsonify({'error': 'URL manquante'}), 400

        short_code = generate_short_code()
        url_mapping[short_code] = long_url
        short_url = request.host_url + short_code
        return jsonify({'short_url': short_url})

    return jsonify({'error': 'Mauvais format de requête'}), 400

@app.route('/<short_code>')
def redirect_short_url(short_code):
    long_url = url_mapping.get(short_code)
    if long_url:
        return redirect(long_url)
    else:
        return "URL non trouvée", 404

if __name__ == '__main__':
    app.run(debug=True)
