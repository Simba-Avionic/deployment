# Konfiguracji własnej aplikacji

Przykładowy plik zawierający konfiguracje aplikacji posiadającej komunikacji SOME/IP (minimum)

```
{
    "app": {
        "name":"ExampleApp",
        "bootMode":0,
        "logger":{
            "app_id":"EXAM",
            "app_des":"Przykladowa Aplikacja",
            "log_level":"kInfo",
            "log_mode":"kConsole|kDLT"
        },
        "someip": {
            "service_id": 10,
            "mode": "kUDP|kIPC",
            "port": 1011,
            "platform": "engine_computer",
            "methods": [
                {
                    "name": "exampleMethod",
                    "id": 10
                },
                {
                    "name": "exampleMethod2",
                    "id": 11
                }
            ],
            "events": [
                {
                    "name": "exampleEvent",
                    "id": 32769
                }
            ],
            "req_methods": [
                "ExampleApp/exampleMethod2"
            ],
            "req_events": [
                "ExampleApp/exampleEvent"
            ]
        }
    }
}
```

## Możliwe parametry:
---
DlA NIEOPISANYCH PARAMETROW SPRAWDŹ PODSTAWOWY PLIK
---