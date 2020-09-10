from django.shortcuts import render
from django.http import Http404
from .models import Pet
from .models import User
from .forms import PetForm
from .forms import UserForm

def home(request):
    if 'logged_in' in request.session.keys():
        if not request.session['logged_in']:
            user_form = UserForm()
            return render(request, 'sign_in.html', {'form': user_form, 'note': 'Please login first'})
    pets = Pet.objects.all()
    print(request.session['user'])
    return render(request, 'home.html', {
        "pets": pets,
    })

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id = pet_id)
    except: 
        raise Http404('pet object not found')
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })

def add_new_pet(request):
    if(request.method == "POST"):
        filled_form = PetForm(request.POST)
        print(filled_form.errors)
        if(filled_form.is_valid()):
            filled_form.save()
            note = "Thank you, %s for adding %s" %(filled_form.cleaned_data['submitter'], filled_form.cleaned_data['name']) 
            new_form = PetForm()
            return render(request, 'add_new_pet.html', {
                'petform': new_form,
                'note': note
            })
        else:
            new_form = PetForm()
            return render(request, 'add_new_pet.html', {
                'petform': new_form,
                'note': "there was some error"
            })
    else:
        form = PetForm()
        return render(request, 'add_new_pet.html', {
            'petform': form
        })

def edit_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    pets = Pet.objects.all()
    if(request.method=="POST"):
        filled_form = PetForm(request.POST, instance=pet)
        if(filled_form.is_valid()):
            filled_form.save()
            return render(request, 'home.html', {
                'pet_id': pet_id,
                'pets': pets
            })
        else:
            filled_form = PetForm(instance = pet)
            return render(request, 'edit_pet.html', {
                'filled_form': filled_form,
                'pet_id': pet_id,
            })
    else:
        filled_form = PetForm(instance=pet)
        return render(request, 'edit_pet.html', {
            'filled_form': filled_form,
            'pet_id': pet_id,
        })

def sign_up(request):
    if request.method == "POST" :
        filled_form = UserForm(request.POST)
        if filled_form.is_valid():
            try:
                user = User.objects.get(email=filled_form.cleaned_data.get("email"))
                user_form = UserForm()
                return render(request, 'sign_up.html', {'form': user_form, 'note': 'user already exists'})
            except User.DoesNotExist:
                filled_form.save()
                user_form = UserForm()
                return render(request, 'sign_in.html', {'form': user_form, 'note': 'Login to proceed'})
    else:
        user_form = UserForm()
        return render(request, 'sign_up.html', {'form': user_form})

def sign_in(request):
    user_form = UserForm()
    if request.method == "POST":
        try: 
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['logged_in'] = True
            pets = Pet.objects.all()
            return render(request, 'home.html', {'pets': pets})
        except User.DoesNotExist:
            request.session['logged_in'] = False
            return render(request, 'sign_in.html', {'form': user_form, 'note': 'please try again'})
    else:
        if 'logged_in' in request.session.keys():
            if request.session['logged_in']:
                pets = Pet.objects.all()
                return render(request, 'home.html', {'pets': pets})
        return render(request, 'sign_in.html', {'form': user_form})

def sign_out(request):
    if 'logged_in' in request.session.keys():
        if request.session['logged_in']:
            request.session['logged_in'] = False
    user_form = UserForm()
    return render(request, 'sign_in.html', {'form': user_form })