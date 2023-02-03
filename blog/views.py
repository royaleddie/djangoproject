from django.shortcuts import render


posts = [
    {
        'title' : 'Royal',
        'author' : 'Roy Ray',
        'datPosted' : '23re june, 2009',
        'content' : 'jfjsldjklk'
    },

    {
        'title' : 'Royal',
        'author' : 'Roy Ray',
        'datPosted' : '23re june, 2009',
        'content' : 'jfjsldjklk'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})