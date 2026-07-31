from flask import Flask, jsonify,Blueprint,render_template,request
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

weather=Blueprint("weather",__name__)
@weather.route("/weather")
def get_weather():
    city_name=request.args.get("city")
    api_key=os.getenv("WEATHER_API_KEY")
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metricc"
    response=requests.get(url)
    data=response.json()
    if response.status_code!=200:
        error_msg=data.get("message","Enter a valid city")
        return render_template("base.html",error=error_msg.title())
    icon_code=data.get('weather',[{}])[0].get('icon','01d')
    icon_url=f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    weather_data={
        "city":data.get('name','City not found'),
        'country':data.get('sys',{}).get('country',""),
        'date':datetime.now().strftime("%A, %I: %M %p"),
        'temperature':f"{round(data.get('main',{}).get('temp',273.15)-273.15)}°C",
        'condition':data.get('weather',[{}])[0].get('description','no data').title(),
        'wind':f"{round(data.get('wind',{}).get('speed',0)*3.6,1)} km/hr",
        'humidity':f"{data.get('main',{}).get('humidity',0)}%",
        'visibility':f"{round(data.get('visibility',0)/1000,1)} km",
        'icon':icon_url
    }
    
    return render_template("base.html",weather=weather_data)




