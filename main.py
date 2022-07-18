from flask import Flask, jsonify, request

from storage import articleslist, likedarticles, dislikedarticles
from demographic import output
from contentfilter import get_recommendations

app = Flask(__name__)

@app.route("/getarticle")
def getarticle():
    articledata = {
        "url": articleslist[0][11],
        "title": articleslist[0][12],
        "text": articleslist[0][13],
        "lang": articleslist[0][14],
        "total_events": articleslist[0][15]
    }
    return jsonify({
        "data": articledata,
        "status": "success"
    })

@app.route("/likedarticle")
def likedarticle():
    article = articleslist[0]
    likedarticles.append(article)
    articleslist.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/dislikedarticle")
def dislikedarticle():
    article = articleslist[0]
    dislikedarticles.append(article)
    articleslist.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/populararticle")
def populararticle():
    articledata = []
    for article in output:
        _d = {
           "url": article[0],
            "title": article[1],
            "text": article[2],
            "lang": article[3],
            "total_events": article[4] 
        }
        articledata.append(_d)
    return jsonify({
        "data": articledata,
        "status": "success"
    }), 200

@app.route("/recommendedarticle")
def recommendedarticle():
    recommendedarticles = []
    for likedarticle in likedarticles:
        output = get_recommendations(likedarticle[4])
        for data in output:
            recommendedarticle.append(data)
    import itertools
    recommendedarticle.sort()
    recommendedarticle = list(recommendedarticle for recommendedarticle,_ in itertools.groupby(recommendedarticle))
    articledata = []
    for recommended in recommendedarticle:
        _d = {
            "url": recommended[0],
            "title": recommended[1],
            "text": recommended[2],
            "lang": recommended[3],
            "total_events": recommended[4] 
        }
        articledata.append(_d)
    return jsonify({
        "data": articledata,
        "status": "success"
    }), 200


if __name__ = "__main__":
    app.run()