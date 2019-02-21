from django.shortcuts import render
from bug.models import Bug
from apitest.models import Single_interface,Enveronment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def bug_manage(request):
    username=request.session.get('user','')
    bug_list=Bug.objects.all()
    bug_count = Bug.objects.all().count()  # 统计模块数
    paginator = Paginator(bug_list, 10)  # 生成paginator对象，设置每页显示10条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认未第一页
    currentPage = int(page)  # 把获取到的当前页面数转换成整数类型
    try:
        bug_list = paginator.page(page)  # 获取当前页码的记录列表
    except  PageNotAnInteger:
        bug_list = paginator.page(1)  # 如果输入的页码不是整数则显示第一页内容
    except EmptyPage:
        bug_list = paginator.page(paginator.num_pages)
    return render(request,'bug_manage.html',{'user':username,'bugs':bug_list,'bugcounts':bug_count})
