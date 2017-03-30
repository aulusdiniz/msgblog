from django.shortcuts import render
from trees.models import Tree

# Create your views here.
def tree_view(request, tree_id):
    tree = Tree.objects.get(id=tree_id)
    context = {'tree': tree}
    return render(request,'tree-view.html', context)

def tree_list(request):
    context = {'tree': 'none'}
    return render(request, 'tree-list.html', context)

def tree(request):
    trees = Tree.objects.all()
    context = {'trees': trees}
    return render(request,'base.html', context)
