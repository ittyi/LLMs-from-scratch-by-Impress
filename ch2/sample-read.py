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
        if i >= 50:
            break
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
