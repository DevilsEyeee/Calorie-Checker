from django.shortcuts import render

#P6IrXRmfXQdBB3e5yOUbyw==oG3xFLdeEa03aFoQ (THIS IS THE KEY)
#API Used: https://api-ninjas.com/api/nutrition 

# Create your views here.
def home(request):
    import requests
    import json
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url + query, headers={'X-Api-Key': 'P6IrXRmfXQdBB3e5yOUbyw==oG3xFLdeEa03aFoQ'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as error:
            api = "There was an error!"
            print(error)
        return render(request, 'index.html', {'api': api})
    else:
        return render(request, 'index.html', {'query': 'Enter a valid query'})