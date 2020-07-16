# pip install googletrans

from googletrans import Translator
sentence = str(input("say..."))
translator = Translator()
translated_sentence = translator.translate(sentence,src='en',dest='bn')
print(translated_sentence.text)