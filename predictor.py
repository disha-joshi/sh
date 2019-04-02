import pandas as pd
#%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# pass in column names for each CSV as the column name is not given in the file and read them using pandas.
# You can check the column names from the readme file

#Reading users file:
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('C:\\coldstart\\ml-100k\\u.user', sep='|', names=u_cols,encoding='latin-1')

#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('C:\\coldstart\\ml-100k\\u.data', sep='\t', names=r_cols,encoding='latin-1')

#Reading items file:
i_cols = ['movie_id', 'movie_title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('C:\\coldstart\\ml-100k\\u.item', sep='|', names=i_cols,
encoding='latin-1')

# print(users.shape)
# #print(users.head())
# print(users.sort_values(by='user_id', ascending=True))

# print(ratings.shape)
# #print(ratings.head())
# print(ratings.sort_values(by='movie_id', ascending=True))

# print(items.shape)
# print(items.head())
# #print(users.sort_values(by='user_id', ascending=True))

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_train = pd.read_csv('C:\\coldstart\\ml-100k\\ua.base',  sep='\t',names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('C:\\coldstart\\ml-100k\\ua.test', sep='\t', names=r_cols, encoding='latin-1')
ratings_train.shape, ratings_test.shape
#print(ratings_train.shape)
#print(ratings_test.shape)
#print(ratings_train.head)
#print(ratings_test.head)

n_users = ratings.user_id.unique().shape[0]
#print(n_users)
n_items = ratings.movie_id.unique().shape[0]
#print(n_items)

data_matrix = np.zeros((n_users, n_items))
for line in ratings.itertuples():
   data_matrix[line[1]-1, line[2]-1] = line[3]
   
# print("data matrix")
# print(data_matrix)

from sklearn.metrics.pairwise import pairwise_distances 
user_similarity = pairwise_distances(data_matrix, metric='cosine')
item_similarity = pairwise_distances(data_matrix.T, metric='cosine')
# print("user sim")
# print(user_similarity)
# print("item sim")
# print(item_similarity)

def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        #We use np.newaxis so that mean_user_rating has same format as ratings
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
    return pred
#print(pred)

def similarityPrediction(Twodlist):
   user = {}
   count = 0
   #print("\n\n List val\n\n")
   
   #print(str(Twodlist[0]))
   for i in Twodlist:
      user[str(count)] = getMaxIndex(i)
      count = count + 1
   return user

def getMaxIndex(listed):
   count = 0
   index = 0
   max  = -1
   for i in listed:
      if max < i:
         max = i
         index = count
      count = count+1
   return index

def similarityPredictionItem(Twodlist):
   user = {}
   count = 0
#   print("\n\n List val\n\n")
   
  # print(str(Twodlist[0]))
   for i in Twodlist:
      user[str(count)] = getMaxIndexItem(i, 5)
      count = count + 1
   return user

def getMaxIndexItem(list1, N):
    my_list = list(list1)
    my_list1 = list(list1)
    final_list = []
    for i in range(0, N):
        max1 = -1
        count = 0
        for j in my_list:      
            if j > max1: 
                max1 = j
                index = count
            count= count + 1
        my_list.remove(my_list[index])
        final_list.append(my_list1.index(my_list[index]))
        
          
    return final_list

user_prediction = predict(data_matrix, user_similarity, type='user')
item_prediction = predict(data_matrix, item_similarity, type='item')
# print("user_prediction")
# print(user_prediction)
# print("item_prediction")
# print(item_prediction)

user = {}
user= similarityPrediction(user_similarity)
#print(str(user))

iItem = {}
iItem= similarityPredictionItem(item_similarity)
#print(str(iItem))

#count = 0
#print(str(user['1']))
def getMovie(a, ratedData):
   for i in range(len(items)):
      if ratedData.movie_id.iloc[a] == items.movie_id.iloc[i]:
         break
   return i

def predictUserMovie(x):
    ratedData = ratings[ratings.user_id == user[x]].sort_values(by='rating', ascending=False)
   #print(ratedData)
   #print(ratedData.movie_id.iloc[1] == items.movie_id.iloc[1])
    n = []
    for i in range(5):       #          ................................... number of movies to predict
       s = (items.movie_title.iloc[getMovie(i, ratedData)])
       n.append(s)
    return n
       

def predictItemMovie(x):

   for i in range(5):       #          ................................... number of movies to predict
      print(items[items.movie_id == iItem[x][i]].movie_title)



def a(a):
        x = similarityPredictionItem(item_similarity)
        listed = []
        listed = x[a]
        m = []
 #       print(listed)
        for i in listed:
            m.append(items.loc[i-1]['movie_title'])
        return m


