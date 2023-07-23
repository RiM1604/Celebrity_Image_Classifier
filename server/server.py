from flask import Flask,request,jsonify
import util
app=Flask(__name__)


@app.route('/Hi',methods=['GET','POST'])
def hello():
    return "<h2>HI</h2>"
@app.route('/classify_image',methods=['GET','POST'])
def classify():
    image_data=request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__=="__main__":
    util.load_saved_artifacts()
    app.run(debug=True)