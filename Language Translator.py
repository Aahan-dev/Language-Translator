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


   