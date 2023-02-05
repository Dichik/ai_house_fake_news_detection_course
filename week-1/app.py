import pandas as pd

from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/fakes', methods=['GET'])
def get_fake_news():
    dataset = pd.read_csv('data/data.csv')
    result = dataset[dataset['is_fake'] == 1]['text']
    response_dict = {
        'data': result.to_json()
    }
    return make_response(response_dict, 200)


@app.route('/trues', methods=['GET'])
def get_true_news():
    dataset = pd.read_csv('data/data.csv')
    result = dataset[dataset['is_fake'] == 0]['text']
    response_dict = {
        'data': result.to_json()
    }
    return make_response(response_dict, 200)


@app.route('/filter_by', methods=['GET'])
def get_filtered_by_tag():
    args = request.args
    label = args.get("tag", default=None, type=str).replace("%20", " ")
    if label is None:
        return make_response({"message": "Bad request"}, 400)

    dataset = pd.read_csv('data/data.csv')
    result = dataset[dataset['label'] == label]['text']
    response_dict = {
        'data': result.to_json()
    }
    return make_response(response_dict, 200)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
