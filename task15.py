# #task15
# import json
# import pprint
# file = open("imdb_movies_with_cast.json","r+")
# content = json.load(file)
# # pprint.pprint(content)
# total_cast = []
# for i in content:
# 	for j in i["cast"]:
# 		for k,l in j.items():
# 			if k == "name":
# 				total_cast.append(l)
# uniq_terms = set(total_cast)

# dict_fot_count_of_actor = {}

# for i in uniq_terms:
# 	count_of_each_actor = 0
# 	for j in total_cast:
# 		if i == j:
# 			count_of_each_actor+=1

# 	dict_fot_count_of_actor[i] = count_of_each_actor

# # pprint.pprint(dict_fot_count_of_actor)

# file = open("task_15.json","w+")
# json.dump(dict_fot_count_of_actor,file,indent=2)