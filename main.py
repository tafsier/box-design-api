from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Box Design API is Running!"

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json

        # ??????? ???????? ????????
        company_name = data.get('company_name')
        slogan = data.get('slogan')
        logo_url = data.get('logo_url')
        address = data.get('address')
        dieline_url = data.get('dieline_url')
        color = data.get('color')
        product_type = data.get('product_type')

        # ? ??? ??? ????? ?????? ???????? (?????? ???? ????? ???????)
        return jsonify({
            "status": "success",
            "message": "Data received successfully",
            "data": data
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=False)