# # #task5

# #def the function
# def scrape_top_list():
# 	import time
# 	import requests
# 	import json
# 	from bs4 import BeautifulSoup
# 	import pprint
# 	from random import randint

# 	file_of_imdb = open("imdb.json","r")
# 	dict_of_10_movies = json.load(file_of_imdb)

# 	## finding the link of the top 10 movies:-

# 	list_of_total_dictionery = []

# 	##finding of name of the movie and name of the director

# 	for each_movie in range(len(dict_of_10_movies)):
# 		total_dictionery = {}
# 		for each_movie_key,each_movie_value in dict_of_10_movies[each_movie].items():
# 			if each_movie_key == "name":
# 				total_dictionery[each_movie_key] = each_movie_value
# 			if each_movie_key == "url":
# 				responds = requests.get(each_movie_value)
# 				time.sleep(randint(1,5))

# 				soup = BeautifulSoup(responds.text,"html.parser")
# 				main_div = soup.find("div",class_="plot_summary")


# 				#this is for director name
# 				anchors_of_main_div = main_div.find("div",class_="credit_summary_item")
# 				a_href = anchors_of_main_div.find_all(("a")) 
# 				list_of_director = []

# 				for director_name in a_href:
# 					list_of_director.append(director_name.text)
# 				total_dictionery["director"] = list_of_director

# 				#finding the languages and country

# 				text_block_div = soup.find_all("div",class_="txt-block")
# 				list_of_languages = []

# 				for i in text_block_div:
# 					h4_tags = i.find_all("h4")
# 					for h4_tag in h4_tags:
# 						a_hrefs = i.find_all("a")
# 						for a_href in a_hrefs:
# 							if "Country:" in h4_tag:
# 								total_dictionery["Country:"] = a_href.text
# 							elif "Language:" in h4_tag:
# 								list_of_languages.append(a_href.text)

# 						total_dictionery["Language:"] = list_of_languages
				

# 					#finding the run time of the movie

# 					run_time_of_movie = i.find("time")
# 					for h4_tag in h4_tags:
# 						if "Runtime:" in h4_tag:
# 							total_dictionery["Runtime:"] = run_time_of_movie.text


# 				#finding the genre:-

# 				list_of_movies_genre = []

# 				gener_div = soup.find_all("div",class_="see-more inline canwrap")
# 				for gener in gener_div:
# 					h4_tags_gener = gener.find_all("h4")
# 					for h4_tag_gener in h4_tags_gener:
# 						a_hrefs_gener = gener.find_all("a")
# 						for a_href_gener in a_hrefs_gener:
# 							if  "Genres:" in h4_tag_gener:
# 								list_of_movies_genre.append(a_href_gener.text)

# 							total_dictionery["Genres:"]=list_of_movies_genre
				
# 				#finding the story line
# 				div_summery_text = main_div.find("div",class_="summary_text")
# 				total_dictionery["bio"] = div_summery_text.text.strip()

# 	#finding_the poster column

# 				requests_of_link = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
# 				time.sleep(randint(1,5))

# 				soup_of_main_page = BeautifulSoup(requests_of_link.text,"html.parser")
# 				tbody = soup_of_main_page.find("tbody",class_="lister-list") 
# 				trs = tbody.find_all("tr")

# 				for tr in trs:
# 					table_row = tr.find_all("td",class_="posterColumn")
# 					for a_tag in table_row:
# 						anchore_tag = a_tag.find("a")
# 						image_anchore = anchore_tag.find("img")["src"]
# 						total_dictionery["poster_image_url"] = image_anchore
# 	#dumping of the 10 movies
# 		list_of_total_dictionery.append(total_dictionery)
# 	#dump all the data of 250 movies
# 	with open("imdb_movies.json","w+") as hai_vanu:
# 		json.dump(list_of_total_dictionery,hai_vanu,indent=2)

# #calling of the function
# scrape_top_list()


