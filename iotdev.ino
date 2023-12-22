#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "Wokwi-GUEST";
const char* password = "";
const char* mqttServer = "broker.hivemq.com";
const int mqttPort = 1883;
const char* clientId = "Temp sensor #1";

const float BETA = 3950;

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  analogReadResolution(10);
  pinMode(34, INPUT); // Assuming the NTC is connected to pin 34
  pinMode(14, OUTPUT);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Connect to MQTT broker
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);

  while (!client.connected()) {
    if (client.connect(clientId)) {
      Serial.println("Connected to MQTT broker");
    } else {
      Serial.print("Failed to connect to MQTT broker, rc=");
      Serial.println(client.state());
      delay(2000);
    }
  }
}

void loop() {
  int analogValue = analogRead(34);
  float celsius = 1 / (log(1 / (1023. / analogValue - 1)) / BETA + 1.0 / 298.15) - 273.15;
  Serial.print("Temperature: ");
  Serial.print(celsius);
  Serial.println(" ℃");

  // Publish temperature to MQTT topic
  char temperatureStr[10];
  sprintf(temperatureStr, "%.2f ℃", celsius);
  client.publish("/will/sensor_flask/sensor1", temperatureStr);

  client.loop();

  // Additional logic using the temperature value, e.g., controlling an output
  if (celsius >= 35) {
    digitalWrite(14, HIGH);
  } else {
    digitalWrite(14, LOW);
  }

  delay(1000);
}

void callback(char* topic, byte* payload, unsigned int length) {
  // Handle incoming messages if needed
}
