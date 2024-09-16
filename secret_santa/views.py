from django.shortcuts import redirect, render
from secret_santa.form_names import ParticipantForm
from secret_santa.game_utils import generate_pairs

def get_participants(request):
    return request.session.get("participants", [])

def set_participants(request, participants):
    """saving"""
    request.session["participants"] = participants
    request.session.modified = True

def handle_add_participant(request, participants):
    """handle adding participant"""
    form = ParticipantForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        participants.append(name)
        set_participants(request, participants)
        return redirect("secret-santa")
    else:
        return render(request, "santa.html", {
            "form": form,
            "participants": participants,
            "pairs": None
        })

def handle_generate_pairs(request, participants):
    """handle generating couples"""
    if len(participants) > 1:
        pairs = generate_pairs(participants)
        return render(request, "santa.html", {
            "form": ParticipantForm(),
            "participants": participants,
            "pairs": pairs
        })
    else:
        error_message = "Minimum 2 players required."
        return render(request, "santa.html", {
            "form": ParticipantForm(),
            "participants": participants,
            "pairs": None,
            "error_message": error_message
        })

def handle_reset(request):
    """handle reseting"""
    set_participants(request, [])
    return redirect("secret-santa")

def handle_go_back(request):
    """handle back"""
    set_participants(request, [])
    return redirect("homepage")

def secret_santa(request):
    participants = get_participants(request)
    pairs = None

    if request.method == "POST":
        if "add" in request.POST:
            return handle_add_participant(request, participants)
        elif "generate" in request.POST:
            return handle_generate_pairs(request, participants)
        elif "reset" in request.POST:
            return handle_reset(request)
        elif "go-back" in request.POST:
            return handle_go_back(request)
    else:
        form = ParticipantForm()

    return render(request, "santa.html", {
        "form": form,
        "participants": participants,
        "pairs": pairs
    })
