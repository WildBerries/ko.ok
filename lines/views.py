import json

from django.shortcuts import render, redirect

from .models import Recipe

# Create your views here.


LINES = {'lines_list': ['hot', 'cold', 'pizza', 'pasta', 'dessert', 'bar']}


def toSearch(request):
    """ Redirects to search view used as a "Home page"
    """
    return redirect('search')


def search(request):
    """ Searches through recipes from all lines
    """
    context = {}
    try:
        context['recipes_all'] = Recipe.objects.all()
    except Recipe.DoesNotExist:
        context['recipes_all'] = None
    context.update(LINES)
    return render(request, 'lines/search.html', context=context)


def line_content(request, line_name):
    try:
        recipes = Recipe.objects.filter(line=line_name)
    except Recipe.DoesNotExist:
        recipes = ['No recipes Found']
    context = {'line_name': line_name,
               'recipes': recipes
               }
    context.update(LINES)
    return render(request, 'lines/line.html', context=context)


def recipe_details(request, line_name, recipe_slug):
    context = {'line_name': line_name}
    try:
        recipe = Recipe.objects.get(slug=recipe_slug)
        context['recipe'] = recipe
        recipe.tools = toolsInColumns(recipe.tools, 2)
    except Recipe.DoesNotExist:
        context['recipe'] = None
    context.update(LINES)
    return render(request, 'recipe/details.html', context=context)



def recipe_ingridients(request, line_name, recipe_slug):
    context = {'line_name': line_name}
    try:
        recipe = Recipe.objects.get(slug=recipe_slug)
        recipe.ingridients = json.loads(recipe.ingridients)
        recipe.ingridients_headers = json.loads(recipe.ingridients_headers)
        context['recipe'] = recipe
    except Recipe.DoesNotExist:
        context['recipe'] = None
    context.update(LINES)
    return render(request, 'recipe/ingridients.html', context=context)


def recipe_technology(request, line_name, recipe_slug):
    context = {'line_name': line_name}
    try:
        recipe = Recipe.objects.get(slug=recipe_slug)
        context['recipe'] = recipe
        recipe.tools = toolsInColumns(recipe.tools, 2)
    except Recipe.DoesNotExist:
        context['recipe'] = None
    context.update(LINES)
    return render(request, 'recipe/technology.html', context=context)



# content preparation block
def toolsInColumns(tools_str, two_or_thee):
    """ Cleans and Split data into tuples.
        Items stored per tuple according to integer variable.
    """
    tools_clean = [tool.strip().lower().capitalize() for tool in tools_str.split(',')]
    """
    # removes duplicates
    for i in tools_clean:
        while tools_clean.count(i) > 1:
            tools_clean.remove(i)
    """
    tools = ['{}. {}'.format(i + 1, tools_clean[i]) for i in range(len(tools_clean))]

    cut = int(len(tools)/2) + 1 if len(tools) % 2 else int((len(tools)/2))
    first = tools[:cut]
    second = tools[cut:]
    
    if len(first) == len(second):
        result = list(zip(first, second))
    else:
        result = list(zip(first, second)) + [(first[-1], '')]

    return result


    
    

