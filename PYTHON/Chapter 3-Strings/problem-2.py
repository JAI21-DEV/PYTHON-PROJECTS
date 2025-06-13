letter = '''Dear <|name|>,
You are selected!
<|date|>'''

print(letter.replace("<|name|>" , "Jai").replace("<|date|>" , "29 nov. 2003"))