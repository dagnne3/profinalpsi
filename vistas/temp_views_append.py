def tours_view(request):
    if 'user_id' not in request.session:
         return redirect('login')
    
    tours = Tour.objects.all()
    username = request.session.get('username')
    
    context = {
        'tours': tours,
        'username': username
    }
    return render(request, "tours.html", context)
