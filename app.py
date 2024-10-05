from flask import Flask, render_template, request, redirect
from database import init_db, add_contact_message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Update the name of your database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

@app.route('/')
def home():
    return render_template('index.html')  # Adjust this if you have a specific home template

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    add_contact_message(name, email, message)
    return redirect('/contact')  # Redirect back to the contact page after submission

# Remove the messages route
# @app.route('/messages')
# def messages():
#     all_messages = get_all_contact_messages()  # Get all messages from the database
#     return render_template('messages.html', messages=all_messages)  # Render a new template for messages

if __name__ == '__main__':
    app.run(debug=True)
