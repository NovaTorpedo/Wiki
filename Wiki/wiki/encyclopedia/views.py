from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util

def converter2(word):
     content = util.get_entry(word)
     markdowner = Markdown()
     new_contents = markdowner.convert(content)
     if content != None:
          return new_contents
     else:
          return None

def converter(request, name): 
    entries = util.list_entries()
    """entries2 = [element.lower() for element in entries]"""
    if name in entries:
        contents = util.get_entry(name)
        markdowner = Markdown()
        new_contents = markdowner.convert(contents)
        return render(request, "encyclopedia/entry.html",{
            "contents":new_contents,
            "title":name.capitalize()
        })
    else:
        return render(request, "encyclopedia/error.html",{
            "message":"The Page you are looking For does not exist"
        })
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
"""def search(request):
    if request.method == "POST":
        search_entry = request.POST['q']
        entries = util.list_entries()
        entries2 = [element.lower() for element in entries]
        contents = util.get_entry(search_entry)
        markdowner = Markdown()
        new_contents = markdowner.convert(contents)
        entries = util.list_entries()
        for entry in entries:
            if entry.lower() == search_entry:
                a = converter2(entry)
            else:
                a = None
        if a != None:
            return render(request, "encyclopedia/entry.html",{
            "contents":a,
            "title":search_entry.capitalize()
            })
        else:
            for name in entries:
                if search_entry in name.lower():
                    return render(request, "encyclopedia/search.html",{
                        "contents":name,
                        "title":search_entry,
                        "name":name
                    })"""
def search(request):
    if request.method == "POST":
        search_entry = request.POST['q']
        entries = util.list_entries()
        for entry in entries:
            if entry.lower() == search_entry:
                a = converter2(entry)
                return render(request, "encyclopedia/entry.html",{
                    "contents":a,
                    "title":entry.capitalize()
                })
            elif search_entry in entry.lower():
                match = entry
        else:
            if match:
                return render(request, "encyclopedia/search.html",{
                    "contents":util.get_entry(match),
                    "title":match.capitalize(),
                    "name":match
                })
            else:
                return render(request, "encyclopedia/search.html",{
                    "title":search_entry.capitalize(),
                    "name":search_entry
                })
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST["title"]
        contents = request.POST["contents"]
        entries = util.list_entries()
        if title in entries:
            return render(request, "encyclopedia/error.html",{
                    "message":"This page already exists"
                })
        else:
            newpage = util.save_entry(title, contents)
            a = converter2(title)
            return render(request, "encyclopedia/entry.html",{
                "contents":a,
                "title":title.capitalize()
            })
def edit_page(request):
    if request.method == "POST":
        title = request.POST["page_title"]
        contents = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "contents":contents,
            "title":title
        })
def save_page(request):
        if request.method == "POST":
            title = request.POST["title"]
            contents = request.POST["contents"]
            newpage = util.save_entry(title, contents)
            a = converter2(title)
            return render(request, "encyclopedia/entry.html",{
                "contents":a,
                "title":title.capitalize()
            })
def random_page(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    page = converter2(entry)
    return render(request,"encyclopedia/entry.html",{
        "contents":page,
        "title":entry
    })


        



