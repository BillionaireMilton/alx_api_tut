# import dependencies here 
from flask import Flask, jsonify
from models import setup_db, Plant
from flask_cors import CORS, cross_origin


# Define the create_app function 
def create_app(test_config=None):
    # Create and configure the app
    # include the first parameter: Here, __name__ is the name of the current python module
    app = Flask(__name__, instance_relative_config=True)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PUT, PATCH, DELETE, OPTIONS')
        return response

    # @cross_origin()
    @app.route('/')
    def hello():
        return jsonify({'message':'Hello world'})
    
    @app.route('/hello')
    @cross_origin()
    def get_greeting():
        return jsonify({'message': 'Another Hello World!'})

    @app.route('/entrees', methods=['GET'])
    def get_entrees():
        page = request.args.get('page', 1, type=int)

    ### starting real tests here
    @app.route('/plants')
    def get_plants():
        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]
        return jsonify({
            'success': True,
            'plants': formatted_plants,
            'total_plants': len(formatted_plants)
        })
    # return the app instance
    return app