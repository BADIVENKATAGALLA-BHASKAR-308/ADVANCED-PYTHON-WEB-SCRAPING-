
# import itertools
# import json
# import pprint
# # print all the json data
# data_of_movies = open("imdb_movies.json","r")
# full_data = json.load(data_of_movies)
# directors_list = []
# dict_of_language = {}

# #finding the list of directors non repeated
# for each_dict in full_data:
#     for key,value in each_dict.items():
#         if key == 'director':
#             for individual_name in value:
#                 if individual_name not in directors_list:
#                     directors_list.append(individual_name)
# #finding the dictionery for director name and language list
# dict_of_director = {}
# total_list = []
# for single_director in directors_list:
# 	list_dict = []
# 	for each_dict in full_data:
# 		for i in each_dict['director']:
# 			if single_director in i:
# 				list_dict.append(each_dict["Language:"])
# 	dict_of_director[single_director] = list(itertools.chain(*list_dict))
# # finding the output
# main_dict = {}
# for director_name,language_list in dict_of_director.items():
# 	set_ = set(language_list)
# 	dict_ = {}	
# 	for i in set_:
# 		count_of_lang = 0
# 		for j in language_list:
# 			if i == j:
# 				count_of_lang+=1
# 		dict_[i] = count_of_lang 
# 	main_dict[director_name] = dict_
# pprint.pprint(main_dict)