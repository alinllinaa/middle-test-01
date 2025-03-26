import pytest
from main import count_words_and_sentences

@pytest.fixture
def simple_text(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Привіт! Це тестовий файл. Тут два речення?")
    return file

def test_count_words_and_sentences(simple_text):
    words, sentences = count_words_and_sentences(simple_text)
    assert words == 7
    assert sentences == 3
