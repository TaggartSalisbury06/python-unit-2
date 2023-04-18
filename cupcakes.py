from abc import ABC,abstractmethod
import csv
from pprint import pprint

class Cupcake(ABC):
  size = "regular"
  def __init__(self, name, price, flavor, frosting, filling):
    self.name = name
    self.price = price
    self.flavor = flavor
    self.frosting = frosting
    self.filling = filling
    self.sprinkles = []

  def add_sprinkles(self, *args):
    for sprinkle in args:
      self.sprinkles.append(sprinkle)
  
  @abstractmethod 
  def calculate_price(self, quantity):
    return quantity * self.price

class Large(Cupcake):
  size = "large"

  def calculate_price(self, quantity):
    return quantity * self.price

class Regular(Cupcake):
  size = "regular"

  def calculate_price(self, quantity):
    return quantity * self.price

class Mini(Cupcake):
  size = "mini"

  def __init__(self, name, price, flavor, frosting):
    self.name = name
    self.price = price
    self.flavor = flavor
    self.frosting = frosting
    self.sprinkles = []

  def calculate_price(self, quantity):
    return quantity * self.price

cupcake1 = Regular("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)
cupcake4 = Regular("Triple Chocolate", 2.99, "Chocolate", "Chocolate", "Chocolate")
cupcake1.add_sprinkles("Chocolate")
cupcake5 = Regular("Strawberry", 2.99, "Stawberry", "Vanilla", None)

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3,
    cupcake4,
    cupcake5
]

def add_cupcake(file, cupcake):
  with open(file, "a", newline="\n") as csvfile:
    fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    for cupcake in cupcakes:
      if hasattr(cupcake, "filling"):
        writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
      else:
        writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

def new_csv(file, cupcakes):
  with open(file, "w", newline = "\n") as csvfile:
    fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for cupcake in cupcakes:
      if hasattr(cupcake, "filling"):
        writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
      else:
        writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

new_csv("sample.csv", cupcake_list)

def get_all_cupcakes(file):
  with open(file) as csvfile:
    reader = csv.DictReader(csvfile)
    reader = list(reader)
    return reader

def get_a_cupcake(file):
  for cupcake in get_cupcake(file):
    if cupcake["name"] == name:
      return cupcake
  return None



def read_csv(file):
  with open(file) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
     pprint(row)