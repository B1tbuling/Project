from django.shortcuts import redirect


def go_to_post(request):
    return redirect('blog/')