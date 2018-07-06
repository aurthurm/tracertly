from django.shortcuts import render
from boards.models import Board

def home(request):
    heading = "Public Boards"
    public_boards = Board.objects.all().filter(public=True).exclude(archived=True)
    context = {
    	'heading': heading,
    	'boards': public_boards
    }
    return render(request, 'home.html', context=context)
