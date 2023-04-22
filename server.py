from flask import Flask, render_template, url_for, redirect
from cupcakes import get_all_cupcakes, find_cupcake, add_cupcake_dictionary, remove_cupcake_dictionary

app = Flask(__name__)



@app.route("/")
def home():
  order_total = round(sum([float(x["price"]) for x in get_all_cupcakes("order.csv")]), 2)
  return render_template("index.html", cupcakes = get_all_cupcakes("cupcakes.csv"), items_num = len(get_all_cupcakes("order.csv")), order_total = order_total)


@app.route("/individual-cupcakes/<name>")
def individual_cupcakes(name):
  cupcake = find_cupcake("cupcakes.csv", name)

  if cupcake:
    return render_template("individual-cupcakes.html", cupcake=cupcake)
  else:
    return "Sorry cupcake not found"
  

@app.route("/order")
def order():
  order_total = round(sum([float(x["price"]) for x in get_all_cupcakes("order.csv")]), 2)
  cupcakes=get_all_cupcakes("order.csv")

  cupcakes_counted = []
  cupcake_set = set()

  for cupcake in cupcakes:
      cupcake_set.add((cupcake["name"], cupcake["price"], cupcakes.count(cupcake)))


  return render_template("order.html", cupcakes=cupcake_set, order_total=order_total, items_num = len(get_all_cupcakes("order.csv")))

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
  cupcake = find_cupcake("cupcakes.csv", name)

  if cupcake:
    add_cupcake_dictionary("order.csv", cupcake)
    return redirect(url_for("home"))
  else:
    return "Sorry cupcake not found"

@app.route("/delete-cupcake/<name>")
def delete_cupcake(name):
  cupcake = find_cupcake("order.csv", name)

  if cupcake:
    remove_cupcake_dictionary("order.csv", cupcake)
    return redirect(url_for("home"))
  else:
    return "Sorry cupcake not found"

if __name__ == "__main__":
  app.env = "development"
  app.run(debug = True, port = 8000, host = "localhost")