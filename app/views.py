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
