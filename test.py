import pickle

try:
    with open("movie_list.pkl", "rb") as f:
        data = pickle.load(f)
    print("Pickle file loaded successfully!")
    print(data.head())  # Print the first few rows if it's a DataFrame
except Exception as e:
    print("Error loading pickle file:", e)
