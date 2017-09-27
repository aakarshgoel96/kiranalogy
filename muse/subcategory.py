import csv
import numpy as np
import pandas as pd
from scipy import stats
import math
import io
import requests
from io import StringIO
from datetime import datetime
import matplotlib.pyplot as plt

import cufflinks as cf
cf.set_config_file(offline=True)
import plotly as py
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot,offline
import plotly.graph_objs as go
from django.conf import settings
import os
def gethtmlanalysis(subcategory):

#category=raw_input()

	
	df = pd.read_csv(os.path.join(settings.BASE_DIR, "muse/musedb.csv"),sep=',',error_bad_lines=False,warn_bad_lines=False)

	df_cat=df[df["SUBCATEGORY_DESC"]==subcategory]

	del df

	brand=df_cat["BRAND_DESC"].value_counts()
	l=brand.sum()
	reg=pd.DataFrame({'labels':brand.index.tolist(), 'values':brand.values.tolist()})
	brand=brand[brand>(l*0.008)]
	trace = go.Pie(labels=brand.index.tolist(), values=brand.values.tolist())
	data=go.Data([trace])
	layout=go.Layout(title="Top Brands of  "+subcategory + " with total number of items sold")

	figure=go.Figure(data=data,layout=layout)

	offline.plot(figure,filename=os.path.join(settings.BASE_DIR, "templates/tpl/subcat-brand.html"), auto_open=False)
