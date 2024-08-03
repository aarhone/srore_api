from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        'name': 'Wonderful Store',
        'items': [
            {
                'name': 'sofa',
                'price': 45.99
            }
        ]
    }
]
@app.get('/store')
def get_info():
    return stores

@app.post('/store')
def create_store():
    data = request.get_json()
    new_store = { 'name': data['name'], 'items': []}
    stores.append(new_store)
    return stores, 201

@app.post('/store/<names>/item')
def add_item(names):
    for s in stores:
        if s['name'] == names:
            datas = request.get_json()
            new_item = {'name': datas['name'], 'price': datas['price']}
            s['items'].append(new_item)
            return s, 201
        else:
            return {'message': 'store not found'}, 404

@app.get('/store/<names>')
def store_info(names):
    for s in stores:
        if s['name'] == names:
            return s, 201
        else:
            return {'message': 'store not found'}, 404

# if __name__ == '__main__':
#     app.run()