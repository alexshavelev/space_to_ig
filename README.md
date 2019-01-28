# Download photos and post to IG

Project can be download photos from spacex and hubble apis and post them to IG

### How to install
Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies

```
git clone ..
cd /path/to/dir
pip install -r requirements.txt
```

Then create '.env' file and put here IG username and password in next format 
```
USERNAME=<login>
PASSWORD=<pass>
```

### How to use
Collect photos from SpaceX:
```
python fetch_spacex.py
```
Collect photos from Hubble:
```
python fetch_hubble.py
```
Upload to IG page:
```
python post_to_instagram.py
```

Or do all steps together
```
python fetch_spacex.py && python fetch_hubble.py && python post_to_instagram.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
