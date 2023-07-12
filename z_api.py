import requests
import json

url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"

querystring = {"muscle":"biceps"}

headers = {
	"X-RapidAPI-Key": "61cd55e820msh974e4f6aaf2f71ap1e058djsn6403464e46e7",
	"X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


print(response.json())
