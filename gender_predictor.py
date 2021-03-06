import pickle

classifier = pickle.load(open('models/gender_model2.sav', 'rb'))
cv = pickle.load(open('data/corpus.sav', 'rb'))

while True:
    name = input('Input Name:')
    name = cv.transform([name]).toarray()
    predval = classifier.predict(name)
    predprob = classifier.predict_proba(name)
    print('Gender: '+predval[0])
    if predval[0] == 'm':
    	print(f'Confidence : {predprob[0][1]*100}%')
    else:
    	print(f'Confidence : {predprob[0][0]*100}%')