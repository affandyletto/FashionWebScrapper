import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
from time import sleep
import urllib.request
import os 
from re import search
import sqlite3
connection = sqlite3.connect('store_transactions.db')
cursor = connection.cursor()
url = 'https://www2.hm.com/en_gb/men/shop-by-product/t-shirts-and-vests.html'

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

command1="""CREATE TABLE IF NOT EXISTS images(image_id INTEGER PRIMARY KEY)"""
cursor.execute(command1)


for a in range(0,5):
	images = driver.find_elements_by_class_name('hm-product-item')
	print("scrap ke "+str(a+1))
	sleep(2)
	images[a].click()
	sleep(1)
	url=driver.current_url
	imageId=url[-5:-14]
	print(imageId)
	sleep(3)
	lookbook=2
	flatlay=1
	#Image1
	
	try:
		os.mkdir("Product "+str(a+1))
		image = driver.find_element_by_class_name('product-detail-main-image-container').find_element_by_tag_name('img').get_attribute("src")
		naming="Product "+str(a+1)+"/Lookbook_1_HM_"+str(a+1)+".png"
		urllib.request.urlretrieve(image,naming)
		cursor.execute("INSERT INTO images VALUES(imageId)")
	except:
		pass
	
	#image2
	try:
		image = driver.find_elements_by_class_name('pdp-secondary-image')[0].find_element_by_tag_name('img').get_attribute("src")
		
		if search("5BLOOKBOOK",image):
			naming="Product "+str(a+1)+"/Lookbook_"+str(lookbook)+"_HM_"+str(a+1)+".png"
			urllib.request.urlretrieve(image,naming)
			lookbook+=1
		elif "5BDESCRIPTIVESTILLLIFE" in image:
			naming="Product "+str(a+1)+"/Flatlay_"+str(flatlay)+"_HM_"+str(a+1)+".png"
			urllib.request.urlretrieve(image,naming)
			flatlay+=1
		print("gambar ke 2")
	except:
		pass


	try:
	#image3
		image = driver.find_elements_by_class_name('pdp-secondary-image')[1].find_element_by_tag_name('img').get_attribute("src")
		
		if search("5BLOOKBOOK",image):
			naming="Product "+str(a+1)+"/Lookbook_"+str(lookbook)+"_HM_"+str(a+1)+".png"
			urllib.request.urlretrieve(image,naming)
			lookbook+=1
		elif "5BDESCRIPTIVESTILLLIFE" in image:
			naming="Product "+str(a+1)+"/Flatlay_"+str(flatlay)+"_HM_"+str(a+1)+".png"
			urllib.request.urlretrieve(image,naming)
			flatlay+=1
		print("gambar ke 3")
	except:
		pass


	try:
	#image4
		image = driver.find_elements_by_class_name('pdp-secondary-image')[2].find_element_by_tag_name('img').get_attribute("src")
		
		if search("5BLOOKBOOK",image):
			naming="Product "+str(a+1)+"/Lookbook_"+str(lookbook)+"_HM_"+str(a+1)+".png"
			urllib.request.urlretrieve(image,naming)
			lookbook+=1
		elif "5BDESCRIPTIVESTILLLIFE" in image:
			naming="Product "+str(a+1)+"/Flatlay_"+str(flatlay)+"_HM_"+str(a+1)+".png"
			urllib.request.urlretrieve(image,naming)
			flatlay+=1
		print("gambar ke 4")
	except:
		pass


	try:
	#image5
		image = driver.find_elements_by_class_name('pdp-secondary-image')[3].find_element_by_tag_name('img').get_attribute("src")
		
		if search("5BLOOKBOOK",image):
			naming="Product "+str(a+1)+"/Lookbook_"+str(lookbook)+"_HM_"+str(a+1)+".png"
			urllib.request.urlretrieve(image,naming)
			lookbook+=1
		elif "5BDESCRIPTIVESTILLLIFE" in image:
			naming="Product "+str(a+1)+"/Flatlay_"+str(flatlay)+"_HM_"+str(a+1)+".png"
			urllib.request.urlretrieve(image,naming)
			flatlay+=1
		print("gambar ke 5")
	except:
		pass
	sleep(1)
	driver.execute_script("window.history.go(-1)")
	sleep(1)

'''
loadMore = driver.find_element_by_id('showmore')
for a in range(0,10):
	sleep(5)
	loadMore.click()
'''