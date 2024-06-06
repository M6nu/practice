from flask import Flask, render_template

app = Flask(__name__)
# crea una route -> un url  si tratta di un decorator
@app.route("/")
def index():
    stuff = "this is <strong>bold</strong> text "
    #return "<h1>Hello, World!</h1>"
    favorite_player=['Cr7','Guendouzi','MacTominey','B.Fernadez','Harrit','L.Modric','L.Diaz']
    return render_template("index.html", stuff= stuff, favorite_player= favorite_player)

# localhost:5000/user/Paul
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)
    # return "<h1>Hello, {}</h1>".format(name)
    
# Create a Custon error pages

# Invalid URL 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")