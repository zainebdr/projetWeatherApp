from kafka import KafkaConsumer
import json

# Créer un consommateur Kafka qui écoute le sujet "weather"
consumer = KafkaConsumer(
    'weather',
    bootstrap_servers=['localhost:9092'],
    api_version=(0,11,5),
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Boucler sur les messages reçus
for message in consumer:
    # Extraire les données météorologiques du message
    weather_data = message.value
    print(weather_data)
