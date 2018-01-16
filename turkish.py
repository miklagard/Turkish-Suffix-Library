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
					 , u"ö": u"ü"
					 , u"o": u"u"
					 , u"ı": u"ı"
					 , u"i": u"e"
					 , u"u": u"u"
					 , u"ü": u"e"
	}
	
	# The exception words which has non-Turkish origins donn't fit for standard Turkish Major Wovel Harmony
	# beacuse of the vocal difference which doesn't exist in Turkish.
	EXCEPTION_WORDS = [
		u"ahval"
		, u"akropol"
		, u"alkol"
		, u"ametal"
		, u"amiral"
		, u"ampul"
		, u"anormal"
		, u"bandrol"
		, u"bemol"
		, u"beşamol"
		, u"bilkat"
		, u"cemaat"
		, u"cemal"
		, u"deccal"
		, u"dikkat"
		, u"ekol"
		, u"ekümenapol"
		, u"emsal"
		, u"enstrümantal"
		, u"enternasyonal"
		, u"faal"
		, u"faul"
		, u"final"
		, u"general"
		, u"glikol"
		, u"gol"
		, u"hakikat"
		, u"hal"
		, u"harf"
		, u"hayal"
		, u"hilal"
		, u"hiperbol"
		, u"hol"
		, u"integral"
		, u"iştigal"
		, u"istikbal"
		, u"istiklal"
		, u"jurnal"
		, u"kabul"
		, u"kalp"
		, u"kanaat"
		, u"kapital"
		, u"karambol"
		, u"katedral"
		, u"kefal"
		, u"kemal"
		, u"kıraat"
		, u"kolestrol"
		, u"kontrol"
		, u"koramiral"
		, u"korgeneral"
		, u"legal"
		, u"liberal"
		, u"liyakat"
		, u"lokal"
		, u"mahmul"
		, u"mahsul"
		, u"maktul"
		, u"makul"
		, u"meal"
		, u"menkul"
		, u"mentol"
		, u"meral"
		, u"meraşal"
		, u"meşekkat"
		, u"meşgul"
		, u"metal"
		, u"metaryal"
		, u"metrapol"
		, u"mineral"
		, u"misal"
		, u"moral"
		, u"müzikal"
		, u"müzikhol"
		, u"nasyonal"
		, u"normal"
		, u"ohal" # abbreviation
		, u"oramiral"
		, u"orjinal"
		, u"oryantal"
		, u"oval"
		, u"parabol"
		, u"paranormal"
		, u"pastoral"
		, u"perhidrol"
		, u"petrol"
		, u"radikal"
		, u"refakat"
		, u"resital"
		, u"resul"
		, u"rol"
		, u"saat"
		, u"sadakat"
		, u"santral"
		, u"şefkat"
		, u"şevval"
		, u"sinyal"
		, u"sosyal"
		, u"spesiyal"
		, u"sual"
		, u"tefal" # brand
		, u"termal"
		, u"terminal"
		, u"total"
		, u"trambol"
		, u"tropikal"
		, u"tuğamiral"
		, u"tuğgeneral"
		, u"tümgeneral"
		, u"turnusol"
		, u"tuval"
		, u"usul"
		, u"zelal"
		, u"zerdeçal"
		, u"zeval"
		, u"ziraat"
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
	
	
	def lastVowel(self, pword):
		word = self.makeLower(pword)
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
	
	def lastLetter(self, pword):
		word = self.makeLower(pword)
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
			
			if getLastLetter in self.DISCONTINIOUS_HARD_CONSONANTS:
				returndata[u"discontinious_hard_consonant"] = True
				getLastLetter = self.SOFTEN_DHC[self.DISCONTINIOUS_HARD_CONSONANTS.index(getLastLetter)]
				returndata[u"soften_consonant"] = getLastLetter

			if getLastLetter in self.HARD_CONSONANTS:
				returndata[u"hard_consonant"] = True

				if getLastLetter in self.DISCONTINIOUS_HARD_CONSONANTS_AFTER_SUFFIX:
					returndata[u"discontinious_hard_consonant_for_suffix"] = True
					getLastLetter = self.SOFTEN_DHC_AFTER_SUFFIX[self.DISCONTINIOUS_HARD_CONSONANTS_AFTER_SUFFIX.index(getLastLetter)]
					returndata[u"soften_consonant_for_suffix"] = getLastLetter
	
		return returndata	
	
	def makePlural(self, pword, param = {}):
		word = pword

		if "proper_noun" in param:
			word = word + "'"
		
		if self.lastVowel(word)[u"tone"] == u"front":
			returndata = self.concat(word, u"lar")
		else:
			returndata = self.concat(word, u"ler")
			
		return returndata

	#-i hali   
	def makeAccusative(self, pword, param = {}): # not finished yet
		#firslty exceptions for o (he/she/it) 
		word = pword
		
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

	#-e hali
	def makeDative(self, pword, param = {}):
		#firslty exceptions for ben (I) and you (sen)
		word = pword

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

	#-de hali
	def makeGenitive(self, pword, param = {}):
		word = pword

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

	#-den hali
	def makeAblative(self, pword, param = {}):
		word = pword

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
	
	#-de hali	
	def makeLocative(self, pword, param = {}):
		word = pword

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
	def possessiveAffix(self, pword, param = {}):
		word = pword
		
		person = str(param.get("person", 3))
		quantity = param.get("quantity", "singular")
	
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

			elif person == "3":
				word = self.concat(word, u"s")
				word = self.concat(word, minorHarmonyLetter)
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
	def makeInfinitive(self, pword, param = {}):
		word = pword

		if param.get("negative", False) == True:
			if self.lastVowel(word)[u"tone"] == u"front":
				returndata = self.concat(word, u"mamak")
			else:
				returndata = self.concat(word, u"memek")
		else: 
			if self.lastVowel(word)[u"tone"] == u"front":
				returndata = self.concat(word, u"mak")
			else:
				returndata = self.concat(word, u"mek")
			
		return returndata	


	# Şimdiki zaman 
	#	   * arıyorum
	#	   * For alternative usage of present continuous tense, check the function makePresentContinuous2
	def makePresentContinuous(self, pword, param = {}):
		word = pword

		getLastLetter = self.lastLetter(word)
		getLastVowel = self.lastVowel(word)

		lastLetterIsVowel = getLastLetter[u"letter"] in self.VOWELS

		if param.get("negative", False) == False:
			if u"discontinious_hard_consonant" in getLastLetter and getLastVowel[u"vowel_count"] > 1:
				word = self.concat(word[0:len(word) - 1], getLastLetter[u"soften_consonant"])
	
			if lastLetterIsVowel:
				word = self.concat(word[:-1], self.MINOR_HARMONY[word[-1]])
			else:
				word = self.concat(word, self.MINOR_HARMONY[getLastVowel[u"letter"]])
		else:
			word = self.concat(word, u"m")
			word = self.concat(word, self.MINOR_HARMONY[getLastVowel[u"letter"]])


		word = self.concat(word, "yor")

		if param.get("question", False) == True:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, u" muyum")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u" musun")
				elif param.get("person", 3) == 3:
					word = self.concat(word, u" mu")
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, u" muyuz")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u" musunuz")
				elif param.get("person", 3) == 3:
					word = self.makePlural(word)
					word = self.concat(word, u" m")
					if self.lastVowel(word)[u"tone"] == u"front":
						word = self.concat(word, u"ı")
					else:
						word = self.concat(word, u"i")
		else:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, u"um")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u"sun")
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, u"uz")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u"sunuz")
				elif param.get("person", 3) == 3:
					word = self.makePlural(word)


		return word

	def makePresentContinuous2(self, pword, param = {}):
	# There are two ways to express "present continuous tense in Turkish "
	# This kind is not common in daily Turkish usage anymore
	#	   * aramaktayım
	#	   * yapmaktayım

		word = self.makeInfinitive(pword, param = {})

		if self.lastVowel(word)[u"tone"] == u"front" and param.get("negative", False) == True:
			word = self.concat(word, u"ma")
		else:
			word = self.concat(word, u"me")


		if self.lastVowel(word)[u"tone"] == u"front":
			word = self.concat(word, u"ta")
		else:
			word = self.concat(word, u"te")

		if param.get("question", False)  == False:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, u"y")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"m")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u"s")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"n")
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, u"y")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"z")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u"s")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"n")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"z")
				elif param.get("person", 3) == 3:
					word = self.makePlural(word)
		elif param.get("question", False) == True:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"y")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"m")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"s")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"n")
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"y")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"z")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"s")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"n")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
					word = self.concat(word, u"z")
				elif param.get("person", 3) == 3:
					word = self.makePlural(word)
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)[u"letter"]])
		return word 

	# Geniş zaman
	def makePresentSimple(self, pword, param = {}):
		word = pword
		getLastLetter = self.lastLetter(word)
		getLastVowel = self.lastVowel(word)

		lastLetterIsVowel = getLastLetter[u"letter"] in self.VOWELS
	
		minorHarmonyLetter = self.MINOR_HARMONY[getLastVowel[u"letter"]]
		minorHarmonyLetterFF = self.MINOR_HARMONY_FOR_FUTURE[getLastVowel[u"letter"]]
		minorHA = self.MINOR_HARMONY_FOR_FUTURE[minorHarmonyLetter]

		if param.get("negative", False) == False:
			if u"discontinious_hard_consonant" in getLastLetter and getLastVowel[u"vowel_count"] > 1:
				word = self.concat(word[0:len(word) - 1], getLastLetter[u"soften_consonant"])

		if param.get("question", False) == True: 
			if param.get("negative", False) == False:
				if lastLetterIsVowel == False:
					word = self.concat(word, minorHarmonyLetterFF)

				word = self.concat(word, u"r")

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "y")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"m")
					elif param.get("person", 3) == 2:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"n")
					elif param.get("person", 3) == 3:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)				
				elif param.get("quantity", "singular") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "y")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"z")
					elif param.get("person", 3) == 2:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"n")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"z")
					elif param.get("person", 3) == 3:
						word = self.makePlural(word)
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)	
			if param.get("negative", True) == True:
				getLastVowel = self.lastVowel(word)
				minorHarmonyLetterFF = self.MINOR_HARMONY_FOR_FUTURE[getLastVowel[u"letter"]]

				word = self.concat(word, u"m")
				word = self.concat(word, minorHarmonyLetterFF)
				word = self.concat(word, u"z")

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "y")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"m")
					elif param.get("person", 3) == 2:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"n")
					elif param.get("person", 3) == 3:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)				
				elif param.get("quantity", "singular") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "y")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"z")
					elif param.get("person", 3) == 2:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"n")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"z")
					elif param.get("person", 3) == 3:
						word = self.makePlural(word)
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)	
		elif param.get("question", False) == False: 
			if param.get("negative", False) == False:
				if lastLetterIsVowel == False:
					word = self.concat(word, minorHarmonyLetterFF) 
				
				word = self.concat(word, u"r")

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"m")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"n")
				elif param.get("quantity", "singular") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"z")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"n")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, u"z")
					elif param.get("person", 3) == 3:
						word = self.makePlural(word)
			elif param.get("negative", False) == True:
				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, u"m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, u"m")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, u"z")
						word = self.concat(word, u"s")
						word = self.concat(word, self.MINOR_HARMONY[minorHA]) 
						word = self.concat(word, u"n")
					elif param.get("person", 3) == 3:
						word = self.concat(word, u"m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, u"z")
				elif param.get("quantity", "singular") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, u"m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, u"y")
						word = self.concat(word, self.MINOR_HARMONY[minorHA]) 
						word = self.concat(word, u"z")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, u"z")
						word = self.concat(word, u"s")
						word = self.concat(word, self.MINOR_HARMONY[minorHA])
						word = self.concat(word, u"n")
						word = self.concat(word, self.MINOR_HARMONY[minorHA]) 
						word = self.concat(word, u"z")
					elif param.get("person", 3) == 3:
						word = self.concat(word, u"m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, u"z")
						word = self.makePlural(word)

		return word

	# Gelecek zaman
	def makeFuture(self, pword, param = {}):
		word = pword

		if param.get("negative", False) == True:
			if self.lastVowel(word)[u"tone"] == u"front":
				word = self.concat(word, u"ma")
			else:
				word = self.concat(word, u"me")

		getLastLetter = self.lastLetter(word)
			
		if u"vowel" in getLastLetter:
			word = self.concat(word, u"y")

		if param.get("question", False) == True:
			if self.lastVowel(word)[u"tone"] == u"front":
				if param.get("person", 3) == 3 and param.get("quantity", "singular") == "plural":
					word = self.concat(word, u"acaklar ")
				else:
					word = self.concat(word, u"acak ")

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, u"mıyım")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"mısın")
					elif param.get("person", 3) == 3:
						word = self.concat(word, u"mı")
				elif param.get("quantity", "singular") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, u"mıyız")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"mısınız")
					elif param.get("person", 3) == 3:
						word = self.concat(word, u"mı")
			else:
				word = self.concat(word, u"ecek ")
				if param.get("person", 3) == 3 and param.get("quantity", "singular") == "plural":
					word = self.concat(word, u"ecekler ")
				else:
					word = self.concat(word, u"ecek ")

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, u"miyim")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"misin")
					elif param.get("person", 3) == 3:
						word = self.concat(word, u"mi")
				elif param.get("quantity", "singular") == True:
					if param.get("person", 3) == 1:
						word = self.concat(word, u"miyiz")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"misiniz")
					elif param.get("person", 3) == 3:
						word = self.concat(word, u"mi")
		elif param.get("question", False) == False:
			if self.lastVowel(word)[u"tone"] == u"front":
				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, u"acağım")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"acaksın")
					elif param.get("person", 3) == 3:
						word = self.concat(word, u"acak")
				elif param.get("quantity", "singular") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, u"acağız")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"acaksınız")
					elif param.get("person", 3) == 3:
						word = self.concat(word, u"acaklar")
			else:
				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, u"eceğim")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"eceğiz")
					elif param.get("person", 3) == 3:
						word = self.concat(word, u"ecek")
				elif param.get("quantity", "plural") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, u"eceğiz")
					elif param.get("person", 3) == 2:
						word = self.concat(word, u"eceksiniz")
					elif param.get("person", 3) == 3:
						word = self.concat(word, u"ecekler")

		return word

	
	# Not the same with English past perfect tense
	# This usage is for past tense of an action which is heared/learned but not witnessed.
	# mişli geçmiş zaman veya öğrenilen geçmiş zaman
	def makePastPerfect(self, pword, param = {}):
		word = pword

		if param.get("negative", False) == True:
			word = self.concat(word, u"m")

			if self.lastVowel(word)[u"tone"] == u"front":
				word = self.concat(word, u"a")
			else:
				word = self.concat(word, u"e")

		getLastVowel = self.lastVowel(word)
		minorHarmonyLetter= self.MINOR_HARMONY[getLastVowel[u"letter"]]

		word = self.concat(word, u"m")
		word = self.concat(word, minorHarmonyLetter)
		word = self.concat(word, u"ş")

		if param.get("question", False) == False:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"m")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u"s")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"n")
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"z")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u"s")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"n")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"z")
				elif param.get("person", 3) == 2:
					word = self.makePlural(word)
		elif param.get("question", False) == True:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"y")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"m")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"s")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"n")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, minorHarmonyLetter)
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"y")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"z")
				elif param.get("person", 3) == 2:
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"s")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"n")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, u"z")
				elif param.get("person", 3) == 2:
					word = self.makePlural(word)
					word = self.concat(word, u" ")
					word = self.concat(word, u"m")
					word = self.concat(word, minorHarmonyLetter)
		return word
	# Unified verbs (Birleşik fiiler) 
	# Ability - Yeterlilik: kızabilir (bil) (English modal auxiliary verb: Can)
	# Swiftness - Tezlik: koşuver (ver) ()
	# Continuity - Süreklilik: gidedursun, bakakalmak, uyuyakalmak (dur, kal, gel, koy)
	# Approach - Yaklaşma: (yaz) düzeyazmak


