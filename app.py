from flask import Flask, render_template, request, redirect, url_for
from DB_operation import get_client_data, add_client_data

app = Flask(__name__)

# Hardcoded credentials for simplicity
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin"

@app.route('/', methods=['GET', 'POST'])
def login():
    error_message = None  # Initialize error message

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return render_template('search.html')
        else:
            error_message = "Invalid username or password"

    return render_template('login.html', error_message=error_message)

@app.route('/search', methods=['GET', 'POST'])
def search_results():
    if request.method == 'POST':
        client_id = request.form['client_id']
        client_data = get_client_data(client_id)
        if client_data:
            return redirect(url_for('client_data', client_id=client_id))
        else:
            return render_template('search.html', not_found_message="Client not found")

    return render_template('search.html', not_found_message=None)

@app.route('/client/<client_id>', methods=['GET'])
def client_data(client_id):
    client_data = get_client_data(client_id)
    if client_data:
        return render_template('client_data.html', client=client_data)
    else:
        return "Client not found"

@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        client_id = add_client_data(name, email, phone)
        return redirect(url_for('client_data', client_id=client_id))

    return render_template('add_client.html')

if __name__ == '__main__':
    app.run(debug=True)
