from googletrans import Translator, LANGUAGES


class LanguageTranslator:
    def __init__(self):
        """Initialize the Language Translator with a Translator instance."""
        self.translator = Translator()  # Create a translator object


    def translate(self, text, src_lang, dest_lang):
        """
        Translate text from a source language to a destination language.


        Args:
            text (str): The text to translate.
            src_lang (str): The source language code.
            dest_lang (str): The destination language code.


        Returns:
            str: The translated text.
        """
        try:
            # Perform the translation
            translated = self.translator.translate(text, src=src_lang, dest=dest_lang)
            return translated.text  # Return the translated text
        except Exception as e:
            return f"Error: {str(e)}"  # Return error message if translation fails


    def display_languages(self):
        """Display available languages for translation."""
        print("Available languages:")
        for lang_code, lang_name in LANGUAGES.items():
            print(f"{lang_code}: {lang_name}")




def main():
    """Main function to run the Language Translator."""
    translator = LanguageTranslator()  # Create an instance of the LanguageTranslator




    # Display available languages
    translator.display_languages()




    # Get user input for text to translate
    text_to_translate = input("Enter text to translate: ")
    src_lang = input("Enter source language code (e.g., 'en' for English): ")
    dest_lang = input("Enter destination language code (e.g., 'es' for Spanish): ")




    # Perform translation
    translated_text = translator.translate(text_to_translate, src_lang, dest_lang)




    # Display the translated text
    print("Translated text:", translated_text)




if __name__ == "__main__":
    main()  # Run the main function