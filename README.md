# IoT_System
William Svensson IoT22

IoT Enhet: simulerad i Wokwi. Simulerar en ESP32 med NTC temperatur sensor. 
IoT Enheten kommunicerar med MQTT genom att göra en publish till mqtt-broker.

API: Flask API som lyssnar på mqtt-broker genom subscribe till samma topic som IoT-enhet
/get endpoint förser applikation med data från IoT-enheten

Klient: klient genom en applikation byggd med Tkinter som hämtar information från API och skriver ut information för sensorn
i applikationen finns det S1-S5 som simulerar 5st temp sensorer (notera att endast S1 fungerar då det endast finns en IoT enhet)

Tanken är att det ska finnas t.ex. 5st enheter i ett hus som mäter temperaturer i respektive rum som du sedan kan se genom applikationen

Utveckling: Tanke är att sedan koppla någon typ av uppvärmare/AC till systemet så du kan styra rummets temperatur
