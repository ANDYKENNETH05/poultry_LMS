from django.shortcuts import render,  redirect, get_object_or_404

# Create your views here.

from .models import Breed, FeedType, MedicationDrug, FeedingRecord


def home(request):
    return render(request, 'home.html')

def breed_list(request):
    breeds = Breed.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        age = request.POST['age']
        weight = request.POST['weight']
        Breed.objects.create(name=name, quantity=quantity, age=age, weight=weight)
        return redirect('breed_list')
    return render(request, 'breed_list.html', {'breeds': breeds})

def breed_update(request, pk):
    breed = get_object_or_404(Breed, pk=pk)
    if request.method == 'POST':
        breed.name = request.POST['name']
        breed.quantity = request.POST['quantity']
        breed.age = request.POST['age']
        breed.weight = request.POST['weight']
        breed.save()
        return redirect('breed_list')
    return render(request, 'breed_form.html', {'breed': breed})

def breed_delete(request, pk):
    breed = get_object_or_404(Breed, pk=pk)
    breed.delete()
    return redirect('breed_list')


# --------------------
# FEEDTYPE
# --------------------
def feedtype_list(request):
    feedtypes = FeedType.objects.all()
    if request.method == 'POST':
        feed_type = request.POST['feed_type']
        quantity = request.POST['quantity']
        unit = request.POST['unit']
        purchase_date = request.POST['purchase_date']
        expiry_date = request.POST['expiry_date']
        FeedType.objects.create(
            feed_type=feed_type,
            quantity=quantity,
            unit=unit,
            purchase_date=purchase_date,
            expiry_date=expiry_date
        )
        return redirect('feedtype_list')
    return render(request, 'feedtype_list.html', {'feedtypes': feedtypes})

def feedtype_update(request, pk):
    feedtype = get_object_or_404(FeedType, pk=pk)
    if request.method == 'POST':
        feedtype.feed_type = request.POST['feed_type']
        feedtype.quantity = request.POST['quantity']
        feedtype.unit = request.POST['unit']
        feedtype.purchase_date = request.POST['purchase_date']
        feedtype.expiry_date = request.POST['expiry_date']
        feedtype.save()
        return redirect('feedtype_list')
    return render(request, 'feedtype_form.html', {'feedtype': feedtype})

def feedtype_delete(request, pk):
    feedtype = get_object_or_404(FeedType, pk=pk)
    feedtype.delete()
    return redirect('feedtype_list')


# --------------------
# MEDICATIONDRUG
# --------------------
def medicationdrug_list(request):
    drugs = MedicationDrug.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        MedicationDrug.objects.create(name=name, description=description)
        return redirect('medicationdrug_list')
    return render(request, 'medicationdrug_list.html', {'drugs': drugs})

def medicationdrug_update(request, pk):
    drug = get_object_or_404(MedicationDrug, pk=pk)
    if request.method == 'POST':
        drug.name = request.POST['name']
        drug.description = request.POST['description']
        drug.save()
        return redirect('medicationdrug_list')
    return render(request, 'medicationdrug_form.html', {'drug': drug})

def medicationdrug_delete(request, pk):
    drug = get_object_or_404(MedicationDrug, pk=pk)
    drug.delete()
    return redirect('medicationdrug_list')


# --------------------
# FEEDINGRECORD
# --------------------
def feedingrecord_list(request):
    records = FeedingRecord.objects.all()
    breeds = Breed.objects.all()
    feedtypes = FeedType.objects.all()
    if request.method == 'POST':
        breed_id = request.POST['breed']
        feedtype_id = request.POST['feed_type']
        date = request.POST['date']
        quantity = request.POST['quantity']
        FeedingRecord.objects.create(
            breed_id=breed_id,
            feed_type_id=feedtype_id,
            date=date,
            quantity=quantity
        )
        return redirect('feedingrecord_list')
    return render(request, 'feedingrecord_list.html', {
        'records': records,
        'breeds': breeds,
        'feedtypes': feedtypes
    })

def feedingrecord_update(request, pk):
    record = get_object_or_404(FeedingRecord, pk=pk)
    breeds = Breed.objects.all()
    feedtypes = FeedType.objects.all()
    if request.method == 'POST':
        record.breed_id = request.POST['breed']
        record.feed_type_id = request.POST['feed_type']
        record.date = request.POST['date']
        record.quantity = request.POST['quantity']
        record.save()
        return redirect('feedingrecord_list')
    return render(request, 'feedingrecord_form.html', {
        'record': record,
        'breeds': breeds,
        'feedtypes': feedtypes
    })

def feedingrecord_delete(request, pk):
    record = get_object_or_404(FeedingRecord, pk=pk)
    record.delete()
    return redirect('feedingrecord_list')
