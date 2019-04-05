from django import forms

unique_ingredients = {'bacon': 1, 'egg': 2, 'cheese': 3, 'roll': 4, 'sausage': 5, 'ham': 6, 'steak': 7, 'hashbrown': 8, 'hero': 9, 
                      'homefries': 10, 'toast': 11, 'roastbeef': 12, 'onion': 13, 'pepper': 14, 'tomato': 15, 'mushroom': 16, 'eggwhite': 17, 'turkeybacon': 18, 
                      'avocado': 19, 'spinach': 20, 'pancake': 21, 'frenchtoast': 22, 'waffles': 23, 'bagel': 24, 'creamcheese': 25, 'jelly': 26, 'butter': 27}
prices = [2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00]
class PreferenceForm(forms.Form):
    highPrice = forms.CharField(label="Price Range", max_length = 4)
    highCal = forms.CharField(label="Calorie Range", max_length=3)
    ingredient = forms.CharField(label="Preffered Ingredient", max_length = 20)