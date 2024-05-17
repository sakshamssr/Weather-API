echo "BUILD START"
python3.9 -m ensurepip --upgrade
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt
echo "BUILD END"

