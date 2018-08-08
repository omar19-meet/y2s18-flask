from flask import Flask, render_template, url_for
app = Flask(__name__)
@app.route('/')
def home_page():
    fav_players=["Salah","Mbappe","Ronaldo"]
    likes_same_sport=True
    return render_template("index.html",fav_players=fav_players,
     likes_same_sport=likes_same_sport)

if __name__ == '__main__':
   app.run(debug = True)