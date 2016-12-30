from django.shortcuts import render_to_response, render
from django.http import HttpResponse

# Create your views here.

# return the type of the content
# string / image / video
def analysisType(content):
	if content.startswith("http"):
		return "image"
	return "string"

def parse(request):
	filepath = request.GET.get("file", None)
	if filepath == None:
		return HttpResponse("miss file specification")

	result = list()
	lines = open(filepath, "r").readlines()
	lines = map(lambda x : x.strip(), lines)
	for line in lines:
		parts = line.split("\t")
		splited_line = list()
		for part in parts:
			cell_data = dict()
			cell_data["content"] = part
			cell_data["type"] = analysisType(part)
			cell_data["class"] = "data"
			splited_line.append(cell_data)
		result.append(splited_line)
	print result
	return render_to_response("parse.html", {"result": result})
