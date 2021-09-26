phrase = input()
if '_' in phrase:
    phrase = phrase.split('_')
    phrase = [x.capitalize() for x in phrase]
    new_phrase = ''.join(phrase)
else:
    new_phrase = phrase.capitalize()
print(new_phrase)
