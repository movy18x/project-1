from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from . import util
from markdown import *
import random
md = Markdown()
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def createPage(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    if title is not None and content is not None:
        util.save_entry(str(title) ,str(content))
        return render(request,"encyclopedia/createPage.html")

def singal_page(request , entry):
    entry_page = util.get_entry(entry)
    return render(request , "encyclopedia/selectedEntry.html" , context={
        "title": entry,
        "content": md.convert(str(entry_page))
    })

def edit(request , entry):
    entry_before_edit = util.get_entry(entry)
    entry_after_edit = request.POST.get('edit_content')
    if entry_after_edit is not None:
        entry_before_edit = entry_after_edit
        util.save_entry(str(entry), str(entry_after_edit))
    return render(request , 'encyclopedia/editPage.html' , context={
        "content":entry_before_edit,
        "new_content":entry_after_edit}
    )

def randomPage(request):
    entry_list = util.list_entries()
    random_entry = random.choice(entry_list)
    random_entry_content = util.get_entry(random_entry)
    return render(request, 'encyclopedia/selectedEntry.html' , context={
        "title": random_entry,
        "content": md.convert(str(random_entry_content)),
    })
def search(request):
    q = request.POST.get('q','')
    entries = util.list_entries()
    for entry in entries:
        if str(q.upper()) == str(entry.upper()):
            content = util.get_entry(entry)
            return render(request, "encyclopedia/selectedEntry.html", context={
                "title": entry,
                "content": md.convert(str(content))})
        elif str(q.upper()) in entry.upper():
            return render(request, "encyclopedia/index.html" , context={
                "entries": [entry]
            })
