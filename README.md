# RaspIP
This is a small school / hobby project aiming to ease the use of Raspberry Pi by removing the need for a display and a keyboard for IP lookup needed for SSH connection.

## Features
- Send an email with SSID and local IP address from Raspberry 4 upon boot and possible reconnects
- Configure multiple WiFis with different priorities

## Setup
1. Download this repository into Raspberry 4

2. Create a Gmail account for Raspberry
    - **It is recommended to create dedicated Gmail account for the Raspberry**
    - Allow less secure apps on Raspberry's Gmail account. See [https://support.google.com/a/answer/6260879?hl=en]

3. Fill config.py

4. Edit /etc/wpa_supplicant/wpa_supplicant.conf
    - **Set update_config=0**
    - Add WiFi networks as you please. RaspIP will attempt to join them in priority order

    ```yaml
    networks = {
        ssid: "your ssid here"
        psk: "your wifi password here"
        priority: "wanted priority here"
        key_mgmt: "WPA-PSK"
    }

5. Configure /etc/rc.local to start RaspIP at boot
    - Add following before *exit 0*
    
    ```yaml
    ...

    cd path/to/RaspIP/src
    python3 RaspIP_Watcher.py &

    exit 0

6. Reboot

## Killing RaspIP

- Run the following to find process id
    ```
    ps -aux | grep RaspIP
- Run the following to kill the process
    ```
    sudo kill <process id>
