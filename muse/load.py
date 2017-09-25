import os
os.system('jupyter nbconvert --to notebook --execute gen_analysis.ipynb')
os.system('jupyter nbconvert gen_analysis.nbconvert.ipynb')