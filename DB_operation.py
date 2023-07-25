import sqlite3

def get_client_data(client_id):
    conn = sqlite3.connect('clients.db')  # Change the database name if needed
    cursor = conn.cursor()

    # Execute the SQL query to fetch the client data by client_id
    cursor.execute("SELECT * FROM clients WHERE id=?", (client_id,))
    client_data = cursor.fetchone()

    cursor.close()
    conn.close()

    if client_data:
        return {
            "id": client_data[0],
            "name": client_data[1],
            "email": client_data[2],
            "phone": client_data[3]
        }
    else:
        return None
    

def add_client_data(name, email, phone):
    conn = sqlite3.connect('clients.db')  # Change the database name if needed
    cursor = conn.cursor()

    # Execute the SQL query to insert a new client data and retrieve the autoincremented id
    cursor.execute("INSERT INTO clients (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    client_id = cursor.lastrowid

    conn.commit()
    cursor.close()
    conn.close()

    return client_id