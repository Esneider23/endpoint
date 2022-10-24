from flask import Flask, jsonify, render_template
import requests
import controller

server = Flask(__name__)


@server.get('/')
def index():
    return "word"


@server.route('/stock/vehiculos')
def stockL():
    return controller.listVeh()


@server.route('/shopcar')
def shopCarL():
    return controller.lShopCar()

"""
@server.route('/shopven')
def shopVenL():
    return controller.shopVen()


@server.route('/stock/vehiculos')
def stockL():
    return controller.listVeh()


@server.route('/stock/vehiculos/<string:id>')
def vehName(id):
    return controller.getVeh(id)


@server.route('/supplier')
def supplierL():
    return controller.listSupplier()


def page_not_found(error):
    return render_template('404.html')
"""

if __name__ == '__main__':
    server.run(debug=True)