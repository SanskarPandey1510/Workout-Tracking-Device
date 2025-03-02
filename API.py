APP_ID="f9fd23fb"
API_KEY="2aa86fb85a417586d9666c276d367f74"
h={
    # 'Content-Type': 'application/json',
"x-app-id":APP_ID,
    
"x-app-key":API_KEY,

}

parameters = {
    "query": "swam for 1 hour",
    "gender": "male",
    "weight_kg": "70",
    "height_cm":"169",
    "age": "20",
}

Host_Domain	="https://trackapi.nutritionix.com"
import requests
response=requests.post('https://trackapi.nutritionix.com/v2/natural/exercise',headers=h,json=parameters)
print(response.json())