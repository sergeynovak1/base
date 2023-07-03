from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .enums import Role
from .models import User
from .forms import EditProfileForm, CreateUserForm


@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    role_filter = request.GET.get('role')
    search_query = request.GET.get('search')
    users = User.objects.all()

    if search_query:
        users = users.filter(Q(username__icontains=search_query) | Q(email__icontains=search_query))

    if role_filter:
        users = users.filter(role=role_filter)

    return render(request, 'user_list.html', {'users': users, 'role_filter': role_filter, 'roles': Role.choices, 'search_query': search_query})


@user_passes_test(lambda u: u.is_superuser)
def user_card(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_card.html', {'user': user})


@user_passes_test(lambda u: u.is_superuser)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = EditProfileForm(instance=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('user_card', args=[user_id]))

    return render(request, 'edit_user.html', {'form': form, 'roles': Role.choices, 'user_id': user_id})


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    else:
        return redirect('user_card', user_id=user_id)


@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            role = form.cleaned_data.get('role')

            if role == Role.admin:
                user = User.objects.create_superuser(
                    email=user.email,
                    password=form.cleaned_data.get('password'),
                    username=user.username
                )
            else:
                user = User.objects.create_user(
                    email=user.email,
                    password=form.cleaned_data.get('password'),
                    username=user.username,
                    role=role
                )

            return redirect('user_list')
    return render(request, 'create_user.html', {'form': form})