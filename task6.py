# #task6

# def analyse_movies_language(movies_detail_dictionery):

# 	import pprint
# 	import json
# 	json_language_file=open("imdb_movies.json","r")
# 	language_file= json.load(json_language_file)


# 	list_of_languages = []
# 	for i in language_file: 
# 		for keys,values in i.items():
# 			if keys == "Language:":
# 				for k in values:
# 					if k not in list_of_languages:
# 						list_of_languages.append(k)

# 	dict_of_languages = {}
# 	for language in list_of_languages:
# 		count_of_language = 0
# 		for l in language_file:
# 			for keys,values in l.items():
# 				if keys == "Language:":
# 					for each_value in values:
# 						if each_value == language:
# 							count_of_language+=1
# 		dict_of_languages[language] = count_of_language

# 	pprint.pprint(dict_of_languages)

# #calling of function

# analyse_movies_language(dict_of_languages)
