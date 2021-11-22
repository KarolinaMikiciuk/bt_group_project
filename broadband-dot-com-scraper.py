from bs4 import BeautifulSoup
import pandas as pd
import requests as rq

all_reviews_contents = [] #3186 reviews 
all_reviews_locations = []
all_reviews_dates = []
all_reviews_ratings = []


for page_num in range(81): #there are 80 pages of reviews, start at page 1, not page 0, so put (1,81)
    url = f"https://www.broadband.co.uk/broadband/providers/bt/reviews//page:{page_num}/#reviews"
    result_fetched = rq.get(url)
    content_soup = BeautifulSoup(result_fetched.content, 'html.parser') #using lxml parser features='lxml'
    
    #  # GET ALL REVIEW METADATA
    # reviews_all_meta = content_soup.find_all(class_="review") #class_="review" #class_="stars right"

    # GET REVIEW CONTENT
    reviews_contents = content_soup.find_all("blockquote")
    for review_content in reviews_contents:  
        content = review_content.get_text()[10:-8]
        content = content.replace(","," ")
        all_reviews_contents.append(content)

    # GET REVIEW LOCATION 
    reviews_locations = content_soup.find_all(class_="review__location")
    for review_location in reviews_locations:
        location = (review_location.get_text()[19:-8]).strip()
        all_reviews_locations.append(location)
    
    # GET REVIEW DATE
    reviews_dates = content_soup.find_all(class_="review__date")
    for review_date in reviews_dates:
        date = review_date.get_text()[15:-8]
        all_reviews_dates.append(date)
    
    # GET REVIEW RATINGS
    reviews_ratings = content_soup.find_all(class_="ratings")
    for review_rating in reviews_ratings:  
        rating = review_rating.get_text() # ratingValue
        #all_reviews_ratings.append(rating)
        #print(review_rating)

review_df = pd.DataFrame({
'content' :all_reviews_contents,
'location':all_reviews_locations,
'date' : all_reviews_dates
})

#print(all_reviews_ratings)

review_df.to_csv("/home/mrfox/Desktop/bt_group_project/scraped_csv_one.csv", index=False)