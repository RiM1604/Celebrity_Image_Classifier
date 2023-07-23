import webscrape
from selenium import webdriver

wd= webdriver.Chrome()

lionel_url="https://www.google.com/search?q=lionel+messi+photos&tbm=isch&ved=2ahUKEwjlrcGuxaKAAxXMmGMGHa7sAOoQ2-cCegQIABAA&oq=lionel+messi+photos&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6CAgAEIAEELEDOg0IABCKBRCxAxCDARBDOgoIABCKBRCxAxBDOgcIABCKBRBDOgsIABCABBCxAxCDAVClCFicGmDsG2gDcAB4AIABoAGIAcIJkgEDMC45mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=5um7ZOWiOsyxjuMPrtmD0A4&bih=786&biw=1536"
lionel_t_class="Q4LuWd"
# r48jcc pT0Scc iPVvYb
lionel_p_class="iPVvYb"

ronaldo_url="https://www.google.com/search?q=cristiano+ronaldo&tbm=isch&ved=2ahUKEwjU1dO0xaKAAxVw5TgGHT19AI8Q2-cCegQIABAA&oq=cristiano+ronaldo&gs_lcp=CgNpbWcQAzIKCAAQigUQsQMQQzIHCAAQigUQQzIHCAAQigUQQzIICAAQgAQQsQMyBwgAEIoFEEMyDQgAEIoFELEDEIMBEEMyBwgAEIoFEEMyBwgAEIoFEEMyCggAEIoFELEDEEMyBwgAEIoFEEM6BAgjECc6BQgAEIAEOgcIIxDqAhAnOggIABCxAxCDAVC8UFiChAFg-ogBaAJwAHgAgAGRAYgB-Q6SAQQxMS44mAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=8-m7ZJSQM_DK4-EPvfqB-Ag&bih=786&biw=1536"
ronaldo_t_class="Q4LuWd"
ronaldo_p_class="iPVvYb"

neymar_url="https://www.google.com/search?sxsrf=AB5stBifwtZT3AaKIKmh3gPbLbWmbv-G-w:1690037247141&q=neymar+photos&tbm=isch&sa=X&ved=2ahUKEwishZeux6KAAxXBd2wGHZ25DIIQ0pQJegQIERAB&biw=1536&bih=786&dpr=1.25"
neymar_t_class="Q4LuWd"
neymar_p_class="iPVvYb"

lionel_urls=webscrape.get_urls(wd,2,20,lionel_url,lionel_t_class,lionel_p_class)
ronaldo_urls=webscrape.get_urls(wd,2,20,ronaldo_url,ronaldo_t_class,ronaldo_p_class)
neymar_urls=webscrape.get_urls(wd,2,20,neymar_url,neymar_t_class,neymar_p_class)


webscrape.get_images(lionel_urls,"lionel_messi")
webscrape.get_images(ronaldo_urls,"cristiano_ronaldo")
webscrape.get_images(neymar_urls,"neymar")

