from django.shortcuts import render
from django.http import Http404
from .models import Pet
from .forms import PetForm

def home(request):
    pets = Pet.objects.all()
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
