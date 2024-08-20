from flask import Flask, render_template, url_for, request, redirect
import os
import csv

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_csv(data):
	with open('./serverlogs/database.csv', mode='a') as database:
		full_name = data["full_name"]
		email = data["email"]
		phone_number = data["phone_number"]
		message = data["message"]
		csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([full_name,email,phone_number,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		
		# loggin = os.path.join('serverlogs', 'logs.txt')

		# full_name = data.get('full_name', '')
		# email = data.get('email', '')
		# phone_number = data.get('phone_number', '')
		# message = data.get('message', '')

		# log_entry = f"{full_name} : {email} : {phone_number} : {message}\n"

		# if os.path.getsize(loggin) == 0:
		# 	header = "Full Name : Email : Phone Number : Message\n\n"
		# 	with open(loggin, 'w') as file2:
		# 		file2.write(header)


		# with open(loggin, 'a') as file:
		# 	file.write(log_entry)
		return redirect('/thankyou.html')

	else:
		return "something went wrong"


# $env:FLASK_DEBUG = "1"

if __name__ == '__main__':
    app.run(debug=True)


