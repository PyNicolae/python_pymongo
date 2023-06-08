from pymongo import MongoClient

client = MongoClient()
db = client.movie

movies = db.movies

movie_title = input("Enter the movie title: ")
movie_gender = input("Enter the movie gender: ")
movie_year = input("Enter movie's launch year: ")

movie_details={
    'title': movie_title,
    'gender': movie_gender,
    'year':movie_year
}

movies.insert_one(movie_details)

querryresult = movies.find()

for r in querryresult:
    print("Movie: {}| Gender: {}| Year:{}".format(r['title'],r['gender'],r['year']))
