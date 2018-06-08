"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['v2net.py']
APP_NAME = 'V2Net'
DATA_FILES = ['extension', 'profile', 'icon.png']
OPTIONS = {
    'emulate_shell_environment': True,
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'LSUIElement': True,
        'CFBundleVersion': "0.1.4",
        'CFBundleShortVersionString': "0.1.4"
    }
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
