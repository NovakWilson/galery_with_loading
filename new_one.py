from flask import render_template, make_response, request, session, redirect
from flask import Flask


app = Flask(__name__)


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    img_list = ['/static/img/mars2.jpg', '/static/img/mars3.jpg']
    if request.method == 'POST':
        f = request.files['file'].filename
        img_list.append('/static/img/{}'.format(f))
    return render_template('galery_with_loading.html', img_list=img_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
