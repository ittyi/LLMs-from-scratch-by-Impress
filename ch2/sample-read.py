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
