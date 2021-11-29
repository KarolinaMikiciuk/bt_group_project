from bs4 import BeautifulSoup
import requests as rq
import csv
from utils import get_review_content, get_review_date, get_review_location, get_review_meta_data, get_review_ratings, save_into_csv

dest_folder = "/home/mrfox/Desktop/bt_group_project/data"
page_start = 1
page_end = 2 #81

for page_num in range(page_start,page_end):

    reviews_meta_data = get_review_meta_data(page_num)
    reviews_contents = get_review_content(reviews_meta_data)
    reviews_dates = get_review_date(reviews_meta_data)
    reviews_locations = get_review_location(reviews_meta_data)
    #reviews_ratings = get_review_ratings(reviews_meta_data)
    #reviews_ratings = group_corresponding_ratings(reviews_ratings)

    save_into_csv(dest_folder,page_num,reviews_locations, reviews_dates, reviews_contents)
