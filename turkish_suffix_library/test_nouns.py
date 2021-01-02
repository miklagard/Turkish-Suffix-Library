from turkish_suffix_library.turkish import Turkish

print(Turkish('araba').genitive().to_string())
print(Turkish('araba').dative().to_string())
print(Turkish('araba').ablative().to_string())
print(Turkish('araba').accusative().to_string())

print(Turkish('Cem').genitive(proper_noun=True).to_string())
print(Turkish('Cem').dative(proper_noun=True).to_string())
print(Turkish('Cem').ablative(proper_noun=True).to_string())
print(Turkish('Cem').accusative(proper_noun=True).to_string())

print(Turkish('çanta').possessive_affix(person=1).to_string())
print(Turkish('çanta').possessive_affix(person=2).to_string())
print(Turkish('çanta').possessive_affix(person=3).to_string())

print(Turkish('çanta').possessive_affix(person=1, plural=True).to_string())
print(Turkish('çanta').possessive_affix(person=2, plural=True).to_string())
print(Turkish('çanta').possessive_affix(person=3, plural=True).to_string())