tr = turkish()

print (tr.makePresentContinuous(u"at", { "negative": False, "question": False, "person": 1, "quantity": "singular" }))
print (tr.makePresentContinuous(u"at", { "negative": False, "question": False, "person": 2, "quantity": "singular" }))
print (tr.makePresentContinuous(u"at", { "negative": False, "question": False, "person": 3, "quantity": "singular" }))
print (tr.makePresentContinuous(u"at", { "negative": False, "question": False, "person": 1, "quantity": "plural" }))
print (tr.makePresentContinuous(u"at", { "negative": False, "question": False, "person": 2, "quantity": "plural" }))
print (tr.makePresentContinuous(u"at", { "negative": False, "question": False, "person": 3, "quantity": "plural" }))

print (tr.makePresentContinuous(u"at", { "negative": False, "question": True, "person": 1, "quantity": "singular" }))
print (tr.makePresentContinuous(u"at", { "negative": False, "question": True, "person": 2, "quantity": "singular" }))
print (tr.makePresentContinuous(u"at", { "negative": False, "question": True, "person": 3, "quantity": "singular" }))
print (tr.makePresentContinuous(u"at", { "negative": False, "question": True, "person": 1, "quantity": "plural" }))
print (tr.makePresentContinuous(u"at", { "negative": False, "question": True, "person": 2, "quantity": "plural" }))
print (tr.makePresentContinuous(u"at", { "negative": False, "question": True, "person": 3, "quantity": "plural" }))

