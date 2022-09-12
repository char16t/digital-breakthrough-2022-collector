import blobcity as bc

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk
from solution.logging import rootLogger
from solution.train_doc2vec_summary import build_d2v_summary_model 
from solution.load_data import \
    df_issues_train, \
    df_comment_train, \
    df_emp, \
    df_issues_test, \
    df_comment_test, \
    merged, \
    X_train, \
    X_test, \
    y_train, \
    y_test


build_d2v_summary_model()
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

# ------------------------------------------------

model = bc.train(df=my_df, target="Y_column")
model.spill("my_code.py")
model.spill("my_code.ipynb")
