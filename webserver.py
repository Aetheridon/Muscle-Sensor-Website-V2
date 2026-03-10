from networking import connect
import threading
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
stop_event = threading.Event()

latest_data = {
    "sensorA0": 0,
    "sensorA1": 0
}

@app.route("/", methods=["POST", "GET"])
def connection_page():
    if request.method == "POST":
        ip = request.form.get("ip")
        port = int(request.form.get("port"))

        if stop_event.is_set():
            stop_event.clear()

        connect_thread = threading.Thread(
            target=connect,
            args=(ip, port, latest_data, stop_event), 
            daemon=True
        )
        connect_thread.start()

        return redirect(url_for("connected_page", ip=ip))
    else: 
        return render_template("connection_page.html")

@app.route("/connected", methods=["POST", "GET"])
def connected_page():
    ip = request.args.get("ip")

    if request.method == "POST":
        if request.form.get("disconnect"):
            stop_event.set()

            return redirect(url_for("connection_page"))
    else:
        return render_template("active_connection.html", ip=ip)

@app.route("/sensor_data")
def sensor_data():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(debug=True)
