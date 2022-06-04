"""
Definition of views.
"""
from django.views.generic import ListView
from datetime import datetime
from django.shortcuts import render , redirect
from django.http import HttpRequest
from .models import ADSBInfo, ADSBImg
from django.contrib.auth.decorators import login_required
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger



#主页（展示所有飞机信息的界面）
#@login_required
def home(request):
    #搜索组件
    data_dict = {}
    search_data = request.GET.get('query', "")
    if search_data:
        data_dict["HexID__contains"] = search_data

    adsbinfolist = ADSBInfo.objects.filter(**data_dict).order_by("id")

    #分页组件，Paginator(数据来源,每页显示行数)
    try:
        #获取链接中的page值，这里为了分页显示序号，将链接里面的值转换为int
        current_page  = int(request.GET.get('page', 1))
    except PageNotAnInteger:
        #如果链接中没有page，则为1
        current_page  = 1
    #定义每页显示的数据数量
    per_page = 10
    #计算：当前第几页-1，乘以每页显示数据数量
    #这个值用于：分页显示序号，即第二页显示序号11，第三页显示21
    page_start = (current_page-1) * per_page
    #第二个per_page参数代表每一页显示的数据个数
    p = Paginator(adsbinfolist, per_page, request=request)
    page_list = p.page(current_page )
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'adsbinfolist':adsbinfolist,
            'search_data':search_data,
            'year':datetime.now().year,
            'page_list': page_list,
            'page_start': page_start,
        }
    )


#新增飞机信息页面
@login_required
def add(request):
    errorHexID = ''
    #表单提交使用POST方法
    if request.method == 'POST':
        #获取表单里面的值
        HexID = request.POST.get('HexID')
        Flag = request.POST.get('Flag')
        Callsign = request.POST.get('Callsign')
        Registration = request.POST.get('Registration')
        Type = request.POST.get('Type')


        ADSBinfo_list = ADSBInfo.objects.filter(HexID=HexID)
        try: 
            #get获取img表的此Type
            image = ADSBImg.objects.get(Type=Type)
        except ADSBImg.DoesNotExist:
            #如果get到空值报错的话，把image置为None
            image = None
        #获取图片地址
        img = request.FILES.get('img')

        #如果没有这个机型，就需要在img表里新增这个机型和图片
        if image == None:
                ADSBImgadd = ADSBImg.objects.create(
                Type = Type,
                img = img,
                )
                ADSBImgadd.save()
        #如果有这个机型，但是没有输入图片的话，就跳过这一步(即不保存图片)
        elif img == None:
        #判断图片是否为空，为空的话就不更新图片地址
            pass
        #如果有机型且有图片输入，即可更新图片地址
        else:
            #图片更新使用单独的上传（upload_to）方法，否则会丢失img/路径
            image.img = request.FILES.get('img')
            image.save()

        #这里保存Info表的内容
        #判断HexID是否已存在
        if ADSBinfo_list :
            errorHexID = '出现错误，%s地址码已经存在了' % HexID
            return render(request,'app/add.html',
                            {
                                'errorHexID' : errorHexID,
                                }
                            )
        #判断地址码是否为空，为空时报错
        elif HexID == '' :
            errorHexID = '出现错误，地址码为空'
            return render(request,'app/add.html',
                            {
                                'errorHexID' : errorHexID,
                                }
                            )
        else:
            #HexID不存在且非空的话即可新增Info的数据
            ADSBInfoadd = ADSBInfo.objects.create(
                    HexID = HexID,
                    Flag = Flag,
                    Callsign = Callsign,
                    Registration = Registration,
                    Type = Type,
                    )
            ADSBInfoadd.save()
            #如果新增数据成功，则跳转至主页
            return redirect('/')


    #不提交数据的情况下，就使用GET方法，直接显示add界面
    else:
        return render(
            request,
            'app/add.html',
            {
                'year':datetime.now().year,
            }
        )

#飞机信息详情界面（内含修改数据操作）
@login_required
def detail(request, id):
    errorHexID = ''
    #获取表单里面的值
    HexID = request.POST.get('HexID')
    Flag = request.POST.get('Flag')
    Callsign = request.POST.get('Callsign')
    Registration = request.POST.get('Registration')
    Type = request.POST.get('Type')
    #获取ADSBInfo表里面此id的QuerySet集合
    adsbinfo = ADSBInfo.objects.get(id=id)

    #获取adsbinfo里面的Type字段的值
    ADSBinfo_Type = adsbinfo.Type
    #获取ADSBImg表里面Type的QuerySet，即一个集合，与上文adsbinfo内容格式一样
    try:
        ADSBimg = ADSBImg.objects.get(Type = ADSBinfo_Type)
    except ADSBImg.DoesNotExist:
        ADSBimg = None
    #如果是表单提交，使用的是POST方式，就使用下面的内容
    if request.method == "POST":
        try:
            if HexID == '':
                errorHexID = '修改失败，地址码为空'
                return render(request,'app/detail.html',
                {
                    'adsbinfo': adsbinfo,
                    'ADSBimg': ADSBimg,
                    'errorHexID' : errorHexID,
                    }
                )
            else:
                #使用update方法更新普通数据
                ADSBInfo.objects.filter(id=id).update(HexID=HexID,
                                                    Flag=Flag,
                                                    Callsign=Callsign,
                                                    Registration=Registration,
                                                    Type=Type,
                                                    )
                #图片更新使用单独的上传（upload_to）方法，否则会丢失img/路径
                image = ADSBInfo.objects.get(id=id)
                #获取图片地址
                image.img = request.FILES.get('img')
                #判断图片是否为空，为空的话就不更新图片地址
                if image.img == None:
                    pass
                else:
                    image.save()
                #修改完内容后重新回到详情界面
                return redirect('/')
        except Exception as e:
            adsbinfo = ADSBInfo.objects.get(id=id)
            print(e)
            errorHexID = "修改失败，请检查输入！"
            return render(request,'app/detail.html',
                            {
                                'adsbinfo': adsbinfo,
                                'ADSBimg': ADSBimg,
                                'errorHexID' : errorHexID,
                                }
                            )



    #直接进入详情页的话，使用的是GET方式，就显示下面内容
    else: 
        return render(
            request,
            'app/detail.html',
            {
                'adsbinfo': adsbinfo,
                'ADSBimg': ADSBimg,
                'year':datetime.now().year,
            }
        )




#删除数据页面
@login_required
def delete(request):
    #通过GET方法从链接中获取id
    id = request.GET.get('id')
    #将这个id的所有数据删除
    ADSBInfo.objects.filter(id=id).delete()
    #删除完了重定向回index
    return redirect('/')


#联系方式页面
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'联系开发者:',
            'year':datetime.now().year,
        }
    )


#关于页面
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'ADS-B系统',
            'describe':'名称释义',
            'synopsis':'系统简介',
            'year':datetime.now().year,
        }
    )


