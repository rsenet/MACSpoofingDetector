# About apkFram

**MACSpoofingDetector** was written in order to quickly allow any system administrator to identify a Rogue Access Point based on Sequence Number usurpation.

## Usage

Print the help to get all necessary information

```bash
└─# python3 spoofMacBySNDetector.py --help
usage: spoofMacBySNDetector.py [-h] [--bssid BSSID] [--int INT]

Access Point MAC Spoofing Detector

options:
  -h, --help     show this help message and exit
  --bssid BSSID  Specify targeted Access Point MAC Address (BSSID)
  --int INT      Specify Monitor Interface
```

You just have to specify the interface (with Mode Monitor enabled) and the targeted BSSID:

```bash
└─# python3 spoofMacBySNDetector.py --int wlan0 --bssid 48:2f:6b:XX:XX:XX
Access Point MAC: 48:2f:6b:XX:XX:XX with SSID b'Rsenet-guest'
52992
53328
53424
53472
53520
53712
```

To be continued ...


## Setting the interface to monitor mode:

```bash
└─# airmon-ng start wlan0


PHY Interface Driver    Chipset

phy4  wlan0   88XXau    Realtek Semiconductor Corp. RTL8812AU 802.11a/b/g/n/ac 2T2R DB WLAN Adapter
    (monitor mode enabled)
```


## Author

Régis SENET ([rsenet](https://github.com/rsenet))


## Contributing

Bug reports and pull requests are welcome on [GitHub](https://github.com/rsenet/apkfram).

## License

The project is available as open source under the terms of the [GPLv3](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)
