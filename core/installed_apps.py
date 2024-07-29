from django.contrib import messages

INSTALLEDAPPS = [
    'corsheaders', 
    'users',
    'elixir_of_links',
    'meteoromancers_forecast',
    'philosophers_stone_extractor',
    'chronomancers_timer',
    'transmutation_engine',
    "frontend"
]

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
