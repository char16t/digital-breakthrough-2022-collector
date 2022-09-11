Install dependencies:

```sh
make install_deps
```

Generate solution (`target/solution.csv`):

```sh
make solve
```

# Problems and solutions

Problem:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/mbertoni/software/miniconda3/envs/test/lib/python3.7/site-packages/gensim/__init__.py", line 11, in <module>
    from gensim import parsing, corpora, matutils, interfaces, models, similarities, utils  # noqa:F401
  File "/home/mbertoni/software/miniconda3/envs/test/lib/python3.7/site-packages/gensim/corpora/__init__.py", line 6, in <module>
    from .indexedcorpus import IndexedCorpus  # noqa:F401 must appear before the other classes
  File "/home/mbertoni/software/miniconda3/envs/test/lib/python3.7/site-packages/gensim/corpora/indexedcorpus.py", line 14, in <module>
    from gensim import interfaces, utils
  File "/home/mbertoni/software/miniconda3/envs/test/lib/python3.7/site-packages/gensim/interfaces.py", line 19, in <module>
    from gensim import utils, matutils
  File "/home/mbertoni/software/miniconda3/envs/test/lib/python3.7/site-packages/gensim/matutils.py", line 1024, in <module>
    from gensim._matutils import logsumexp, mean_absolute_difference, dirichlet_expectation
  File "gensim/_matutils.pyx", line 1, in init gensim._matutils
ValueError: numpy.ndarray size changed, may indicate binary incompatibility. Expected 88 from C header, got 80 from PyObject
```

Solution:

```sh
pip uninstall gensim
pip install gensim --no-binary :all:
```
