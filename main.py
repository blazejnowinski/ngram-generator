import json
from collections import Counter
import random

def generuj_ngramy(nazwa_pliku_wejsciowego, slowa):
    """
    Przetwarza listę słów, generuje ngramy, liczy ich wystąpienia,
    a następnie tworzy ważone i przetasowane listy.
    """
    print("Rozpoczynam generowanie ngramów...")
    
    # Liczniki dla poszczególnych n-gramów
    bigram_counts = Counter()
    trigram_counts = Counter()
    tetragram_counts = Counter()

    # Pętla przez każde słowo z listy
    for word in slowa:
        # Generowanie bigramów (sekwencje 2-literowe)
        if len(word) >= 2:
            for i in range(len(word) - 1):
                bigram_counts[word[i:i+2]] += 1
        
        # Generowanie trigramów (sekwencje 3-literowe)
        if len(word) >= 3:
            for i in range(len(word) - 2):
                trigram_counts[word[i:i+3]] += 1

        # Generowanie tetragramów (sekwencje 4-literowe)
        if len(word) >= 4:
            for i in range(len(word) - 3):
                tetragram_counts[word[i:i+4]] += 1
    
    print(f"Znaleziono {len(bigram_counts)} unikalnych bigramów.")
    print(f"Znaleziono {len(trigram_counts)} unikalnych trigramów.")
    print(f"Znaleziono {len(tetragram_counts)} unikalnych tetragramów.")

    def stworz_wazona_liste(counter):
        """Tworzy listę, w której każdy element jest powtórzony zgodnie z jego wagą."""
        print(f"Tworzę ważoną listę dla {sum(counter.values())} elementów...")
        lista = []
        for item, count in counter.items():
            lista.extend([item] * count)
        random.shuffle(lista) # Tasowanie listy dla lepszego efektu treningowego
        return lista

    # Tworzenie list
    bigrams_list = stworz_wazona_liste(bigram_counts)
    trigrams_list = stworz_wazona_liste(trigram_counts)
    tetragrams_list = stworz_wazona_liste(tetragram_counts)
    
    # Tworzenie jednej, zbiorczej listy
    all_ngrams_list = bigrams_list + trigrams_list + tetragrams_list
    random.shuffle(all_ngrams_list)

    # Zapisywanie do plików
    print("Zapisuję ngramy do plików .txt...")
    with open('bigrams.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(bigrams_list))
        
    with open('trigrams.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(trigrams_list))
        
    with open('tetragrams.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(tetragrams_list))

    with open('all_ngrams.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_ngrams_list))
        
    print("\nGotowe! Pliki zostały wygenerowane pomyślnie.")
    print(f"bigrams.txt - {len(bigrams_list)} linii")
    print(f"trigrams.txt - {len(trigrams_list)} linii")
    print(f"tetragrams.txt - {len(tetragrams_list)} linii")
    print(f"all_ngrams.txt - {len(all_ngrams_list)} linii")


if __name__ == '__main__':
    try:
        with open('polish_5k.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            slowa_z_pliku = data['words']
        generuj_ngramy('polish_5k.json', slowa_z_pliku)
    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku 'polish_5k.json'.")
        print("Upewnij się, że plik JSON znajduje się w tym samym folderze co skrypt.")
