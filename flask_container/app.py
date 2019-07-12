# TODO: add api call to return distance of bus from bus stop in meters
# TODO: add api call to return time remaining for bus to get to the stop

# stop name bus route

from flask import *
import readingbusesapi as BusWrapper

app = Flask(__name__)

######### client handler for html/css/js ###################################
@app.route('/<html_file>', methods=['GET'])
def get_html(html_file): return render_template(html_file)


@app.route('/css/<css_file>')
def get_css(css_file): return render_template("/css/" + css_file)


@app.route('/images/<img_file>')
def get_img(img_file):
    print("SENDING IMAGE")
    return send_from_directory('images/', img_file)


@app.route('/fonts/<font_file>')
def get_font(font_file): return render_template("/fonts/" + font_file)
######################################################################################


@app.route('/get_all_stops')
def get_all_stops():
    data = BusWrapper.ReadingBusesAPI("qkYDA2l4Al")
    return jsonify(data.RequestAllStops())


@app.route('/get_bus_arrival', methods=['POST'])
def get_bus_arrival():
    bus_service = request.form['bus_service']
    bus_stop = request.form['bus_stop']
    dummy = {"predictedTime(s)": 1000}
    return jsonify(dummy)


@app.route("/get_service_times", methods=['GET'])
def get_service_times():
    bus_stop = request.form['bus_stop']
    data = predictTimes(bus_stop)
    return jsonify(data)


# just for looking back at.  Won't actually be used
@app.route('/login', methods=['POST'])
def login():

    print("username: " + request.form['username'])
    print("password: " + request.form['password'])

    return_data = {"username": request.form['username'], "password": request.form['password']}
    return jsonify(return_data)


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
