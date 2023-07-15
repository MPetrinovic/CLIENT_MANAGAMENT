from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials for simplicity
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin"

# Dummy client data for demonstration purposes
CLIENT_DATA = {
    "1": {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
    },
    "2": {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "phone": "9876543210"
    }
}

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
        if client_id in CLIENT_DATA:
            return redirect(url_for('client_data', client_id=client_id))
        else:
            return render_template('search.html', not_found_message="Client not found")

    return render_template('search.html')

@app.route('/client/<client_id>', methods=['GET'])
def client_data(client_id):
    if client_id in CLIENT_DATA:
        data = CLIENT_DATA[client_id]
        return render_template('client_data.html', client=data)
    else:
        return "Client not found"

@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        new_client_id = str(len(CLIENT_DATA) + 1)
        CLIENT_DATA[new_client_id] = {"name": name, "email": email, "phone": phone}

        return redirect(url_for('client_data', client_id=new_client_id))

    return render_template('add_client.html')

if __name__ == '__main__':
    app.run(debug=True)
