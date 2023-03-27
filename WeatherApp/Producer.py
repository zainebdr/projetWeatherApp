import json
from kafka import KafkaProducer
import requests
import geocoder

def get_weatherdata(choix,ville):
    # Remplacez {API key} par votre propre clé API
    api_key = "0747defefc71f82a572276d367a1be31"

    #Donner le choix à l'utilisateur 
    
    if choix==1:
            # Récupérer les coordonnées géographiques actuelles de l'utilisateur
        g = geocoder.ip('me')
        # Extraire la latitude et la longitude des coordonnées géographiques
        latitude, longitude = g.latlng

        # URL de l'API avec les paramètres de latitude, longitude et clé API
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
 
    else:
        
        # URL de l'API avec les paramètres de la ville et de la clé API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}"
            
    # Envoyer une requête GET à l'API
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Extraire les données JSON de la réponse
        data = response.json()

        # Convertir la température de Kelvin en Celsius
        temp_celsius = data['main']['temp'] - 273.15

        # Créer un dictionnaire pour stocker les données météorologiques
        weather_data = {
            'ville': ville,
            'latitude': latitude,
            'longitude': longitude,
            'temps': data['weather'][0]['description'],
            'temperature': temp_celsius,
            'pression_atmospherique': data['main']['pressure'],
            'humidite': data['main']['humidity']
        }

        # Convertir le dictionnaire en JSON
        weather_data_json = json.dumps(weather_data)
        print("Je vais essayer d'envoyer")

        # Créer un producteur Kafka
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            api_version=(0,11,5),
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

        # Envoyer les données météorologiques au sujet "weather"
        producer.send('weather', value=weather_data_json)

        # Fermer le producteur Kafka
        producer.close()
    else:
        # Afficher le code d'erreur HTTP si la requête a échoué
        print(f"Erreur de requête : {response.status_code}")

    print("Jai envoyé")
get_weatherdata(1,"")






