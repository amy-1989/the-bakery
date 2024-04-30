from django.shortcuts import render

def bag(request):
    """ View to render the shopping bag page"""
    
    return render(request, 'bag/bag.html')
