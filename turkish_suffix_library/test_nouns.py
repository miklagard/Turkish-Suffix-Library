from turkish_suffix_library.turkish import Turkish

print(Turkish('araba').dative())
print(Turkish('araba').ablative())
print(Turkish('araba').accusative())

print(Turkish('Cem').dative(proper_noun=True))
print(Turkish('Cem').ablative(proper_noun=True))
print(Turkish('Cem').accusative(proper_noun=True))

print(Turkish('çanta').possessive(person=1))
print(Turkish('çanta').possessive(person=2))
print(Turkish('çanta').possessive(person=3))

print(Turkish('çanta').possessive(person=1, plural=True))
print(Turkish('çanta').possessive(person=2, plural=True))
print(Turkish('çanta').possessive(person=3, plural=True))

print(f'{Turkish("Elif").genitive(proper_noun=True)} {Turkish("Öküz").possessive(person=3)}.')
