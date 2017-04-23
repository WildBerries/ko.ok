import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'kook.settings')

import django
django.setup()

import json

from lines.models import Recipe

import codecs
from pprint import pprint 







TARGET_DIR = r'C:\Ocr_out'
IMAGE_DIR = r'C:\Ocr_out\media'

IMAGE_FILE = [file for file in os.listdir(IMAGE_DIR) if '.png' in file][0]
ALL_FILES = [os.path.join(TARGET_DIR, file) for file in os.listdir(TARGET_DIR)]
INGRIDIESNTS_DATA = [os.path.join(TARGET_DIR, file) for file in os.listdir(TARGET_DIR) if '_ing_' in file]

UNIQUE_HEADERS = {'number': '№ ингридиента',
                  'name': 'Наименование',
                  'weight_brutto': 'Вес брутто, г',
                  'weight_netto': 'Вес нетто,г',
                  'measure': 'Мера',
                  'weight_overall': 'Вес готового продукта, г/мл'
                  }



def getData(in_file_name):
    for file in ALL_FILES:
        if in_file_name in file:
            with codecs.open(file, "r", "utf_8_sig") as data:
                value = data.read()
                value_stripped = value.replace('\n', '')
                if 'brutto' in file:
                    value_stripped = value_stripped.replace('Е', '')
                    value_stripped = value_stripped.replace(' ', '')
                    value_stripped = value_stripped.replace('б', '6')
                if 'netto' in file:
                    value_stripped = value_stripped.replace('Е', '')
                    value_stripped = value_stripped.replace(' ', '')
                    value_stripped = value_stripped.replace('б', '6')
                elif 'number' in file:
                    value_stripped = value_stripped.replace('Е', '')
                    value_stripped = value_stripped.replace(' ', '')
                    value_stripped = value_stripped.replace('б', '6')
                elif 'name' in file:
                    value_stripped = value_stripped.replace('®', '*')
                elif 'mera' in file:
                    value_stripped = value_stripped.replace('Е', '')
                    value_stripped = value_stripped.replace(' ', '')
                    value_stripped = value_stripped.replace('б', '6')
                elif 'weight_overall' in file:
                    value_stripped = value_stripped.replace('Е', '')
                    value_stripped = value_stripped.replace(' ', '')
                    value_stripped = value_stripped.replace('б', '6')
                return value_stripped

            


ALL_LINES = ['hot', 'cold', 'pizza', 'pasta', 'dessert', 'bar']
what_line = int(input(
    'what line is it?:\n'
    '1 - hot\n'
    '2 - cold\n'
    '3 - pizza\n'
    '4 - pasta\n'
    '5 - dessert\n'
    '6 - bar\n'))

line = ALL_LINES[what_line-1]

#title 2
title = getData('title')
#date released 3
date_released = getData('date')
#date updated 4
date_update = ''.join([i for i in getData('Update') if i.isdigit() or i == '.'])
#tools 5
tools = getData('tools')
#serving_dish 6
serving_dish = getData('serving_dish')
#cooking time 7
cooking_time = getData('cooking_time')
# ingridients 8
ingridients = {}
# 01_ing_brutto.txt 01_ing_name.txt 01_ing_netto.txt 01_ing_number.txt 01_ing_weight_overall.txt
for ing_file in INGRIDIESNTS_DATA:
    filename = ing_file.split('\\')[-1]
    if not ingridients.get(filename[:2], ''):
        ingridients[filename[:2]] = {}
    if 'brutto' in filename:
        ingridients[filename[:2]].update({'brutto': getData(filename) or ''})
    elif 'netto' in filename:
        ingridients[filename[:2]].update({'netto': getData(filename) or ''})
    elif 'number' in filename:
        ingridients[filename[:2]].update({'number': getData(filename) or ''})
    elif 'name' in filename:
        ingridients[filename[:2]].update({'name': getData(filename) or ''})
    elif 'mera' in filename:
        ingridients[filename[:2]].update({'measure': getData(filename) or ''})
    elif 'weight_overall' in filename:
        ingridients[filename[:2]].update({'weight_overall': getData(filename) or ''})

#remove blank rows
to_remove = []
for key in ingridients:
    check = []
    for sub_key in ingridients[key]:
        check.append(ingridients[key][sub_key])
    print('IT IS CHECK', check, check.count(None))
    print(len(ingridients[key][sub_key]))
    print(len(ingridients[key]))
    if check.count('') == 5 and len(ingridients[key]) == 5:
        to_remove.append(key)
    elif check.count('') == 6 and len(ingridients[key]) == 6:
        to_remove.append(key)
print('IT IS TO BE REMOVED', to_remove)
list(filter(ingridients.pop, to_remove))

ingridients = json.dumps(ingridients)

# ingridients_headers 9


ingridients_headers = json.dumps(UNIQUE_HEADERS)

#dish output 10
dish_output = getData('dish_output')
# cooking technology 11
cooking_technology = getData('technology')
#nutrition 12., 13., 14., 15.
nutrition_caloricity = getData('Caloricity')
nutrition_proteins = getData('proteins')
nutrition_fats = getData('fats')
nutrition_carbohydrates = getData('carbohydrates')
#decor delivery 16
decor_delivery = getData('delivery')
#organoleptic stats 17
organoleptic_stats = getData('Organoleptic')



print('01. line:', line)
print('02. title:', title)
print('03. release date:', date_released)
print('04. update:', date_update)
print('05. tools:', tools)
print('06. cooking time:', serving_dish)
print('07. cooking time:', cooking_time)
print('08. ingridients:'), pprint(ingridients)
print('09. ingridients_headers:'), pprint(ingridients_headers)
print('10. dish output:', dish_output)
print('11. cooking technology:', cooking_technology)
print('12., 13., 14., 15. nutrition:', nutrition_caloricity, nutrition_proteins, nutrition_fats, nutrition_carbohydrates)
print('16. decor delivery:', decor_delivery)
print('17. organoleptic stats:', organoleptic_stats)
print('18. image_file:', IMAGE_FILE)





def populate():
    recipe, not_exists = Recipe.objects.get_or_create(title=title)
    if not_exists:
        print('Creating a new Recipe: {}'.format(title))

    recipe.line = line
    recipe.title = title
    recipe.date_released = date_released
    recipe.date_update = date_update
    recipe.tools = tools
    recipe.serving_dish = serving_dish
    recipe.cooking_time = cooking_time
    recipe.image_filename = IMAGE_FILE
    recipe.ingridients = ingridients
    recipe.ingridients_headers = ingridients_headers
    recipe.dish_output = dish_output
    recipe.cooking_technology = cooking_technology
    recipe.nutrition_caloricity = nutrition_caloricity
    recipe.nutrition_proteins = nutrition_proteins
    recipe.nutrition_fats = nutrition_fats
    recipe.nutrition_carbohydrates = nutrition_carbohydrates
    recipe.decor_delivery = decor_delivery
    recipe.organoleptic_stats = organoleptic_stats
    
    recipe.save()
    
    return recipe



if __name__ == "__main__":
    print("Starting kook_project population script ..... ", end='')
    populate()
    print("Done!")

