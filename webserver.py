from networking import connect
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def connection_page():
    if request.method == "POST":
        ip = request.form.get("ip")
        port = int(request.form.get("port"))
        connect(HOST=ip, PORT=port) #TODO: Async
        return f"<h1>Conncted to {ip} at port {port}</h1>"
    else: 
        return render_template("connection_page.html")

if __name__ == "__main__":
    app.run(debug=True)
