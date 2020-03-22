from django.shortcuts import render, redirect
from .models import flag
import requests
import json


categories = []
categories_url = []



def CategoryView(request):


    r = requests.get('https://simple-drf.herokuapp.com/api/category')
    d = json.loads(r.text)
    for e in d:
        l = list(e.values())
        categories.append(l[2])
        categories_url.append(l[1])


    s = requests.get('https://simple-drf.herokuapp.com/api/article')
    a = json.loads(s.text)
    b = a[0]

    links = []
    ratings = []
    categories_ = []
    for link in a:
        links.append(list(link.values())[2])
        ratings.append(list(link.values())[3])
        categories_.append(list(link.values())[4])

    cats = []
    for c in categories_:
        sub_cats = []
        for d in c:
            d = int(d[-2])
            sub_cats.append(categories[d-1])
        cats.append(sub_cats)

    newlist = []
    for i in range(len(links)):
        my_dict = {}
        my_dict['link'] = links[i]
        my_dict['rating'] = ratings[i]
        my_dict['categories'] = cats[i]
        newlist.append(my_dict)

    return render(request, 'index.html', {'cats': cats, 'links': links, 'ratings': ratings, 'nn': newlist, 'categori': categories})


def add_article(request):
    if request.method == 'POST':
        link = request.POST['link']
        rating = float(request.POST['rating'])
        categoriees = request.POST.getlist('categoriees')
        catt = []
        print(categoriees)
        for c in categoriees:
            n = categories.index(c)
            catt.append(categories_url[n])
        print(catt)

        # data = {'link':link, 'rating':rating, 'categories':catt}
        # r = requests.post('https://simple-drf.herokuapp.com/api/article/', params=data)

        url = 'https://simple-drf.herokuapp.com/api/article/'
        payload = {'link':link, 'rating':rating, 'categories':catt}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)

        print(link)
        print(rating)
        print(catt)
        print(r)

        return redirect('/console/category')
