def get_file_contents(path):
	with open(path, "r") as f:
		return f.read()

def read_lines(path):
	with open(path, "r") as f:
		return f.readlines()