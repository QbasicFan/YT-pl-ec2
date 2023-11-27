from django.shortcuts import render
# Create your views here.
from .models import bookMark, catego
from .forms import bookMarkForm, categoForm



def ytpList(request):

   cat = catego.objects.all()
   book = bookMark.objects.all()




   love = book.filter(cate__title = "From Love").order_by('-id')
   hip = book.filter(cate__title = "Hip Hop").order_by('-id')
   rap = book.filter(cate__title = "Rap Francais").order_by('-id')
   elec = book.filter(cate__title = "Electro").order_by('-id')
   alb = book.filter(cate__title = "Albums").order_by('-id')
   wesh = book.filter(cate__title = "Wesh").order_by('-id')
   mov = book.filter(cate__title = "Movies").order_by('-id')
   doc = book.filter(cate__title = "Documentaries").order_by('-id')

   form = bookMarkForm()
   form1 = categoForm()






   content ={
      "love":love,
      "hip":hip,
      "rap":rap,
      "elec":elec,
      "alb":alb,
      "wesh":wesh,
      "mov":mov,
      "doc":doc,

      "cat":cat,
      "book":book,

      "form":form,
      "form1":form1,

      }

   if request.method == 'POST':
        form = bookMarkForm(request.POST)
        form1 = categoForm(request.POST)


        if form.is_valid():
            form.save()
            return render(request, 'bff/ytpList.html', content)

        elif form1.is_valid():
            form1.save()
            return render(request, 'bff/ytpList.html', content)            
        else:
            return render(request, 'bff/error.html', content)



   return render(request, 'bff/ytpList.html', content )


