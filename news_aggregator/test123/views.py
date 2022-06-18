from ctypes import resize
from email.policy import HTTP
from django.shortcuts import render

# Create your views here.
import warnings
warnings.filterwarnings("ignore")
from django.http import HttpResponse,JsonResponse
# from jmespath import search
from psaw import PushshiftAPI
from newsapi import NewsApiClient
from test123.models import Favourite, News_data
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt


expiry_in_sec = 30
def index(request):
    newsapi = NewsApiClient(api_key='308a6f539b7046eebd6097699248b9bb')
    api = PushshiftAPI()
    q = request.GET.get('query','abc')
    testing = News_data.objects.filter(search_word=q).exists()
    print(testing)
    if testing is True:
        data_find=News_data.objects.filter(search_word=q)
        expiry = data_find[0].pub_date + timedelta(seconds=expiry_in_sec)
        if str(datetime.now()) < str(expiry):
            data_base_result=[]        
            for i in data_find:
                temp={}
                temp['id']=i.id
                temp['headline']=i.headline
                temp['link']=i.url
                temp['source']=i.source
                data_base_result.append(temp)
            print("DATA BASE RESULT")
            return JsonResponse(data_base_result,safe=False)
        else:
            
            data_find.delete()
            print("data_del")
    news_api = newsapi.get_top_headlines(q=q)
    redit = list(api.search_submissions(subreddit='news',q=q,limit=20,fields=['created_utc', 'url','title']))
    news_api_headlines =news_api['articles']
    agg_news = []
    
    for i in news_api_headlines:
        temp={}
        temp['headline']=i['title']
        temp['link']=i['url']
        temp['source']='newsapi'
        agg_news.append(temp)
    for i in redit:
        temp={}
        temp['headline']=i.title
        temp['link']=i.url
        temp['source']='reditt'
        agg_news.append(temp)       
    my_entries = list()
    for i in range(len(agg_news)):
        my_entries.append(News_data(headline=agg_news[i]['headline'],url=agg_news[i]['link'],source=agg_news[i]['source'],search_word=q,pub_date=datetime.now()))

    News_data.objects.bulk_create(my_entries)
    print("API CALL RESULT")
    return JsonResponse(agg_news,safe=False)

@csrf_exempt
def favourite(request):
    user = request.GET.get('user', None)

    if request.method == "POST":
        id_ = request.GET.get('id', None)
        try:
            data_find=News_data.objects.get(id=id_)
    
        except:
            return JsonResponse("invalid Request",safe=False)
        data,created=Favourite.objects.get_or_create(user_name=user,news_id=data_find)
        if data.favourite==False:
            data.favourite=True
        else:
            data.favourite=False
        data.save()
        output=[{"user":data.user_name,'favourite':data.favourite,"id":data.news_id.id,'headline':data.news_id.headline,'link':data.news_id.url,
        'source':data.news_id.source}]
        return JsonResponse(output,safe=False)
    data = Favourite.objects.filter(user_name=user)
    result=[]
    for i in data:
        temp={}
        if i.favourite is True:
            temp['id']=i.news_id.id
            temp['headline']=i.news_id.headline
            temp['link']=i.news_id.url
            temp['source']=i.news_id.source
            result.append(temp)

        
    return JsonResponse(result,safe=False)
