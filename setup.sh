# Update apt
apt-get update

# Create virtual env and install requirements
apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt

# Enable and run poseidon service
cp gaia.service /etc/systemd/system
systemctl enable gaia
systemctl start gaia
