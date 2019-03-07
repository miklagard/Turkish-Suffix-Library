#!/usr/bin/python
# -*- coding: utf-8 -*-

class turkish:
	VOWELS = "aıoöuüei"
	FRONT_VOWELS = "aıo"
	BACK_VOWELS = "eiöü"
	HARD_CONSONANTS = "fstkçşhp"
	DISCONTINIOUS_HARD_CONSONANTS = "pçtk"
	SOFTEN_DHC = "bcdğ"
	DISCONTINIOUS_HARD_CONSONANTS_AFTER_SUFFIX = "pçk"
	SOFTEN_DHC_AFTER_SUFFIX = "bcğ"	
	MINOR_HARMONY = {
		"a": "ı"
		, "e": "i"
		, "ö": "ü"
		, "o": ""
		, "ı": "ı"
		, "i": "i"
		, "": ""
		, "ü": "ü"
	}
	
	MINOR_HARMONY_FOR_FUTURE = {
		"a": "a"
		, "e": "e"
		, "ö": "ü"
		, "o": ""
		, "ı": "ı"
		, "i": "e"
		, "": ""
		, "ü": "e"
	}
	
	# The exception words which has non-Turkish origins donn't fit for standard Turkish Major Wovel Harmony
	# beacuse of the vocal difference which doesn't exist in Turkish.
	EXCEPTION_WORDS = [
		"ahval"
		, "akropol"
		, "alkol"
		, "ametal"
		, "amiral"
		, "ampul"
		, "anormal"
		, "bandrol"
		, "bemol"
		, "beşamol"
		, "bilkat"
		, "cemaat"
		, "cemal"
		, "deccal"
		, "dikkat"
		, "ekol"
		, "ekümenapol"
		, "emsal"
		, "enstrümantal"
		, "enternasyonal"
		, "faal"
		, "faul"
		, "final"
		, "general"
		, "glikol"
		, "gol"
		, "hakikat"
		, "hal"
		, "harf"
		, "hayal"
		, "hilal"
		, "hiperbol"
		, "hol"
		, "integral"
		, "iştigal"
		, "istikbal"
		, "istiklal"
		, "jurnal"
		, "kabul"
		, "kalp"
		, "kanaat"
		, "kapital"
		, "karambol"
		, "katedral"
		, "kefal"
		, "kemal"
		, "kıraat"
		, "kolestrol"
		, "kontrol"
		, "koramiral"
		, "korgeneral"
		, "legal"
		, "liberal"
		, "liyakat"
		, "lokal"
		, "mahmul"
		, "mahsul"
		, "maktul"
		, "makul"
		, "meal"
		, "menkul"
		, "mentol"
		, "meral"
		, "meraşal"
		, "meşekkat"
		, "meşgul"
		, "metal"
		, "metaryal"
		, "metrapol"
		, "mineral"
		, "misal"
		, "moral"
		, "müzikal"
		, "müzikhol"
		, "nasyonal"
		, "normal"
		, "ohal" # abbreviation
		, "oramiral"
		, "orjinal"
		, "oryantal"
		, "oval"
		, "parabol"
		, "paranormal"
		, "pastoral"
		, "perhidrol"
		, "petrol"
		, "radikal"
		, "refakat"
		, "resital"
		, "resul"
		, "rol"
		, "saat"
		, "sadakat"
		, "santral"
		, "şefkat"
		, "şevval"
		, "sinyal"
		, "sosyal"
		, "spesiyal"
		, "sual"
		, "tefal" # brand
		, "termal"
		, "terminal"
		, "total"
		, "trambol"
		, "tropikal"
		, "tuğamiral"
		, "tuğgeneral"
		, "tümgeneral"
		, "turnusol"
		, "tuval"
		, "usul"
		, "zelal"
		, "zerdeçal"
		, "zeval"
		, "ziraat"
	]

	
	EXCEPTION_MISSING = {
		"isim": "ism",
		"kasır": "kasr",
		"kısım": "kısm",
		"af": "aff",
		"ilim": "ilm",
		#"hatır": "hatr", # for daily usage only
		"boyun": "boyn",
		"nesil": "nesl",
		"koyun": "koyn", # koyun (sheep) or koyun (bosom)? for koyun (sheep) there is no exception but for koyun (bosom) there is. aaaaargh turkish!!
		"karın": "karn" #same with this, karın (your wife) or karın (stomach)? for karın (your wife) there is not a such exception
		#katli, katle, katli etc. it doesn't really have a nominative case but only with suffixes?
	}	 

	def isUpper(self, pword):
		word = pword
		word = word.replace("ı", "i").replace("İ", "I").replace("ş", "s").replace("Ş", "S").replace("ğ", "g").replace("Ğ", "G").replace("ü", "").replace("Ü", "U").replace("ç", "c").replace("Ç", "C").replace("ö", "o").replace("Ö", "O")
		return word.isupper()
	
	def makeLower(self, pword):
		word = pword
		return word.replace("İ", "i").replace("I", "ı").lower()
	
	def makeUpper(self, pword):
		word = pword 
		return word.replace("i", "İ").replace("ı", "I").upper()
	 
	def concat(self, xstr1, xstr2):
		str1 = xstr1
		str2 = xstr2 
		if self.isUpper(str1) == True:
			returndata = str1 + makeUpper(str2)
		else:
			returndata = str1 + str2
		
		return returndata
	
	def fromUpperOrLower(self, pnewWord, prefWord):
		newWord = pnewWord
		prefWord = prefWord

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

		returndata = ""

		for letter in word:
			if letter in self.FRONT_VOWELS:
				vowel_count = vowel_count + 1
				returndata = {"letter": letter, "tone": "front"}
			elif letter in self.BACK_VOWELS:
				vowel_count = vowel_count + 1
				returndata = {"letter": letter, "tone": "back"}
	
		# fake return for exception behaviour in Turkish
		if word in self.EXCEPTION_WORDS:
			if returndata["letter"] == "o":
				returndata = {"letter": "ö", "tone": "back"}
			elif returndata["letter"] == "a":
				returndata = {"letter": "e", "tone": "back"}
			elif returndata["letter"] == "":
				returndata = {"letter": "ü", "tone": "back"}
			
		if returndata == "":
			returndata = {"letter": "", "tone": "back"}
	
		returndata["vowel_count"] = vowel_count
		return returndata
	
	def lastLetter(self, pword):
		word = self.makeLower(pword)
		returndata = {}
		getLastLetter = word[len(word) - 1]
		if getLastLetter == "'":
			getLastLetter = word[len(word) - 2]
		
		returndata["letter"] = getLastLetter	  
		
		if getLastLetter in self.VOWELS:
			returndata["vowel"] = True
			if getLastLetter in self.FRONT_VOWELS:
				returndata["front_vowel"] = True
			else:
				returndata["back_vowel"] = True
		else:
			returndata["consonant"] = True
			
			if getLastLetter in self.DISCONTINIOUS_HARD_CONSONANTS:
				returndata["discontinious_hard_consonant"] = True
				getLastLetter = self.SOFTEN_DHC[self.DISCONTINIOUS_HARD_CONSONANTS.index(getLastLetter)]
				returndata["soften_consonant"] = getLastLetter

		getLastLetter = word[len(word) - 1]
		if getLastLetter == "'":
			getLastLetter = word[len(word) - 2]

		if getLastLetter in self.HARD_CONSONANTS:
				returndata["hard_consonant"] = True

				if getLastLetter in self.DISCONTINIOUS_HARD_CONSONANTS_AFTER_SUFFIX:
					returndata["discontinious_hard_consonant_for_suffix"] = True
					getLastLetter = self.SOFTEN_DHC_AFTER_SUFFIX[self.DISCONTINIOUS_HARD_CONSONANTS_AFTER_SUFFIX.index(getLastLetter)]
					returndata["soften_consonant_for_suffix"] = getLastLetter
	
		return returndata	
	
	def makePlural(self, pword, param = {}):
		word = pword

		if "proper_noun" in param:
			word = word + "'"
		
		if self.lastVowel(word)["tone"] == "front":
			returndata = self.concat(word, "lar")
		else:
			returndata = self.concat(word, "ler")
			
		return returndata

	#-i hali   
	def makeAccusative(self, pword, param = {}): # not finished yet
		#firslty exceptions for o (he/she/it) 
		word = pword
		
		lowerWord = self.makeLower(word)
	
		proper_noun = param.get("proper_noun", False)
	
		if lowerWord == "o":
			if proper_noun == True:
				returndata = self.fromUpperOrLower("O'nu", word)
			else:
				returndata = self.fromUpperOrLower("onu", word)
		else:
			if lowerWord in self.EXCEPTION_MISSING and proper_noun == True:
				word = self.fromUpperOrLower(self.EXCEPTION_MISSING[lowerWord], word)
				lowerWord = self.makeLower(word)
			
			getLastLetter = self.lastLetter(word)
			getLastVowel = self.lastVowel(word)
			
			if proper_noun == True:
				word += "'"

			if "vowel" in getLastLetter:
				word = self.concat(word, "y")
			elif "discontinious_hard_consonant" in getLastLetter and proper_noun == False:
				if getLastVowel["vowel_count"] > 1:
					word = self.concat(word[0:len(word) - 1], getLastLetter["soften_consonant"])
	
			word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
	
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
	
		if lowerWord == "ben" and proper_noun == False:
			returndata = fromUpperOrLower("bana", word)
		elif lowerWord == "sen" and proper_noun == False:
			returndata = self.fromUpperOrLower("sana", word)
		else:
			if lowerWord in self.EXCEPTION_MISSING and proper_noun == False:
				word = self.fromUpperOrLower(self.EXCEPTION_MISSING[lowerWord], word)
				lowerWord = self.makeLower(word)
	
			getLastLetter = self.lastLetter(word)
			getLastVowel = self.lastVowel(word)
				
			if "vowel" in getLastLetter:
				word = self.concat(word, "y")
			elif "discontinious_hard_consonant_for_suffix" in getLastLetter:
				if getLastVowel["vowel_count"] > 1 and proper_noun == False:
					word = self.concat(word[0:len(word) - 1], getLastLetter["soften_consonant_for_suffix"])
	
			if getLastVowel["tone"] == "front":
				word = self.concat(word, "a")
			else:
				word = self.concat(word, "e")
			
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

		if "hard_consonant" in getLastLetter:
			word = self.concat(word, "t")
		else:
			word = self.concat(word, "d")

		if getLastVowel["tone"] == "front" and not word in self.EXCEPTION_WORDS:
			word = self.concat(word, "a")
		else:
			word = self.concat(word, "e")
		
		return word

	#-den hali
	def makeAblative(self, pword, param = {}):
		word = pword

		getLastLetter = self.lastLetter(word)
		getLastVowel = self.lastVowel(word)
		proper_noun = param.get("proper_noun", False)
	
		if proper_noun == True:
			word += "'"
	
		if getLastLetter["letter"] in self.HARD_CONSONANTS:
			word = self.concat(word, "t")
		else:
			word = self.concat(word, "d")
	
		if getLastVowel["tone"] == "front":
			word = self.concat(word, "an")
		else:
			word = self.concat(word, "en")
		
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
			word = self.concat(word, "t")
		else:
			word = self.concat(word, "d")
	
		if getLastVowel["tone"] == "front":
			word = self.concat(word, "a")
		else:
			word = self.concat(word, "e")
		
		returndata = word
		
		return returndata
	
	# İyelik ekleri
	def possessiveAffix(self, pword, param = {}):
		position = param.get("position", 1)
		word = pword
		
		person = str(param.get("person", 3))
		quantity = param.get("quantity", "singular")
	
		proper_noun = param.get("proper_noun", False)
			
		if not(person == "3" and quantity == "plural"):
			getLastLetter = self.lastLetter(word)
			getLastVowel = self.lastVowel(word)
			
			if proper_noun == True:
				word += "'"
			elif "discontinious_hard_consonant" in getLastLetter:
				if getLastVowel["vowel_count"] > 1:
					word = self.concat(word[0:len(word) - 1], getLastLetter["soften_consonant"])
				if (self.makeLower(word) in self.EXCEPTION_MISSING): 
					word = self.fromUpperOrLower(self.EXCEPTION_MISSING[self.makeLower(word)], word)
		
		getLastLetter = self.lastLetter(word)
		getLastVowel = self.lastVowel(word)
		
		lastLetterIsVowel = getLastLetter["letter"] in self.VOWELS
		
		minorHarmonyLetter = self.MINOR_HARMONY[getLastVowel["letter"]]
	
		if quantity == "singular":
			if lastLetterIsVowel == False:
				word = self.concat(word, minorHarmonyLetter)
	
			if person == "1": 
				word = self.concat(word, "m")
			
			elif person == "2": 
				word = self.concat(word, "n")

			elif person == "3":
				word = self.concat(word, "s")
				word = self.concat(word, minorHarmonyLetter)
		else:
			if person == "1":
				if lastLetterIsVowel == False:
					word = self.concat(word, minorHarmonyLetter)
				word = self.concat(word, "m")				
				word = self.concat(word, minorHarmonyLetter)
				word = self.concat(word, "z")				
			elif person == "2":
				if lastLetterIsVowel == False:
					word = self.concat(word, minorHarmonyLetter)
				word = self.concat(word, "n")				
				word = self.concat(word, minorHarmonyLetter)
				word = self.concat(word, "z")				
			else:
				if self.makeLower(word) == "ism":
					word = self.fromUpperOrLower("isim", word)
				word = self.makePlural(word)
				word = self.concat(word, minorHarmonyLetter)
			
		return word

	# Mastar eski
	def makeInfinitive(self, pword, param = {}):
		word = pword

		if param.get("negative", False) == True:
			if self.lastVowel(word)["tone"] == "front":
				returndata = self.concat(word, "mamak")
			else:
				returndata = self.concat(word, "memek")
		else: 
			if self.lastVowel(word)["tone"] == "front":
				returndata = self.concat(word, "mak")
			else:
				returndata = self.concat(word, "mek")
			
		return returndata	


	# Şimdiki zaman 
	#	   * arıyorum
	#	   * For alternative usage of present continuous tense, check the function makePresentContinuous2
	def makePresentContinuous(self, pword, param = {}):
		word = pword

		getLastLetter = self.lastLetter(word)
		getLastVowel = self.lastVowel(word)

		lastLetterIsVowel = getLastLetter["letter"] in self.VOWELS

		if param.get("negative", False) == False:
			#if "discontinious_hard_consonant" in getLastLetter and getLastVowel["vowel_count"] > 1:
			#	word = self.concat(word[0:len(word) - 1], getLastLetter["soften_consonant"])

			if word == "git":
				word = "gid"
	
			if lastLetterIsVowel:
				word = self.concat(word[:-1], self.MINOR_HARMONY[word[-1]])
			else:
				word = self.concat(word, self.MINOR_HARMONY[getLastVowel["letter"]])
		else:
			word = self.concat(word, "m")
			word = self.concat(word, self.MINOR_HARMONY[getLastVowel["letter"]])


		word = self.concat(word, "yor")

		if param.get("question", False) == True:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, " muyum")
				elif param.get("person", 3) == 2:
					word = self.concat(word, " musun")
				elif param.get("person", 3) == 3:
					word = self.concat(word, " m")
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, " muyuz")
				elif param.get("person", 3) == 2:
					word = self.concat(word, " musunuz")
				elif param.get("person", 3) == 3:
					word = self.makePlural(word)
					word = self.concat(word, " m")
					if self.lastVowel(word)["tone"] == "front":
						word = self.concat(word, "ı")
					else:
						word = self.concat(word, "i")
		else:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, "um")
				elif param.get("person", 3) == 2:
					word = self.concat(word, "sun")
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, "uz")
				elif param.get("person", 3) == 2:
					word = self.concat(word, "sunuz")
				elif param.get("person", 3) == 3:
					word = self.makePlural(word)


		return word

	def makePresentContinuous2(self, pword, param = {}):
	# There are two ways to express "present continuous tense in Turkish "
	# This kind is not common in daily Turkish usage anymore
	#	   * aramaktayım
	#	   * yapmaktayım
		word = pword

		if param.get("negative", False) == True:
			if self.lastVowel(word)["tone"] == "front":
				word = self.concat(word, "ma")
			else:
				word = self.concat(word, "me")

		word = self.makeInfinitive(word, param = {})

		if self.lastVowel(word)["tone"] == "front":
			word = self.concat(word, "ta")
		else:
			word = self.concat(word, "te")

		if param.get("question", False)  == False:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, "y")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "mu")
				elif param.get("person", 3) == 2:
					word = self.concat(word, "s")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "n")
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, "y")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "z")
				elif param.get("person", 3) == 2:
					word = self.concat(word, "s")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "n")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "z")
				elif param.get("person", 3) == 3:
					word = self.makePlural(word)
		elif param.get("question", False) == True:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "y")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "m")
				elif param.get("person", 3) == 2:
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "s")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "n")
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "y")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "z")
				elif param.get("person", 3) == 2:
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "s")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "n")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
					word = self.concat(word, "z")
				elif param.get("person", 3) == 3:
					word = self.makePlural(word)
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
		return word 

	# Geniş zaman
	def makePresentSimple(self, pword, param = {}):
		word = pword
		getLastLetter = self.lastLetter(word)
		getLastVowel = self.lastVowel(word)

		lastLetterIsVowel = getLastLetter["letter"] in self.VOWELS
	
		minorHarmonyLetter = self.MINOR_HARMONY[getLastVowel["letter"]]
		minorHarmonyLetterFF = self.MINOR_HARMONY_FOR_FUTURE[getLastVowel["letter"]]
		minorHA = self.MINOR_HARMONY_FOR_FUTURE[minorHarmonyLetter]

		if param.get("negative", False) == False:
			if "discontinious_hard_consonant" in getLastLetter and getLastVowel["vowel_count"] > 1:
				word = self.concat(word[0:len(word) - 1], getLastLetter["soften_consonant"])
			if word == "git":
				word = "gid"

		if param.get("question", False) == True: 
			if param.get("negative", False) == False:
				if lastLetterIsVowel == False:
					word = self.concat(word, minorHarmonyLetterFF)

				word = self.concat(word, "r")

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "y")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "m")
					elif param.get("person", 3) == 2:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "n")
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
						word = self.concat(word, "z")
					elif param.get("person", 3) == 2:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "n")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "z")
					elif param.get("person", 3) == 3:
						word = self.makePlural(word)
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)	
			elif param.get("negative", False) == True:
				getLastVowel = self.lastVowel(word)

				if self.lastVowel(word)["tone"] == "front":
					minorHarmonyLetterFF = "a"
				else:
					minorHarmonyLetterFF = "e"

				word = self.concat(word, "m")
				word = self.concat(word, minorHarmonyLetterFF)
				word = self.concat(word, "z")

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "y")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "m")
					elif param.get("person", 3) == 2:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "n")
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
						word = self.concat(word, "z")
					elif param.get("person", 3) == 2:
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "n")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "z")
					elif param.get("person", 3) == 3:
						word = self.makePlural(word)
						word = self.concat(word, " ")
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetter)	
		elif param.get("question", False) == False: 
			if param.get("negative", False) == False:
				if lastLetterIsVowel == False:
					word = self.concat(word, minorHarmonyLetterFF) 
				
				word = self.concat(word, "r")

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "m")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "n")
				elif param.get("quantity", "singular") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "z")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "s")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "n")
						word = self.concat(word, minorHarmonyLetter)
						word = self.concat(word, "z")
					elif param.get("person", 3) == 3:
						word = self.makePlural(word)
			elif param.get("negative", False) == True:
				if self.lastVowel(word)["tone"] == "front":
					minorHarmonyLetterFF = "a"
				else:
					minorHarmonyLetterFF = "e"

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, "m")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, "z")
						word = self.concat(word, "s")
						word = self.concat(word, self.MINOR_HARMONY[minorHA]) 
						word = self.concat(word, "n")
					elif param.get("person", 3) == 3:
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, "z")
				elif param.get("quantity", "singular") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, "y")
						word = self.concat(word, self.MINOR_HARMONY[minorHA]) 
						word = self.concat(word, "z")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, "z")
						word = self.concat(word, "s")
						word = self.concat(word, self.MINOR_HARMONY[minorHA])
						word = self.concat(word, "n")
						word = self.concat(word, self.MINOR_HARMONY[minorHA]) 
						word = self.concat(word, "z")
					elif param.get("person", 3) == 3:
						word = self.concat(word, "m")
						word = self.concat(word, minorHarmonyLetterFF)
						word = self.concat(word, "z")
						word = self.makePlural(word)

		return word

	# Gelecek zaman
	def makeFuture(self, pword, param = {}):
		word = pword

		if param.get("negative", False) == True:
			if self.lastVowel(word)["tone"] == "front":
				word = self.concat(word, "ma")
			else:
				word = self.concat(word, "me")

		getLastLetter = self.lastLetter(word)
		getLastVowel = self.lastVowel(word)

		if "vowel" in getLastLetter:
			if word == "de":
				word = "di"
			elif word == "ye":
				word = "yi"

			word = self.concat(word, "y")
		elif "discontinious_hard_consonant" in getLastLetter and getLastVowel["vowel_count"] > 1 and param.get("negative", False) == False:
			word = self.concat(word[0:len(word) - 1], getLastLetter["soften_consonant"])
		

		if param.get("negative", False) == False:
			if word == "git":
				word = "gid"


		if param.get("question", False) == True:
			if self.lastVowel(word)["tone"] == "front":
				if param.get("person", 3) == 3 and param.get("quantity", "singular") == "plural":
					word = self.concat(word, "acaklar ")
				else:
					word = self.concat(word, "acak ")

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, "mıyım")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "mısın")
					elif param.get("person", 3) == 3:
						word = self.concat(word, "mı")
				elif param.get("quantity", "singular") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, "mıyız")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "mısınız")
					elif param.get("person", 3) == 3:
						word = self.concat(word, "mı")
			else:
				if param.get("person", 3) == 3 and param.get("quantity", "singular") == "plural":
					word = self.concat(word, "ecekler ")
				else:
					word = self.concat(word, "ecek ")

				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, "miyim")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "misin")
					elif param.get("person", 3) == 3:
						word = self.concat(word, "mi")
				elif param.get("quantity", "singular") == True:
					if param.get("person", 3) == 1:
						word = self.concat(word, "miyiz")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "misiniz")
					elif param.get("person", 3) == 3:
						word = self.concat(word, "mi")
		elif param.get("question", False) == False:
			if self.lastVowel(word)["tone"] == "front":
				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, "acağım")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "acaksın")
					elif param.get("person", 3) == 3:
						word = self.concat(word, "acak")
				elif param.get("quantity", "singular") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, "acağız")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "acaksınız")
					elif param.get("person", 3) == 3:
						word = self.concat(word, "acaklar")
			else:
				if param.get("quantity", "singular") == "singular":
					if param.get("person", 3) == 1:
						word = self.concat(word, "eceğim")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "eceğiz")
					elif param.get("person", 3) == 3:
						word = self.concat(word, "ecek")
				elif param.get("quantity", "plural") == "plural":
					if param.get("person", 3) == 1:
						word = self.concat(word, "eceğiz")
					elif param.get("person", 3) == 2:
						word = self.concat(word, "eceksiniz")
					elif param.get("person", 3) == 3:
						word = self.concat(word, "ecekler")

		return word

	
	# Not the same with English past perfect tense
	# This usage is for past tense of an action which is heared/learned but not witnessed.
	# mişli geçmiş zaman veya öğrenilen geçmiş zaman
	def makePastPerfect(self, pword, param = {}):
		word = pword

		if param.get("negative", False) == True:
			word = self.concat(word, "m")

			if self.lastVowel(word)["tone"] == "front":
				word = self.concat(word, "a")
			else:
				word = self.concat(word, "e")

		getLastVowel = self.lastVowel(word)
		minorHarmonyLetter= self.MINOR_HARMONY[getLastVowel["letter"]]

		word = self.concat(word, "m")
		word = self.concat(word, minorHarmonyLetter)
		word = self.concat(word, "ş")

		if param.get("question", False) == False:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "m")
				elif param.get("person", 3) == 2:
					word = self.concat(word, "s")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "n")
			elif param.get("quantity", "singular") == "plural":
				if param.get("person", 3) == 1:
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "z")
				elif param.get("person", 3) == 2:
					word = self.concat(word, "s")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "n")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "z")
				elif param.get("person", 3) == 3:
					word = self.makePlural(word)
		elif param.get("question", False) == True:
			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "y")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "m")
				elif param.get("person", 3) == 2:
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "s")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "n")
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
					word = self.concat(word, "z")
				elif param.get("person", 3) == 2:
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "s")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "n")
					word = self.concat(word, minorHarmonyLetter)
					word = self.concat(word, "z")
				elif param.get("person", 3) == 3:
					word = self.makePlural(word)
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, minorHarmonyLetter)
		return word

	# Unified verbs (Birleşik fiiler) (Not a suffix but for "can-bil" modal verb, this is necessary)
	# Ability - Yeterlilik: kızabil (bil) (English modal auxiliary verb: Can)
	# Swiftness - Tezlik: koşuver (ver) 
	# Continuity - Süreklilik: gidedur, bakakal, alıkoy (dur, kal, gel, koy)
	# Approach - Yaklaşma: (yaz) düzeyaz
	def unifyVerbs(self, pword, param = {}):
		word = pword

		if word == "de":
			word = "di"
		elif word == "ye":
			word = "yi"


		getLastLetter = self.lastLetter(word)
		getLastVowel = self.lastVowel(word)
		getAuxLastVowel = self.lastVowel(param["auxiliary"])
		minorHarmonyLetter = self.MINOR_HARMONY[getLastVowel["letter"]]			
		getLastLetter = self.lastLetter(word)

		if "vowel" in getLastLetter:
			word = self.concat(word, "y")
		elif "discontinious_hard_consonant" in getLastLetter and getLastVowel["vowel_count"] > 1:
			word = self.concat(word[0:len(word) - 1], getLastLetter["soften_consonant"])


		if param.get("negative", False) == False:
			if param["auxiliary"] in ["ver", "koy"]:
				word = self.concat(word, minorHarmonyLetter)
			elif getLastVowel["tone"] == "front":
				word = self.concat(word, "a")
			else:
				word = self.concat(word, "e")

			word = self.concat(word, param["auxiliary"])
		if param.get("negative", False) == True:
			if param["auxiliary"] == "bil":
				if getLastVowel["tone"] == "front":
					word = self.concat(word, "ama")
				else:
					word = self.concat(word, "eme")
			else:
				if param["auxiliary"] in ["ver", "koy"]:
					word = self.concat(word, minorHarmonyLetter)
				elif getLastVowel["tone"] == "front":
					word = self.concat(word, "a")
				else:
					word = self.concat(word, "e")

				word = self.concat(word, param["auxiliary"])

				if getAuxLastVowel["tone"] == "front":
					word = self.concat(word, "a")
				else:
					word = self.concat(word, "e")
		return word 

	# Gereklilik kipi (-meli, -malı)
	def makeMust(self, pword, param = {}):
		word = pword
		getLastVowel = self.lastVowel(word)

		if getLastVowel["tone"] == "front":
			letterA = "a"
			letterI = "ı"
		else:
			letterA = "e"
			letterI = "i"


		if param.get("negative", False) == True:
			word = self.concat(word, "m")
			word = self.concat(word, letterA)

		word = self.concat(word, "m")
		word = self.concat(word, letterA)
		word = self.concat(word, "l")
		word = self.concat(word, letterI)

		if param.get("person", 3) == 3 and param.get("quantity", "singular") == "plural":
			word = self.makePlural(word)

		if param.get("question", False) == True:
			word = self.concat(word, " ")
			word = self.concat(word, "m")
			word = self.concat(word, letterI)

		if param.get("quantity", "singular") == "singular":
			if param.get("person", 3) == 1:
				word = self.concat(word, "y")
				word = self.concat(word, letterI)
				word = self.concat(word, "m")
			elif param.get("person", 3) == 2:
				word = self.concat(word, "s")
				word = self.concat(word, letterI)
				word = self.concat(word, "n")
		elif param.get("quantity", "singular") == "plural":
			if param.get("person", 3) == 1:
				word = self.concat(word, "y")
				word = self.concat(word, letterI)
				word = self.concat(word, "z")
			elif param.get("person", 3) == 2:
				word = self.concat(word, "s")
				word = self.concat(word, letterI)
				word = self.concat(word, "n")
				word = self.concat(word, letterI)
				word = self.concat(word, "z")

		return word

	# Dilek - Şart kipi (-se, -sa)
	def makeWishCondition(self, pword, param = {}):
		word = pword
		getLastVowel = self.lastVowel(word)

		if getLastVowel["tone"] == "front":
			letterA = "a"
			letterI = "ı"
		else:
			letterA = "e"
			letterI = "i"

		if param.get("negative", False) == True:
			word = self.concat(word, "m")
			word = self.concat(word, letterA)

		word = self.concat(word, "s")
		word = self.concat(word, letterA)
	
		if param.get("quantity", "singular") == "singular":
			if param.get("person", 3) == 1:
				word = self.concat(word, "m")
			elif param.get("person", 3) == 2:
				word = self.concat(word, "n")
		else: # Plural 
			if param.get("person", 3) == 1:
				word = self.concat(word, "k")
			elif param.get("person", 3) == 2:
				word = self.concat(word, "n")
				word = self.concat(word, letterI)
				word = self.concat(word, "z")
			elif param.get("person", 3) == 3:
				word = self.makePlural(word)

		if param.get("question", False) == True:
			word = self.concat(word, " ")
			word = self.concat(word, "m")
			word = self.concat(word, letterI)

		return word

	# İstek kipi (geleyim, gelesin, gele, gelelim, gelesiniz, geleler)
	def makeWish(self, pword, param = {}):
		word = pword
		getLastLetter = self.lastLetter(word)
		getLastVowel = self.lastVowel(word)

		if getLastVowel["tone"] == "front":
			letterA = "a"
			letterI = "ı"
		else:
			letterA = "e"
			letterI = "i"

		if param.get("negative", False) == True:
			word = self.concat(word, "m")
			word = self.concat(word, letterA)
			word = self.concat(word, "y")
			word = self.concat(word, letterA)
		else:
			if word == "de":
				word = "di"
			elif word == "ye":
				word = "yi"

			if word == "git":
				word = "gid"

			if "vowel" in getLastLetter:
				word = self.concat(word, "y")
			elif  "discontinious_hard_consonant" in getLastLetter and getLastVowel["vowel_count"] > 1:
				word = self.concat(word[0:len(word) - 1], getLastLetter["soften_consonant"])
			
			word = self.concat(word, letterA)

		if param.get("quantity", "singular") == "singular":
			if param.get("person", 3) == 1:
				word = self.concat(word, "y")
				word = self.concat(word, letterI)
				word = self.concat(word, "m")
			elif param.get("person", 3) == 2:
				word = self.concat(word, "s")
				word = self.concat(word, letterI)
				word = self.concat(word, "n")
		else:
			if param.get("person", 3) == 1:
				word = self.concat(word, "l")
				word = self.concat(word, letterI)
				word = self.concat(word, "m")
			elif param.get("person", 3) == 2:
				word = self.concat(word, "s")
				word = self.concat(word, letterI)
				word = self.concat(word, "n")
				word = self.concat(word, letterI)
				word = self.concat(word, "z")
			elif param.get("person", 3) == 3:
				word = self.makePlural(word)

		if param.get("question", False) == True:
			word = self.concat(word, " ")
			word = self.concat(word, "m")
			word = self.concat(word, letterI)

		return word 

	# Make the verb command
	# Usage: do it, break it, come!
	# As different from English, command optative mood is valid also for 3rd person in Turkish
	#    but never for 1st person.
	# For the second person, there is no suffix
	def makeCommand(self, pword, param = {}):
		word = pword
		getLastVowel = self.lastVowel(word)

		#self.MINOR_HARMONY[self.lastVowel(word)["letter"]]

		if param.get("negative", False) == True:
			word = self.concat(word, "m")
			if getLastVowel["tone"] == "front":
				word = self.concat(word, "a")
			else:
				word = self.concat(word, "e")

		getLastLetter = self.lastLetter(word)
		getLastVowel = self.lastVowel(word)
		minor = self.MINOR_HARMONY[self.lastVowel(word)["letter"]]
		
		if param.get("quantity", "singular") == "singular":
			if param.get("person", 2) == 3:
				word = self.concat(word, "s")
				word = self.concat(word, minor)
				word = self.concat(word, "n")

				if param.get("question", False) == True:
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, minor)
		else: # Plural
			if param.get("person", 2) == 2:
				if word == "de":
					word = "di"
				elif word == "ye":
					word = "yi"

				if "vowel" in getLastLetter:
					word = self.concat(word, "y")
				elif "discontinious_hard_consonant" in getLastLetter and getLastVowel["vowel_count"] > 1 and param.get("negative", False) == False:
					word = self.concat(word[0:len(word) - 1], getLastLetter["soften_consonant"])

				if word == "git":
					word = "gid"

				word = self.concat(word, minor)
				word = self.concat(word, "n")

				if param.get("formal", False) == True:
					word = self.concat(word, minor)
					word = self.concat(word, "z")
			elif param.get("person", 2) == 3:
				word = self.concat(word, "s")
				word = self.concat(word, minor)
				word = self.concat(word, "n")
				word = self.makePlural(word)
				if param.get("question", False) == True:
					word = self.concat(word, " ")
					word = self.concat(word, "m")
					word = self.concat(word, minor)

		return word

	# Past tense
	# -di'li geçmiş zama
	def makePast(self, pword, param = {}):
		word = pword
		getLastVowel = self.lastVowel(word)
		getLastLetter = self.lastLetter(word)
		minor = self.MINOR_HARMONY[self.lastVowel(word)["letter"]]

		if param.get("negative", False) == True:
			word = self.concat(word, "m")
			if getLastVowel["tone"] == "front":
				word = self.concat(word, "a")
			else:
				word = self.concat(word, "e")

		getLastVowel = self.lastVowel(word)
		getLastLetter = self.lastLetter(word)
		minor = self.MINOR_HARMONY[self.lastVowel(word)["letter"]]

		if "hard_consonant" not in getLastLetter or "vowel" in getLastLetter:
			ps = "d"
		else:
			ps = "t"

		if param.get("quantity", "singular") == "singular":
			if param.get("person", 3) == 1:
				word = self.concat(word, ps)
				word = self.concat(word, minor)
				word = self.concat(word, "m")
			elif param.get("person", 3) == 2:
				word = self.concat(word, ps)
				word = self.concat(word, minor)
				word = self.concat(word, "n")
			elif param.get("person", 3) == 3:
				word = self.concat(word, ps)
				word = self.concat(word, minor)
		else: # plural
			if param.get("person", 3) == 1:
				word = self.concat(word, ps)
				word = self.concat(word, minor)
				word = self.concat(word, "k")
			elif param.get("person", 3) == 2:
				word = self.concat(word, ps)
				word = self.concat(word, minor)
				word = self.concat(word, "n")
				word = self.concat(word, minor)
				word = self.concat(word, "z")
			elif param.get("person", 3) == 3:
				word = self.concat(word, ps)
				word = self.concat(word, minor)
				word = self.makePlural(word)

		if param.get("question", False) == True:
			getLastVowel = self.lastVowel(word)
			minor = self.MINOR_HARMONY[self.lastVowel(word)["letter"]]

			word = self.concat(word, " ")	
			word = self.concat(word, "m")
			word = self.concat(word, minor)

		return word

	# Bilinen geçmiş zamanın hikayesi
	# yaptıydım, yaptıydın, yaptıydı, yaptıydık, yaptıydınız, yaptıydılar
	# yaptı mıydım, yaptı mıydın, yaptı mıydı, yaptı mıydık, yaptı mıydınız, yaptılar mıydı
	def makePastPast(self, pword, param = {}):
		word = pword

		if param.get("person", 3) == 3 and param.get("question", False) == True and param.get("quantity", "singular") == "plural":
			word = self.makePast(word, {
				"person": 3,
				"quantity": "singular",
				"negative": param.get("negative", False),
			})
		else:
			word = self.makePast(word, {
				"person": 3,
				"quantity": "singular",
				"negative": param.get("negative", False),
				"question": param.get("question", False)
			})

			word = self.concat(word, "y")

		if param.get("person", 3) == 3 and param.get("question", False) == True and param.get("quantity", "singular") == "plural":
			word = self.makePlural(word)

			word = self.concat(word, " ")
			word = self.concat(word, "m")
			if self.lastVowel(word)["tone"] == "front":
				word = self.concat(word, "ı")
			else:
				word = self.concat(word, "i")
		else:
			word = self.makePast(word, {
				"person": param.get("person", 3),
				"quantity": param.get("quantity", "singular")
			})

		return word

	# Bilinen geçmiş zamanın şartı
	# durduysam, durduysan, durduysa, durduysak, durduysanız, durdularsa
	# dursa mıydım, dursa mıydın, dursa mıydı, dursa mıydık, dursalar mıydı
	def makePastCondition(self, pword, param = {}):
		word = pword

		if param.get("question", False) == False:
			word = self.makePast(word, {
				"person": 3,
				"negative": param.get("negative", False)
			})

			word = self.concat(word, "y")

			word = self.makeWishCondition(word, {
				"person": param.get("person", 3),
				"quantity": param.get("quantity", "singular")
			})
		else:
			word = self.makeWishCondition(word, {
				"person": 3,
				"negative": param.get("negative", False)
			})

			if param.get("person", 3) == 3 and param.get("quantity", "singular") == "plural":
				word = self.makePlural(word)
			
			if self.lastVowel(word)["tone"] == "front":
				letter = "ı"
			else:
				letter = "i"
			
			word = self.concat(word, " ")
			word = self.concat(word, "m")
			word = self.concat(word, letter)
			word = self.concat(word, "y")
			word = self.concat(word, "d")
			word = self.concat(word, letter)

			if param.get("quantity", "singular") == "singular":
				if param.get("person", 3) == 1:
					word = self.concat(word, "m")
				elif param.get("person", 3) == 2:
					word = self.concat(word, "n")
			else:
				if param.get("person", 3) == 1:
					word = self.concat(word, "k")
				elif param.get("person", 3) == 2:
					word = self.concat(word, "n")
					word = self.concat(word, letter)
					word = self.concat(word, "z")
		return word 

	# Öğrenilen geçmiş zamanın hikayesi
	# Yapmışlardı (-miş -di)
	# Example: It is heard by someone that somebody did something in the past
	def makePastPastPerfect(self, pword, param = {}):
		word = pword 

		if param.get("person") == 3 and param.get("quantity") == "plural" and param.get("question", False) == True:
			word = self.makePastPerfect(word, { 
				"negative": param.get("negative", False), 
				"question": param.get("question", False),
				"person": param.get("person", 3),
				"quantity": param.get("quantity", "singular")
			})
		else:
			word = self.makePastPerfect(word, { 
				"negative": param.get("negative", False), 
				"question": param.get("question", False),
			})

		if param.get("question", False) == True:
			word = self.concat(word, "y")

		if param.get("person") == 3 and param.get("quantity") == "plural" and param.get("question", False) == True:
			word = self.makePast(word, { 
				"person": param.get("person", 3)
			})
		else:
			word = self.makePast(word, { 
				"person": param.get("person", 3),
				"quantity": param.get("quantity", "singular"),
			})

		return word

	# Öğrenilen geçmiş zamanın rivayeti
	# Duymuşmuşum Duymuşmuşsun Duymuşmuş Duymuşmuşuz Duymuşmuşunuz Duymuşmuşlar
	# Duymuş mumuymuşum? Duymuş mumuymuşsun? Duymuş mumuymuş? Duymuş mumuymuşuz? Duymuş mumuymuşsunuz Duymuşlar mıymış?
	def makePastPerfectPastPerfect(self, pword, param = {}):
		word = pword

		word = self.makePastPerfect(word, { "negative": param.get("negative", False)} )

		if param.get("question", False) == False:
			word = self.makePastPerfect(word, {
				"person": param.get("person", 3),
				"quantity": param.get("quantity", "singular"),
				"question": param.get("question", False)
			})
		else:
			if param.get("person", 3) == 3 and param.get("quantity", "singular") == "plural":
				word = self.makePlural(word)
				minor = self.MINOR_HARMONY[self.lastVowel(word)["letter"]]
				
				word = self.concat(word, " ")
				word = self.concat(word, "m")
				word = self.concat(word, minor)
				word = self.concat(word, "y")
				word = self.concat(word, "m")
				word = self.concat(word, minor)
				word = self.concat(word, "ş")
			else:
				minor = self.MINOR_HARMONY[self.lastVowel(word)["letter"]]
				word = self.concat(word, " ")
				word = self.concat(word, "m")
				word = self.concat(word, minor)
				word = self.concat(word, "y")
				word = self.makePastPerfect(word, {
					"person": param.get("person", 3),
					"quantity": param.get("quantity", "singular")
				})
		return word

	# Gelecek zamanın rivayeti
	# Yapacaklardı (-acak -mış)
	# Example: It is heard by someone that somebody will do something in the past
	def makePastPerfectFuture(self, pword, param = {}):
		word = pword 

		if param.get("person") == 3 and param.get("quantity") == "plural" and param.get("question", False) == True:
			word = self.makeFuture(word, { 
				"negative": param.get("negative", False), 
				"question": param.get("question", False),
				"person": param.get("person", 3),
				"quantity": param.get("quantity", "singular")
			})
		else:
			word = self.makeFuture(word, { 
				"negative": param.get("negative", False), 
				"question": param.get("question", False),
			})


		if param.get("person") == 3 and param.get("quantity") == "plural" and param.get("question", False) == True:
			word = self.concat(word, "m")
			word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
			word = self.concat(word, "y")
			word = self.makePastPerfect(word, { 
				"person": param.get("person", 3)
			})
		else:
			if param.get("question", False) == True:
				word = self.concat(word, "y")

			word = self.makePastPerfect(word, { 
				"person": param.get("person", 3),
				"quantity": param.get("quantity", "singular"),
			})

		return word

	# Gelecek zamanın hikayesi
	# Yapacaklardı (-acak -tı)
	# Example: Somebody will do something in the past
	def makePastFuture(self, pword, param = {}):
		word = pword 

		if param.get("person") == 3 and param.get("quantity") == "plural" and param.get("question", False) == True:
			word = self.makeFuture(word, { 
				"negative": param.get("negative", False), 
				"question": param.get("question", False),
				"person": param.get("person", 3),
				"quantity": param.get("quantity", "singular")
			})
		else:
			word = self.makeFuture(word, { 
				"negative": param.get("negative", False), 
				"question": param.get("question", False),
			})


		if param.get("person") == 3 and param.get("quantity") == "plural" and param.get("question", False) == True:
			word = self.concat(word, "m")
			word = self.concat(word, self.MINOR_HARMONY[self.lastVowel(word)["letter"]])
			word = self.concat(word, "y")
			word = self.makePast(word, { 
				"person": param.get("person", 3)
			})
		else:
			if param.get("question", False) == True:
				word = self.concat(word, "y")

			word = self.makePast(word, { 
				"person": param.get("person", 3),
				"quantity": param.get("quantity", "singular"),
			})

		return word

