import csv

articleslist = []

with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    articleslist = data[1:]

likedarticles = []
dislikedarticles = []