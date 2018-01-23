from retrieve_image_data import RtrvData as rd
# Open image file for reading (binary mode)
x = rd('./')
tags = x.get_exif('./images/img3.JPG',True,True)
# Return Exif tags
spec = tags['file size']
print spec

