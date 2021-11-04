import pickle

root = "file/"

f = open(root+"list.pickle", "wb")
test = [1,2,3,4,5]
pickle.dump(test, f)
f.close

del test

f = open(root+"list.pickle","rb")
test = pickle.load(f)
f.close

print(test)