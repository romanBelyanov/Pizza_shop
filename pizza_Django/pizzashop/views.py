from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import Menu

def index(request):
    return render(request, 'users/index.html')
def menu(request):
    if request.user.username != None:
        context = {"is_login": True, "login": request.user.username}
    else:
        context = {"is_login": False}
    return render(request, 'pizzashop/menu.html', context)

def basket(request):
    context = {"dish1": False, "dish2": False, "dish3": False, "dish4": False, "dish5": False, "dish6": False}
    if request.user.username != None:
        context["is_login"] = True
    else:
        context["is_login"] = False
    basket_ = request.session.get('basket', {})
    print(basket_)
    for i in list(basket_.keys()):
        context[f"dish{i}"] = True
        menu = Menu.objects.get(id=i)
        context[f"name{i}"] = menu.name
        context[f"about{i}"] = menu.description
        context[f"price{i}"] = menu.price
        context[f"amount{i}"] = basket_[i]
    return render(request, "pizzashop/basket.html", context)


@login_required
def add_to_basket(request, product_id):
    product_id = str(product_id)
    basket = request.session.get('basket', {})
    basket[product_id] = basket.get(product_id, 0) + 1
    request.session['basket'] = basket
    print(basket)

    return redirect('/menu')