 # CFG Course Final Project
 
 Team: Radhika Kumar, Elizabeth Arevalo, Isobel Blythe, Karolina Mikiciuk, Sunaina Parvathi
 
 ## Project Folder Structure 
 
 ```
.
└── bt_group_project
    ├── analysis
    │   ├── EDA_Null_Values_1.ipynb
    │   ├── review_count_plot.ipynb
    │   └── StarRating_Analysis.ipynb
    ├── data
    │   ├── bt_data.csv
    │   ├── bt_data_with_locations.csv
    │   ├── data_file_10.csv
    │   ├── data_file_11.csv
    │   ├── data_file_12.csv
    │   ├── data_file_13.csv
    │   ├── data_file_14.csv
    │   ├── data_file_15.csv
    │   ├── data_file_16.csv
    │   ├── data_file_17.csv
    │   ├── data_file_18.csv
    │   ├── data_file_19.csv
    │   ├── data_file_1.csv
    │   ├── data_file_20.csv
    │   ├── data_file_21.csv
    │   ├── data_file_22.csv
    │   ├── data_file_23.csv
    │   ├── data_file_24.csv
    │   ├── data_file_25.csv
    │   ├── data_file_26.csv
    │   ├── data_file_27.csv
    │   ├── data_file_28.csv
    │   ├── data_file_29.csv
    │   ├── data_file_2.csv
    │   ├── data_file_30.csv
    │   ├── data_file_31.csv
    │   ├── data_file_32.csv
    │   ├── data_file_33.csv
    │   ├── data_file_34.csv
    │   ├── data_file_35.csv
    │   ├── data_file_36.csv
    │   ├── data_file_37.csv
    │   ├── data_file_38.csv
    │   ├── data_file_39.csv
    │   ├── data_file_3.csv
    │   ├── data_file_40.csv
    │   ├── data_file_41.csv
    │   ├── data_file_42.csv
    │   ├── data_file_43.csv
    │   ├── data_file_44.csv
    │   ├── data_file_45.csv
    │   ├── data_file_46.csv
    │   ├── data_file_47.csv
    │   ├── data_file_48.csv
    │   ├── data_file_49.csv
    │   ├── data_file_4.csv
    │   ├── data_file_50.csv
    │   ├── data_file_51.csv
    │   ├── data_file_52.csv
    │   ├── data_file_53.csv
    │   ├── data_file_54.csv
    │   ├── data_file_55.csv
    │   ├── data_file_56.csv
    │   ├── data_file_57.csv
    │   ├── data_file_58.csv
    │   ├── data_file_59.csv
    │   ├── data_file_5.csv
    │   ├── data_file_60.csv
    │   ├── data_file_61.csv
    │   ├── data_file_62.csv
    │   ├── data_file_63.csv
    │   ├── data_file_64.csv
    │   ├── data_file_65.csv
    │   ├── data_file_66.csv
    │   ├── data_file_67.csv
    │   ├── data_file_68.csv
    │   ├── data_file_69.csv
    │   ├── data_file_6.csv
    │   ├── data_file_70.csv
    │   ├── data_file_71.csv
    │   ├── data_file_72.csv
    │   ├── data_file_73.csv
    │   ├── data_file_74.csv
    │   ├── data_file_75.csv
    │   ├── data_file_76.csv
    │   ├── data_file_77.csv
    │   ├── data_file_78.csv
    │   ├── data_file_79.csv
    │   ├── data_file_7.csv
    │   ├── data_file_80.csv
    │   ├── data_file_8.csv
    │   └── data_file_9.csv
    ├── data_cleaning.ipynb
    ├── gb.csv
    ├── nltk_sentiment_analysis.ipynb
    ├── README.md
    ├── report.pdf
    ├── requirements.txt
    ├── review_trend_plot.ipynb
    ├── src
    │   ├── broadband-dot-com-scraper.py
    │   ├── bt_wordcloud.png
    │   ├── location_functions.ipynb
    │   ├── nlp_pipeline.ipynb
    │   ├── utils.py
    │   └── wordfrequencycloud.py
    ├── team_project.ipynb
    └── uk_locations.csv

```

* The analysis folder contains the statistical analysis code. 
* The data folder contains all of the data that we have scraped for our project.
*  Files gb.csv and uk_locations.csv are files containing data necessary for the cleansing stage of the locations data. 
*  The file nltk_sentiment_analysis.ipynb, as well as src/nlp_pipeline.ipynb contain the sentiment analysis code, the former being a file containing the analysis, while the latter contains functions used for cleaning the review data. 
*  Files utils.py and broadband-dot-com-scraper.py contain the code used for scraping the data from the website. 
*  The report.pdf contains our project report.
*  The team_project.ipynb contains visualisations, without code, as well as our conclusions and insights from the collected data; the target audience for this notebook are project stakeholders. Finally, wordfrequencycloud.py contains the code for producing a word cloud.

Separating analysis and the different stages of the data project lifecycle is necessary in the case of our project, as having everything in one notebook would freeze your computer when trying to run it. 

The nlp_pipeline.ipynb contains functions necessary to clean the review data. It used to contain the topic modelling code and keyword extraction code (using Gensim and nltk-rake), but this code did not make it into the final project due to ridiculously intensive CPU usage. 

## Steps for running the code
### Our project is divided into two main parts: statistical analysis and NLP (sentiment) analysis. The code for the two sections should be run completely separately to avoid burning your CPU. 

1. Clone the repository.
2. Run  $pip install -r requirements.txt
3. You may run the src/broadband-dot-com-scraper.py manually or use the data files that have already been scraped and saved in the data/ folder.
4. For statistical analysis run:
   * wordfrequencycloud.py
   * EDA_Null_Values_1.ipynb
   * review_count_plot.ipynb
   * StarRating_Analysis.ipynb
   * location_functions.ipynb
   it is not recommended to run them all at once due to the CPU usage
5. For the sentiment analysis run:
   * nltk_sentiment_analysis.ipynb
6. For our conclusions see the team_project.ipynb
