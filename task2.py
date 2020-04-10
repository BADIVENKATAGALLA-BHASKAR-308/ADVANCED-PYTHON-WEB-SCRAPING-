webscraping:- task2


def group_by_year():
	import pprint
	import json
	years_list = []
	unique_years_list = []
	with open("imdb.json","r") as list_of_data:
		data = json.load(list_of_data)
		for dict_value in data:
			for i,j in dict_value.items():
				if i=="year":
					years_list.append(j)


		for unique_years in years_list:
			if unique_years not in unique_years_list:
				unique_years_list.append(unique_years)

		unique_years_list.sort()

	#seperation of dictoineries

		total_dictionery = {}

		for year_ in unique_years_list:
			list_of_specific_year = []

			for dict_of_data in data:
				for dict_value in dict_of_data.values():
					if year_ == dict_value:
						list_of_specific_year.append(dict_of_data)
				
				total_dictionery[year_] = list_of_specific_year

		pprint.pprint(total_dictionery)

group_by_year()


