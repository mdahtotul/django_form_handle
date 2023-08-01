from django import forms
from django.core import validators


class ContactForm(forms.Form):
    CHOICES = [("S", "Small"), ("M", "Medium"), ("L", "Large")]
    PIZZA_TYPE = [("P", "Pepperoni"), ("M", "Mashroom"), ("B", "Beef")]

    name = forms.CharField(
        label="User Name",
        initial="e.g: John Doe",
        help_text="Total length must be within 3 to 25 characters",
    )
    email = forms.EmailField(label="User Email")
    age = forms.IntegerField(label="Age", min_value=1)
    weight = forms.FloatField(label="Weight", min_value=1)
    balance = forms.DecimalField(label="Balance", min_value=0, required=False)
    bod = forms.DateField(
        label="Birthday",
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
    )
    appointment = forms.DateTimeField(
        label="Appointment",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
    )
    check = forms.BooleanField(label="Agree", required=False)
    shape = forms.ChoiceField(label="Shape", choices=CHOICES)
    size = forms.ChoiceField(label="Size", choices=CHOICES, widget=forms.RadioSelect)
    pizza = forms.MultipleChoiceField(
        label="Pizza",
        choices=PIZZA_TYPE,
        widget=forms.CheckboxSelectMultiple,
    )
    comment = forms.CharField(
        label="Comment",
        max_length=300,
        help_text="Maximum 300 characters",
        required=False,
        widget=forms.Textarea(
            attrs={
                "id": "comment",
                "class": "form-control text-danger text-bold",
                "placeholder": "Write some comment here...",
            }
        ),
    )


# for file upload
# class ContactForm(forms.Form):
#     name = forms.CharField(label="User Name")
#     file = forms.FileField(label="Upload File")

# with custom validation
# class StudentData(forms.Form):
#     name = forms.CharField(
#         label="Name", widget=forms.TextInput(attrs={"class": "form-control"})
#     )
#     email = forms.CharField(
#         label="Email", widget=forms.EmailInput(attrs={"class": "form-control"})
#     )

#     def clean(self):
#         cleaned_data = super().clean()
#         val_name = self.cleaned_data["name"]
#         val_email = self.cleaned_data["email"]
#         if len(val_name) < 10:
#             raise forms.ValidationError("Name must be at least 10 characters long")

#         if ".com" not in val_email:
#             raise forms.ValidationError("Email must contain .com")


# with django.core validators
class StudentData(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[
            validators.MinLengthValidator(3, "Name must be at least 3 characters long"),
            validators.MaxLengthValidator(
                25, "Maximum length must be at most 25 characters long"
            ),
        ],
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        validators=[validators.EmailValidator("Enter a valid email")],
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        validators=[
            validators.MinValueValidator(1, "Age must be at least 1"),
            validators.MaxValueValidator(100, "Age must be at most 100"),
        ],
    )
    cv_upload = forms.FileField(
        label="Upload CV",
        validators=[
            validators.FileExtensionValidator(
                allowed_extensions=["pdf", "doc", "docx"],
                message="Only pdf and doc files are allowed",
            )
        ],
        required=False,
    )


class PasswordValidation(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[
            validators.MinLengthValidator(3, "Name must be at least 3 characters long"),
            validators.MaxLengthValidator(
                25, "Maximum length must be at most 25 characters long"
            ),
        ],
    )
    new_pass = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        validators=[
            validators.MinLengthValidator(
                6, "Password must be at least 6 characters long"
            )
        ],
    )
    confirm_pass = forms.CharField(
        label="Confirm-Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        validators=[
            validators.MinLengthValidator(
                6, "Confirm Password must be at least 6 characters long"
            )
        ],
    )

    def clean(self):
        cleaned_data = super().clean()
        val_new_pass = cleaned_data.get("new_pass")
        val_confirm_pass = cleaned_data.get("confirm_pass")

        if (val_new_pass and val_confirm_pass) and (val_new_pass != val_confirm_pass):
            msg = "New Password and Confirm Password must be same"
            self.add_error("confirm_pass", msg)
