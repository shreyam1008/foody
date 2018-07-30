from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def aa():
    pass

@csrf_exempt
def test_func(request):

    if request.method =="GET":
        return JsonResponse({"hello there": "general kenobi"})
    elif request.method == 'POST':
        a = request.POST
        print(a.get("email"))

    return HttpResponseRedirect("")

