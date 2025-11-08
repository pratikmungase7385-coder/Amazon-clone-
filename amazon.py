from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
   
    boxes = [
        {"title": "Easy updates elevated", "img": "images/13.avif", "text": "See more"},
        {"title": "Shop for your home", "img": "images/3.webp", "text": "Discover more in home"},
        {"title": "Shop Fashion for less", "img": "images/4.jpg", "text": "See all deals"},
        {"title": "Score the top PCs", "img": "images/5.jpg", "text": "More"},
        {"title": "Level up your beauty", "img": "images/14.jpg", "text": "See more"},
        {"title": "Cloths", "img": "images/7.jpg", "text": "More"},
        {"title": "Books", "img": "images/10.webp", "text": "See all deals"},
        {"title": "Smartphones", "img": "images/8.jpeg", "text": "Discover more"},
    ]

   
    special_boxes = [
        {"img": "images/12.webp", "link": "motophone"},
        {"img": "images/13.webp"},
        {"img": "images/16.webp"},
    ]

    return render_template("amazon.html", boxes=boxes, special_boxes=special_boxes)




@app.route("/matophone")
def motophone():
    return render_template("motophone.html")







app.run(port=4000,debug=True)