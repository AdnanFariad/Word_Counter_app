from django.shortcuts import render
import operator

def index(request):
    return render(request, 'home.html')

def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    length = len(word_list)

    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sorted_list = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'text':data, 'length':length, 'word_dict':sorted_list})