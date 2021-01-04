from turkish_suffix_library.turkish import Turkish

print(Turkish('araba').dative())
print(Turkish('sebep').ablative())
print(Turkish('sebep').accusative())
print(Turkish('ecdat').accusative())

print(Turkish('çanta').plural().possessive(person=1).ablative().to_json())
print(Turkish('aparat').possessive(person=2))
print(Turkish('batak').possessive(person=3))

print(Turkish('idrak').possessive(person=1, plural=True))
print(Turkish('ok').possessive(person=2, plural=True))
print(Turkish('çanta').possessive(person=3, plural=True))

print(f'{Turkish("Elif").genitive(proper_noun=True)} {Turkish("Öküz").possessive(person=3)}.')

print(Turkish('dört').ordinal())
print(Turkish('yedi').distributive())
