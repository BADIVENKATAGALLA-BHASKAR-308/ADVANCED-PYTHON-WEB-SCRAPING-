
## task7
# import pprint
# import json
# json_directors_file=open("imdb_movies.json","r")
# director_file= json.load(json_directors_file)


# list_of_dirctors = []

# for i in director_file: 
# 	for keys,values in i.items():
# 		if keys == "director":
# 			for director_name in values:
# 				if director_name not in list_of_dirctors:
# 					list_of_dirctors.append(director_name)
# # pprint.pprint(list_of_dirctors)
# dict_of_directors = {}
# for each_director in list_of_dirctors:
# 	count_director = 0
# 	for individual_dict in director_file:
# 		for keys,values in individual_dict.items():
# 			if keys == "director":
# 				for i in values: 
# 					if i == each_director:
# 						count_director+=1

# 	dict_of_directors[each_director] = count_director

# pprint.pprint(dict_of_directors)