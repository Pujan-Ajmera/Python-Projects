from langdetect import detect
import pycountry
from translate import Translator

def get_language_name(language_code):
    try:
        language = pycountry.languages.get(alpha_2=language_code)
        return language.name if language else "Unknown Language"
    except:
        return "Unknown Language"

text = input("Enter any text in any language: ")
language_code = detect(text)

language_name = get_language_name(language_code)

print(f"The detected language is: {language_name}")


translateIt = input("Translate it ?(type yes if yes): ")
if(translateIt == "yes"):
    lang = input("enter the language in which you want to translate: ")
    translator= Translator(from_lang=language_name,to_lang=lang)
    translation = translator.translate(text)
    print(translation)

print("ThankYou")