import sqlite3
conn = sqlite3.connect('database.db')
conn.execute('''delete from verbs''')

def exec(cmd, tense, verb, params = {}):
	gen = eval("%s(%s, %s)" % (cmd, verb, params))

	if params.get("quantity", "singular") == "singular":
		plurality = "0"
	else:
		plurality = "1"

	if params.get("negative", False) == False:
		negative = "0"
	else:
		negative = "1"

	if params.get("question", False) == False:
		question = "0"
	else:
		question = "1"

	person = params.get("person", 3) 

	sql  = "insert into verbs(generated, tense, question, person, plurality, negative, source_verb) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (gen, tense, question, person, plurality, negative, sample_verb)

	conn.execute(sql)

verbs = [
"aç"
, "ağla"
, "ak"
, "al"
, "anla"
, "anlat"
, "ara"
, "art"
, "aş"
, "at"
, "ayır"
, "ayrıl"
, "azal"
, "bağır"
, "bağla"
, "bak"
, "bas"
, "başla"
, "bekle"
, "belirle"
, "belirt"
, "benze"
, "bırak"
, "bil"
, "bin"
, "bitir"
, "bit"
, "bozul"
, "bul"
, "büyü"
, "çalış"
, "çal"
, "çekil"
, "çek"
, "çevir"
, "çıkar"
, "çık"
, "çiz"
, "dayan"
, "değerlendir"
, "değiş"
, "değiştir"
, "de"
, "devam et"
, "dikkat et"
, "dile"
, "dinle"
, "doğ"
, "dolaş"
, "doldur"
, "dön"
, "dönüş"
, "dur"
, "duy"
, "düş"
, "düşün"
, "düzenle"
, "ekle"
, "etkile"
, "et"
, "evlen"
, "fark et"
, "geçir"
, "geç"
, "geliş"
, "geliştir"
, "gel"
, "gerçekleş"
, "gerek"
, "getir"
, "gir"
, "git"
, "giy"
, "gönder"
, "gör"
, "görün"
, "görüş"
, "göster"
, "götür"
, "gül"
, "hareket et"
, "hatırla"
, "hazırla"
, "hisset"
, "iç"
, "ifade et"
, "ilerle"
, "ilgilen"
, "inan"
, "incele"
, "in"
, "iste"
, "izle"
, "kabul et"
, "kaç"
, "kaldır"
, "kalk"
, "kal"
, "kapat"
, "karış"
, "karıştır"
, "karşıla"
, "karşılaş"
, "katıl"
, "kaybet"
, "kazan"
, "kes"
, "kıl"
, "konuş"
, "kork"
, "kor"
, "koş"
, "koy"
, "kullan"
, "kur"
, "kurtar"
, "kurtul"
, "ok"
, "ol"
, "oluş"
, "otur"
, "oyna"
, "öde"
, "öğren"
, "öldür"
, "öl"
, "paylaş"
, "sağla"
, "sahip ol"
, "san"
, "satın al"
, "sat"
, "say"
, "seç"
, "sev"
, "seyret"
, "sok"
, "sor"
, "söyle"
, "söylen"
, "söz et"
, "sun"
, "sürdür"
, "sür"
, "tanı"
, "taşı"
, "tercih et"
, "topla"
, "toplan"
, "tut"
, "uğraş"
, "ulaş"
, "unut"
, "uygula"
, "uy"
, "uy"
, "uzan"
, "uzat"
, "üret"
, "var"
, "ver"
, "vur"
, "yakala"
, "yaklaş"
, "yak"
, "yan"
, "yap"
, "yararlan"
, "yarat"
, "yardımcı ol"
, "yaşa"
, "yat"
, "yayıl"
, "yayımlan"
, "yazıl"
, "yaz"
, "ye"
, "yüksel"
, "yürü"
]

