import random #ランダム抽出で使う
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from gensim.models import Word2Vec

text = '目から鱗'

token_filters = [CompoundNounFilter()] #こっち使う
a = Analyzer(token_filters=token_filters)
tokens=a.analyze(text)
word_list=[]
stop_word_set = set(['た','ない','が','じゃ', 'なく','では','は', 'の', 'に', 'を' ,'て', 'さ', 'から', 'も', 'として', 'な', 'や', 'など', 'まで', 'へ','という', 'により', 'による', 'によって', 'か', 'において', 'について', 'のみ', 'における', 'だけ', 'にて', 'とともに', 'ながら', 'に対して', 'と共に', 'ものの', 'にかけて', 'たり', 'ほど', 'ので', 'といった', 'に関する', 'に', '対する', 'に対し', 'ん', 'しか', 'にとって', 'つつ', 'に関して', 'わ', 'なさ', 'を通じて', 'よ', 'ずつ', 'ばかり', 'にわたって', 'にあたる', 'ね', 'にも', 'こそ', 'を通して', 'かい', 'に際して', 'のに', 'をもって', 'さえ', 'にわたり', 'すら', 'に従って', 'にあたって', 'って', 'にわたる', 'にあたり', 'に従い', 'べ', 'ぜ', 'ぞ', 'ど', 'け', 'か所', 'にし', 'につき', 'ねん', 'に当たる', 'に際し', 'につれて', 'とか', 'だり', 'につれ', 'をめぐって', 'てん', 'もん', 'に当たって', 'にまつわる', 'の子', 'にあ', 'は元', 'を以て', 'デ', 'ぐらい', 'にかけ', 'やら', 'かな', 'しも', 'なんて', 'に関し', 'で', 'ある', '。', '、' ])
model = Word2Vec.load("word2vec.model")

for token in tokens: #品詞情報と表層系を取得、助詞は最初から弾く
    surface = token.surface #表層形を取得
    hinshi = token.part_of_speech.split(',')[0] #品詞情報のみ抽出
    if surface not in stop_word_set and hinshi == "動詞" or '名詞' or '形容詞':
        if random.random() > 0.5: #順番に、50%の確立でランダム抽出を行うかどうか
            result = model.most_similar(surface)[0][0]
            print(result)
            word_list.append(result)
        else: #そのままword_listに追加
            word_list.append(surface)
    else: #名詞でなければそのままword_listに追加
        word_list.append(surface)
#print("".join(word_list)) #文字列をくっつけて表示
change_word = "".join(word_list)
print(change_word)