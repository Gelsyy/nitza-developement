import os
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    HttpResponseRedirect)
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import permission_required, login_required

from .forms import (
    UserProfileForm,
    UserCreateForm,
    AssociatedCreateForm,
    UserUpdateForm,
)

from .models import (
    User,
    UserProfile,
    Associated,
)


@permission_required('auth.user.can_add_user')
def create_user(request):
    form = UserProfileForm()
    userCform = UserCreateForm()
    if request.method == 'POST':
        userCform = UserCreateForm(request.POST)
        if userCform.is_valid():
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                username = userCform.cleaned_data['username']
                password = userCform.cleaned_data['password1']
                firstname = userCform.cleaned_data['first_name']
                lastname = userCform.cleaned_data['last_name']
                email = userCform.cleaned_data['email']
                role = form.cleaned_data['role']
                phone_number = form.cleaned_data['phone_number']
                avatar = form.cleaned_data['avatar']
                user = User.objects.create_user(username=username,
                                                first_name=firstname,
                                                last_name=lastname,
                                                password=password,
                                                email=email)
                UserProfile.objects.create(user=user,
                                           role=role,
                                           avatar=avatar,
                                           phone_number=phone_number)
                return redirect('list-user')
    context = {
        'form': form,
        'user_form': userCform
    }
    return render(request, 'users/user_create.html', context)


@permission_required('auth.user.can_add_user')
def update_user(request, id):
    # fetch the object related to passed id
    profile = get_object_or_404(UserProfile, id=id)

    if profile.avatar:
        path = profile.avatar.path

    form = UserProfileForm(instance=profile)
    userCform = UserUpdateForm(instance=profile.user)

    if request.method == 'POST':
        userCform = UserUpdateForm(request.POST, instance=profile.user)
        if userCform.is_valid():
            form = UserProfileForm(
                request.POST, request.FILES, instance=profile)
            # save the data from the form and
            # redirect to detail_view
            if form.is_valid():
                if len(request.FILES) > 0:
                    try:
                        profile.avatar.storage.delete(path)
                    except Exception as error:
                        print(error)
                profile.user.save()
                profile.save()
                return redirect('list-user')

    # add form dictionary to context
    context = {
        'form': form,
        'user_form': userCform
    }

    return render(request, 'users/user_update.html', context)


@permission_required('auth.user.can_add_user')
def list_user(request):
    profiles = UserProfile.objects.exclude(id=request.user.profile_user.id)
    print(profiles)
    return render(request, 'users/user_list.html', {'profiles': profiles})


@permission_required('auth.user.can_add_user')
def delete_user(request, id):
    # fetch the object related to passed id
    profile = get_object_or_404(UserProfile, id=id)
    try:
        profile.avatar.storage.delete(profile.avatar.path)
    except Exception as error:
        print(error)
    profile.user.delete()  # Profile is deleted by cascade behavior
    return redirect('list-user')


# -------------------- Associated ----------------------------

@login_required
def create_provider(request):
    return create_associated(request, 'provider')


@login_required
def create_client(request):
    return create_associated(request, 'client')


def create_associated(request, type):
    initial = {'type': type}
    form = AssociatedCreateForm(initial=initial)
    next = request.GET.get('next', 'list-{}'.format(type))
    if request.method == 'POST':
        form = AssociatedCreateForm(request.POST, request.FILES)
        if form.is_valid():
            associated = form.save()
            request.session['associated_id'] = associated.id
            return redirect(next)
    context = {
        'form': form
    }
    return render(request, 'users/associated_create.html', context)


@login_required
def update_associated(request, id):
    # fetch the object related to passed id
    associated = get_object_or_404(Associated, id=id)
    if associated.avatar:
        path = associated.avatar.path
    # pass the object as instance in form
    form = AssociatedCreateForm(instance=associated)

    if request.method == 'POST':
        # pass the object as instance in form
        form = AssociatedCreateForm(
            request.POST, request.FILES, instance=associated)

        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            if len(request.FILES) > 0:
                try:
                    associated.avatar.storage.delete(path)
                except Exception as error:
                    print(error)
            form.save()
            if associated.type == 'client':
                return redirect('list-client')
            if associated.type == 'provider':
                return redirect('list-provider')

    # add form dictionary to context
    context = {
        'form': form
    }

    return render(request, 'users/associated_update.html', context)


@login_required
def list_provider(request):
    return list_associated(request, 'provider')


@login_required
def list_client(request):
    return list_associated(request, 'client')


@login_required
def detail_associated(request, id):
    # fetch the object related to passed id
    associated = get_object_or_404(Associated, id=id)
    return render(request, 'users/associated_detail.html', {'associated': associated,
                                                            'title': 'Associated detail'})


def list_associated(request, type):
    associateds = Associated.objects.filter(type=type)
    return render(request, 'users/associated_list.html', {'associateds': associateds,
                                                          'type': type})


@login_required
def delete_associated(request, id):
    # fetch the object related to passed id
    associated = get_object_or_404(Associated, id=id)
    try:
        associated.avatar.storage.delete(associated.avatar.path)
    except Exception as error:
        print(error)
    associated.delete()
    return redirect('list-{}'.format(associated.type))
