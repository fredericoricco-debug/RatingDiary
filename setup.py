from setuptools import setup

print("If you only get this line, read the readme.md file on how to use RatingDiary!")

DATA_FILES = ['appinfo.json', 'generalinfo.json']
OPTIONS = {
    'iconfile':'icon/icon.icns',
}

setup(name="RatingDiary",
    app=["main.py"],
    options={'py2app': OPTIONS},
    setup_requires=["py2app"],
    data_files = DATA_FILES
)
