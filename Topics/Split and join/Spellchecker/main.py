dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input().split()
incorrect_words = [x for x in sentence if x not in dictionary]
if incorrect_words:
    print('\n'.join(incorrect_words))
else:
    print('OK')
