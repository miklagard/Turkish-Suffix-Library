VOWELS = 'aıoöuüei'

FRONT_VOWELS = 'aıou'

BACK_VOWELS = 'eiöü'

HARD_CONSONANTS = 'fstkçşhp'

DISCONTINUOUS_HARD_CONSONANTS = 'pçtk'

SOFTEN_DHC = 'bcdğ'

DISCONTINUOUS_HARD_CONSONANTS_AFTER_SUFFIX = 'pçk'

SOFTEN_DHC_AFTER_SUFFIX = 'bcğ'

MINOR_HARMONY = {
    'a': 'ı'
    , 'e': 'i'
    , 'ö': 'ü'
    , 'o': 'u'
    , 'ı': 'ı'
    , 'i': 'i'
    , 'u': 'u'
    , 'ü': 'ü'
}

MINOR_HARMONY_FOR_FUTURE = {
    'a': 'a'
    , 'e': 'e'
    , 'ö': 'ü'
    , 'o': 'u'
    , 'ı': 'ı'
    , 'i': 'e'
    , 'u': 'u'
    , 'ü': 'e'
}


# The exception words which has non-Turkish origins donn't fit for standard Turkish Major Wovel Harmony
# beacuse of the vocal difference which doesn't exist in Turkish.
MAJOR_HAMONY_EXCEPTIONS = [
    'ahval'
    , 'akropol'
    , 'alkol'
    , 'ametal'
    , 'amiral'
    , 'ampul'
    , 'anormal'
    , 'bandrol'
    , 'bemol'
    , 'beşamol'
    , 'bilkat'
    , 'cemaat'
    , 'cemal'
    , 'deccal'
    , 'dikkat'
    , 'ekol'
    , 'ekümenapol'
    , 'emsal'
    , 'enstrümantal'
    , 'enternasyonal'
    , 'faal'
    , 'faul'
    , 'final'
    , 'general'
    , 'glikol'
    , 'gol'
    , 'hakikat'
    , 'hal'
    , 'harf'
    , 'hayal'
    , 'hilal'
    , 'hiperbol'
    , 'hol'
    , 'integral'
    , 'iştigal'
    , 'istikbal'
    , 'istiklal'
    , 'jurnal'
    , 'kabul'
    , 'kalp'
    , 'kanaat'
    , 'kapital'
    , 'karambol'
    , 'katedral'
    , 'kefal'
    , 'kemal'
    , 'kıraat'
    , 'kolestrol'
    , 'kontrol'
    , 'koramiral'
    , 'korgeneral'
    , 'legal'
    , 'liberal'
    , 'liyakat'
    , 'lokal'
    , 'mahmul'
    , 'mahsul'
    , 'maktul'
    , 'makul'
    , 'meal'
    , 'menkul'
    , 'mentol'
    , 'meral'
    , 'meraşal'
    , 'meşekkat'
    , 'meşgul'
    , 'metal'
    , 'metaryal'
    , 'metrapol'
    , 'mineral'
    , 'misal'
    , 'moral'
    , 'müzikal'
    , 'müzikhol'
    , 'nasyonal'
    , 'normal'
    , 'ohal' # abbreviation
    , 'oramiral'
    , 'orjinal'
    , 'oryantal'
    , 'oval'
    , 'parabol'
    , 'paranormal'
    , 'pastoral'
    , 'perhidrol'
    , 'petrol'
    , 'radikal'
    , 'refakat'
    , 'resital'
    , 'resul'
    , 'rol'
    , 'saat'
    , 'sadakat'
    , 'santral'
    , 'şefkat'
    , 'şevval'
    , 'sinyal'
    , 'sosyal'
    , 'spesiyal'
    , 'sual'
    , 'tefal' # brand
    , 'termal'
    , 'terminal'
    , 'total'
    , 'trambol'
    , 'tropikal'
    , 'tuğamiral'
    , 'tuğgeneral'
    , 'tümgeneral'
    , 'turnusol'
    , 'tuval'
    , 'usul'
    , 'zelal'
    , 'zerdeçal'
    , 'zeval'
    , 'ziraat'
]


EXCEPTION_MISSING = {
    'isim': 'ism',
    'kasır': 'kasr',
    'kısım': 'kısm',
    'af': 'aff',
    'ilim': 'ilm',
    #'hatır': 'hatr', # for daily usage only
    'boyun': 'boyn',
    'nesil': 'nesl',
    'koyun': 'koyn', # koyun (sheep) or koyun (bosom)? for koyun (sheep) there is no exception but for koyun (bosom) there is. aaaaargh turkish!!
    'karın': 'karn' #same with this, karın (your wife) or karın (stomach)? for karın (your wife) there is not a such exception
    #katli, katle, katli etc. it doesn't really have a nominative case but only with suffixes?
}    
