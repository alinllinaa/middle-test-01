import re

def count_words_and_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Рахуємо речення
    sentence_endings = r'\.{3}|[.!?]'
    sentences = re.findall(sentence_endings, text)
    num_sentences = len(sentences)

    # Рахуємо слова
    separators = r'[\s,;:]+'
    words = re.split(separators, text.strip())
    words = [word for word in words if word]
    num_words = len(words)

    return num_words, num_sentences

if __name__ == "__main__":
    file_path = "text.txt"
    words, sentences = count_words_and_sentences(file_path)
    print(f"Слів: {words}")
    print(f"Речень: {sentences}")
