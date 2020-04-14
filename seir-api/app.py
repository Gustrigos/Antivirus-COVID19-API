from flask import Flask, jsonify, abort, make_response, request
from models import Model
from params import *

##### Model ####
def model_setup(user_params=False):
	
	# user_initial_conditions = 
	# user_params = 
	# user_t = 

	if user_params:
		model = Model(name="SEIR",initial_conditions=user_initial_conditions,params=user_params,t=user_t)
		model_results = model.get_estimates()

		return model_results 		


	# default parameters
	else:
		model = Model(name="SEIR",initial_conditions=Condiciones_Iniciales,params=parametros,t=periodo_evaluacion)
		model_results = model.get_estimates()

		return model_results 

model_results = model_setup()

##### API ###### 
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# GET Commands
@app.route('/api/seir', methods=['GET'])
def get_seir():

	seir_data = {'seir': model_results}

	# looks for any arguments after api/seir
	# eg: api/seir?estimate=susceptible
	if 'estimate' in request.args:
		query = request.values['estimate']

		if query in seir_data['seir'].keys():
			return jsonify({'{}'.format(query) : seir_data['seir'][query]})

		else:
			abort(404)
	else:
		return jsonify(seir_data)

# # POST 
# @app.route('/api/seir', methods=['POST'])
# def create_params():
# 	if not request.json or not 'title' in request.json:
#         abort(400)

if __name__ == '__main__':
    app.run(debug=True)


