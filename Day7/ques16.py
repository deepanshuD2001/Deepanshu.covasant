from flask import Flask,render_template,request
import os
app=Flask(__name__)

result=""

@app.route("/updatefortoday")
def updatefortoday():
    return render_template('updatefortoday.html',data=result)
    
@app.route("/update",methods=['GET','POST'])
def updatedata():
    global result
    if request.method=='POST':
        new_data=str(request.form.get("editor")).strip()
        if result.startswith(new_data):
            new_data=result[:len(data)]
            print(new_data)
            
            return render_template('updatefortoday.html',data=new_data)
        else:
            result=new_data
            print(result)
            return render_template('updatefortoday.html',data=new_data)
    else:
        return "None"

@app.route("/share")
def share():
    print(result)
    return render_template('share.html',data=result)

@app.route("/clearnotepadtxt")
def clear():
    global result
    print("data is created",result)
    result=""
    return render_template("delete.html",data=result)
    
if __name__=='__main__':
    app.run()