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
