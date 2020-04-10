# # #task1_webscraping:-

# import requests
# from bs4 import BeautifulSoup
# import pprint,json
# list_of_data = []
# def scrape_top_list():
# 	request_of_imdb=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
# 	soup=BeautifulSoup(request_of_imdb.text,"html.parser")
# 	div_mode = soup.find("div",class_="lister")
# 	tbody = div_mode.find("tbody",class_="lister-list")
# 	#empty lists
# 	list_position_of_movies = []
# 	list_of_movie_names=[]
# 	list_years_of_movies = []
# 	movise_rating = []
# 	urls_of_all_movies_list=[]
# 	#position of  the movies
# 	count=0
# 	position_of_movies = tbody.find_all("td",class_="posterColumn")
# 	for position in position_of_movies:
# 		count+=1
# 		list_position_of_movies.append(count)
# 	# find the movie names fromimdb
# 	tds = tbody.find_all("td",class_="titleColumn")
# 	for table_data in tds:
# 		list_of_movie_names.append((table_data.find("a")).text)
# 	#releasing year of the movie
# 	list_years_of_releasing = tbody.find_all("td",class_="titleColumn")
# 	for year_of_movie in list_years_of_releasing:
# 		list_years_of_movies.append((year_of_movie.find("span")).text)
# 	years_int_list = []
# 	for j in list_years_of_movies:
# 		str1 = ""
# 		for k in range(len(j)):
# 			if j[k] == "(" or j[k] == ")":
# 				continue
# 			else:
# 				str1+=j[k]
# 			str2 = int(str1)
# 		years_int_list.append(str2)
# 	#  find ratings from imdb
# 	rating_of_movies = tbody.find_all("td",class_="ratingColumn imdbRating")
# 	for rating in rating_of_movies:
# 		movise_rating.append((rating.find("strong")).text)
# 	#url of each movie
# 	urls_of_movies = tbody.find_all("td",class_="titleColumn")
# 	for urls in urls_of_movies:
# 		urls_of_all_movies_list.append(urls.find("a")["href"])
# 	#the total information of task1
# 	for i in range(250):
# 		data_of_movies = {}
# 		data_of_movies["position"] = list_position_of_movies[i]
# 		data_of_movies["name"] = list_of_movie_names[i]
# 		data_of_movies["year"] = years_int_list[i]
# 		data_of_movies["rating"] = movise_rating[i]
# 		data_of_movies["url"] = "https://www.imdb.com"+urls_of_all_movies_list[i]
# 		list_of_data.append(data_of_movies.copy())
# 		# pprint.pprint(list_of_data)
# 		# return list_of_datae 
# scrape_top_list()
# with open("imdb.json","w+") as naik:
# 	json.dump(list_of_data,naik,indent=4)

