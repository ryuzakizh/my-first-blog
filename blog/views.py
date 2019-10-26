from django.shortcuts import render

# Create your views here.
def post_list(request):
	return render(request, 'blog/post_list.html', {}) #this view just takes a request, passes it to render(collect) function that will put together our template