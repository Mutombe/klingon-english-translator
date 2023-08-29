import unittest
from translation import load_translations_from_csv, translate_to_klingon, conjugate_verb, generate_flashcards

class TranslationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_translations_from_csv('data.csv')

    def test_translate_to_klingon_existing_word(self):
        translation, example = translate_to_klingon('hello')
        self.assertEqual(translation, 'nuqneH')
        self.assertEqual(example, "nuqneH 'oH Qap?")
        
    
    def test_translate_to_klingon_nonexistent_word(self):
        translation, example = translate_to_klingon('unknown')
        self.assertIsNone(translation)
        self.assertIsNone(example)
    
    def test_conjugate_verb_present_tense(self):
        conjugated_verb = conjugate_verb('run', 'present')
        self.assertEqual(conjugated_verb, 'runa')
    
    def test_conjugate_verb_past_tense(self):
        conjugated_verb = conjugate_verb('play', 'past')
        self.assertEqual(conjugated_verb, 'played')
    
    def test_conjugate_verb_future_tense(self):
        conjugated_verb = conjugate_verb('sing', 'future')
        self.assertEqual(conjugated_verb, 'will sing')
    
    def test_conjugate_verb_invalid_tense(self):
        conjugated_verb = conjugate_verb('jump', 'invalid')
        self.assertIsNone(conjugated_verb)
    
    def test_generate_flashcards(self):
        flashcards = generate_flashcards(3)
        self.assertEqual(len(flashcards), 3)
        for flashcard in flashcards:
            self.assertIn('word', flashcard)
            self.assertIn('translation', flashcard)

if __name__ == '__main__':
    unittest.main()