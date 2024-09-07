from django.shortcuts import render

posts = [
    {
        'author':'John',
        'title':'First Post',
        'content':'This is the first post',
        'date_posted':'July 15, 2021'
    },
    
    {
        'author':'Jane doe',
        'title':'Second Post',
        'content':'This is the second post',
        'date_posted':'July 17, 2021'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html',context)  

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
# Create your views here.