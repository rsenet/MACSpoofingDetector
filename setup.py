from setuptools import setup, find_packages

long_description = "MACSpoofingDetector is a simple utility allowing to identify Access Point MAC Spoofing on Wireless network"

setup(
    name="MACSpoofingDetector",
    version="0.1",
    description="Access Point MAC Spoofing Detector",
    long_description=long_description,
    url="https://github.com/rsenet/MACSpoofingDetector",
    author="Régis SENET",
    author_email="regis.senet@orhus.fr",
    license="GPLv3",

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: MacOS'
        'Topic :: Utilities',
        'Topic :: Security',
    ],

    packages=find_packages(),

    python_requires='>3.6',

    scripts=['MACSpoofingDetector.py'],
)
