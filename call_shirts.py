import os

for i in range(1,19):

	shirt_path="original_shirts/"+str(i)+".png"
	print(shirt_path)
	os.system("python wrapper.py  --shirt_path={}".format(shirt_path))