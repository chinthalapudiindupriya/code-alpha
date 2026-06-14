from googletrans import Translator

translator = Translator()

print("=== Language Translation Tool ===")

text = input("Enter text: ")
src = input("Source language (e.g., en): ")
dest = input("Target language (e.g., hi): ")

translated = translator.translate(text, src=src, dest=dest)

print("\nTranslated Text:")
print(translated.text)
