    for diphthong in DIPHTHONGS:
        if diphthong in word:
            place_diphthong = word.index(diphthong)
            pronunciation_before_diph = ''
            for char in (word[:place_diphthong]):
                pronunciation_before_diph += get_consonant_pronunciation(char)
                pronunciation_before_diph += get_vowel_pronunciation(char)
                pronunciation_after_diph = ''
            for char in (word[place_diphthong + 2 :]):
                pronunciation_after_diph += get_consonant_pronunciation(char)
                pronunciation_after_diph += get_vowel_pronunciation(char)
            pronunciation = pronunciation_before_diph + get_diphthong_pronunciation(diphthong) + pronunciation_after_diph
            return pronunciation
    pronunciation = ''
    for char in word:
        if 'dj' in word:
            place_dj = word.index('dj')
            pronunciation_before_dj = ''
            for char in (word[:place_dj]):
                pronunciation_before_dj += get_consonant_pronunciation(char)
                pronunciation_before_dj += get_vowel_pronunciation(char)
                pronunciation_after_dj = ''
            for char in (word[place_dj + 2 :]):
                pronunciation_after_dj += get_consonant_pronunciation(char)
                pronunciation_after_dj += get_vowel_pronunciation(char)
            pronunciation = pronunciation_before_dj + 'J' + pronunciation_after_dj
            return pronunciation
    pronunciation += get_consonant_pronunciation(char)
    pronunciation += get_vowel_pronunciation(char)
    return pronunciation
