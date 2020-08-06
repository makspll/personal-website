from django.conf import settings

def debug_mode_processor(request):
    debug_flag = settings.DEBUG

    return{"debug_flag":debug_flag}