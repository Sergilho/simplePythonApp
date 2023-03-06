from flask import Flask, request, jsonify
from product_service.entities.entities import Product
from product_service.service import ProductService

app = Flask(__name__)
service = ProductService()


@app.route('/products', methods=['POST'])
def Post():
    data = request.get_json()
    product = Product(name=data['name'], price=data['price'])
    created_product = service.CreateProduct(product)
    return jsonify(created_product.__dict__), 201


@app.route('/products/<int:product_id>', methods=['GET'])
def Get(product_id):
    product = service.GetProductById(product_id)
    if product:
        return jsonify(product.__dict__)
    else:
        return jsonify({'error': 'Product not found'}), 404


@app.route('/products', methods=['GET'])
def GetAllProducts():
    products = service.GetAllProducts()
    return jsonify([product.__dict__ for product in products])


@app.route('/products/<int:product_id>', methods=['PUT'])
def Put(product_id):
    data = request.get_json()
    product = Product(id=product_id, name=data['name'], price=data['price'])
    updated_product = service.UpdateProduct(product)
    if updated_product:
        return jsonify(updated_product.__dict__)
    else:
        return jsonify({'error': 'Product not found'}), 404


@app.route('/products/<int:product_id>', methods=['DELETE'])
def Delete(product_id):
    deleted_product = service.DeleteProduct(product_id)
    if deleted_product:
        return jsonify(deleted_product.__dict__)
    else:
        return jsonify({'error': 'Product not found'}), 404



if __name__ == '__main__':
    app.run()
