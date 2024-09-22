#                       folder 3 : your first rest API            #
# video 4: flask from flask
# video 8: module:jasonify for convert variable into json.
# video 9: module: request: This object provides access to incoming request data.
from flask import Flask, jsonify, request, render_template
# video 4: Create a Flask application instance
app = Flask(__name__)
# video 7: Create a list of dictionaries to store information about stores
stores = [
    {
        'name': 'my wonderful store',
        'items': [
            {
                'name': 'my item',
                'price': '19.99'
            }
        ]
    }
]
# video 4: create app routes
# @app.route('/')

# video 4: create function name hammad 
#  def hammad():
#       return "hello world"

# video 10:create app routes
@app.route('/')
# video 10  full home function :index.html render. see template inside index.html # Define a route for the home page
def home():
# video 10: Define the home function to render the index.html template    
    return render_template("index.html")
# video 7: Define a route to create a new store using the POST method 
# POST /store data: {name}

@app.route('/store', methods=['POST'])
# video 7: Define the create_store function to handle creating a new store
  
def create_store():
# video 9: Get the JSON data from the request
    request_data = request.get_json()
# video 9: Create a new store dictionary with the given name and an empty list of items
    new_store = {
        'name': request_data['name'],
        'items': []
    }
# video 9: Add the new store to the stores list
    stores.append(new_store)
# video 9: Return the new store as a JSON response   
    return jsonify(new_store)

# video 7:  Define a route to get a specific store by name using the GET method
# GET /store/<string:name>
@app.route('/store/<string:name>')

# video 7: Define the get_store function to handle retrieving a store by name
def get_store(name):
# video 9: Iterate through the list of stores   
    for store in stores:
# video 9: If a store with the given name is found.  
        if store['name'] == name:
# video 9: return it as a JSON response             
            return jsonify(store)
# video 9: If no store with the given name is found, return an error message       
    return jsonify({'message': 'store not found'})

# video 7: Define a route to get all stores using the GET method
# GET /store
@app.route('/store')

# video 7: Define the get_stores function to handle retrieving all stores
def get_stores():
# video 8: Return the list of stores as a JSON response  
    return jsonify({'stores': stores})
 
#  video 7:Define a route to create a new item in a specific store using the POST method
# POST /store/<string:name>/item {name:, price:}

@app.route('/store/<string:name>/item', methods=['POST'])

# video 7: Define the create_item_in_store function to handle creating a new item in a specific store
def create_item_in_store(name):
# video 9: # Get the JSON data from the request  
    request_data = request.get_json()
# video 9:  Iterate through the list of stores   
    for store in stores:
# video 9: If a store with the given name is found       
        if store['name'] == name:
# video 9: Create a new item with the given name and price                       
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
# video 9: Add the new item to the store's list of items                      
            store['items'].append(new_item)
# video 9: Return the new item as a JSON response           
            return jsonify(new_item)
# video 9: If no store with the given name is found, return an error message        
    return jsonify({'message': 'store not found'})

# video 7: define a route to get all items in a specific store using the GET method 
# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')

# video 7: Define the get_item_in_store function to handle retrieving items in a specific store
def get_item_in_store(name):
# video 9: terate through the list of stores   
    for store in stores:
# video 9: If a store with the given name is found.        
        if store['name'] == name:
# video 9: return its items as a JSON response            
            return jsonify({'items': store['items']})
# video 9: If no store with the given name is found, return an error message                  
    return jsonify({'message': 'store not found'})

# video 7: POST and GET method explanations:

"""
post : used to receive data.
get : used to send data back only.

post/store data : {name} # create a new store with a given name.
get/store/<string:name> # get a store for a given name and return data about it.
get/store # return list of all stores.
post/store/<string:name>/item {name:, price:} # create an item inside a specific store with a given name.
get/store/<string:name>/item # get all items in a specific store.
"""

# video 4: Run the Flask application on port 5003
if __name__ == '__main__':
    app.run(port=5003)
