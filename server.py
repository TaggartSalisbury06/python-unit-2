from flask import Flask, render_template, url_for, redirect
from cupcakes import get_all_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)



@app.route("/")
def home():
  order_total = round(sum([float(x["price"]) for x in get_all_cupcakes("order.csv")]), 2)
  return render_template("index.html", cupcakes = get_all_cupcakes("cupcakes.csv"), items_num = len(get_all_cupcakes("order.csv")), order_total = order_total)

@app.route("/cupcakes")
def all_cupcakes():
  return render_template("cupcakes.html")

@app.route("/individual-cupcakes")
def individual_cupcakes():
  return render_template("individual-cupcakes.html")

@app.route("/order")
def order():
  return render_template("order.html", cupcakes = get_all_cupcakes("order.csv"))

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
  cupcake = find_cupcake("cupcakes.csv", name)

  if cupcake:
    add_cupcake_dictionary("order.csv", cupcake)
    return redirect(url_for("home"))
  else:
    return "Sorry cupcake not found"

if __name__ == "__main__":
  app.env = "development"
  app.run(debug = True, port = 8000, host = "localhost")