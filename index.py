from flask import Flask , render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("pagina.html")
@app.route("/quienes")
def quienes():
    return render_template("quienes.html ")
@app.route("/rayservicios")
def rayservicios():
    return render_template("rayservicios.html")
@app.route("/contactos")
def contactos():
    return render_template("contactos.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/trabajos")
def trabajos():
    return render_template("trabajos.html")
@app.route("/productos")
def productos():
    return render_template("productos.html")
if __name__ =="__main__":
    app.run(debug=True)


    


 