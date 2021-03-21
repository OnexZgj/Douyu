from selenium import webdriver
import time

class Douyu(object):

    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def run(self):
        # url
        # driver
        # get
        self.driver.get(self.url)
        # //*[@id="listAll"]/section[2]/div[2]/ul/li[1]
        while True:
            time.sleep(3)
            data_list = self.parse_data()
            self.save_data(data_list)
            # next
            try:
                el_next = self.driver.find_element_by_xpath('//*[contains(text(),"下一页")]')
                self.driver.execute_script('scrollTo(0,1000000)')
                el_next.click()
            except:
                break


    def parse_data(self):
        room_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div')

        print(len(room_list))
        src = self.driver.find_element_by_xpath('//a/div[1]/div[1]/img').get_attribute('src')
        print(src)

        # next

        data_list = []
        for room in room_list:
            temp = {}
            temp['title'] = room.find_element_by_xpath('./a[1]/div[2]/div[1]/h3').text
            # //*[@id="listAll"]/section[2]/div[2]/ul/li[1]/div/a/div[2]/div[2]/span/text()
            temp['hot'] = room.find_element_by_xpath('./a[1]/div[2]/div[2]/span').text
            temp['owner'] = room.find_element_by_xpath('./a[1]/div[2]/div[2]/h2').text
            # //*[@id="listAll"]/section[2]/div[2]/ul/li[1]/div/a/div[1]/div[1]/img
            temp['src'] = room.find_element_by_xpath('./a/div[1]/div[1]/img').get_attribute('src')
            print(temp)
            data_list.append(temp)
        return data_list

    def save_data(self, data_list):
        for data in data_list:
            print(data)



if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()