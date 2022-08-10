from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "hello clarusway"

@app.route("/admin")
def admin():
    return "admin view"
@app.route("/second")
def second():
    return "bize her yer trabson"
@app.route("/third/subthird")
def third():
    return "this is the suppage of third page"

@app.route('/forth/<string:id>')
def forth(id):
    return f"id number is {id}"

@app.route("/admin/login")
def admin_login():
    return "this is the page for admins to login"

if __name__=="__main__":
    app.run(debug=True)
