from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


# Route for the homepage
@app.route("/")
def home():
    return render_template("patient_login.html")  # Must have index.html in the templates folder


# Route for another page
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")  # Must have about.html in the templates folder


# Route to redirect to the about page
@app.route("/go-to-about")
def go_to_about():
    return redirect(url_for('about'))  # Redirects to the about route


# Start the server only when running the file
if __name__ == "__main__":
    app.run(debug=True)
