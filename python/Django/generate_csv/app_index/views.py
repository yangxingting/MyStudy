from django.http import HttpResponse,StreamingHttpResponse
import csv
from django.template import loader


# Create your views here.
def view_index(request):

    response=HttpResponse(content_type='text/csv')
    # Content-Disposition ：告诉浏览器如何处理这个文件; attachent：文件作为附件形式下载 ; filename：文件名
    response['Content-Disposition']="attachent;filename=userlist.csv"
    writer=csv.writer(response)
    writer.writerow(['username','age'])
    writer.writerow(['zhangsan','18'])
    writer.writerow(['linxiaomeng','19'])

    return response

#将csv文件定义为一个模板
def view_template_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachent;filename=userlist.csv"
    myContext= {
        'rows':[
            ['username','age'],
            ['zhangsan','18'],
            ['linxiaomeng','19'],
        ]
    }

    #获取模板
    template=loader.get_template('namelist.txt')
    #将数据传入到模板中
    csv_template=template.render(myContext)
    #将模版添加到response中
    response.content=csv_template

    return response

def view_large_csv(request):
    response = StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachent;filename=data.csv"

    # response.streaming_content=('username,age\n','zhangsan,18\n')
    rows=("name{},{}\n".format(row,row) for row in range(0,2000))

    response.streaming_content=rows
    return response
