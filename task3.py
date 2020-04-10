#task3

#define a function for task3

# def group_by_decade():

# 	import pprint
# 	import json
# 	years_list = []
# 	unique_years_list = []
# 	with open("imdb.json","r") as list_of_data:
# 		data = json.load(list_of_data)
# 		for dict_value in data:
# 			for i,j in dict_value.items():
# 				if i=="year":
# 					years_list.append(j)

# 	#finding of unique years
# 		for unique_years in years_list:
# 			if unique_years not in unique_years_list:
# 				unique_years_list.append(unique_years)

# 	# finding the decades list
# 		dacade_list = []
# 		for i in unique_years_list:
# 			a = i%10
# 			b=i-a
# 			dacade_list.append(b)
# 			dacade_list.sort()
		
# 	# finding the unique decade years
# 		unique_list = []
# 		for i in dacade_list:
# 			if i not in unique_list:
# 				unique_list.append(i)
# 		# print(unique_list)
# 	#finding the data of the decade movies in seperate in list
		
# 		dict_of_individual_decade_movies ={}
		
# 		for decade_year in unique_list:
# 			list_individual_decade_movies = []
# 			for movies_dict in data:
# 				for year_of_individual_movies in movies_dict.values():
# 					if type(year_of_individual_movies) == int:
# 						if decade_year <= year_of_individual_movies <= decade_year+9:
# 							list_individual_decade_movies.append(movies_dict)
# 			dict_of_individual_decade_movies[decade_year] = list_individual_decade_movies
						
# 		pprint.pprint(dict_of_individual_decade_movies)



# #calling of the function
# group_by_decade()
