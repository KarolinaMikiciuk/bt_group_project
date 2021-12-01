import requests as rq
import csv
from bs4 import BeautifulSoup

def get_review_meta_data(page_num):
    """Returns all metadata for reviews on specified page."""
    reviews_all_meta = []
    # fetch data
    url = f"https://www.broadband.co.uk/broadband/providers/bt/reviews//page:{page_num}/#reviews"
    result_fetched = rq.get(url)
    content_soup = BeautifulSoup(result_fetched.content, 'lxml') #using lxml parser features='lxml'

    # find html of the review class in the content soup
    reviews_all_meta = content_soup.find_all(class_="review") 
    return reviews_all_meta

def get_review_content(reviews_all_meta):
    """Return the contents of the review + ~~~. Returns ~~~ if not found."""
    reviews_content = []
    for review in reviews_all_meta:
        content = review.blockquote.text
        content = content.replace(',',' ')
        reviews_content.append(content.replace('\t','').replace('\r','').replace('\n','')+"~~~")

    return reviews_content

def get_review_date(reviews_all_meta):
    """Returns the review date."""
    dates = []
    for review in reviews_all_meta:
        review_dates = review.div("div", {"class": "review__date"}) # iterating through divs with diff classes
        for review_date in review_dates:
            date_str = review_date.dd.text
            extracted_date = date_str.replace('\t','').replace('\n','')
            dates.append(extracted_date+"~~~") # always present
    return dates

def get_review_location(reviews_all_meta):
    """Returns the review location + ~~~. Returns ~~~ if not found."""
    locations = []

    for review in reviews_all_meta:
        review_locations = review.div("div", {"class": "review__location"})

        for review_loc in review_locations:
            location = review_loc.dd.text
            locations.append(location.replace('\t','').replace('\r','').replace('\n','')+"~~~")
    return locations


def save_into_csv(dest_folder,page_num, reviews_locations, reviews_dates, reviews_contents, reviews_rating):
    """Saves data from page X to data_file_X.csv in dest_folder."""
    file_name = dest_folder+f"/data_file_{page_num}.csv"
    
    with open(file_name,'a') as csv_file:
        header = ['content','location','date','satisfaction','customer_service','speed','reliability,']
        writer = csv.writer(csv_file)
        writer.writerow(header)
                         
        
        for i in range(len(reviews_dates)): 
                
            content = reviews_contents[i]
            location = reviews_locations[i]
            date = reviews_dates[i]
            
            satisfaction = reviews_rating[i][0] 
            customer_service = reviews_rating[i][1]
            speed = reviews_rating[i][2]
            reliability = reviews_rating[i][3]
            
            data = [content,location,date, satisfaction,customer_service,speed,reliability]
            writer.writerow(data)


def get_review_ratings(reviews_all_meta):
    """Returns a list of where each element is all the ratings given. ~~~ for no ratings."""
    ratings = []
    for review in reviews_all_meta:
        review_ratings = review.ul #.li   #('div',{"class" : "stars right"})

        if review and review_ratings: 
            rating = review_ratings.text.replace('\n','').replace('\t','').replace('\r','')
            ratings.append(rating+"~~~") # Nones don't get displayed

        else:
            ratings.append("~~~")
    return ratings

def clean_review_ratings(ratings):
    """Returns a list of lists with the ratings. Returns ~~~ for no rating given."""
    rating_types = ['Satisfaction','Service','Speed','Reliability'] 
    tuples = []
    
    for rating in ratings:
        r_tuples = []
        
        rating_list = rating.split(' ')
        rating_str =  "-".join(rating_list)
        rating_str = rating_str.replace('Customer-','').replace('-stars','').replace('-star','')        
        rating_list = rating_str.split('-')
            
        for rating_type in rating_types:
            
            if rating_type in rating_list:
                index = rating_list.index(rating_type)
                r_tuples.append(rating_list[index+1])    
            elif rating_type not in rating_list:
                r_tuples.append('~~~')
        tuples.append(r_tuples)   
        
    return tuples