import re

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
    
print("Total number of character:", len(raw_text))
print(raw_text[:99])

text = "Hello, world. This is a test"
result = re.split(r'(\s)', text)
print(result)
# ['Hello,', ' ', 'world.', ' ', 'This', ' ', 'is', ' ', 'a', ' ', 'test']

result = re.split(r'([,.]|\s)', text)
print(result)
# ['Hello', ',', '', ' ', 'world', '.', '', ' ', 'This', ' ', 'is', ' ', 'a', ' ', 'test']

result = [item for item in result if item.strip()]
print(result)
# ['Hello', ',', 'world', '.', 'This', 'is', 'a', 'test']

text = "Hello, world. Is this-- a test?"
result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
# ['Hello', ',', '', ' ', 'world', '.', '', ' ', 'Is', ' ', 'this', '--', '', ' ', 'a', ' ', 'test', '?', '']
result = [item.strip() for item in result if item.strip()]
print(result)
# ['Hello', ',', 'world', '.', 'Is', 'this', '--', 'a', 'test', '?']

preprocessed = re.split('([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
# 4690
print(preprocessed[:30])
# ['I', 'HAD', 'always', 'thought', 'Jack', 'Gisburn', 'rather', 
# 'a', 'cheap', 'genius', '--', 'though', 'a', 'good', 'fellow', 
# 'enough', '--', 'so', 'it', 'was', 'no', 'great', 'surprise', 
# 'to', 'me', 'to', 'hear', 'that', ',', 'in']

# 2.3 トークンをトークンIDに変換する
all_word = sorted(set(preprocessed))
vocab_size = len(all_word)
print(vocab_size)
# 1130

vocab = {token: integer for integer, token in enumerate(all_word)}

for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 10:
        break
# i >= 50: の時↓
# ('!', 0)
# ('"', 1)
# ("'", 2)
# ('(', 3)
# (')', 4)
# (',', 5)
# ('--', 6)
# ('.', 7)
# (':', 8)
# (';', 9)
# ('?', 10)
# ('A', 11)
# ('Ah', 12)
# ('Among', 13)
# ('And', 14)
# ('Are', 15)
# ('Arrt', 16)
# ('As', 17)
# ('At', 18)
# ('Be', 19)
# ('Begin', 20)
# ('Burlington', 21)
# ('But', 22)
# ('By', 23)
# ('Carlo', 24)
# ('Chicago', 25)
# ('Claude', 26)
# ('Come', 27)
# ('Croft', 28)
# ('Destroyed', 29)
# ('Devonshire', 30)
# ('Don', 31)
# ('Dubarry', 32)
# ('Emperors', 33)
# ('Florence', 34)
# ('For', 35)
# ('Gallery', 36)
# ('Gideon', 37)
# ('Gisburn', 38)
# ('Gisburns', 39)
# ('Grafton', 40)
# ('Greek', 41)
# ('Grindle', 42)
# ('Grindles', 43)
# ('HAD', 44)
# ('Had', 45)
# ('Hang', 46)
# ('Has', 47)
# ('He', 48)
# ('Her', 49)
# ('Hermia', 50)

# シンプルなテキストトークナイザ
class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab# encode, decode メソッドでアクセスできるように語彙をクラス属性として格納
        self.int_to_str = {i:s for s,i in vocab.items()}# トークンIDを元のテキストトークンにマッピングする逆引き語彙を作成
    
    # 入力テキストをトークンIDに変換
    def encode(self, text):
        preprocessed = re.split('([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    
    # トークンを変換してテキストに戻す
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)# 指定された句読点の前にあるスペースを削除
        return text

tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know,"
           Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)
# painted. の場合 [1, 56, 2, 850, 988, 602, 533, 746, 7, 1126, 596, 5, 1, 67, 7, 38, 851, 1108, 754, 793, 7]
# painted, の場合 [1, 56, 2, 850, 988, 602, 533, 746, 5, 1126, 596, 5, 1, 67, 7, 38, 851, 1108, 754, 793, 7]

print(tokenizer.decode(ids))
# " It' s the last he painted, you know," Mrs. Gisburn said with pardonable pride.

# tokenizer にまだない語彙で実行するとエラーになる。
text = "Hello, do you like tea?"
# print(tokenizer.encode(text))
# KeyError: 'Hello'
# このことから、語彙を増やすために大規模で多様な訓練データセットを考慮する必要があることがわかる。

all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<[endoftext]>", "<unk>"])
vocab = {token:integer for integer,token in enumerate(all_tokens)}

print(len(vocab.items()))
# 1132 # ここ以前（42 行目）の語彙のサイズは 1130 だったけど 2 つ追加された

for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)
# ('younger', 1127)
# ('your', 1128)
# ('yourself', 1129)
# ('<[endoftext]>', 1130)
# ('<unk>', 1131)

class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab# encode, decode メソッドでアクセスできるように語彙をクラス属性として格納
        self.int_to_str = {i:s for s,i in vocab.items()}# トークンIDを元のテキストトークンにマッピングする逆引き語彙を作成
    
    # 入力テキストをトークンIDに変換
    def encode(self, text):
        preprocessed = re.split('([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        preprocessed = [# 未知の単語を<unk>トークンに置き換える
            item if item in self.str_to_int
            else "<unk>" for item in preprocessed
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    
    # トークンを変換してテキストに戻す
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)# 指定された句読点の前にあるスペースを削除
        return text

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <endoftext> ".join((text1, text2))
print(text)
# Hello, do you like tea? <endoftext> In the sunlit terraces of the palace.

tokenizer = SimpleTokenizerV2(vocab)
print(tokenizer.encode(text))
# [1131, 5, 355, 1126, 628, 975, 10, 1131, 55, 988, 956, 984, 722, 988, 1131, 7]
# <endoftext> が 1130, <unk> が 1131

print(tokenizer.decode(tokenizer.encode(text)))
# <unk>, do you like tea? <unk> In the sunlit terraces of the <unk>.
# 「The Verdict」 に Hello, place は含まれていないため置き換わっている。

from importlib.metadata import version
import tiktoken

print("tiktoken version:", version("tiktoken"))
# tiktoken version: 0.9.0