print (tr.makePresentContinuous(u"at", { "negative": True, "question": False, "person": 1, "quantity": "singular" }))
print (tr.makePresentContinuous(u"at", { "negative": True, "question": False, "person": 2, "quantity": "singular" }))
print (tr.makePresentContinuous(u"at", { "negative": True, "question": False, "person": 3, "quantity": "singular" }))
print (tr.makePresentContinuous(u"at", { "negative": True, "question": False, "person": 1, "quantity": "plural" }))
print (tr.makePresentContinuous(u"at", { "negative": True, "question": False, "person": 2, "quantity": "plural" }))
print (tr.makePresentContinuous(u"at", { "negative": True, "question": False, "person": 3, "quantity": "plural" }))

print (tr.makePresentContinuous2(u"at", { "negative": True, "question": True, "person": 1, "quantity": "singular" }))
print (tr.makePresentContinuous2(u"at", { "negative": True, "question": True, "person": 2, "quantity": "singular" }))
print (tr.makePresentContinuous2(u"at", { "negative": True, "question": True, "person": 3, "quantity": "singular" }))
print (tr.makePresentContinuous2(u"at", { "negative": True, "question": True, "person": 1, "quantity": "plural" }))
print (tr.makePresentContinuous2(u"at", { "negative": True, "question": True, "person": 2, "quantity": "plural" }))
print (tr.makePresentContinuous2(u"at", { "negative": True, "question": True, "person": 3, "quantity": "plural" }))

