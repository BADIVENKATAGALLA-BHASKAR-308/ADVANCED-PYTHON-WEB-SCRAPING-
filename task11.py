# # task11

# import pprint
# import json
# json_geners_file=open("imdb_movies.json","r")
# geners_file= json.load(json_geners_file)


# list_of_geners = []

# for i in geners_file: 
# 	for keys,values in i.items():
# 		if keys == "Genres:":
# 			for gener_name in values:
# 				if gener_name not in list_of_geners:
# 					list_of_geners.append(gener_name)
# # pprint.pprint(list_of_dirctors)
# dict_of_geners = {}
# for each_gener in list_of_geners:
# 	count_geners = 0
# 	for individual_gener in geners_file:
# 		for keys,values in individual_gener.items():
# 			if keys == "Genres:":
# 				for i in values: 
# 					if i == each_gener:
# 						count_geners+=1


# 	dict_of_geners[each_gener] = count_geners

# pprint.pprint(dict_of_geners)