from turkish_suffix_library.turkish import Turkish

print(Turkish('araba').genitive())
print(Turkish('araba').dative())
print(Turkish('araba').ablative())
print(Turkish('araba').accusative())

print(Turkish('Cem').genitive(proper_noun=True))
print(Turkish('Cem').dative(proper_noun=True))
print(Turkish('Cem').ablative(proper_noun=True))
print(Turkish('Cem').accusative(proper_noun=True))

print(Turkish('çanta').possessive_affix(person=1))
print(Turkish('çanta').possessive_affix(person=2))
print(Turkish('çanta').possessive_affix(person=3))

print(Turkish('çanta').possessive_affix(person=1, plural=True))
print(Turkish('çanta').possessive_affix(person=2, plural=True))
print(Turkish('çanta').possessive_affix(person=3, plural=True))
