from confluent_kafka import Consumer
import json

# Créer un consommateur Kafka qui écoute le sujet "weather"
print("Je m'execute")
c=Consumer({'bootstrap.servers':'broker:29092','group.id':'python-consumer'})
print("Je me suis connecté au broker")
c.subscribe(['weather'])

# Boucler sur les messages reçus


def main():
    while True:
        msg=c.poll(1.0) #timeout
#msg = c.consume(num_messages=1, timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data = msg.value()
        print(data)
        c.close()
if __name__ == '__main__':
    main()
