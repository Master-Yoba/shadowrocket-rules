**English** | [**Русский**](https://github.com/Master-Yoba/shadowrocket-rules/blob/main/README.ru.md)

# What is This

The project automatically generates RULE-SET `.list` files daily for use in [Shadowrocket](https://apps.apple.com/ru/app/shadowrocket/id932747118) configs (a popular xray client on iOS, iPadOS, macOS, tvOS platforms).

The geosite and geoip [sing-box](https://github.com/SagerNet/sing-box) `srs` files from https://github.com/runetfreedom/russia-v2ray-rules-dat are used as source data.

# Usage

All files can be found [in the release branch](https://github.com/Master-Yoba/shadowrocket-rules/tree/release). A detailed description of the features of each file's contents [can be found in the source data repository](https://github.com/runetfreedom/russia-v2ray-rules-dat/blob/main/README.md).

Direct links to some files that may be of most interest to users in the Russian Federation:

- **geosite ru-blocked**
    - [https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-ru-blocked.list](https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-ru-blocked.list)

- **geosite ru-blocked-all**
    - [https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-ru-blocked.list](https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-ru-blocked-all.list)

- **geosite category-ru**
    - [https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-category-ru.list](https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-category-ru.list)

- **geoip ru-blocked**
    - [https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geoip/geoip-ru-blocked.list](https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geoip/geoip-ru-blocked.list)

- **geoip ru**
    - [https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geoip/geoip-ru.list](https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geoip/geoip-ru.list)


These links can be added to your Shadowrocket configuration as follows:
```
# Example rules
[Rule]
# domain list ru-blocked goes to proxy
RULE-SET,https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-ru-blocked.list,PROXY
```

## How it works

You can run the parser yourself.
Before the first run, it is recommended to run `prepare.sh` once. It will create the necessary directories and download the [sing-box](https://github.com/SagerNet/sing-box) binary from the releases on GitHub, which is necessary for parsing.

You need to place the input `srs` files in the `singbox-rules` directory and run:

```
python3 parse.py
```

The resulting `.list` files will be in the `shadowrocket-rules` directory