tr = turkish()

for vrb in verbs:
	sample_verb = vrb
	print (vrb)
	tense = "Mastar"
	exec ("tr.makeInfinitive", tense, "sample_verb")
	exec ("tr.makeInfinitive", tense, "sample_verb", { "negative": True})

	#tense = "Birleşik fiil"
	#exec ("tr.unifyVerbs", tense, "sample_verb", {"auxiliary": "bil", "negative": False})
	#exec ("tr.unifyVerbs", tense, "sample_verb", {"auxiliary": "bil", "negative": True})
		
	tense = "Emir kipi"
	exec ("tr.makeCommand", tense, "sample_verb", { "person": 2 })
	exec ("tr.makeCommand", tense, "sample_verb", { "person": 3 })
	exec ("tr.makeCommand", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makeCommand", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makeCommand", tense, "sample_verb", { "person": 2, "quantity": "plural", "formal": True })
	exec ("tr.makeCommand", tense, "sample_verb", { "person": 3, "quantity": "plural" })
	exec ("tr.makeCommand", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makeCommand", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makeCommand", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makeCommand", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makeCommand", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makeCommand", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural", "formal": True })
	exec ("tr.makeCommand", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })
	exec ("tr.makeCommand", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Şimdiki zaman"
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "person": 1 }) 
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePresentContinuous", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePresentContinuous", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Şimdiki zaman 2"
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "person": 1 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePresentContinuous2", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Gelecek zaman"
	exec ("tr.makeFuture", tense, "sample_verb", { "person": 1 })
	exec ("tr.makeFuture", tense, "sample_verb", { "person": 2 })
	exec ("tr.makeFuture", tense, "sample_verb", { "person": 3 })
	exec ("tr.makeFuture", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makeFuture", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makeFuture", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makeFuture", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makeFuture", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makeFuture", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makeFuture", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeFuture", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeFuture", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 1})
	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 2})
	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 3})
	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Geniş zaman"
	exec ("tr.makePresentSimple", tense, "sample_verb", { "person": 1 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePresentSimple", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePresentSimple", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })


	tense = "Geçmiş zaman"
	exec ("tr.makePast", tense, "sample_verb", { "person": 1 })
	exec ("tr.makePast", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePast", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePast", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePast", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePast", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePast", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePast", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePast", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePast", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePast", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePast", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePast", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Gereklilik kipi"
	exec ("tr.makeMust", tense, "sample_verb", { "person": 1 })
	exec ("tr.makeMust", tense, "sample_verb", { "person": 2 })
	exec ("tr.makeMust", tense, "sample_verb", { "person": 3 })
	exec ("tr.makeMust", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makeMust", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makeMust", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makeMust", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makeMust", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makeMust", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makeMust", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeMust", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeMust", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeMust", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Dilek-Şart kipi"
	exec ("tr.makeWishCondition", tense, "sample_verb", { "person": 1 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "person": 2 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "person": 3 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makeWishCondition", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeWishCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "İstek kipi"
	exec ("tr.makeWish", tense, "sample_verb", { "person": 1 })
	exec ("tr.makeWish", tense, "sample_verb", { "person": 2 })
	exec ("tr.makeWish", tense, "sample_verb", { "person": 3 })
	exec ("tr.makeWish", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makeWish", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makeWish", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makeWish", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makeWish", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makeWish", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makeWish", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeWish", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeWish", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makeWish", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Öğrenilen geçmiş zaman"
	exec ("tr.makePastPerfect", tense, "sample_verb", { "person": 1 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePastPerfect", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Öğrenilen geçmiş zamanın hikayesi"
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "person": 1 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Öğrenilen geçmiş zamanın rivayeti"
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "person": 1 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfectPastPerfect", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Gelecek zamanın rivayeti"
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "person": 1 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPerfectFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Gelecek zamanın hikayesi"
	exec ("tr.makePastFuture", tense, "sample_verb", { "person": 1 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePastFuture", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePastFuture", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePastFuture", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastFuture", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastFuture", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastFuture", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	tense = "Geçmiş zamanın hikayesi"
	exec ("tr.makePastPast", tense, "sample_verb", { "person": 1 })
	exec ("tr.makePastPast", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePastPast", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePastPast", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePastPast", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePastPast", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePastPast", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePastPast", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePastPast", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePastPast", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPast", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPast", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastPast", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })


	tense = "Bilinen geçmiş zamanın şartı"
	exec ("tr.makePastCondition", tense, "sample_verb", { "person": 1 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "person": 2 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "person": 3 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "person": 1, "quantity": "plural" })
	exec ("tr.makePastCondition", tense, "sample_verb", { "person": 2, "quantity": "plural" })
	exec ("tr.makePastCondition", tense, "sample_verb", { "person": 3, "quantity": "plural" })

	exec ("tr.makePastCondition", tense, "sample_verb", { "question": True, "person": 1 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "question": True, "person": 2 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "question": True, "person": 3 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastCondition", tense, "sample_verb", { "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastCondition", tense, "sample_verb", { "question": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "person": 1 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "person": 2 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "person": 3 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "person": 3, "quantity": "plural" })

	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 1 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 2 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 3 })
	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 1, "quantity": "plural" })
	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 2, "quantity": "plural" })
	exec ("tr.makePastCondition", tense, "sample_verb", { "negative": True, "question": True, "person": 3, "quantity": "plural" })

	conn.commit()

conn.close()

print (tr.makeGenitive("araba"))
print (tr.makeDative("araba"))
print (tr.makeAblative("araba"))
print (tr.makeAccusative("araba"))

print (tr.makeGenitive("Cem", { "proper_noun": True} ))
print (tr.makeDative("Cem", { "proper_noun": True} ))
print (tr.makeAblative("Cem", { "proper_noun": True} ))
print (tr.makeAccusative("Cem", { "proper_noun": True} ))


print (tr.possessiveAffix("çanta", {"person": 1, "quantity": "singular"}))
print (tr.possessiveAffix("çanta", {"person": 2, "quantity": "singular"}))
print (tr.possessiveAffix("çanta", {"person": 3, "quantity": "singular"}))

print (tr.possessiveAffix("çanta", {"person": 1, "quantity": "plural"}))
print (tr.possessiveAffix("çanta", {"person": 2, "quantity": "plural"}))
print (tr.possessiveAffix("çanta", {"person": 3, "quantity": "plural"}))

