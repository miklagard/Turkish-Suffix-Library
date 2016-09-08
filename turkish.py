#!/usr/bin/python
# -*- coding: utf-8 -*-

class turkish:
    VOWELS = u"aıoöuüei"
    FRONT_VOWELS = u"aıou"
    BACK_VOWELS = u"eiöü"
    HARD_CONSONANTS = u"fstkçşhp"
    DISCONTINIOUS_HARD_CONSONANTS = u"pçtk"
    SOFTEN_DHC = u"bcdğ"
    DISCONTINIOUS_HARD_CONSONANTS_AFTER_SUFFIX = u"pçk"
    SOFTEN_DHC_AFTER_SUFFIX = u"bcğ"    
    MINOR_HARMONY = {
                     u"a": u"ı"
                     , u"e": u"i"
                     , u"ö": u"ü"
                     , u"o": u"u"
                     , u"ı": u"ı"
                     , u"i": u"i"
                     , u"u": u"u"
                     , u"ü": u"ü"
    }
    
    MINOR_HARMONY_FOR_FUTURE = {
                     u"a": u"a"
                     , u"e": u"e"
                     , u"ö": u"e"
                     , u"o": u"a"
                     , u"ı": u"a"
                     , u"i": u"e"
                     , u"u": u"a"
                     , u"ü": u"e"
    }
    
    
    
    EXCEPTION_WORDS = [u"kontrol", u"bandrol", u"alpul", u"ametal", u"anormal", u"amiral"
                       , u"sadakat", u"santral", u"şefkat", u"usul", u"normal", u"oryantal", u"hakikat"
                       , u"hayal", u"saat", u"kemal", u"gol", u"kalp", u"metal", u"faul", u"mineral", u"alkol"
                       , u"misal", u"meal", u"oramiral", u"tuğamiral", u"orjinal", u"koramiral", u"general"
                       , u"tümgeneral", u"tuğgeneral", u"korgeneral", u"petrol", u"liberal", u"meral", u"bantrol"
                       , u"hiperbol", u"perhidrol", u"zanaat", u"ahval", u"paranormal", u"iştigal"
                       , u"metrapol", u"ekümenapol", u"lokal", u"lügat", u"liyakat", u"legal", u"mentol"
                       , u"beşamol", u"meşgul", u"meşekkat", u"oval", u"mahsul", u"makul", u"meraşal"
                       , u"metaryal", u"nasihat", u"radikal", u"moral", u"dikkat", u"rol", u"sinyal"
                       , u"sosyal", u"total", u"şevval", u"sual", u"spesiyal", u"tuval", u"turnusol", u"hol"
                       , u"tropikal", u"zeval", u"zelal", u"terminal", u"termal", u"resul", u"sadakat", u"resital"
                       , u"refakat", u"pastoral", u"hal", u"müzikal", u"müzikhol", u"menkul", u"mahmul", u"maktul"
                       , u"kolestrol", u"kıraat", u"ziraat", u"kapital", u"katedral", u"kabul", u"kanaat", u"jurnal"
                       , u"kefal", u"istiklal", u"integral", u"final", u"ekol", u"emsal", u"enternasyonal"
                       , u"nasyonal", u"enstrümantal", u"harf", u"cemal", u"cemaat", u"glikol", u"karambol", u"parabol"
                       , u"kemal"
                       ]
    
    EXCEPTION_MISSING = {
                         u"isim": u"ism",
                         u"kasır": u"kasr",
                         u"kısım": u"kısm",
                         u"af": u"aff",
                         u"ilim": u"ilm",
                         #u"hatır": u"hatr", # for daily usage only
                         u"boyun": u"boyn",
                         u"nesil": u"nesl",
                         u"koyun": u"koyn", # koyun (sheep) or koyun (bosom)? for koyun (sheep) there is no exception but for koyun (bosom) there is. aaaaargh turkish!!
                         u"karın": u"karn" #same with this, karın (your wife) or karın (stomach)? for karın (your wife) there is not a such exception
                         #katli, katle, katli etc. it doesn't really have a nominative case but only with suffixes?
                        }     
    def isUpper(self, word):
        word = word.replace(u"ı", u"i").replace(u"İ", u"I").replace(u"ş", u"s").replace(u"Ş", u"S").replace(u"ğ", u"g").replace(u"Ğ", u"G").replace(u"ü", u"u").replace(u"Ü", u"U").replace(u"ç", u"c").replace(u"Ç", u"C").replace(u"ö", u"o").replace(u"Ö", u"O")
        return word.isupper()
    
    def makeLower(self, word):
        return word.replace(u"İ", u"i").replace(u"I", u"ı").lower()
    
    def makeUpper(self, word):
        return word.replace(u"i", u"İ").replace(u"ı", u"I").upper()
     
    def concat(self, str1, str2):
        if self.isUpper(str1) == True:
            returndata = str1 + makeUpper(str2)
        else:
            returndata = str1 + str2
        
        return returndata
    
    def fromUpperOrLower(self, newWord, refWord):
        if self.isUpper(refWord[len(refWord) - 1]):
            returndata = self.makeUpper(newWord)
        else:
            if self.isUpper(refWord[0]):
                returndata = self.makeUpper(newWord[0]) + self.makeLower(newWord[1:])
            else:
                returndata = self.makeLower(newWord)
    
        return returndata 
    
    
    def lastVowel(self, word):
        word = self.makeLower(word)
        vowel_count = 0
        for letter in word:
            if letter in self.FRONT_VOWELS:
                vowel_count = vowel_count + 1
                returndata = {u"letter": letter, u"tone": u"front"}
            elif letter in self.BACK_VOWELS:
                vowel_count = vowel_count + 1
                returndata = {u"letter": letter, u"tone": u"back"}
    
        # fake return for exception behaviour in Turkish
        if word in self.EXCEPTION_WORDS:
            if returndata[u"letter"] == u"o":
                returndata = {u"letter": u"ö", u"tone": u"back"}
            elif returndata[u"letter"] == u"a":
                returndata = {u"letter": u"e", u"tone": u"back"}
            elif returndata[u"letter"] == u"u":
                returndata = {u"letter": u"ü", u"tone": u"back"}
            
        if returndata == "":
            returndata = {u"letter": "", u"tone": u"back"}
    
        returndata[u"vowel_count"] = vowel_count
        return returndata
    
    def lastLetter(self, word):
        word = self.makeLower(word)
        returndata = {}
        getLastLetter = word[len(word) - 1]
        if getLastLetter == "'":
            getLastLetter = word[len(word) - 2]
        
        returndata[u"letter"] = getLastLetter      
        
        if getLastLetter in self.VOWELS:
            returndata[u"vowel"] = True
            if getLastLetter in self.FRONT_VOWELS:
                returndata[u"front_vowel"] = True
            else:
                returndata[u"back_vowel"] = True
        else:
            returndata[u"consonant"] = True
            
            if getLastLetter in self.HARD_CONSONANTS:
                returndata[u"hard_consonant"] = True
                
                if getLastLetter in self.DISCONTINIOUS_HARD_CONSONANTS_AFTER_SUFFIX:
                    returndata[u"discontinious_hard_consonant_for_suffix"] = True
                    getLastLetter = self.SOFTEN_DHC_AFTER_SUFFIX[self.DISCONTINIOUS_HARD_CONSONANTS_AFTER_SUFFIX.index(getLastLetter)]
                    returndata[u"soften_consonant_for_suffix"] = getLastLetter
    
        return returndata    
    
    def makePlural(self, word, param = {}):
        if "proper_noun" in param:
            word = word + "'"
        
        if self.lastVowel(word)[u"tone"] == u"front":
            returndata = self.concat(word, u"lar")
        else:
            returndata = self.concat(word, u"ler")
            
        return returndata

        
    def makeAccusative(self, word, param = {}): # not finished yet
        #firslty exceptions for o (he/she/it) 
        
        lowerWord = self.makeLower(word)
    
        proper_noun = param.get("proper_noun", False)
    
        if lowerWord == u"o":
            if proper_noun == True:
                returndata = self.fromUpperOrLower(u"O'nu", word)
            else:
                returndata = self.fromUpperOrLower(u"onu", word)
        else:
            if lowerWord in self.EXCEPTION_MISSING and proper_noun == True:
                word = self.fromUpperOrLower(self.EXCEPTION_MISSING[lowerWord], word)
                lowerWord = self.makeLower(word)
            
            getLastLetter = self.lastLetter(word)
            getLastVowel = self.lastVowel(word)
            
            if proper_noun == True:
                word += "'"
            
            if u"vowel" in getLastLetter:
                word = self.concat(word, u"y")
            elif u"discontinious_hard_consonant_for_suffix" in getLastLetter and proper_noun == False:
                if getLastVowel[u"vowel_count"] > 1:
                    word = self.concat(word[0:len(word) - 1], getLastLetter[u"soften_consonant_for_suffix"])
    
            word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
    
            returndata = word
                
        return returndata        

    
    def makeDative(self, word, param = {}):
        #firslty exceptions for ben (I) and you (sen)
        proper_noun = param.get("proper_noun", False)
        
        lowerWord = self.makeLower(word)
        
        if proper_noun == True:
            word += "'"
    
        if lowerWord == u"ben" and proper_noun == False:
            returndata = fromUpperOrLower(u"bana", word)
        elif lowerWord == u"sen" and proper_noun == False:
            returndata = self.fromUpperOrLower(u"sana", word)
        else:
            if lowerWord in self.EXCEPTION_MISSING and proper_noun == False:
                word = self.fromUpperOrLower(self.EXCEPTION_MISSING[lowerWord], word)
                lowerWord = self.makeLower(word)
    
            getLastLetter = self.lastLetter(word)
            getLastVowel = self.lastVowel(word)
                
            if u"vowel" in getLastLetter:
                word = self.concat(word, u"y")
            elif u"discontinious_hard_consonant_for_suffix" in getLastLetter:
                if getLastVowel[u"vowel_count"] > 1 and proper_noun == False:
                    word = self.concat(word[0:len(word) - 1], getLastLetter[u"soften_consonant_for_suffix"])
    
            if getLastVowel[u"tone"] == u"front":
                word = self.concat(word, u"a")
            else:
                word = self.concat(word, u"e")
            
            returndata = word
        
        if returndata.isupper():
            returndata = makeUpper(returndata)    
        
        return returndata

    
    def makeGenitive(self, word, param = {}):
        getLastLetter = self.lastLetter(word)
        getLastVowel = self.lastVowel(word)
        lowerWord = self.makeLower(word)
        proper_noun = param.get("proper_noun", False)
        
        if proper_noun == True:
            word += "'"
        if lowerWord in self.EXCEPTION_MISSING:
            word = self.fromUpperOrLower(self.EXCEPTION_MISSING[lowerWord], word)
            lowerWord = self.makeLower(word)
        
        if u"vowel" in getLastLetter:
            word = self.concat(word, u"n")
        elif u"discontinious_hard_consonant_for_suffix" in getLastLetter and proper_noun == False:
            if getLastVowel["vowel_count"] > 1:
                word = self.concat(word[0:len(word) - 1], getLastLetter[u"soften_consonant_for_suffix"])
    
        word = self.concat(word, self.MINOR_HARMONY[getLastVowel[u"letter"]])
        word = self.concat(word, u"n")
        
        returndata = word
        
        return returndata

    
    def makeAblative(self, word, param = {}): 
        getLastLetter = self.lastLetter(word)
        getLastVowel = self.lastVowel(word)
        proper_noun = param.get("proper_noun", False)
    
        if proper_noun == True:
            word += "'"
    
        if getLastLetter["letter"] in self.HARD_CONSONANTS:
            word = self.concat(word, u"t")
        else:
            word = self.concat(word, u"d")
    
        if getLastVowel[u"tone"] == u"front":
            word = self.concat(word, u"an")
        else:
            word = self.concat(word, u"en")
        
        returndata = word
        
        return returndata
    
    
    def makeLocative(self, word, param = {}):
        getLastLetter = self.lastLetter(word)
        getLastVowel = self.lastVowel(word)
        proper_noun = param.get("proper_noun", False)
    
        if proper_noun == True:
            word += "'"
    
        if getLastLetter["letter"] in self.HARD_CONSONANTS:
            word = self.concat(word, u"t")
        else:
            word = self.concat(word, u"d")
    
        if getLastVowel[u"tone"] == u"front":
            word = self.concat(word, u"a")
        else:
            word = self.concat(word, u"e")
        
        returndata = word
        
        return returndata
    
    # İyelik ekleri
    def possessiveAffix(self, word, param):
        
        person = str(param[u"person"])
        quantity = param[u"quantity"]
    
        proper_noun = param.get("proper_noun", False)
            
        if not(person == "3" and quantity == "plural"):
            getLastLetter = self.lastLetter(word)
            getLastVowel = self.lastVowel(word)
            
            if proper_noun == True:
                word += "'"
            elif u"discontinious_hard_consonant_for_suffix" in getLastLetter:
                if getLastVowel[u"vowel_count"] > 1:
                    word = self.concat(word[0:len(word) - 1], getLastLetter[u"soften_consonant_for_suffix"])
                if (self.makeLower(word) in self.EXCEPTION_MISSING): 
                    word = self.fromUpperOrLower(self.EXCEPTION_MISSING[self.makeLower(word)], word)
        
        getLastLetter = self.lastLetter(word)
        getLastVowel = self.lastVowel(word)
        
        lastLetterIsVowel = getLastLetter[u"letter"] in self.VOWELS
        
        minorHarmonyLetter = self.MINOR_HARMONY[getLastVowel[u"letter"]]
    
        if quantity == u"singular":
            if lastLetterIsVowel == False:
                word = self.concat(word, minorHarmonyLetter)
    
            if person == "1": 
                word = self.concat(word, u"m")
            
            elif person == "2": 
                word = self.concat(word, u"n")
        else:
            if person == "1":
                if lastLetterIsVowel == False:
                    word = self.concat(word, minorHarmonyLetter)
                word = self.concat(word, u"m")                
                word = self.concat(word, minorHarmonyLetter)
                word = self.concat(word, u"z")                
            elif person == "2":
                if lastLetterIsVowel == False:
                    word = self.concat(word, minorHarmonyLetter)
                word = self.concat(word, u"n")                
                word = self.concat(word, minorHarmonyLetter)
                word = self.concat(word, u"z")                
            else:
                if self.makeLower(word) == u"ism":
                    word = self.fromUpperOrLower(u"isim", word)
                word = self.makePlural(word)
                word = self.concat(word, minorHarmonyLetter)
            
        return word

    # Mastar eski
    def makeInfinitive(self, word):
        if self.lastVowel(word)[u"tone"] == u"front":
            returndata = self.concat(self, word, u"mak")
        else:
            returndata = self.concat(self, word, u"mek")
            
        return returndata    

    # Şimdiki zaman
    def makePresentContinuous(self, word, param):
        getLastLetter = self.lastLetter(word)
        getLastVowel = self.lastVowel(word)

        lastLetterIsVowel = getLastLetter[u"letter"] in self.VOWELS

        if param["negative"] == False:
            if lastLetterIsVowel:
                word = self.concat(word[:-1], self.MINOR_HARMONY[word[-1]])
            else:
                word = self.concat(word, self.MINOR_HARMONY[getLastVowel[u"letter"]])
        else:
            word = self.concat(word, u"m")
            word = self.concat(word, self.MINOR_HARMONY[getLastVowel[u"letter"]])


        word = self.concat(word, "yor")

        if param["question"]: 
            if param["quantity"] == "singular":
                if param["person"] == 1:
                    word = self.concat(word, " muyum")
                elif param["person"] == 2:
                    word = self.concat(word, " musun")
            elif param["quantity"] == "plural":
                if param["person"] == 1:
                    word = self.concat(word, " muyuz")
                elif param["person"] == 2:
                    word = self.concat(word, " musunuz")
                elif param["person"] == 3:
                    word = self.concat(word, " mı")            
        else:
            if param["quantity"] == "singular":
                if param["person"] == 1:
                    word = self.concat(word, "um")
                elif param["person"] == 2:
                    word = self.concat(word, "sun")
            elif param["quantity"] == "plural":
                if param["person"] == 1:
                    word = self.concat(word, "uz")
                elif param["person"] == 2:
                    word = self.concat(word, "sunuz")
                elif param["person"] == 3:
                    word = self.concat(word, "lar")


        return word

    # Geniş zaman
    def makePresent(self, word, param):
        pass

