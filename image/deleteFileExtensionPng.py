import os
files = os.listdir();
for file in files:
	if file.endswith(".png"):
		os.remove(file)