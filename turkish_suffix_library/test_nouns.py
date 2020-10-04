from turkish_suffix_library import turkish

print(turkish.make_genitive('araba'))
print(turkish.make_dative('araba'))
print(turkish.make_ablative('araba'))
print(turkish.make_accusative('araba'))

print(turkish.make_genitive('Cem', proper_noun=True))
print(turkish.make_dative('Cem', proper_noun=True))
print(turkish.make_ablative('Cem', proper_noun=True))
print(turkish.make_accusative('Cem', proper_noun=True))

print(turkish.possessive_affix('çanta', person=1, quantity='singular'))
print(turkish.possessive_affix('çanta', person=2, quantity='singular'))
print(turkish.possessive_affix('çanta', person=3, quantity='singular'))

print(turkish.possessive_affix('çanta', person=1, quantity='plural'))
print(turkish.possessive_affix('çanta', person=2, quantity='plural'))
print(turkish.possessive_affix('çanta', person=3, quantity='plural'))

print(
    turkish.make_ablative(
        turkish.possessive_affix(
            turkish.make_accusative('Merak'),
            person=2
        )
    )
)
print(turkish.make_accusative('Şafak'))

print(turkish.make_dative('murat'))
