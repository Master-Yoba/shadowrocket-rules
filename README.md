[**English**](https://github.com/Master-Yoba/shadowrocket-rules/blob/main/README.en.md) | **Русский**

# Что это

Проект автоматически ежедневно генерирует RULE-SET файлы `.list` для использования в конфигах [Shadowrocket](https://apps.apple.com/ru/app/shadowrocket/id932747118) (популярный xray клиент на платформах iOS, iPadOS, macOS, tvOS).

В качестве исходных данных используются geosite и geoip [sing-box](https://github.com/SagerNet/sing-box) `srs` файлы из https://github.com/runetfreedom/russia-v2ray-rules-dat


# Использование

Все файлы можно найти [в ветке release](https://github.com/Master-Yoba/shadowrocket-rules/tree/release). С детальным описанием особенностей содержимого каждого файла [можно ознакомиться в исходном репозитории](https://github.com/runetfreedom/russia-v2ray-rules-dat/blob/main/README.md).

Прямые ссылки на некоторые файлы, которые могут быть наиболее интересны пользователям в РФ:

- **geosite ru-blocked**
    - [https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-ru-blocked.list](https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-ru-blocked.list)

- **geosite ru-blocked-all**
    - [https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-ru-blocked-all.list](https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-ru-blocked-all.list)

- **geosite category-ru**
    - [https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-category-ru.list](https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-category-ru.list)

- **geoip ru-blocked**
    - [https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geoip/geoip-ru-blocked.list](https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geoip/geoip-ru-blocked.list)

- **geoip ru**
    - [https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geoip/geoip-ru.list](https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geoip/geoip-ru.list)

Эти ссылки можно добавлять в конфигурацию Shadowrocket таким образом:
```
# Пример правил
[Rule]
# Список доменов ru-blocked открывать через прокси
RULE-SET,https://raw.githubusercontent.com/Master-Yoba/shadowrocket-rules/release/rules-geosite/geosite-ru-blocked.list,PROXY
```

## Как это работает

Скрипт для парсинга можно запустить самостоятельно.
Перед первым запуском рекомендуется единократно запустить `prepare.sh`. Он создаст необходимые директории и скачает из релизов на гитхабе бинарник [sing-box](https://github.com/SagerNet/sing-box), который необходим для парсинга.

Необходимо поместить входные `srs` файлы в директорию `singbox-rules` и запустить:

```
python3 parse.py
```

Результирующие `.list` файлы будут в директории `shadowrocket-rules`

