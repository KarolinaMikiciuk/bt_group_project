import csv


def get_review_meta_data(page_num):
    """Returns all metadata for reviews on specified page."""
    reviews_all_meta = []
    # fetch data
    url = f"https://www.broadband.co.uk/broadband/providers/bt/reviews//page:{page_num}/#reviews"
    result_fetched = rq.get(url)
    content_soup = BeautifulSoup(result_fetched.content, 'lxml') #using lxml parser features='lxml'

    # find html of the review class in the content soup
    reviews_all_meta = content_soup.find_all(class_="review") #class_="review" #class_="stars right"
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



def save_into_csv(dest_folder,page_num, reviews_locations, reviews_dates, reviews_contents):
    """Saves data from page X to data_file_X.csv in dest_folder."""
    file_name = dest_folder+f"/data_file_{page_num}.csv"

    with open(file_name,'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['content','location','date','satisfaction','customer_service','speed','reliability'])

        for i in range(len(reviews_dates)):

            content = reviews_contents[i]
            location = reviews_locations[i]
            date = reviews_dates[i]

#             satisfaction = reviews_rating[i][0] # here list index out of range; 11 items in reviews, 40 in dates
#             customer_service = reviews_rating[i][1]
#             speed = reviews_rating[i][2]
#             reliability = reviews_rating[i][3]

            csv_file.write(f"{content},{location},{date},")
           #",{satisfaction},{customer_service},{speed},{reliability},")
