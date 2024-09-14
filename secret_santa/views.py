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
                request.session["participants"] = participants
                return redirect("secret-santa")
            else:
                return render(
                    request,
                    "santa.html",
                    {"form": form, "participants": participants, "pairs": pairs},
                )

        elif "generate" in request.POST:
            if len(participants) % 2 == 0:
                pairs = generate_pairs(participants)
            else:
                form = ParticipantForm()
                pairs = None
                error_message = "the number of players must be even"
                return render(
                    request,
                    "santa.html",
                    {
                        "form": form,
                        "participants": participants,
                        "pairs": pairs,
                        "error_message": error_message,
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
