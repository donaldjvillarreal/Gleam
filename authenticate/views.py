# coding=utf-8
from authenticate.forms import UserForm, UserProfileForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from authenticate.models import User, UserProfile
from diagnostic.models import SurveySet


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Check if surveySet exists under their session id
            if request.session.exists(request.session.session_key):
                survey_set = SurveySet.objects.filter(session=request.session.session_key)
                if survey_set.exists():
                    survey_set = survey_set.first()
                    survey_set.user = user
                    survey_set.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            username = request.POST['username']
            password = request.POST['password']
            userlogin = authenticate(username=username, password=password)
            login(request, userlogin)

            return HttpResponseRedirect(request.GET.get('next', reverse('authenticate:login')))

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'authenticate/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Gleam account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'authenticate/login.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')


def profile(request, user_id):
    user_ob = User.objects.get(id=user_id)
    user = UserProfile.objects.get(user=user_ob)
    return render(request, 'authenticate/profile.html', {'user': user})
