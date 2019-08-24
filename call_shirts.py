import os

for i in range(0,19):

	shirt_path="original_shirts/"+I+".png"
	print(shirt_path)
	os.system("python wrapper.py  --shirt_path".format(shirt_path))