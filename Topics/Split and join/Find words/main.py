sentence = input().split()
words = [word for word in sentence if word.endswith('s')]
print('_'.join(words))
