# import time
# import requests
# from bs4 import BeautifulSoup
# from random import randint
# import json
# import pprint

# mega_list1 = []
# mega_list2 = []

# links_data_list = open("imdb.json","r")
# links_data = json.load(links_data_list)
# list_of_combination = []
# for each_dict in links_data:
# 	dict_for_cast = {}
# 	for key,link in each_dict.items():
# 		if key == "url":
# 			response = requests.get(link)
# 			soup = BeautifulSoup(response.text,"html.parser")
# # finding the cast and crew and ids:-
# 			cast_div = soup.find("table",class_="cast_list")
# 			trs = cast_div.find_all("tr")
# 			count_of_tr = 0
# 			ids_list = []
# 			for tr in trs:
# 				count_of_tr+=1
# 				if count_of_tr == 1:
# 					continue
# 				else:
# 					a_tags_list = tr.find_all("td")
# 					count_td = 0
# 					for i in a_tags_list:
# 						count_td+=1
# 						if count_td == 2:
# 							a = i.find("a")["href"][6:15]
# 							# print(a)
# 							ids_list.append(a)
# 			# print(ids_list)
# 			mega_list2.append(ids_list)

# #finding the cst name only:-
# 			list_of_cast_names = []
# 			count=0
# 			for tr in trs:
# 				count += 1
# 				if count ==1:
# 					continue
# 				else:
# 					tds = tr.find_all("td")
# 					count_a = 0
# 					for i in tds:
# 						count_a +=1
# 						if count_a ==2:
# 							list_of_cast_names.append(i.text.strip())
# 						a_tags = i.find_all("a")
# 						print(a_tags)
# 						print(i)
# 			# print(list_of_cast_names)
# 			mega_list1.append(list_of_cast_names)	

###for total list of ids:-
# #list_of_ids = open("ids_list.json","w+")
# #json.dump(mega_list2,list_of_ids,indent=2)

###for total list of cast of all movies:-
# #list_of_ids = open("ids_list.json","w+")
## json.dump(mega_list2,list_of_ids,indent=2)


# import time
# import requests
# from bs4 import BeautifulSoup
# from random import randint
# import json
# import pprint

# list_of_ids = open("ids_list.json","r+")
# ids_list = json.load(list_of_ids)

# list_of_cast = open("cast_list.json","r+")
# cast_list = json.load(list_of_cast)

# list_of_movie_name = open("imdb.json","r+")
# movie_names_list = json.load(list_of_movie_name)

# list_of_all = []

# for i in range(len(cast_list)):
# 	list_of_each_movie = []
	
# 	for j in range(len(ids_list[i])):
# 		dict_for_actor = {}
# 		dict_for_actor["imdb_id"] = ids_list[i][j]
# 		dict_for_actor["name"] = cast_list[i][j]
# 		# print(dict_for_actor)
# 	# print()
# 		list_of_each_movie.append(dict_for_actor)
# 	list_of_all.append(list_of_each_movie)

	
# dict_of_all = {}
# for i in range(len(movie_names_list)):
# 	for keys,values in movie_names_list[i].items():
# 		if keys == "name":
# 			dict_of_all[values] = list_of_all[i]
##pprint.pprint(dict_of_all)

# file_for_task12 = open("task12.json","w+")
# json.dump(dict_of_all,file_for_task12,indent=2)


