import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from solution.load_data import \
    df_issues_train, \
    df_comment_train, \
    df_emp, \
    df_issues_test, \
    df_comment_test, \
    merged

# Кластеризируем задачи по summary
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(merged["summary"])]
# max_epochs = 100
# vec_size = 20
# alpha = 0.025

# model = Doc2Vec(vector_size=vec_size,
#                 alpha=alpha, 
#                 min_alpha=0.00025,
#                 min_count=1,
#                 dm =0)
  
# model.build_vocab(tagged_data)

# for epoch in range(max_epochs):
#     print('iteration {0}'.format(epoch))
#     model.train(tagged_data,
#                 total_examples=model.corpus_count,
#                 epochs=model.epochs)
#     # decrease the learning rate
#     model.alpha -= 0.0002
#     # fix the learning rate, no decay
#     model.min_alpha = model.alpha

# model.save("target/d2v.model")

model= Doc2Vec.load("target/d2v.model")

def cast_vector(row):
    r = np.array(list(map(lambda x: x.astype('double'), row)))
    return r
    
def to_vec(text):
  test_data = word_tokenize(text.lower())
  return cast_vector(model.infer_vector(test_data))

vectors = []
for s in merged["summary"]:
  vectors.append(to_vec(s))
vecs = pd.DataFrame(vectors)
vecs.head()
merged["summary_vectorized"] = vectors

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=100, random_state=42) 
kmeans.fit(vecs)

res = pd.DataFrame()
res["kmean"] = kmeans.labels_
res['kmean'].value_counts()
merged["summary_cluster"] = res["kmean"]

X_train, X_test, y_train, y_test = train_test_split(
    merged[['project_id', 'summary_cluster']],
    merged[['overall_worklogs']],
    test_size=0.33, 
    random_state=42,
)


from sklearn.dummy import DummyRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from xgboost import XGBRegressor

for strategy in ["mean", "median"]:
  dummy = DummyRegressor(strategy=strategy)
  dummy.fit(X_train, y_train)
  y_pred = dummy.predict(X_test)
  print("DummyRegressor [strategy=" + strategy + "], R2: " + str(r2_score(y_test, y_pred)))

regressor = DecisionTreeRegressor(random_state=42)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("DecisionTreeRegressor, R2: " + str(r2_score(y_test, y_pred)))

reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print("LinearRegression, R2: " + str(r2_score(y_test, y_pred)))

bst = XGBRegressor()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print("XGBRegressor, R2: " + str(r2_score(y_test, y_pred)))

reg = RandomForestRegressor()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print("RandomForestRegressor, R2: " + str(r2_score(y_test, y_pred)))
