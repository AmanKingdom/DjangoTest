from django.shortcuts import render
from django.template.loader import get_template
from datetime import datetime
from django.http import HttpResponse

def index(request, mvno='0'):
    mv_list = [{'name': '赤色引擎复刻生命接触', 'mvcode': 'd0705x2bafk'},
               {'name': 'beyond1998', 'mvcode': 'd0680g00di4'},
               {'name': '海阔天空歌迷改版', 'mvcode': 'v0551a3qo9g'},
               {'name': '海阔天空珍藏版', 'mvcode': 'w0640fdsjc2'},]
    template = get_template('index.html')
    now = datetime.now()
    hour = now.timetuple().tm_hour
    mvno = mvno
    mv = mv_list[int(mvno)]
    html = template.render(locals())

    return HttpResponse(html)

def project2(request):
    now = datetime.now()
    hour = now.timetuple().tm_hour
    template = get_template('project2index.html')
    years = range(2018, 1899, -1)
    try:
        user_name = request.GET['user_name']
        user_id = request.GET['user_id']
        user_password = request.GET['user_password']
        user_password2 = request.GET['user_password2']
        user_type = request.GET.getlist('user_type')
        for type in user_type:
            print(type)
    except:
        user_name = None
        user_id = None
        user_password = None
        user_password2 = None
        user_type = None
    if user_name is None and user_id is None and user_password is None and user_password2 is None:
        verified = ''
    elif user_name is not "" and user_password == user_password2 and user_password is not "":
        verified = '注册成功'
    else:
        verified = '注册失败'
    html = template.render(locals())
    return HttpResponse(html)
