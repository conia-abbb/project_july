#words = ["shut", "up", "and", "dance", "with", "me"]
#root = [len(word) for word in words]
#print(root)

words = ["shut", "up", "and", "dance", "with", "me"]
root = [len(word) for word in words if word != "and"]
print (root)