from networking import connect
import threading
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def connection_page():
    if request.method == "POST":
        ip = request.form.get("ip")
        port = int(request.form.get("port"))

        connect_thread = threading.Thread(
            target=connect,
            args=(ip, port), 
            daemon=True
        )
        connect_thread.start()

        return f"<h1>Conncted to {ip} at port {port}</h1>"
    else: 
        return render_template("connection_page.html")

if __name__ == "__main__":
    app.run(debug=True)
