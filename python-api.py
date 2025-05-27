from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Item 1", "description": "Description of item 1"},
    {"id": 2, "name": "Item 2", "description": "Description of item 2"},
    {"id": 3, "name": "Item 3", "description": "Description of item 3"}
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.json
    if not new_item or 'name' not in new_item:
        return jsonify({"error": "Invalid item data"}), 400
    
    # Generate a new ID
    new_id = max(item["id"] for item in items) + 1
    new_item["id"] = new_id
    items.append(new_item)
    
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
