from flask import Flask,render_template,request,url_for,redirect

app=Flask(__name__)

li=[]
@app.route("/",methods=["POST","GET"])
def yut():
    if request.method=="POST":
        search=request.form.get("search")
        li.append(search)
        for i in li:
            if i==search:
                return redirect(url_for(i))
      
    return render_template("index.html",L=li)

@app.route("/Feel")
def video():
    return render_template("videoplayer.html")


@app.route("/muruga")
def muruga():
    return render_template("muruga.html")


@app.route("/zootopia")
def zootopia():
    return render_template("zootopia.html")


@app.route("/tamil")
def tamil():
    return render_template("tamil.html")







if __name__=="__main__":
    app.run(debug=True)