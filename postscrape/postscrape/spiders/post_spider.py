import scrapy

class Post_Spider(scrapy.Spider):
    name = "posts"
    page = 1

    start_urls = [
        'https://www.kayak.co.in/Hyderabad-Hotels.7297.hotel.ksp'
    ]
    def parse(self, response):

        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        list_data = response.css('div.c44F-content .c44F-item')
        for i in range(0, len(list_data), 1):
            print(list_data[i].css('div.soom .soom-photo-wrapper .soom-photo::attr(src)').get())
            print(list_data[i].css('div.soom .soom-content-wrapper .soom-description-wrapper .soom-description .soom-name span::text').get())
            print(list_data[i].css('div.soom .soom-content-wrapper .soom-description-wrapper .soom-description .soom-rating-wrapper span::text').get())
            print(list_data[i].css('div.soom .soom-content-wrapper .soom-description-wrapper .soom-description .soom-price-section .soom-neighborhood::text').get())
            print(list_data[i].css('div.soom .soom-content-wrapper .soom-description-wrapper .soom-price::text').get())
            list_lower = list_data[i].css('div.soom .soom-content-wrapper .soom-freebies-section .soom-freebies .soom-freebie')
            for j in range(0, len(list_lower), 1):
                print(list_lower[j].css('span::text').get())
            print()

        
        # print(len(response.css('div.c44F-content .c44F-item')))
        # list_data = response.css('div.c44F-content .c44F-item')
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # list_data[0].css('div.soom .soom-photo-wrapper') For Image
        # list_data[0].css('div.soom .soom-content-wrapper .soom-description-wrapper') Upper Section
        # list_data[0].css('div.soom .soom-content-wrapper .soom-freebies-section') Lower Section
        # print(list_data[0].css('div.soom .soom-content-wrapper .soom-description-wrapper .soom-description .soom-name span::text').get())
        # print(list_data[0].css('div.soom .soom-content-wrapper .soom-description-wrapper .soom-description .soom-rating-wrapper span::text').get())
        # print(list_data[0].css('div.soom .soom-content-wrapper .soom-description-wrapper .soom-description .soom-price-section .soom-neighborhood::text').get())
        # print(list_data[0].css('div.soom .soom-content-wrapper .soom-description-wrapper .soom-price::text').get())

        # list_lower = list_data[0].css('div.soom .soom-content-wrapper .soom-freebies-section .soom-freebies .soom-freebie')
        # print(list_lower[0].css('span::text').get())
        # print(list_lower[1].css('span::text').get())
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # if str(type(list_data[i].css('div.soom .soom-photo-wrapper .soom-photo::attr(src)').get())) == "<class 'str'>":
        # print("Hidden Image- > " + list_data[i].css('div.soom .soom-photo-wrapper .soom-photo::attr(alt)').get())
        # filename = 'posts-%s.html' % self.page
        # self.page += 1 
        # with open(filename, 'wb') as f:
        #     f.write(response.body)