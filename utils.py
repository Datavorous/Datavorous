import os,json,markdown

def file_list():
	files = []
	for x in os.listdir("posts"):
		if x.endswith(".md"):files.append(x)
	return files		

def get_meta(index):
	file = open(f"posts/{file_list()[index]}","r")
	file_str = markdown.markdown(file.read())
	file.close()
	return json.loads(file_str[(file_str.find("<meta>")+len("<meta>")):(file_str.find("</meta>"))])

def get_content(index):
	html = markdown.markdown(index.read())
	return html.replace(html[(html.find("<meta>")+len("<meta>")):(html.find("</meta>"))],'')

def sort(array):
	for x in range(int(len(array)-1)):
		temp = array[x]
		if (array[x+1]["postno"] > array[x]["postno"]):array[x],array[x+1] = array[x+1],temp 		
	return array		