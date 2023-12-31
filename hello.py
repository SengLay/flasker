from flask import Flask, render_template

# Create flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
# def index():
#     return "<h1>Hello World!</h1>"

# FILTERS!
# ''' safe, capitalize, lower, upper, title, trim, striptags '''

def index():
    first_name = "John"

    stuff = "This is Bold Text"

    fav_pizza = ["Pepperoni", "Cheese", "Mushroom", 41]

    return render_template('index.html',
                           first_name=first_name,
                           stuff=stuff,
                           fav_pizza=fav_pizza)


# localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
    # user_name=name, like we set the argument for the function
    return render_template('user.html', user_name=name)

# Create a custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)