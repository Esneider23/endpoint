from flask import Flask, jsonify, render_template
import requests
import controller

server = Flask(__name__)


@server.get('/')
def index():
    return {"Message": "Welcome to apy"}


"""
@server.route('/')
def index():
    while True:
        main_api = requests.get("https://service-sales-car-cot.herokuapp.com/show")

        # ask what the code that returned us #! if it is 200, so everything it is correct.
        if main_api.status_code == 200:
            print(main_api.json())
            elements =main_api.json()
            #for elements in date:
                #print(elements)
        return jsonify({
            'index': elements

        })
 


@server.route('/shopcar')
def shopCarL():
    return controller.lShopCar()


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