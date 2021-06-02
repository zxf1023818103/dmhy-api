from flask import Flask, jsonify, request
from dmhy import get_homepage

app = Flask(__name__)


@app.route('/api/page/<page>')
def homepage(page):
    try:
        keyword = request.args['keyword']
    except:
        keyword = None

    try:
        simplified_chinese = True if request.args.get('simplified_chinese', 'false', str) == 'true' else False
    except:
        simplified_chinese = False

    return jsonify(get_homepage(page, keyword, simplified_chinese))


if __name__ == '__main__':
    app.run()
