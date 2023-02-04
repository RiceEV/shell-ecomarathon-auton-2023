# Environment Setup Prodecure

- On the REV computers, the CARLA executable should be in the opt directory
    - Just go to /opt/carla-simulator/
    - Run ```./CarlaUE4.sh```
    - This should start the CARLA server, but it should take a while


## Troubleshooting

- Make sure you are using CARLA version 0.9.12, not 0.9.13
    - Rosbridge has an issue with the 0.9.13 version, and you could trick it into thinking
    it is 0.9.12, but to be consistent, just use 0.9.12. It will make everyone happy.