from setuptools import setup

APP = ['main.py']  # Your main Python script
DATA_FILES = ['error.py', 'getWeather.py', 'GUI.py', 'unitConversion.py', 'utilities.py', 'icons', 'resources']  # Folders with extra files
OPTIONS = {
    'argv_emulation': True,      # Makes command-line arguments work
    'iconfile': 'resources/pngtree-collection-of-detailed-weather-icons-for-digital-forecast-applications-png-image_16420442.png', # Optional: your app icon
    'packages': [],              # Add extra packages if needed
    'plist': {
        'CFBundleName': 'WeatherBuddy',   # App name
        'CFBundleVersion': '1.0',
        'CFBundleShortVersionString': '1.0',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)