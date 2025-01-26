# Apartment Ad Refresher

## Installation

1. `sudo apt update`

2. `sudo apt install -y python3 python3-pip firefox`

3. Download newest geckodriver. Raspberry Pi: `wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux-aarch64.tar.gz`

4. `tar -xzf geckodriver-*.tar.gz`

5. `sudo mv geckodriver /usr/local/bin/`

6. `chmod +x /usr/local/bin/geckodriver`

7. `pip install selenium`

8. As admin: `pip install webdriver-manager --break-system-packages`

9. Edit credentials and geckodriver path in constants.py

10. Run main.py

11. (OPT.) Create crontab entry for refreshing on regular basis: 

	`sudo crontab -e`

	`24 * * * * nohup python /Path/To/Repo/app/main.py > /var/log/aar.log 2>&1`
