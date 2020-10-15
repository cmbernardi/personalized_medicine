import pandas as pd
import nltk
#nltk.download('wordnet')
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
import string

# Read datasets
df_train = pd.read_csv('df_train')
df_test = pd.read_csv('df_test')

def pre_processing(text):

	# Lowercasing
	text = text.lower()
	
	# Removing punctuation
	text = ''.join([char for char in text if char not in string.punctuation])
	
	# Tokenization
	text = word_tokenize(text)

	# Stopwords filtering
	stop = stopwords.words('english')
	text = [w for w in text if w not in stop]

	# Removing numbers
	text = [x for x in text if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]

	# Lemmatisation (convert the word into root word)
	lem = WordNetLemmatizer()
	text = [lem.lemmatize(word) for word in text]

	# Back to string from list
	text = " ".join(text)

	return text

df_train.Text = df_train.Text.apply(lambda x: pre_processing(x))
print(df_train.Text[0])
df_train.to_csv('df_train_processed', index=False)

df_test.Text = df_test.Text.apply(lambda x: pre_processing(x))
print(df_test.Text[0])
df_test.to_csv('df_test_processed', index=False)
