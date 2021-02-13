from django.shortcuts import render, redirect

from .models import User, Problem, Answer
from .forms import ProblemForm
from .answer_form import AnswerForm
#from use_word2vec import *

def index(request):
  posts = Problem.objects.all()
  return render(request, 'index.html', {'posts':posts})

def get_create_form(request):
  if request.method == "POST":
        form = ProblemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('index')
  else:
      form = ProblemForm()
  return render(request, 'form.html', {'form': form})

def show(request, pk):
  titles = Problem.objects.get(pk=pk)
  answers = Answer.objects.all()
  return render(request, 'show.html', { 'answers':answers, 'titles':titles  })

def get_answer_form(request):
  if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect("index")
  else:
      form = AnswerForm()
  return render(request, 'answer.html', {'form': form}) 

import random #ランダム抽出で使う
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from gensim.models import Word2Vec
from .word2vec import *

def swap_word(request, pk):

    post = Answer.objects.get(pk=pk)
    text = post.text

    token_filters = [CompoundNounFilter()] #こっち使う
    a = Analyzer(token_filters=token_filters)
    tokens=a.analyze(text)
    word_list=[]
    stop_word_set = set(['た','ない','が','じゃ', 'なく','では','は', 'の', 'に', 'を' ,'て', 'さ', 'から', 'も', 'として', 'な', 'や', 'など', 'まで', 'へ','という', 'により', 'による', 'によって', 'か', 'において', 'について', 'のみ', 'における', 'だけ', 'にて', 'とともに', 'ながら', 'に対して', 'と共に', 'ものの', 'にかけて', 'たり', 'ほど', 'ので', 'といった', 'に関する', 'に', '対する', 'に対し', 'ん', 'しか', 'にとって', 'つつ', 'に関して', 'わ', 'なさ', 'を通じて', 'よ', 'ずつ', 'ばかり', 'にわたって', 'にあたる', 'ね', 'にも', 'こそ', 'を通して', 'かい', 'に際して', 'のに', 'をもって', 'さえ', 'にわたり', 'すら', 'に従って', 'にあたって', 'って', 'にわたる', 'にあたり', 'に従い', 'べ', 'ぜ', 'ぞ', 'ど', 'け', 'か所', 'にし', 'につき', 'ねん', 'に当たる', 'に際し', 'につれて', 'とか', 'だり', 'につれ', 'をめぐって', 'てん', 'もん', 'に当たって', 'にまつわる', 'の子', 'にあ', 'は元', 'を以て', 'デ', 'ぐらい', 'にかけ', 'やら', 'かな', 'しも', 'なんて', 'に関し', 'で', 'ある', '。', '、' ])
    model = Word2Vec.load("word2vec.model")

    for token in tokens: #品詞情報と表層系を取得、助詞は最初から弾く
        surface = token.surface #表層形を取得
        hinshi = token.part_of_speech.split(',')[0] #品詞情報のみ抽出
        if surface not in stop_word_set and hinshi == '名詞' or '形容詞':
            if random.random() > 0.5: #順番に、50%の確立でランダム抽出を行うかどうか
                result = model.most_similar(surface)[0][0]
                #print(result)
                word_list.append(result)
            else: #そのままword_listに追加
                word_list.append(surface)
        else: #名詞でなければそのままword_listに追加
            word_list.append(surface)
    #print("".join(word_list)) #文字列をくっつけて表示
    change_word = "".join(word_list)
    return render(request, 'ai_answer.html', {'change_word':change_word}) 

def delete(request, pk):
  post = Problem.objects.get(pk=pk)
  post.delete()
  return redirect('index')

def answer_delete(request, pk):
  answer = Answer.objects.get(pk=pk)
  answer.delete()
  return redirect("index")





