from django.shortcuts import redirect, render

from secret_santa.form_names import ParticipantForm
from secret_santa.game_utils import generate_pairs


def secret_santa(request):
    if "participants" not in request.session:
        request.session["participants"] = []

    participants = request.session["participants"]
    pairs = None
    form = ParticipantForm()

    if request.method == "POST":
        form = ParticipantForm(request.POST)

        if "add" in request.POST:
            if form.is_valid():
                name = form.cleaned_data["name"]
                participants.append(name)
                request.session.modified = True
                request.session["participants"] = participants
                return redirect("secret-santa")
            else:
                data = {"form": form, "participants": participants, "pairs": pairs}
                return render(request, "santa.html", data)

        elif "generate" in request.POST:
            if len(participants) > 1:
                pairs = generate_pairs(participants)
            else:
                form = ParticipantForm()
                pairs = None
                error_message = "minimum 2 players"
                data = {
                    "form": form,
                    "participants": participants,
                    "pairs": pairs,
                    "error_message": error_message,
                }
                return render(request, "santa.html", data)
            return render(
                request,
                "santa.html",
                {
                    "form": ParticipantForm(),
                    "participants": participants,
                    "pairs": pairs,
                },
            )
        elif "reset" in request.POST:
            request.session["participants"] = []
            return redirect("secret-santa")
        elif "go-back" in request.POST:
            request.session["participants"] = []
            return redirect("homepage")

    else:
        form = ParticipantForm()

    return render(
        request,
        "santa.html",
        {"form": form, "participants": participants, "pairs": pairs},
    )
