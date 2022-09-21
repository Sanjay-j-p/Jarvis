from PyDictionary import PyDictionary
dictionary=PyDictionary()
query = 'regard'
stopwords = ['define']
querywords = query.split()
resultwords  = [word for word in querywords if word.lower() not in stopwords]
result = ''.join(resultwords)
rand = (dictionary.meaning(result))
print(rand)