from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import SystemSettings
from .forms import EditSettingForm


@user_passes_test(lambda u: u.is_superuser)
def setting_list(request):
    search_query = request.GET.get('search')

    settings = SystemSettings.objects.all()

    if search_query:
        settings = settings.filter(Q(key__icontains=search_query) | Q(description__icontains=search_query))

    return render(request, 'setting_list.html', {'settings': settings, 'search_query': search_query})


@user_passes_test(lambda u: u.is_superuser)
def setting_card(request, setting_id):
    setting = get_object_or_404(SystemSettings, id=setting_id)
    return render(request, 'setting_card.html', {'setting': setting})


@user_passes_test(lambda u: u.is_superuser)
def edit_setting(request, setting_id):
    setting = get_object_or_404(SystemSettings, id=setting_id)
    form = EditSettingForm(instance=setting)

    if request.method == 'POST':
        form = EditSettingForm(request.POST, instance=setting)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('setting_card', args=[setting_id]))

    return render(request, 'edit_setting.html', {'form': form, 'setting_id': setting_id, 'key': setting.key})
