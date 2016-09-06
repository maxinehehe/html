import requests
import PIL


h = 'http://www.socwall.com//images/wallpapers/65237-3840x2160.jpg'

pic = requests.get(h)



fp = open('/home/maxinehehe/photo/s1/t1'+'.jpg','wb')
fp.write(pic.content)
fp.close()