print (tr.makeFuture(u"at", { "negative": True, "question": False, "person": 3, "quantity": "plural"}))

print (tr.makeGenitive(u"Öykü", {"proper_noun": True}))
print (tr.makeDative("Fatma", {"proper_noun": True}))
print (tr.makeAblative("Ali", {"proper_noun": True}))
print (tr.makeAccusative(u"Kaliningrad", {"proper_noun": True}))

print (tr.makeGenitive(u"ağaç", {"proper_noun": False}))
print (tr.makeAccusative(u"erik", {"proper_noun": False}))
print (tr.makeAccusative(u"Erik", {"proper_noun": True}))


print (tr.possessiveAffix("çanta", {"person": 1, "quantity": "singular"}))
print (tr.possessiveAffix("çanta", {"person": 2, "quantity": "singular"}))
print (tr.possessiveAffix("çanta", {"person": 3, "quantity": "singular"}))

print (tr.possessiveAffix("çanta", {"person": 1, "quantity": "plural"}))
print (tr.possessiveAffix("çanta", {"person": 2, "quantity": "plural"}))
print (tr.possessiveAffix("çanta", {"person": 3, "quantity": "plural"}))


print (tr.makePresentSimple(u"at", { "negative": False, "question": False, "person": 1, "quantity": "singular" }))
print (tr.makePresentSimple(u"at", { "negative": False, "question": False, "person": 2, "quantity": "singular" }))
print (tr.makePresentSimple(u"at", { "negative": False, "question": False, "person": 3, "quantity": "singular" }))
print (tr.makePresentSimple(u"at", { "negative": False, "question": False, "person": 1, "quantity": "plural" }))
print (tr.makePresentSimple(u"at", { "negative": False, "question": False, "person": 2, "quantity": "plural" }))
print (tr.makePresentSimple(u"at", { "negative": False, "question": False, "person": 3, "quantity": "plural" }))

