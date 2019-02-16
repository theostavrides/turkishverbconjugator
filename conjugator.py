#!/usr/bin/env python
# -*- coding: UTF-8 -*-

verbin = raw_input("Enter verb (e.g. gelmek): ")
verb = verbin.decode('utf-8')
tensein = raw_input("Enter tense (present, past, presentcont, pastcont, future): ")
tense = tensein.decode('utf-8')
formin = raw_input("Enter form (+,-,?,-?): ")
form = formin.decode('utf-8')



						##### DICTIONARIES AND LISTS #####
						
						# Vowel Harmony Rules

vowels = ["a","e","i",u"ı","o",u"ö",u"u",u"ü"]

hardconsonants = ["p", u"ç", "t", "k", "s", u"ş", "f", "h"]

	
vowel4harmony = {"a": u"ı","e": "i","i": "i",u"ı": u"ı","o": "u", u"ö": u"ü", 
	"u": "u", u"ü": u"ü"}

vowel2harmony = {"a": u"a","e": "e","i": "e",u"ı": u"a","o": "a", u"ö": u"e", 
	"u": "a", u"ü": u"e"}
	
						# Irregular Verbs

presentexceptions = ["almak","bilmek","bulmak","durmak","gelmek",u"görmek","kalmak",
					 "olmak",u"ölmek","sanmak", "vermek", "varmak","vurmak"]
					 
futureexceptions = {"demek": "di","yemek": "yi"}
					
mutants = {"gitmek": "gid", "etmek": "ed", "tatmak": "tad", 
		   "ditmek": "did", u"gütmek": u"güd"}
		   
						# Aorist / Present Simple (Geniş Zaman)
						
present_endings = {"i":["im","sin","","iz","siniz","ler"],
				   "u":["um","sun","","uz","sunuz","lar"],
				  u"ı":[u"ım",u"sın","",u"ız",u"sınız","lar"],
				  u"ü":[u"üm",u"sün","",u"üz",u"sünüz","ler"]}
				  
present_negendings = {"a":["mam",u"mazsın","maz",u"mayız",u"mazsınız","mazlar"],
					  "e":["mem","mezsin","mez","meyiz","mezsiniz","mezler"]}
					  
present_qendings = {"i":["miyim?", "misin?", "mi?", "miyiz?", "misiniz?", "ler mi?"],
					"u":["muyum?", "musun?", "mu?", "muyuz?", "musunuz?", u"lar mı?"],
				   u"ı":[u"mıyım?", u"mısın?", u"mı?", u"mıyız?", u"mısınız?", u"lar mı?"],
				   u"ü":[u"müyüm?", u"müsün?", u"mü?", u"müyüz?", u"müsünüz?", "ler mi?"]}
				   
						# Present Continuous (Şimdiki Zaman) 

presentcont_endings = ["yorum", "yorsun", "yor", "yoruz", "yorsunuz", "yorlar"]

presentcont_questionendings = ["muyum", "musun", "mu", "muyuz", "musunuz"]

						# Past Continuous

pastcont_endings = ["yordum", "yordun", "yordu", "yorduk", "yordunuz", "yordular", u"yorlardı"]

pastcont_qendings = ["muydum", "muydun", "muydu", "muyduk", "muydunuz", u"lar mıydı", u"dular mı"]

						# Simple Past (Geçmiş Zaman)
						
past_endings = {"i":["im","in","i","ik","iniz","iler"],
				"u":["um","un","u","uk","unuz","ular"],
			   u"ı":[u"ım",u"ın",u"ı",u"ık",u"ınız", u"ılar"],
			   u"ü":[u"üm",u"ün",u"ü",u"ük",u"ünüz", u"üler"]}
			   

						# Future (Gelecek Zaman)
						
future_endings = {"a":[u"acağım", u"acaksın", "acak", u"acağız", u"acaksınız", "acaklar"],
				  "e":[u"eceğim", "eceksin", "ecek", u"eceğiz", "eceksiniz", "ecekler"]}


				      	##### TOOLS #####

