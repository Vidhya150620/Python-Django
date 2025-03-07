import pymongo

client = pymongo.MongoClient("mongodb+srv://svaithi2004:yHc4GWxLSBeuGj-@cluster0.to7xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["test"]
myCollection = db["products"]
myCollection2 = db["categories"]
