from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse


# Create your views here.
def view_index(request):
    return render(request,'index.html')

#get请求
class BookListView(View):
    #*args : 所有的未知参数 ； **kwargs：所有的关键字参数
    def get(self,request,*args,**kwargs):
        return HttpResponse('booklistview')

#post请求
class AddBookView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'add_book.html')

    def post(self, request, *args, **kwargs):
        bookName=request.POST.get('name')
        bookAuthor=request.POST.get('author')
        print('name:{},author:{}'.format(bookName,bookAuthor))
        return HttpResponse('sucess')

class BookDetail(View):
    def get(self,request,book_name):
        print('bookname: %s' % book_name)
        return HttpResponse('Sucess')

    def http_method_not_allowed(self, request, *args, **kwargs):
        HttpResponse('不支持除get以外的其他请求')

class view_About(TemplateView):
    # 存储模版路径
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
       context = {'phone': '021-88888888'}
       return context  #将context 返回给 about.html
