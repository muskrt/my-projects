from flask import Flask ,render_template

app=Flask(__name__)


@app.route("/")
def head():
    return render_template("index.html",number1=222300,number2=34343)
@app.route("/ml")
def mul():
    var1,var2=232,232323
    return render_template("body.html",num1=var1,num2=var2,multiplication=var1*var2)
if __name__=="__main__":
    app.run(debug=True,port=3000)