from flask import jsonify
import requests

from app import vehName

model = ["https://service-sales-car-cot.herokuapp.com/show", "https://service-sales-car-cot.herokuapp.com/shotcar"]
inf = []

""" def lShopCar():
    uri = requests.get('https://service-sales-car-cot.herokuapp.com/shotcar')
    uri1 = requests.get('https://service-sales-car-cot.herokuapp.com/show')
    car = uri.json()
    car1 = uri1.json()
    print(car)
    return jsonify({'shopCar': car}, {'show': car1} )    """


def lShopCar():
    dataInf = []
    if dataInf != None:
        for i in model:
            data = requests.get(i)
            e = data.json()
            inf.append(e)
        dataInf = [(i) for i in inf]
        print(dataInf)
        inf.clear()
        return jsonify({'shopCar': dataInf})


def shopVen():
    uri = requests.get('https://servicio-carrito-venta.herokuapp.com/')
    vent = uri.json()
    print(vent)

    return jsonify({'stock': vent})


def listVeh():
    uri = requests.get('https://service-stock.herokuapp.com/vehiculos')
    veh = uri.json()
    print(veh)

    return jsonify({'stock': veh})


def getVeh(id):
    uri = requests.get('https://service-stock.herokuapp.com/vehiculos/{0}'.format(id))
    veh_get = uri.json()
    print(veh_get)

    return jsonify({'getVeh': veh_get})


def listSupplier():
    uri = requests.get('https://service-supplier.herokuapp.com/supplier')
    supplier = uri.json()
    print(supplier)

    return jsonify({'supplier': supplier})




