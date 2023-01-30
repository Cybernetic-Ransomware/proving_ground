from flask import Flask, request


app = Flask(__name__)


@app.route('/webhook-callback', methods=['POST'])
def hook():
    print(request.data)
    return 'Testing!'


if __name__ == '__main__':
    app.run(debug=True)
