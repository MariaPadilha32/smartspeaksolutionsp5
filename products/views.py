from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request,'base.html')

def eulogy(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        event_date = request.POST.get('event_date')
        speech_length = request.POST.get('speech_length')
        preference_narrative = request.POST.get('preference_narrative')
        relationship = request.POST.get('relationship')
        mentions = request.POST.get('mentions')
        thanks = request.POST.get('thanks')
        additonal_preferences = request.POST.get('additonal_preferences')
        dos_donts = request.POST.get('dos_donts')
        attendees = request.POST.get('attendees')
        ages = request.POST.get('ages')
        tone_emotional = request.POST.get('tone_emotional')
        tone_heartfelt = request.POST.get('tone_heartfelt')
        tone_inspirational = request.POST.get('tone_inspirational')
        tone_sad = request.POST.get('tone_sad')
        tone_happy = request.POST.get('tone_happy')
        tone_funny = request.POST.get('tone_funny')
        tone_formal = request.POST.get('tone_formal')
        tone_casual = request.POST.get('tone_casual')
        tone_motivational = request.POST.get('tone_motivational')
        tone_reflective = request.POST.get('tone_reflective')
        tone_others = request.POST.get('tone_others')
        user_input = request.POST.get('user_input')

        return HttpResponse('Form submitted successfully!')
    else:
        # Handle GET request or invalid form submission
        return HttpResponse('Invalid request!')


def vows(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        partner-name = request.POST.get('partner_name')
        wedding-date = request.POST.get('wedding_date')
        speech_length = request.POST.get('speech_length')
        history = request.POST.get('history')
        dos_donts = request.POST.get('dos_donts')
        attendees = request.POST.get('attendees')
        ages = request.POST.get('ages')
        tone_emotional = request.POST.get('tone_emotional')
        tone_heartfelt = request.POST.get('tone_heartfelt')
        tone_inspirational = request.POST.get('tone_inspirational')
        tone_sad = request.POST.get('tone_sad')
        tone_happy = request.POST.get('tone_happy')
        tone_funny = request.POST.get('tone_funny')
        tone_formal = request.POST.get('tone_formal')
        tone_casual = request.POST.get('tone_casual')
        tone_motivational = request.POST.get('tone_motivational')
        tone_reflective = request.POST.get('tone_reflective')
        tone_others = request.POST.get('tone_others')
        user_input = request.POST.get('user_input')

        return HttpResponse('Form submitted successfully!')
    else:
        # Handle GET request or invalid form submission
        return HttpResponse('Invalid request!')


def spouse(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        partner-name = request.POST.get('partner_name')
        wedding-date = request.POST.get('wedding_date')
        speech_length = request.POST.get('speech_length')
        history = request.POST.get('history')
        mentions = request.POST.get('mentions')
        thanks = request.POST.get('thanks')
        additonal_preferences = request.POST.get('additonal_preferences')
        dos_donts = request.POST.get('dos_donts')
        attendees = request.POST.get('attendees')
        ages = request.POST.get('ages')
        tone_emotional = request.POST.get('tone_emotional')
        tone_heartfelt = request.POST.get('tone_heartfelt')
        tone_inspirational = request.POST.get('tone_inspirational')
        tone_happy = request.POST.get('tone_happy')
        tone_funny = request.POST.get('tone_funny')
        tone_formal = request.POST.get('tone_formal')
        tone_casual = request.POST.get('tone_casual')
        tone_motivational = request.POST.get('tone_motivational')
        tone_reflective = request.POST.get('tone_reflective')
        tone_others = request.POST.get('tone_others')
        user_input = request.POST.get('user_input')

        return HttpResponse('Form submitted successfully!')
    else:
        # Handle GET request or invalid form submission
        return HttpResponse('Invalid request!')


def spouse(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        name = request.POST.get('name')
        related = request.POST.get('related')
        relationship = request.POST.get('relationship')
        couple_name = request.POST.get('couple_name')
        wedding-date = request.POST.get('wedding_date')
        speech_length = request.POST.get('speech_length')
        history = request.POST.get('history')
        mentions = request.POST.get('mentions')
        thanks = request.POST.get('thanks')
        additonal_preferences = request.POST.get('additonal_preferences')
        dos_donts = request.POST.get('dos_donts')
        attendees = request.POST.get('attendees')
        ages = request.POST.get('ages')
        tone_emotional = request.POST.get('tone_emotional')
        tone_heartfelt = request.POST.get('tone_heartfelt')
        tone_inspirational = request.POST.get('tone_inspirational')
        tone_happy = request.POST.get('tone_happy')
        tone_funny = request.POST.get('tone_funny')
        tone_formal = request.POST.get('tone_formal')
        tone_casual = request.POST.get('tone_casual')
        tone_motivational = request.POST.get('tone_motivational')
        tone_reflective = request.POST.get('tone_reflective')
        tone_others = request.POST.get('tone_others')
        user_input = request.POST.get('user_input')

        return HttpResponse('Form submitted successfully!')
    else:
        # Handle GET request or invalid form submission
        return HttpResponse('Invalid request!')