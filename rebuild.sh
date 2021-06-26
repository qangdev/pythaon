echo "Started"
rm -rf .venv
python3.6 -m venv .venv
.venv/bin/pip3 install -r requirements.txt
echo "Done"