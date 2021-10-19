# Batch Translator
It is a simple code to retrieve related information such as definition, translation, synonyms and, antonyms for given words list. Words are read from a text file named 'words.txt' which is located in same path as the python file. After processing words, retrieved information will be saved into a CSV file named 'words.csv'.

### WordNet
The [WordNet](https://www.nltk.org/howto/wordnet.html) is a part of Python's Natural Language Toolkit. It is a large word database of English Nouns, Adjectives, Adverbs and Verbs. These are grouped into some set of cognitive synonyms, which are called **synsets**.
To use the Wordnet, at first we have to install the NLTK module, then download the WordNet package.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required package:
```bash
pip install nltk
```
```bash
>>> import nltk
>>> nltk.download('wordnet')
```
### Deep Translator
[Deep_Translator](https://pypi.org/project/deep-translator/) is a flexible python package to translate between different languages in a simple way. Basically, the goal of the package is to integrate many translators including  [**Google Translator**](https://translate.google.com/)**, DeepL,** [**Pons**](http://pons.com/)**,** [**Linguee**](https://www.linguee.com/) **and** [**o**](https://mymemory.translated.net/)**thers** in one extensive tool. 

The google translator is already integrated in the deep_translator package and can be directly used by importing it. Then, an instance is created, where the source and target language are given as arguments. The translate method can be used afterwards to return the translated text.

Use pip package manager to install required package:
```bash
pip install deep_translator
```
I assumed the source language is English and the target is Persian. Change source and target languages as you like.

## Usage
To run the batch-translator, first type your desired words into a file named '**words.txt**' (sample file included), then simply start the program by using this command:
```python
python run batch-translator.py
```
It will process all given words and finally will create a csv file named 'words.csv' which has multiple columns:

    word, definition, translation, synonyms, antonyms, examples
Import the generated csv data with Microsoft Excel through Data tab -> From Text/CSV icon.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
