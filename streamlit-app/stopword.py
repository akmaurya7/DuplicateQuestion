import pickle
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
stop_words = stopwords.words('english')

# Save it to a pickle file
with open('stopwords.pkl', 'wb') as f:
    pickle.dump(stop_words, f)
