def function():
	import time
	import requests
	from bs4 import BeautifulSoup
	from random import randint
	import json
	import pprint
	# full_data = open("imdb_movies.json","r")
	# task_4 = json.load(full_data)
	# cast_dict = {}
	# for i in task_4:
	# 	i["cast"] = cast_dict
	mega_list = []
	links_data_list = open("imdb.json","r")
	links_data = json.load(links_data_list)
	for each_dict in links_data:
		list_of_combination = []
		dict_for_cast = {}
		for key,link in each_dict.items():
			if key == "url":
				response = requests.get(link)
				soup = BeautifulSoup(response.text,"html.parser")
				# finding the cast and crew and ids:-
				cast_div = soup.find("table",class_="cast_list")
				trs = cast_div.find_all("tr")
				count_of_first_tr = 0
				list_of_cast_names = []
				list_of_cast_id = []
				list_ =  []
				for tr in trs:
					count_of_first_tr+=1
					if count_of_first_tr == 1:
						continue
					else:
						a_tags =tr.find_all("a")
						count = 0
						for a_tag in a_tags:
							count+=1
							if count == 2:
								list_of_cast_names.append(a_tag.text.strip())

							a_hrefs = tr.find("a")["href"]
							list_of_cast_id.append(a_hrefs)


				dict_of_id_and_cast_name = {}
				for counter in range(len(list_of_cast_names)):
					dict_of_id_and_cast_name["id_name"] = list_of_cast_id[counter]
					dict_of_id_and_cast_name["actor_name"] = list_of_cast_names[counter]
					# print(dict_of_id_and_cast_name)
					list_of_combination.append(dict_of_id_and_cast_name)
				# mega_list.append(list_of_combination)
	return mega_list
	# print()	

function()