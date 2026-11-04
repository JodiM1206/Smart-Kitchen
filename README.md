# Smart-Kitchen

## Description

A monitoring system using 3 different sensor devices that ease workflow in kitchens. It provides real time updates on temperature and humidity for the fridge, stock of inventory using weight, and checks for any water damages via leaks using water sensors. 

## Progress

>*9/23/26* : Worked on scaffolding the project and infrastructure for the project system. Set up docker compose to run the two services it will use, Mosquitto MQTT and PostgreSQL.

>*11/4/26* : I found redundancy on the fridge sensor between the MLX90614 and the BME280, turns out the BME does not only humidity but also pressure and temperature. I am thinking of adding another device that can display temperature and putting the non contact temp readings to good use.

>*11/4/26* : Added the weight scale device to the devices folder, both the weight scale and the temp/humidity devices will use a display which is on its way. Calibration was not needed too badly but it did give weird readings at first, fixed it with a quick calibration formula and returned to normal readings.

