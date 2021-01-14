VOWELS = 'aıoöuüei'
FRONT_VOWELS = 'aıou'
BACK_VOWELS = 'eiöü'

HARD_CONSONANTS = 'fstkçşhp'

DISCONTINUOUS_HARD_CONSONANTS = 'pçtk'
SOFTEN_DHC = 'bcdğ'

DISCONTINUOUS_HARD_CONSONANTS_AFTER_SUFFIX = 'pçk'
SOFTEN_DHC_AFTER_SUFFIX = 'bcğ'

MINOR_HARMONY = {
    'a': 'ı',
    'e': 'i',
    'ö': 'ü',
    'o': 'u',
    'ı': 'ı',
    'i': 'i',
    'u': 'u',
    'ü': 'ü'
}

MINOR_HARMONY_FOR_FUTURE = {
    'a': 'a',
    'e': 'e',
    'ö': 'ü',
    'o': 'u',
    'ı': 'ı',
    'i': 'e',
    'u': 'u',
    'ü': 'e'
}

# When a foreign word ends with b, c or d loaned to Turkish, the last letter transforms into p, ç or t.
# eg. Standard (English) -> Standart (Turkish)
#     Kabāb (Arabic) -> Kebap (Turkish)
# If the loaned word is coming from Arabic and if the last letter is Arabic d,
# and it gets a suffix starting with a vowel, -t turns into -d again.
# Source: Sevan Nisanyan
ARABIC_T = (
    'ait',
    'cedit',
    'cellat',
    'cirit',
    'ecdat',
    'fesat',
    'hamit',
    'hasat',
    'haset',
    'hudut',
    'mabat',
    'mabet',
    'maksat',
    'medet',
    'mescit',
    'mevcut',
    'murat',
    'münferit',
    'reşit',
    'senet',
    'simit',
    'suikast',
    'şahit',
    'şehit',
    'taahhüt',
    'taklit',
    'tecrit',
    'tehdit',
    'tevellüt',
    'velet',
    'vücut'
)

# If a noun has more than one syllable and if the last letter is k,
# while adding a suffix starting with a vowel, the last letter turns into ğ.
# But some Arabic originated nouns are exceptions, the last k remains as k.
# eg. börek + i = böreği (standard Turkish word behaviour)
#     merak + ı = merakı (Arabic-loaned word exception)
# Source: Sevan Nisanyan
ARABIC_K = (
    'hakkak',
    'halik',
    'idrak',
    'ilhak',
    'iltisak',
    'infilak',
    'istimlak',
    'istihkak',
    'iştikak',
    'iştirak',
    'ittifak',
    'memluk',
    'merak',
    'mihrak',
    'mülk',
    'müşfik',
    'müttefik',
    'nifak',
    'sevk',
    'sirk',
    'şerik',
    'taalluk',
    'tarik',
    'zevk'
)

# The exception words which has non-Turkish origins don't fit for standard Turkish Major Vowel Harmony
# because of the vocal difference which doesn't exist in Turkish.
MAJOR_HAMONY_EXCEPTIONS = (
    'ahval',
    'akropol',
    'alkol',
    'ametal',
    'amiral',
    'ampul',
    'anormal',
    'bandrol',
    'bemol',
    'beşamol',
    'bilkat',
    'cemaat',
    'cemal',
    'deccal',
    'dikkat',
    'ekol',
    'ekümenapol',
    'emsal',
    'enstrümantal',
    'enternasyonal',
    'faal',
    'faul',
    'final',
    'general',
    'glikol',
    'gol',
    'hakikat',
    'hal',
    'harf',
    'hayal',
    'hilal',
    'hiperbol',
    'hol',
    'integral',
    'iştigal',
    'istikbal',
    'istiklal',
    'jurnal',
    'kabul',
    'kalp',
    'kanaat',
    'kabahat',
    'kapital',
    'karambol',
    'katedral',
    'kefal',
    'kemal',
    'kıraat',
    'kolestrol',
    'kontrol',
    'koramiral',
    'korgeneral',
    'legal',
    'liberal',
    'liyakat',
    'lokal',
    'mahmul',
    'mahsul',
    'maktul',
    'makul',
    'meal',
    'menkul',
    'mentol',
    'meral',
    'meraşal',
    'meşekkat',
    'meşgul',
    'metal',
    'metaryal',
    'metrapol',
    'mineral',
    'misal',
    'moral',
    'müzikal',
    'müzikhol',
    'nasyonal',
    'normal',
    'ohal' # abbreviation,
    'oramiral',
    'orjinal',
    'oryantal',
    'oval',
    'parabol',
    'paranormal',
    'pastoral',
    'perhidrol',
    'petrol',
    'radikal',
    'refakat',
    'resital',
    'resul',
    'rol',
    'saat',
    'sadakat',
    'santral',
    'şefkat',
    'şevval',
    'sinyal',
    'sosyal',
    'spesiyal',
    'sual',
    'tefal'  # brand,
    'termal',
    'terminal',
    'total',
    'trambol',
    'tropikal',
    'tuğamiral',
    'tuğgeneral',
    'tümgeneral',
    'turnusol',
    'tuval',
    'usul',
    'zelal',
    'zerdeçal',
    'zeval',
    'ziraat'
)


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


N_CONNECTOR = [
    'o', 'bu', 'şu'
]

# de + iyorum = diyorum
VERBS_LOSING_VOWELS = {
    'ye': 'yi',
    'de': 'di'
}

# git -> gider, sat -> satar
VERBS_HARDEN = {
    'git': 'gid',
    'et': 'ed'
}

# K -> G change in some nouns ending with -nk (not all of them, for instance: link, bank)
NK_G_CHANGE = {
    'renk': 'reng',
    'frank': 'frang',
    'frenk': 'freng',
    'prezevenk': 'prezeveng',
    'rengarenk': 'rengareng',
    'mürdesenk': 'mürdeseng',
    'mühresenk': 'mühreseng',
    'şekerrenk': 'şekerreng',
    'plesenk': 'pleseng',
    'denk': 'deng',
    'persenk': 'perseng',
    'çelenk': 'çeleng',
    'filenk': 'fileng',
    'fiyonk': 'fiyong',
    'hevenk': 'heveng',
    'kepenk': 'kepeng',
    'ornitorenk': 'ornitoreng',
    'külünk': 'külüng',
    'pelenk': 'peleng',
    'tırınk': 'tırıng',
    'ahenk': 'aheng',
    'krank': 'krang',
    'skink': 'sking',
    'cenk': 'ceng',
    'zonk': 'zong',
    'künk': 'küng',
    'dink': 'ding',
    'gonk': 'gong',
}

# sererim, silerim (e)
# veririm, gelirim, bilirim (i)
VERB_MINOR_HARMONY_EXCEPTIONS = (
    'ver', 'gel', 'bil',
    'al', 'kal'
)
