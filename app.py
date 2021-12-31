from flask import Flask, render_template, request
from location import traceLocation,storeIp,getData
 
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/data",methods =["GET", "POST"])
def data():
    if request.method == "POST":
        ipaddress = request.form.get("ipdata")
        data = traceLocation(ipaddress)
        return render_template('dashboard.html',data=data)
    return "<h1>BAD REQUEST, PLEASE ENTER VALID IP REQUEST!</h1>"

@app.route("/trace")
def trace():
    ip_addresss = request.remote_addr
    storeIp(ip_addresss)
    return render_template('traceip.html')

@app.route("/getdata")
def dataip():
    data = getData()
    return render_template("show_ip.html",data=data)



if __name__ == "__main__":
    app.run(debug=True, port=8000)