from django.shortcuts import get_object_or_404, render
from .models import Realm

# Create your views here.
def dummy(request):
    return render(request, 'dnd_realm/realm.html')

def realm(request, realm_id):
    realm = get_object_or_404(Realm, pk=realm_id)
    return render(request, 'dnd_realm/realm.html', { 'realm': realm })
