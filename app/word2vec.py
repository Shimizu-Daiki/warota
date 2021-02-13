import logging #学習履歴出すため
from gensim.models import word2vec #word2vecをインポート

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) #ログの付加情報を記載

sentences = word2vec.Text8Corpus('../warota/app/ja.text8')
model = word2vec.Word2Vec(sentences, size=200)
model.save("word2vec.model")
