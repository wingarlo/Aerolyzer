import os
import aerosol
from image_restriction_main import check_image
import sys
import plotly
import plotly.graph_objs as go
from image_restriction_functions import imgRestFuncs as Fxn
from retrieve_image_data import RtrvData as Data

if(check_image("./images/test2.jpg")):
	aero = aerosol.AeroData("./images/test2.jpg")
	x = []
	y = []
	colorIN = []
	results = aero.aerolyzeImage()
	for a,b,c in results:
		x.append(a)
		y.append(b)
	for TFval in results:
		if (TFval[2] == True):
			colorIN.append('rgba(215,63,9,1)')
		else:
			colorIN.append('rgba(0,0,0,1)')


	data = [go.Bar(
		x = x,
		y = y,
		marker=dict(color=colorIN)
	)]

	plotly.offline.plot(data, filename = "aeresults.html")

