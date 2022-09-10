import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML

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

automl = AutoML(
    mode="Explain", 
    eval_metric="r2", 
    explain_level=2, 
    golden_features=False, 
    ml_task="regression",
    #validation_strategy={},
    random_state=42,
)
automl.fit(X_train, y_train)

df_issues_test['summary_vectorized'] = df_issues_test.apply(lambda row: to_vec(row['summary']), axis=1)
df_issues_test['summary_cluster'] = df_issues_test.apply(lambda row: kmeans.predict([row['summary_vectorized']])[0], axis=1)
predictions = automl.predict(df_issues_test[['project_id', 'summary_cluster']])
df_result = pd.DataFrame()
df_result["id"] = df_issues_test["id"]
df_result["overall_worklogs"] = predictions.astype(np.int64)
df_result.to_csv('target/solution.csv', index=False)

