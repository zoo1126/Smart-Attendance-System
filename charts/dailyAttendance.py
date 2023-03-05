from pyecharts import options as opts
from pyecharts.charts import Calendar
from pyecharts.charts import Bar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import datetime
import random


def showALLAtt(att_list,gridLayout):
    print(att_list)
    state_list = ["未打卡人数", "已打卡人数", "迟到人数", "请假人数", "外勤人数"]
    bar = (
        Bar()
            .add_xaxis(state_list)
            .add_yaxis('',att_list)

            .set_global_opts(title_opts=opts.TitleOpts(title="考勤记录可视化", subtitle="公司考勤"))
    ).render('file:///' + 'js/alldailyAttendance.html')
    webView = QWebEngineView()
    webView.setObjectName('webView')
    webView.load(QUrl('file:///' + 'js/alldailyAttendance.html'))

    gridLayout.addWidget(webView)

def showDepAtt(att_list,gridLayout):
    print(att_list)
    state_list = ["未打卡人数", "已打卡人数", "迟到人数", "请假人数", "外勤人数"]
    bar = (
        Bar()
            .add_xaxis(state_list)
            .add_yaxis('',att_list)

            .set_global_opts(title_opts=opts.TitleOpts(title="考勤记录可视化", subtitle="部门考勤"))
    ).render('file:///' + '/js/depdailyAttendance.html')
    webView = QWebEngineView()
    webView.setObjectName('webView')
    webView.load(QUrl('file:///' + 'js/depdailyAttendance.html'))

    gridLayout.addWidget(webView)

def showIndAtt(data,dateMonth,gridLayout):

    c = (
        Calendar()#创建calendar实例
        .add(
            "考勤信息",#添加在数据显示的前面，用于 tooltip 的显示，legend 的图例
            data,#接收数据，格式为 [(日期1, 值1), (日期2, 值2), ...]
            #日历图的配置选项
            calendar_opts=opts.CalendarOpts(
                 # 某一年 range: 2017
                # 某个月 range: '2017-02'
                # 某个区间 range: ['2017-01-02', '2017-02-23']
                # 注意 此写法会识别为['2017-01-01', '2017-02-01']
                # range: ['2017-01', '2017-02']
                range_=dateMonth,#[Range1,Range2],时间范围，可选
                daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),#星期名称选择，此处选中文
                monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),#月份名称选择
                orient='vertical',
                pos_top='140px',
                pos_left='40px',
                pos_right='20px',
                pos_bottom='10px'
            ),
            tooltip_opts=opts.TooltipOpts(formatter='<a><br/>{c}')
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="员工考勤记录"),#标题配置
            visualmap_opts=opts.VisualMapOpts(

                split_number = 5,
                pieces=
                [
                    {
                        "value": 0,  "label": "未打卡", "color": "grey"},
                    {
                        "value": 1,  "label": "已打卡", "color": "green"},
                    {
                        "value": 2,  "label": "迟到", "color": "yellow"},
                    {
                        "value": 3,  "label": "请假", "color": "red"},
                    {
                        "value": 4,  "label": "外勤", "color": "blue"},
                ],
                orient="horizontal",
                is_piecewise=True,

                pos_top='50px',
                pos_left="center",

            ),#展示配置
        ).render('file:///' + "js/ind_calendar_label_setting.html")#渲染名称
    )
    webView = QWebEngineView()
    webView.setObjectName('webView')
    webView.load(QUrl('file:///' + 'js/ind_calendar_label_setting.html'))

    gridLayout.addWidget(webView)

