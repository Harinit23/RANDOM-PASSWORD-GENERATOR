from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=0):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length(request):
    password_length = int(request.form.get('password_length', 0))
    password_length = max(6, min(password_length, 100))
    return password_length

def is_strong_password(password):
    # Check if the password contains at least one uppercase, one lowercase, one digit, and one special character
    return any(c.isupper() for c in password) and any(c.islower() for c in password) \
        and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password)

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_password = ''
    strength_message = ''

    if request.method == 'POST':
        password_length = get_password_length(request)
        generated_password = generate_password(password_length)
        if is_strong_password(generated_password):
            strength_message = 'Strong Password!'
        else:
            strength_message = 'Consider adding uppercase, lowercase, digit, and special character for a stronger password.'

    return render_template('index.html', generated_password=generated_password, strength_message=strength_message)

if __name__ == "__main__":
    app.run(debug=True)
