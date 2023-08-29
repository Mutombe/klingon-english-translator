import argparse
import sys
import random
import csv

translations = {}

def load_translations_from_csv(file_path):
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            translations[row['english']] = {
                'translation': row['klingon'],
                'example': row['example'],
                'verb': row['verb']
            }
            
def translate_to_klingon(word):
    word = word.lower()
    if word in translations:
        return translations[word]['translation'], translations[word]['example']
    else:
        return None, None
    
def conjugate_verb(word, tense):
    word = word.lower()
    if word in translations and translations[word]['verb'] == 'yes':
        if tense == 'present':
            return word + 'a'
        elif tense == 'past':
            return word + 'ed'
        elif tense == 'future':
            return 'will ' + word
        else:
            return word

def random_translation():
    random_word = random.choice(list(translations.keys()))
    return random_word, translations[random_word]['translation']

def generate_flashcards(num_flashcards):
    flashcards = []
    words = random.sample(list(translations.keys()), num_flashcards)
    for word in words:
        translation = translations[word]['translation']
        flashcards.append({'word': word, 'translation': translation})
    return flashcards

def main():
    parser = argparse.ArgumentParser(description='Klingon Translation CLI')
    parser.add_argument('word', help='Word to translate or command to execute')
    parser.add_argument('-e', '--english-to-klingon', action='store_true',
                        help='Translate from English to Klingon')
    parser.add_argument('-c', '--conjugate', metavar='TENSE',
                        help='Conjugate a verb in the specified tense')
    parser.add_argument('-f', '--flashcards', dest='flashcards', metavar='NUM_FLASHCARDS', type=int, 
                        help='Generate flashcards for practicing Klingon')
    parser.add_argument('-l', '--load-csv', metavar='FILE', help='Load translations from a CSV file')
    
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(f"Argument parsing error: {e}")
        sys.exit(1)
        
    word =args.word
    if args.load_csv:
        load_translations_from_csv(args.load_csv)
        
    if args.english_to_klingon:
        translation, example = translate_to_klingon(word)
        if translation:
            print(f"{word} translates to Klingon as: {translation}")
            if example:
                print(f'Example: {example}')
            else:
                print(f'Translation for {word} not found !!')
        else:
            print(f'Translation for {word} not found !!')
                
    elif args.conjugate:
        conjugate_verb = conjugate_verb(word, args.conjugate)
        if conjugate_verb:
            print(conjugate_verb)
        else:
            print(f"Verb for {word} not found or conjugatable !")
        
    elif args.flashcards:
        flashcards = generate_flashcards(args.flashcards)
        print("Flashcards: ")
        for flashcard in flashcards:
            print(f"Word: {flashcard['word']}\tTranslation: {flashcard['translation']}")
    else:
        print('Please specify a valid command.')
        
if __name__ == '__main__':
    main()
