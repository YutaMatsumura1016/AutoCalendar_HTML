from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from src import main

class IndexView(TemplateView):
    template_name = 'AutoCalApp/index.html'
class response:
    res = "null"

def formView(request):
    if request.method == 'POST':
        data = request.POST.get('input_data')
        id = request.POST.get('input_id')
        main.id = id
        if data == "null":
            response.res == "0"
        else:

            response.res = main.yoteiAuto(data)
        return HttpResponseRedirect(reverse('resultView'))
    else:
        response.res == "エラーが発生しました。再度実行してください。"
        return render(request, 'AutoCalApp/index.html')

def resultView(request):
    r=str(response.res)
    if r.isdigit():
        if int(r)==0:
            context = {'message': "登録できる予定がありませんでした。"}
        elif int(r)>0:
            context = {'message': "予定の登録が完了しました。登録件数："+r+"件"}
        else:
            context = {'message': r}
    else:
        context = {'message': r}
    return render(request, 'AutoCalApp/result.html', context)

def topView(request):
    return render(request, 'AutoCalApp/index.html')
