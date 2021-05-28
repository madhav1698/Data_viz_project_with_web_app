import justpy as jp

def app():
    wp=jp.QuasarPage() ##framework used is quaSAR
    h1= jp.QDiv(a=wp,text="Analysis of Course Reviews",classes="text-h3 text-center q-pa-md") #a is arg that says the h1 belongs to web page wp
    p1=jp.QDiv(a=wp,text="These graphs represent course review analysis")
    return wp

jp.justpy(app)