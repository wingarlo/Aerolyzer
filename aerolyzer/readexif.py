from retrieve_image_data import RtrvData as rd
# Open image file for reading (binary mode)
x = rd('./')
tags = x.get_exif('./images/phones/i6s/IMG_0471.jpg',True,True)
# Return Exif tags

original = tags['exif datetimeoriginal']
edited = tags['image datetime']
if (original == edited):
	return True
else:
	return False
