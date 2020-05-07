
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            sku = (request.form['sku'])
            national_inv= float(request.form['national_inv'])
            lead_time = float(request.form['lead_time'])
            in_transit_qty = float(request.form['in_transit_qty'])
            forecast_3_month = float(request.form['forecast_3_month'])
            forecast_6_month = float(request.form['forecast_6_month'])
            forecast_9_month=float(request.form['forecast_9_month'])
            sales_1_month=float(request.form['sales_1_month'])
            sales_3_month=float(request.form['sales_3_month'])
            sales_6_month=float(request.form['sales_6_month'])
            sales_9_month=float(request.form['sales_9_month'])
            min_bank=float(request.form['min_bank'])
            is_potential_issue=(request.form['potential_issue'])
            if(is_potential_issue=='Yes'):
                potential_issue=1
            else:
                potential_issue=0
            pieces_past_due=float(request.form['pieces_past_due'])
            perf_6_month_avg=float(request.form['perf_6_month_avg'])
            perf_12_month_avg=float(request.form['perf_12_month_avg'])
            local_bo_qty=float(request.form['local_bo_qty'])
            is_deck_risk=(request.form['deck_risk'])
            if(is_deck_risk == 'Yes'):
                deck_risk=1
            else:
                deck_risk=0
            is_oe_constraint=(request.form['oe_constraint'])
            if(is_oe_constraint == 'Yes'):
                oe_constraint=1
            else:
                oe_constraint=0
            is_ppap_risk=(request.form['ppap_risk'])
            if(is_ppap_risk == 'Yes'):
                ppap_risk=1
            else:
                ppap_risk=0
            is_stop_auto_buy=(request.form['stop_auto_buy'])
            if(is_stop_auto_buy=='Yes'):
                stop_auto_buy=1
            else:
                stop_auto_buy=0
            is_rev_stop=(request.form['rev_stop'])
            if(is_rev_stop=='Yes'):
                rev_stop=1
            else:
                rev_stop=0
            filename = 'model.pkl'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[sku, national_inv, lead_time, in_transit_qty,forecast_3_month, forecast_6_month, forecast_9_month,sales_1_month, sales_3_month, sales_6_month, sales_9_month,min_bank, potential_issue, pieces_past_due, perf_6_month_avg,perf_12_month_avg, local_bo_qty, deck_risk, oe_constraint,ppap_risk, stop_auto_buy, rev_stop, went_on_backorder]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app