def find_verb_stem(verb):                 
	if (tense == "presentcont" or tense == "pastcont") and (form == "+" or form == "?"):    
		if verb in mutants:
			return mutants[verb]
		elif verb[-4] not in vowels:	      
			return verb[:-3]
		else:
			return verb[:-4]                      
			
	elif (tense == "present") and (form == "+" or form == "?"):
		if verb in mutants:	
			return mutants[verb]
		else:
			return verb[:-3]
			
	elif (tense == "future") and (form == "+" or form == "?"):
		if verb in mutants:	
			return mutants[verb]
		elif verb in futureexceptions:
			return futureexceptions[verb] 
		else:
			return verb[:-3]
		
	else:
		return verb[:-3]
		

def vowel_counter(item):
	c = 0
	for x in vowels:
		c = c + item.count(x)
	return c
			
def find_last_vowel_in_stem(verb):              
	for x in range(-1,-6,-1):
		if find_verb_stem(verb)[x] in vowels:
			return find_verb_stem(verb)[x] 
				
def find_last_vowel_in_item(item):
	for x in range(-1,-6,-1):
		if item[x] in vowels:
			return item[x]
				
def find_buffer_vowel(verb):
	if tense == "future":
		if verb[-4] in vowels:
			return "y"
		else:
			return ""
	
	if tense == "presentcont" or tense =="pastcont":
		if len(find_verb_stem(verb)) == 1:
			return vowel4harmony[verb[1]]
		else:
			return vowel4harmony[find_last_vowel_in_stem(verb)]      
			
def past_buffer(verb):
	if verb[-4] in hardconsonants:
		return "t"
	else:
		return "d"

def find_present_ending(verb):
	stemandr = find_verb_stem(verb) + present_rform(verb)
	return find_last_vowel_in_item(stemandr)
	
def present_rform(verb):
	if verb[-4] in vowels:
		return "r"
	else:
		if verb in presentexceptions:
			return vowel4harmony[find_last_vowel_in_stem(verb)] + "r"
		elif vowel_counter(find_verb_stem(verb)) == 1:
			return vowel2harmony[find_last_vowel_in_stem(verb)] + "r"
		elif vowel_counter(find_verb_stem(verb)) > 1:
			return vowel4harmony[find_last_vowel_in_stem(verb)] + "r"
	

	
						##### CONJUGATOR #####

