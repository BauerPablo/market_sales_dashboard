from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

	data={
		'title':'Dashboard'
	}

	return render_template('index.html', data=data)

def page_not_found(error):
	data={
		'title':'Uups somthing happend!'
	}
	return render_template('page_not_found.html', data=data), 404

if __name__ == "__main__":
	app.register_error_handler(400, page_not_found)
	app.run(debug=True)