from easynmt import EasyNMT
import pickle


model= EasyNMT('opus-mt')

pickle.dump(model, open("best_model.pkl", "wb"))

print('all well done!')
