from django import forms
from django.shortcuts import render
import logging

from . import util


def index(request):
    print("Log message goes here.")
    q = request.GET.get('q')
    if q != None:
        if util.get_entry(q) != None:
            return render(request, "encyclopedia/entry.html", {
                "article": util.get_entry(q),
                "title": q
            })
        else:
            filtered_list = []
            list = util.list_entries()
            for l in list:
                if q in l:
                    filtered_list.append(l)
            return render(request, "encyclopedia/results.html", {
                "results": filtered_list
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "article": util.get_entry(title),
        "title": title
    })

def results(request, results):
    return render(request, "encyclopedia/results.html", {
        "results": results
    })

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        article = request.POST.get('article')
        print("Log message goes here.")

        list = util.list_entries()
        if title not in list:
            f = open(f'{title}.md', "w")
            f.write(title)
            f.write(article)
    return render(request, "encyclopedia/create.html")