print (tr.makePresentSimple(u"seyret", { "negative": True, "question": False, "person": 1, "quantity": "singular" }))
print (tr.makePresentSimple(u"seyret", { "negative": True, "question": False, "person": 2, "quantity": "singular" }))
print (tr.makePresentSimple(u"seyret", { "negative": True, "question": False, "person": 3, "quantity": "singular" }))
print (tr.makePresentSimple(u"seyret", { "negative": True, "question": False, "person": 1, "quantity": "plural" }))
print (tr.makePresentSimple(u"seyret", { "negative": True, "question": False, "person": 2, "quantity": "plural" }))
print (tr.makePresentSimple(u"seyret", { "negative": True, "question": False, "person": 3, "quantity": "plural" }))

print (tr.makePresentSimple(u"at", { "negative": False, "question": True, "person": 1, "quantity": "singular" }))
print (tr.makePresentSimple(u"at", { "negative": False, "question": True, "person": 2, "quantity": "singular" }))
print (tr.makePresentSimple(u"at", { "negative": False, "question": True, "person": 3, "quantity": "singular" }))
print (tr.makePresentSimple(u"at", { "negative": False, "question": True, "person": 1, "quantity": "plural" }))
print (tr.makePresentSimple(u"at", { "negative": False, "question": True, "person": 2, "quantity": "plural" }))
print (tr.makePresentSimple(u"at", { "negative": False, "question": True, "person": 3, "quantity": "plural" }))

print (tr.makePresentSimple(u"at", { "negative": True, "question": True, "person": 1, "quantity": "singular" }))
print (tr.makePresentSimple(u"at", { "negative": True, "question": True, "person": 2, "quantity": "singular" }))
print (tr.makePresentSimple(u"at", { "negative": True, "question": True, "person": 3, "quantity": "singular" }))
print (tr.makePresentSimple(u"at", { "negative": True, "question": True, "person": 1, "quantity": "plural" }))
print (tr.makePresentSimple(u"at", { "negative": True, "question": True, "person": 2, "quantity": "plural" }))
print (tr.makePresentSimple(u"at", { "negative": True, "question": True, "person": 3, "quantity": "plural" }))

print (tr.makeInfinitive(u"at", { "negative": True} ))

print (tr.makePastPerfect(u"ölç", { "negative": True, "question": True, "person": 1, "quantity": "plural" }))