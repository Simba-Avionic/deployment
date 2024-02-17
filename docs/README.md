# Konfiguracji własnej aplikacji

Przykładowy plik zawierający konfiguracje aplikacji nie posiadającej komunikacji SOME/IP (minimum)

```
{
    "app":{
            "name":"ExampleApp",
            "bootMode": 0,
            "logger": {
                "app_id": "EXAM",
                "app_des": "Przykladowa Aplikacja",
                "log_level": "kInfo",
                "log_mode": "kConsole|kDLT"
            }
        }
}
```

## Możliwe parametry:
### "name"

Nazwa aplikacji która może zawierać:
- A-z
- 0-9
- _

Niewolno stosować spacji
### "bootMode"

Level | Opis |
------|------|
0   | Inne aplikacje które nie są krytyczne |
1   | Aplikacje "serwisy" (Niski piorytet) |
2   | Aplikacje "serwisy" (Średni piorytet) |
3   | Aplikacje "serwisy" (Wysoki piorytet) |
4   | Aplikacje z klasy zarazem MW i serwisy (Niski piorytet) |
5   | Aplikacje z klasy zarazem MW i serwisy (Średni piorytet) |
6   | Aplikacje z klasy zarazem MW i serwisy (Wysoki piorytet) |
7   | Aplikacje z klasy MW (Niski piorytet) |
8   | Aplikacje z klasy MW (Średni piorytet) |
9   | Aplikacje z klasy MW (Wysoki piorytet) |
10  | Aplikacje które są potrzebne najszybciej jak np. dlt-service |

--------------------------------------------------------------------
### "logger"
Ustawienia loggera
#### "app_id"

Cztero znakowy identyfikator aplikacji.
Jeśli użyjemy mniej nalezy dopełnić do 4 znaków symbolem : '-'. Przykład "APP-" lub "A---".

#### "app_des"

Krótki opis aplikacji - używane przy starcie w celu łatwego zrozumienia na podstawie samych logów co robi aplikacja.

#### "log_level"

Ustawienie jaki poziom logów ma być zapisywany.
 Dostępne poziomy:
 - kDebug,
 - kInfo,
 - kWarning,
 - kError

 #### "log_mode"

 Ustawienie trybu logowania. Możliwe jest łączenie ich poprzez symbol '|'. Dostępne tryby:

 - kFile -> zapis do pliku (nie wspierane obecnie)
 - kConsole -> Wyświetlają się w terminalu a podczas uruchomienia na urządzeniu docelowym wyswietlają się w terminalu szeregowym po podpięciu poprzez UART.