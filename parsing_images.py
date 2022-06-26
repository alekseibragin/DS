from icrawler.builtin import GoogleImageCrawler

name = input('По какому запросу парсить изображения?\n')
quantity = int(input('Сколько нужно спарсить изображений?\n'))
path = input('Куда сохранить изображения?\n')

google_crawler = GoogleImageCrawler(storage={'root_dir': path})
google_crawler.crawl(keyword=name, max_num=quantity)