#Import dependencies

from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route("/") 
def welcome():

    return render_template("index.html")
    
@app.route("/home") 
def home():

    return render_template("home.html")

@app.route("/predraft") 
def predraft():

    return render_template("predraft.html")

@app.route("/postdraft") 
def postdraft():

    return render_template("postdraft.html")

@app.route("/week3") 
def week3():

    return render_template("week3.html")

@app.route("/week6") 
def week6():

    return render_template("week6.html")

@app.route("/week9") 
def week9():

    return render_template("week9.html")

@app.route("/postseason") 
def postseason():

    return render_template("postseason.html")

@app.route("/mock1") 
def mock1():

    return render_template("mock1.html")

@app.route("/mock2") 
def mock2():

     return render_template("mock2.html")

@app.route("/franchise") 
def franchise():

    return render_template("franchise.html")

# @app.route("/falcon") 
# def falcon():

#     return render_template("falcon_writeup.html")

# @app.route("/sam") 
# def sam():

#     return render_template("sam_writeup.html")

# @app.route("/intro") 
# def twenty():

#     return render_template("intro.html")

# @app.route("/2015") 
# def fifteen():

#     return render_template("2015.html")

# @app.route("/2016") 
# def sixteen():

#     return render_template("2016")

# @app.route("/2017") 
# def seventeen():

#     return render_template("2017.html")

# @app.route("/2018") 
# def eighteen():

#     return render_template("2018.html")

# @app.route("/2019") 
# def nineteen():

#     return render_template("2019.html")

#@app.route("/mock1") 
#def memes():

#    return render_template("memes.html")

#@app.route("/mock2") 
#def memes():

#    return render_template("memes.html")

#@app.route("/qb") 
#def memes():

#    return render_template("memes.html")

#@app.route("/franchise") 
#def memes():

#    return render_template("memes.html")

if __name__ == '__main__':
    app.run(debug=True)
