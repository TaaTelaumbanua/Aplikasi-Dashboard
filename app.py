from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def daftar_product():
    return render_template("index.html")

@app.route("/detail-product")
def detail_product():
    return render_template("detail-product.html")

@app.route("/chackout")
def checkout():
    return render_template("chackout.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/laporan-penjualan")
def laporan_penjualan():
    return render_template("laporan-penjualan.html")

@app.route("/stok-produk")
def stok_produk():
    return render_template("stok-produk.html")

if __name__ == "__main__":
    app.run(debug=True)
