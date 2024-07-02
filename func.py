from googletrans import Translator
vocabulary = {
    "тепер":"pen"
}
Spisok = []
Final = ""
# Translate a sentence from Ukrainian to English
translator = Translator()
text_ukrainian = input()
Language = input('choose the language en/fr/de') 
classic =  text_ukrainian.lower().split(" ")
for word in classic:
    if word in vocabulary:
        res = vocabulary[word]
    else:
        res = word
    Spisok.append(res)
for word in  Spisok:
    Final += word + " "
translated_text = translator.translate(Final, dest=Language)

print(translated_text.text)
'''
print("Перекладений текст:", translated_text.text)

# Function to translate a single word
def translate_word(word, dest_language='en'):
    translator = Translator()
    translated_word = translator.translate(word, dest=dest_language)
    return translated_word.text

# Function to translate a phrase word by word
def translate_phrase(phrase, dest_language='en'):
    translated_phrase = []
    for word in phrase.split():
        translated_word = translate_word(word, dest_language)
        translated_phrase.append(translated_word)
    return ' '.join(translated_phrase)

ukrainian_phrase = "Привіт, як справи?"
foreign_language = 'fr'  # Change to the desired language code
foreign_phrase = translate_phrase(ukrainian_phrase, foreign_language)
print("Translated phrase:", foreign_phrase)

'''