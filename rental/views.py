from django.shortcuts import get_object_or_404, render, redirect
from .models import District, Property, PropertyImage


def property_ads(request):
    properties = Property.objects.all()
    districts = District.objects.all()
    # Filtering based on bachelor allowance
    bachelor_allowed = request.GET.get('bachelor_allowed')
    if bachelor_allowed:
        properties = properties.filter(bachelor_allowed=bool(bachelor_allowed))

    # Filtering based on district
    district = request.GET.get('district')
    if district:
        properties = properties.filter(district__name=district)

    context = {
        'properties': properties,
        'districts':districts
    }
    return render(request, 'rentals.html', context)

# Create your views here.
def ad(request):
    return render(request,'index.html')

def create_property(request):
    if request.method == 'POST':
        # Retrieve form data
        district_id = request.POST.get('district')
        detailed_location = request.POST.get('detailed_location')
        title = request.POST.get('title')
        gmail = request.POST.get('gmail')
        phone = request.POST.get('phone')
        rent = request.POST.get('rent')
        negotiable = request.POST.get('negotiable') == '1'  # Updated line
        advance_deposit = request.POST.get('advance_deposit')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        description = request.POST.get('description')
        kitchen = request.POST.get('kitchen') == '1'  # Updated line
        floor_number = request.POST.get('floor_number')
        condition = request.POST.get('condition')
        electricity = request.POST.get('electricity') == '1'  # Updated line
        gas = request.POST.get('gas') == '1'  # Updated line
        wifi = request.POST.get('wifi') == '1'  # Updated line
        elevator = request.POST.get('elevator') == '1'  # Updated line
        security_guard = request.POST.get('security_guard') == '1'  # Updated line
        cctv = request.POST.get('cctv') == '1'  # Updated line
        bachelor_allowed = request.POST.get('bachelor_allowed') == '1'  # Updated line

        district = District.objects.get(id=district_id)
        property = Property.objects.create(
            district=district,
            detailed_location=detailed_location,
            title=title,
            gmail=gmail,
            phone=phone,
            rent=rent,
            negotiable=negotiable,
            advance_deposit=advance_deposit,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            description=description,
            kitchen=kitchen,
            floor_number=floor_number,
            condition=condition,
            electricity=electricity,
            gas=gas,
            wifi=wifi,
            elevator=elevator,
            security_guard=security_guard,
            cctv=cctv,
            bachelor_allowed=bachelor_allowed
        )

        # Handle property images
        images = request.FILES.getlist('images')
        for image in images:
            PropertyImage.objects.create(property=property, image=image)

        return redirect('index')  # Redirect to the property list page

    districts = District.objects.all()
    context = {'districts': districts}
    return render(request, 'create_property.html', context)

def view_single_property(request, slug):
    # Retrieve the property using the slug
    property = get_object_or_404(Property, title_slug=slug)
    # Retrieve property images
    images = PropertyImage.objects.filter(property=property)

    context = {
        'property': property,
        'images': images
    }
    return render(request, 'single_property.html', context)