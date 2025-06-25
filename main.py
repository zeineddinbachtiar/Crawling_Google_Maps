from module import google_map_review_scrapper

url = 'https://www.google.com/maps/place/Galaxy+Mall+1/@-7.2759917,112.7794289,918m/data=!3m1!1e3!4m8!3m7!1s0x2dd7fb001d72689d:0xbc83309f4de02024!8m2!3d-7.2759917!4d112.7820038!9m1!1b1!16s%2Fg%2F120_4kxz?entry=ttu&g_ep=EgoyMDI1MDYxNS4wIKXMDSoASAFQAw%3D%3D'

scroll_limit = 20

scrapper = google_map_review_scrapper

page_content = scrapper.get_page_content(url, scroll_limit)
review = scrapper.get_review(page_content)
to_df = scrapper.to_dataframe(review)
print(to_df)
scrapper.to_csv(to_df)
