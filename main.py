from flask import Flask, jsonify
from flask_mqtt import Mqtt

app = Flask(__name__)

app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
topic = '/will/sensor_flask/sensor1'

mqtt_client = Mqtt(app)


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        if (mqtt_client.subscribe(topic)):
            print('Successfully subscribed to the topic:', topic)
    else:
        print('Something went wrong:', rc)


# On-message-funktion
@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    m_topic = message.topic
    m_payload = message.payload.decode('utf-8')
    print(f'Received message on topic: {m_topic}: {m_payload}')

    # Extract the sensor ID from the topic
    _, received_sensor_id = m_topic.rsplit('/', 1)
    print(received_sensor_id)

    with open(file='storage.txt', mode='w', encoding='utf-8') as file:
        file.write(received_sensor_id + ": " + m_payload)


@app.route('/get/')
def get_temp():
    with open(file='storage.txt', mode='r', encoding='utf-8') as file:
        data = file.read()
    return jsonify({'text': data}), 200


@app.route('/')
def hello_world():
    return 'Hello Flask API!'


if __name__ == '__main__':
    app.run(debug=True)