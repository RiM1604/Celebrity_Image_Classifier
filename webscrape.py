from selenium import webdriver
from selenium.webdriver.common.by import By
import io,requests
import time
from PIL import Image



wd = webdriver.Chrome()

def get_images(wd,delay,max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    url = "https://www.google.com/search?sxsrf=AB5stBjCIYgls50E8aUh4g3u5_ikwGdD0g:1689956596067&q=dogs&tbm=isch&sa=X&ved=2ahUKEwjOpeD0mqCAAxWoaPUHHdzQCoUQ0pQJegQIFxAB&biw=1536&bih=786&dpr=1.25"
    wd.get(url)
    image_urls=set()
    skip=0
    while len(image_urls)<max_images:
        scroll_down(wd)
        thumbnails= wd.find_elements(By.CLASS_NAME,"Q4LuWd")
        #class="rg_i {classname}"

        for img in thumbnails[len(image_urls)+skip:max_images]:
            try:
                img.click()
                print(f"loop {len(image_urls)}")
                time.sleep(delay)
            except:
                continue
            images= wd.find_elements(By.CLASS_NAME,"iPVvYb")
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

def download_image(download_path,url,filename):
    image_content=requests.get(url).content
    image_file=io.BytesIO(image_content)
    image=Image.open(image_file)
    file_path=download_path+filename

    with open(file_path,"wb") as f:
        image.save(f,"JPEG")
    print("success")


urls=get_images(wd,2,5)
print(urls)
for i,url in enumerate(urls):
    print(url)
    download_image("imgs\\",url,str(i)+".jpg")

wd.quit()