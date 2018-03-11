from django.shortcuts import render

def index(request):
	uid = request.session.get('user')
	if uid is None:
		return render(request, 'index.html')
	else:
		return render(
			request,
			'user.html',
			{'user': User.objects.get(pk=uid)}
		)
	