tr = turkish()

print tr.makePresentContinuous(u"kaç", { "negative": True, "question": False, "person": 1, "quantity": "singular" })
print tr.makePresentContinuous(u"öl", { "negative": True, "question": True, "person": 1, "quantity": "singular" })
print tr.makePresentContinuous(u"ara", { "negative": False, "question": True, "person": 2, "quantity": "plural" })

print tr.makeGenitive(u"Öykü", {"proper_noun": True})
print tr.makeDative("Fatma", {"proper_noun": True})
print tr.makeAblative("Ali", {"proper_noun": True})
print tr.makeAccusative(u"Kaliningrad", {"proper_noun": True})

print tr.makeGenitive(u"ağaç", {"proper_noun": False})
print tr.makeAccusative(u"erik", {"proper_noun": False})
print tr.makeAccusative(u"Erik", {"proper_noun": True})


print tr.possessiveAffix("kavanoz", {"person": 1, "quantity": "singular"})
print tr.possessiveAffix("kavanoz", {"person": 2, "quantity": "singular"})
print tr.possessiveAffix("kavanoz", {"person": 3, "quantity": "singular"})

print tr.possessiveAffix("halter", {"person": 1, "quantity": "plural"})
print tr.possessiveAffix("halter", {"person": 2, "quantity": "plural"})
print tr.possessiveAffix("halter", {"person": 3, "quantity": "plural"})

print tr.possessiveAffix(u"Kenya", {"person": 3, "quantity": "plural"})