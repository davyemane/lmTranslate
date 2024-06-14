from easynmt import EasyNMT

model= EasyNMT('opus-mt')

sentences = ['In dieser Liste definieren wir mehrere Sätze.']
text= ['leo aime les belles filles']
translations = model.translate(text, target_lang='en')

print(f'the translation is:{translations}%')
