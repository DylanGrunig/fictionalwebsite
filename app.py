from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/home')
def hello_world():
   return """
   <h1>HOMEPAGE</h1>
   <br />
   Try these links: <br />
    - <a href='/bootstrap-grid'>Click to buy some dolls...</a><br />
<br />
   """






@app.route('/bootstrap-grid')
def bootstrap_grid():
    return render_template("bootstrap-grid.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/Humandolls')
def HumanDolls():
    return render_template("Humandolls.html")

@app.route('/Gotcha')
def Gotcha():
    return render_template("Gotcha.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/emailsignup')
# def emailsignup():
#     return render_template("emailsignup.html")

# @app.route('/bootstrap')
# def bootstrap():
#     return render_template("bootstrap_template.html")
