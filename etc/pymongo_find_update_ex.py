from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

## 코딩 할 준비 ##

# 1 매트릭스 평점
movie = db.movies.find_one({'title':'매트릭스'})
movie_star= movie['star']

print('--Quiz 1--')
print(movie_star)

# 2 매트릭스와 평점이 같은 것들 제목
print('--Quiz 2--')
movie2_list = list(db.movies.find({'star': movie_star}))
for movie2 in movie2_list:
    print(movie2['title'])

# 3 매트릭스와 평점이 같은 것들 평점 0으로 세팅
print('--Quiz 3--')
for movie2 in movie2_list:
    db.movies.update_one({'star':movie_star}, {'$set':{'star':0}})

# Same function --
 # db.movies.update_many({'star':target_star},{'$set':{'star':0}})

 