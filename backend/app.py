from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate_emissions():
    data = request.json
    server_hours = data.get('server_hours', 0)
    data_transfer = data.get('data_transfer_gb', 0)
    storage = data.get('storage_gb', 0)

    # Simple emission factors (fictional values for demonstration)
    server_emissions = server_hours * 0.5
    data_transfer_emissions = data_transfer * 0.2
    storage_emissions = storage * 0.1

    total_emissions = server_emissions + data_transfer_emissions + storage_emissions

    return jsonify({
        'total_emissions_kg': total_emissions,
        'breakdown': {
            'server_emissions_kg': server_emissions,
            'data_transfer_emissions_kg': data_transfer_emissions,
            'storage_emissions_kg': storage_emissions
        }
    })

if __name__ == '__main__':
    app.run(port=8000)

