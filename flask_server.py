from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
  return render_template('index.html')

@app.route('/submitted.html')
def display_page():
  return render_template('submitted.html')

def check_db(csv):
  with open(csv) as file_to_check:
    line = file_to_check.readline()
    return True if line else False
    
def write_to_csv(data):
  name = data["name"]
  email = data["email"]
  message = data["message"]
  database = 'db.csv'
  with open(database, mode='a', newline='') as db:
    writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    if not check_db(database):
      writer.writerow(['name', 'email', 'message'])
    writer.writerow([name, email, message])
    

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
    data = request.form.to_dict()
    write_to_csv(data)
    return redirect('/submitted.html')
  else:
    return "Please try again..."

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404