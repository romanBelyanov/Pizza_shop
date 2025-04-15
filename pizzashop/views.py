from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import *

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
        context["login"] = request.user.username
    else:
        context["is_login"] = False
    basket_ = request.session.get('basket', {})
    summ = 0
    for i in list(basket_.keys()):
        context[f"dish{i}"] = True
        menu = Menu.objects.get(id=i)
        context[f"name{i}"] = menu.name
        context[f"about{i}"] = menu.description
        context[f"price{i}"] = menu.price
        context[f"amount{i}"] = basket_[i]
        summ += menu.price * basket_[i]
    context["summ"] = summ
    return render(request, "pizzashop/basket.html", context)


@login_required
def add_to_basket(request, product_id):
    product_id = str(product_id)
    basket = request.session.get('basket', {})
    basket[product_id] = basket.get(product_id, 0) + 1
    request.session['basket'] = basket

    return redirect('/menu')

@login_required
def add_to_basket1(request, product_id):
    context = {}
    product_id = str(product_id)
    basket = request.session.get('basket', {})
    basket[product_id] = basket.get(product_id, 0) + 1
    request.session['basket'] = basket
    print(basket)
    summ = 0
    for i in list(basket.keys()):
        menu = Menu.objects.get(id=i)
        summ += menu.price * basket[i]
    context["summ"] = summ

    return redirect('/basket', context)

def delete_from_basket(request, product_id):
    context = {}
    product_id = str(product_id)
    basket = request.session.get('basket', {})
    if basket.get(product_id, 0) == 0:
        return None
    basket[product_id] = basket.get(product_id, 0) - 1
    new_basket = {}
    for i in basket.keys():
        if basket[i] != 0:
            new_basket[i] = basket[i]
    basket = new_basket
    request.session['basket'] = basket
    print(basket)

    summ = 0
    for i in list(basket.keys()):
        menu = Menu.objects.get(id=i)
        summ += menu.price * basket[i]
    context["summ"] = summ
    return redirect('/basket', context)

def do_order(request):
    basket = request.session.get('basket', {})
    print(basket)
    salyami = 0
    tomato_sauce = 0
    cheese = 0
    species = 0
    bazilik = 0
    ham = 0
    ananas = 0
    for i in list(basket.keys()):
        menu = Menu.objects.get(id=i)
        salyami += int(menu.salyami) * basket[i]
        tomato_sauce += int(menu.tomato_sauce) * basket[i]
        cheese += int(menu.cheese) * basket[i]
        species += int(menu.species) * basket[i]
        bazilik += int(menu.bazilik) * basket[i]
        ham += int(menu.ham) * basket[i]
        ananas += int(menu.ananas) * basket[i]
    ava = Availability.objects.get(id=1)
    if ava.salyami - salyami < 0 or ava.tomato_sauce - tomato_sauce < 0 or ava.cheese - cheese < 0 or ava.species - species < 0 or ava.bazilik - bazilik < 0 or ava.ham - ham < 0 or ava.ananas - ananas < 0:
        return render(request, "pizzashop/order.html", {'no_ingridients': True, "login": request.user.username, "is_login": True})
    ava.salyami = ava.salyami - salyami
    ava.tomato_sauce = ava.tomato_sauce - tomato_sauce
    ava.cheese = ava.cheese - cheese
    ava.species = ava.species - species
    ava.bazilik = ava.bazilik - bazilik
    ava.ham = ava.ham - ham
    ava.ananas = ava.ananas - ananas
    ava.save()
    context = {"dish1": False, "dish2": False, "dish3": False, "dish4": False, "dish5": False, "dish6": False}
    if request.user.username != None:
        context["is_login"] = True
        context["login"] = request.user.username
    else:
        context["is_login"] = False
    summ = 0
    for i in list(basket.keys()):
        context[f"dish{i}"] = True
        menu = Menu.objects.get(id=i)
        context[f"name{i}"] = menu.name
        context[f"price{i}"] = menu.price
        context[f"amount{i}"] = basket[i]
        context[f"pricep{i}"] = menu.price * basket[i]
        summ += menu.price * basket[i]
    context["summ"] = summ
    Orders.objects.create(user=request.user.username, pepperoni=context.get("amount1", 0), margaret=context.get("amount2", 0), hawaiian=context.get("amount3", 0), Four_cheeses=context.get("amount4", 0))
    request.session['basket'] = {}
    return render(request, "pizzashop/order.html", context)

def new(request):
    context = {}
    if request.user.username != None:
        context["is_login"] = True
        context["login"] = request.user.username
    else:
        context["is_login"] = False
    return render(request, "pizzashop/new.html", context)

def new_order(request):
    class Character:
        def __init__(self):
            self.a = None
            self.b = None
            self.c = None

        def __str__(self):
            return [self.a, self.b, self.c]


    class CharacterBuilder:
        def __init__(self):
            self.character = Character()

        def set_a(self, a):
            self.character.a = a
            return self

        def set_b(self, b):
            self.character.b = b
            return self

        def set_c(self, c):
            self.character.c = c
            return self
        def build(self):
            return self.character  # Возвращаем готовый объект

    dough = request.POST.get("dough")
    insiding = request.POST.get("insiding")
    species = request.POST.get("species")
    print(dough)
    builder = CharacterBuilder()
    text = (builder.set_a(dough)
              .set_b(insiding)
              .set_c(species)
              .build()
              )
    context = {"dough": dough, "insiding": insiding, "species": species}
    if request.user.username != None:
        context["is_login"] = True
        context["login"] = request.user.username
    else:
        context["is_login"] = False
    return render(request, "pizzashop/new_order.html", context)

def about(request):
    context = {}
    if request.user.username != None:
        context["is_login"] = True
        context["login"] = request.user.username
    else:
        context["is_login"] = False
    return render(request, "pizzashop/about.html", context)

def contacts(request):
    context = {}
    if request.user.username != None:
        context["is_login"] = True
        context["login"] = request.user.username
    else:
        context["is_login"] = False
    return render(request, "pizzashop/contacts.html", context)
