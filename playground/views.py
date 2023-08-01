from django.shortcuts import render
from .forms import ContactForm, StudentData, PasswordValidation


# Create your views here.
def init_playground(req):
    print(req.POST)

    if req.method == "POST":
        user_email = req.POST.get("user_email")
        user_pass = req.POST.get("user_pass")
        car_brand = req.POST.get("car_brand")
        return render(
            req,
            "playground.html",
            {"user_email": user_email, "user_pass": user_pass, "car_brand": car_brand},
        )
    else:
        return render(req, "playground.html")


def submit_form(req):
    # print(req.POST)

    # if req.method == "POST":
    #     user_email = req.POST.get("user_email")
    #     user_pass = req.POST.get("user_pass")
    #     return render(
    #         req, "form.html", {"user_email": user_email, "user_pass": user_pass}
    #     )
    # else:
    return render(req, "form.html")


# normal approach
def django_form(req):
    if req.method == "POST":
        form = ContactForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)

        return render(req, "django_form.html", {"form": form})
    else:
        form = ContactForm()
        return render(req, "django_form.html", {"form": form})


# best approach
# def django_form(req):
#     if req.method == "POST":
#         form = ContactForm(req.POST, req.FILES)
#         if form.is_valid():
#             new_file = form.cleaned_data["file"]  # get file from form
#             with open("./playground/uploads/" + new_file.name, "wb+") as destination:
#                 for chunk in new_file.chunks():
#                     destination.write(chunk)
#             print(form.cleaned_data)

#             return render(req, "django_form.html", {"form": form})
#     else:
#         form = ContactForm()
#         return render(req, "django_form.html", {"form": form})


def student_form(req):
    if req.method == "POST":
        form = StudentData(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)

        return render(req, "django_form.html", {"form": form})
    else:
        form = StudentData()
        return render(req, "django_form.html", {"form": form})


def validate_pass(req):
    if req.method == "POST":
        form = PasswordValidation(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)

        return render(req, "django_form.html", {"form": form})
    else:
        form = PasswordValidation()
        return render(req, "django_form.html", {"form": form})
