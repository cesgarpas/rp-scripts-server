# Raspberry PI Scripts Server Runner
Simple generic server for running scripts in the Raspberry pi which are located inside a folder.

![Scripts server](https://github.com/cesgarpas/rp-scripts-server/blob/main/working-server.png?raw=true)

## Setting up startup run
0. Clone the repository where you want it to be (I will do it in /home/pi):
```
git clone https://github.com/cesgarpas/rp-scripts-server
```

1. Create a new service:
```
sudo nano /etc/systemd/system/scripts-server.service
```

2. Fill it with the following configuration (replacing the working directory with the one where you cloned this repo):
```
[Unit]
Description=scripts-server
After=network.target

[Service]
WorkingDirectory=/home/pi/rp-scripts-server
ExecStart=/usr/bin/python ./scripts-server.py &
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Add a script:
```
nano /home/pi/rp-scripts-server/list-drives.sh
```

Paste and save the following command:
```
sudo lsblk -o UUID,NAME,FSTYPE,SiZE,MOUNTPOINT,LABEL,MODEL
```

Give the script execution permissions:
```
chmod +x /home/pi/rp-scripts-server/list-drives.sh
```

4. Test the service:
```
systemctl start scripts-server
```
It should be accessible at `http://[your.raspberrypi.ip]:5000` and the script (list-drives) should appear and work listing your available drives with extra information.

5. Enable the service for it to run at startup:
```
systemctl enable scripts-server
```

## Add and run scripts
Add any .sh file to the repo folder and restart the service. You will see the scripts list in the view and by clicking on them they will be executed and you will be able to see the output.

## Debug
 - To view the logs of the service run:
```
systemctl status scripts-server
```

 - To run the server locally without using the service you can stop the service, navigate to the server folder and run:
```
export FLASK_APP=scripts-server; flask run --host=0.0.0.0
```
