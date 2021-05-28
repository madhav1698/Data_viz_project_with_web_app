import  justpy as jp
import pandas as pd
from datetime import datetime as dt
from pytz import utc

data=pd.read_csv("reviews.csv",parse_dates=["Timestamp"])
data["Weekday"]=data["Timestamp"].dt.strftime("%A")
data["Daynumber"]=data["Timestamp"].dt.strftime("%w")

weekday_avg= data.groupby(["Weekday","Daynumber"]).mean()
weekday_avg=weekday_avg.sort_values("Daynumber")

chart_def="""
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Aggregated avg ratings per week'
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
    hc.options.xAxis.categories=list(weekday_avg.index)
    hc_data=[{"name":v1,"data":[v2 for v2 in weekday_avg[v1]]} for v1 in weekday_avg.columns]
    hc.options.series= hc_data
    
    return wp

jp.justpy(app)

