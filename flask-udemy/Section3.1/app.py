#                       folder 3 : your first rest API            #

# video 4: flask from flask
# video 8: module:jasonify for convert variable into json.
# video 9: module: request: This object provides access to incoming request data.
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)  # Create a Flask application instance

# In-memory database to store information about stores 
stores=[
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

# create app routes
@app.route('/') 
def home():  
    return render_template("index.html")  # Render the index.html template and return it as the response

# POST /store data: {name} # route to create a new store using the POST method  
@app.route('/store', methods=['POST'])                        
def create_store(): # # Function to handle creating a new store
    request_data = request.get_json() # Get the JSON data from the request
    new_store = {    # Create a new store dictionary with the given name and an empty list of items # inmemory database.         
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)   # Add the new store to the stores list(in memory database)
    return jsonify(new_store)  # Return the new store as a JSON response 

# GET /store/<string:name> # route to get a specific store by name using the GET method
@app.route('/store/<string:name>')
def get_store(name): # get_store function to handle retrieving a store by name
    for store in stores: # Iterate through the list of stores 
        if store['name'] == name: # If a store with the given name is found.
            return jsonify(store) # return it as a JSON response          
    return jsonify({'message': 'store not found'}) # If no store with the given name is found, return an error message  

# GET /store # route to get all stores using the GET method
@app.route('/store')
def get_stores():#  get_stores function to handle retrieving all stores
    return jsonify({'stores': stores})  # Return the list of stores as a JSON response  

# POST /store/<string:name>/item {name:, price:} #route to create a new item in a specific store using the POST method
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):  # create_item_in_store function to handle creating a new item in a specific store
    request_data = request.get_json() # Get the JSON data from the request  
    for store in stores: # Iterate through the list of stores
        if store['name'] == name: # If a store with the given name is found
            new_item = {  # Create a new item with the given name and price
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item) # add the new item to the store's list of items 
            return jsonify(new_item) # Return the new item as a JSON response 
    return jsonify({'message': 'store not found'}) # if no store with the given name is found, return an error message 

# GET /store/<string:name>/item # route to get all items in a specific store using the GET method 
@app.route('/store/<string:name>/item')
def get_item_in_store(name): # get_item_in_store function to handle retrieving items in a specific store
    for store in stores: # iterate through the list of stores  
        if store['name'] == name: # If a store with the given name is found.
            return jsonify({'items': store['items']}) # return its items as a JSON response   
    return jsonify({'message': 'store not found'}) # If no store with the given name is found, return an error message  

# POST and GET method explanations:
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
    app.run(port=5003,debug=True)

