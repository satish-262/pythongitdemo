from flask import Flask,render_template,jsonify,request 
app=Flask(__name__)
data = [
        {"id": 1, "name": "Satish"},
        {"id": 2, "name": "Rahul"}
    ]
@app.route('/')
def home():
    return "api is working"

@app.route('/users',methods=['GET'])
def users():
    
    return  jsonify(data)
@app.route('/user',methods=['post'])
def user_update():
    new_user=request.json 
    data.append(new_user)
    return jsonify({
        "message":"sucessfully created"

    }

    )

@app.route('/html')
def html():
    return render_template("login.html")

@app.route('/add_user_html')
def add_user_html():
    return render_template("add_user.html")
@app.route('/test')
def test():
    l=["satish","villa","chinna"]

    return l
if __name__ == '__main__':
    app.run(debug=True)