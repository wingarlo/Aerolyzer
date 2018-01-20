import exifread
# Open image file for reading (binary mode)
f = open('./phones/i6s/IMG_0471.jpg', 'rb')
out = open('./exiftest','w')
# Return Exif tags
tags = exifread.process_file(f, details=False,stop_tag='ExposureTime')
out.writelines(tags)
