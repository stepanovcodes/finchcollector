from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Import the Cat Model
from .models import Finch

# finches = [
# {'name': 'Finch1', 'species': 'house finch', 'color': 'red', 'age': 1, 'description': 'A common urban finch.'},
#     {'name': 'Finch2', 'species': 'goldfinch', 'color': 'yellow', 'age': 2, 'description': 'Known for its vibrant plumage.'},
#     {'name': 'Finch3', 'species': 'sparrow', 'color': 'brown', 'age': 2, 'description': 'Often found in city parks.'},
#     {'name': 'Finch4', 'species': 'zebra finch', 'color': 'gray', 'age': 1, 'description': 'Distinctive stripes on its throat.'},
#     {'name': 'Finch5', 'species': 'canary', 'color': 'yellow', 'age': 3, 'description': 'Popular pet bird with melodious songs.'},
#     {'name': 'Finch6', 'species': 'purple finch', 'color': 'purple', 'age': 2, 'description': 'Named for its plumage color.'},
#     {'name': 'Finch7', 'species': 'greenfinch', 'color': 'green', 'age': 1, 'description': 'Has a greenish hue.'},
#     {'name': 'Finch8', 'species': 'chaffinch', 'color': 'blue', 'age': 2, 'description': 'Known for its colorful markings.'},
#     {'name': 'Finch9', 'species': 'siskin', 'color': 'yellow-green', 'age': 1, 'description': 'Small and energetic.'},
#     {'name': 'Finch10', 'species': 'linnet', 'color': 'brown', 'age': 3, 'description': 'Recognizable by its brown plumage.'}
# ]

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['species', 'color', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'