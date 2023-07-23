from selenium import webdriver
from selenium.webdriver.common.by import By
import io,requests
import time
from PIL import Image
import os



# wd = webdriver.Chrome()

def get_urls(wd,delay,max_images,url,thumbnail_class=None,img_class=None):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    wd.get(url)
    image_urls=set()
    skip=0
    while len(image_urls)<max_images:
        scroll_down(wd)
        thumbnails= wd.find_elements(By.CLASS_NAME,thumbnail_class)
        #class="rg_i {classname}"

        for img in thumbnails[len(image_urls)+skip:max_images]:
            try:
                img.click()
                print(f"loop {len(image_urls)}")
                time.sleep(delay)
            except:
                continue
            images= wd.find_elements(By.CLASS_NAME,img_class)
            # class="a b c"

            #while using class names 
            #caution: class = "a b c" you can find the element just by using only one part of the class name using .CLASS_NAME attribute
            print("yes")
            print(images)
            for image in images:
                print("going in")
                if image.get_attribute('src') in image_urls:
                    max_images += 1
                    skip += 1
                    break

                if image.get_attribute('src') and 'https' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")

    return image_urls               

def download_image(folder_name,url,filename):

    if not os.path.exists(folder_name):
        try:
            os.mkdir(folder_name)
        except Exception as e:
            print(f"Error occured while creating folder with name {folder_name}")

    image_content=requests.get(url).content
    image_file=io.BytesIO(image_content)
    image=Image.open(image_file)
    file_path=folder_name+"\\"+filename

    with open(file_path,"wb") as f:
        image.save(f,"JPEG")
    print("success")

def get_images(urls,folder_name):
    for i,url in enumerate(urls):
        print(url)
        download_image(folder_name,url,str(i)+".jpg")

# url_temp="https://www.google.com/search?sxsrf=AB5stBjCIYgls50E8aUh4g3u5_ikwGdD0g:1689956596067&q=dogs&tbm=isch&sa=X&ved=2ahUKEwjOpeD0mqCAAxWoaPUHHdzQCoUQ0pQJegQIFxAB&biw=1536&bih=786&dpr=1.25"
# thumbnail_class_temp="Q4LuWd"
# img_class_temp="iPVvYb"

# urls=get_urls(wd,2,5,url_temp,thumbnail_class_temp,img_class_temp)
# # print(urls)
# folder_name="imgs"

# get_images(urls,folder_name)

# wd.quit()