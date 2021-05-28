import  justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc

data=pd.read_csv("reviews.csv",parse_dates=["Timestamp"])
data["Month"]= data["Timestamp"].dt.strftime("%y-%m")
month_avg_by_course=data.groupby(["Month","Course Name"]).count().unstack()
month_avg=data.groupby(["Month"]).mean()

chart_def="""
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def app():
    wp=jp.QuasarPage() ##framework used is quaSAR
    h1= jp.QDiv(a=wp,text="Analysis of Course Reviews",classes="text-h3 text-center q-pa-md") #a is arg that says the h1 belongs to web page wp
    p1=jp.QDiv(a=wp,text="These graphs represent course review analysis")
    hc=jp.HighCharts(a=wp,options=chart_def)
    hc.options.xAxis.categories=list(month_avg_by_course.index)
    hc_data=[{"name":v1,"data":[v2 for v2 in month_avg_by_course[v1]]} for v1 in month_avg_by_course.columns]
    hc.options.series= hc_data
    
    return wp

jp.justpy(app)