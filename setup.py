from setuptools import setup

print("""You can create a distribution version with py2app.
      \nThe current version at the time of writting this doesn't work very well.
      \nTo install this app, just place the py2app folder in your project folder and run:
      \npython3 setup.py py2app
      \nGood Luck!""")

DATA_FILES = ['appinfo.json', 'generalinfo.json']
OPTIONS = {
    'iconfile':'icon.icns',
}

setup(name="RatingDiary",
    app=["main.py"],
    options={'py2app': OPTIONS},
    setup_requires=["py2app"],
    data_files = DATA_FILES
)