def conjugate():
	if tense == "presentcont" and form == "+":                # still need to do exceptions
		for tensenumber in range(0,6):
			print find_verb_stem(verb) + find_buffer_vowel(verb) + presentcont_endings[tensenumber]
	elif tense == "presentcont" and form == "-":   
		for tensenumber in range(0,6):
			print verb[:-2] + find_buffer_vowel(verb) + presentcont_endings[tensenumber]
	elif tense == "presentcont" and form == "?":   
		for tensenumber in range(0,5):
			print find_verb_stem(verb) + find_buffer_vowel(verb) + "yor " +  presentcont_questionendings[tensenumber] + "?"
		print find_verb_stem(verb) + find_buffer_vowel(verb) + u"yorlar mı?"
	elif tense == "presentcont" and form == "-?":
		for tensenumber in range(0,5):
			print verb[:-2] + find_buffer_vowel(verb) + "yor " + presentcont_questionendings[tensenumber] + "?"
		print verb[:-2] + find_buffer_vowel(verb) + u"yorlar mı?" 
		
		
	elif tense == "pastcont" and form == "+":
		for tensenumber in range(0,6):
			print find_verb_stem(verb) + find_buffer_vowel(verb) + pastcont_endings[tensenumber]		
		print "(" + find_verb_stem(verb) + find_buffer_vowel(verb) + pastcont_endings[6] + ")"
	elif tense == "pastcont" and form == "-":
		for tensenumber in range(0,6):
			print verb[:-2] + find_buffer_vowel(verb) + pastcont_endings[tensenumber]
		print "(" + verb[:-2] + find_buffer_vowel(verb) + pastcont_endings[6] + ")"
	elif tense == "pastcont" and form == "?":
		for tensenumber in range(0,5):
			print find_verb_stem(verb) + find_buffer_vowel(verb) + "yor " + pastcont_qendings[tensenumber] + "?"
		print find_verb_stem(verb) + find_buffer_vowel(verb) + "yor" + pastcont_qendings[5] + "?"
		print "(" + find_verb_stem(verb) + find_buffer_vowel(verb) + "yor" + pastcont_qendings[6] + "?" + ")"
	elif tense == "pastcont" and form == "-?":
		for tensenumber in range(0,5):
			print verb[:-2] + find_buffer_vowel(verb) + "yor " + pastcont_qendings[tensenumber] + "?"
		print verb[:-2] + find_buffer_vowel(verb) + "yor" + pastcont_qendings[5] + "?"
		print "(" + verb[:-2] + find_buffer_vowel(verb) + "yor" + pastcont_qendings[6] + "?" + ")"
		
		
	elif tense == "present" and form == "+":   
		for tensenumber in range(0,6):
			print find_verb_stem(verb) + present_rform(verb) + present_endings[vowel4harmony[find_present_ending(verb)]][tensenumber]
	elif tense == "present" and form == "-":
		for tensenumber in range(0,6):
			print find_verb_stem(verb) + present_negendings[vowel2harmony[find_last_vowel_in_stem(verb)]][tensenumber]
	elif tense == "present" and form == "?":    
		for tensenumber in range(0,5):
			print find_verb_stem(verb) + present_rform(verb) + " " + present_qendings[vowel4harmony[find_present_ending(verb)]][tensenumber]
		print find_verb_stem(verb) + present_rform(verb) + present_qendings[vowel4harmony[find_present_ending(verb)]][5]
	elif tense == "present" and form == "-?":    
		for tensenumber in range(0,5):
			print find_verb_stem(verb) + present_negendings[vowel2harmony[find_last_vowel_in_stem(verb)]][2] + " " + present_qendings[vowel4harmony[vowel2harmony[find_last_vowel_in_stem(verb)]]][tensenumber]
		print find_verb_stem(verb) + present_negendings[vowel2harmony[find_last_vowel_in_stem(verb)]][2] + present_qendings[vowel4harmony[find_last_vowel_in_stem(verb)]][5]
		
		
	elif tense == "future" and form == "+":
		for tensenumber in range(0,6):
			print find_verb_stem(verb) + find_buffer_vowel(verb) + future_endings[vowel2harmony[find_last_vowel_in_stem(verb)]][tensenumber]
	elif tense == "future" and form == "-":
		for tensenumber in range(0,6):
			print verb[:-1] + "y" + future_endings[vowel2harmony[verb[-2]]][tensenumber]
	elif tense == "future" and form == "?":
		for tensenumber in range(0,5):
			print find_verb_stem(verb) + find_buffer_vowel(verb) + future_endings[vowel2harmony[find_last_vowel_in_stem(verb)]][2] + " " + present_qendings[vowel4harmony[verb[-2]]][tensenumber]
		print find_verb_stem(verb) + find_buffer_vowel(verb) + future_endings[vowel2harmony[find_last_vowel_in_stem(verb)]][5] + " " + present_qendings[vowel4harmony[verb[-2]]][2]
	elif tense == "future" and form == "-?":
		for tensenumber in range(0,5):
			print verb[:-1] + "y" + future_endings[vowel2harmony[verb[-2]]][2] + " " + present_qendings[vowel4harmony[verb[-2]]][tensenumber]
		print verb[:-1] + "y" + future_endings[vowel2harmony[verb[-2]]][2] + present_qendings[vowel4harmony[verb[-2]]][5]
		
		
	elif tense == "past" and form == "+":
		for tensenumber in range(0,6):
			print verb[:-3] + past_buffer(verb) + past_endings[vowel4harmony[find_last_vowel_in_stem(verb)]][tensenumber]
	elif tense == "past" and form == "-":
		for tensenumber in range(0,6):
			print verb[:-1] + "d" + past_endings[vowel4harmony[verb[-2]]][tensenumber]
	elif tense == "past" and form == "?":
		for tensenumber in range(0,5):
			print verb[:-3] + past_buffer(verb) + past_endings[vowel4harmony[find_last_vowel_in_stem(verb)]][tensenumber] + " m" + vowel4harmony[find_last_vowel_in_stem(verb)] + "?"
		print verb[:-3] + past_buffer(verb) + past_endings[vowel4harmony[find_last_vowel_in_stem(verb)]][5] + " m" + vowel4harmony[verb[-2]] + "?"
																																	
conjugate()   