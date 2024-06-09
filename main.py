from pymongo import MongoClient
import pandas as pd

# 1. Connect to the MongoDB database
mongo_uri = "mongodb://localhost:27017"
client = MongoClient(mongo_uri)
db = client['Emailme']
collection = db['6665a1f77528525616cdcdf6']

# 2. Query the database
query = {}  # You can specify your query here
documents = collection.find(query)

# 3. Process the data
documents_list = list(documents)
df = pd.DataFrame(documents_list)
print(df)

# 4. Close the connection
client.close()
