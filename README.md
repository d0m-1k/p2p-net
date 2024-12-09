# Система P2P сети по Bluetooth

Система представляет собой децентрализованную сеть, которая использует протокол Bluetooth для передачи сообщений между участниками без необходимости сервера. 

## Основные компоненты

1. Шифрование данных: Сообщения между пользователями шифруются с использованием симметричного или асимметричного шифрования (например, AES или RSA). Только отправитель и получатель могут расшифровать данные.
2. Передача через посредников: Сообщение передается от одного участника к другому через цепочку посредников. Каждый участник получает шифрованное сообщение, не зная его содержания. Для этого используются многоуровневые шифры.
3. Открытая архитектура: Все участники являются одновременно отправителями и получателями, что позволяет избежать единой точки отказа.
4. Управление соединениями: Bluetooth обеспечивает локальные соединения, что увеличивает безопасность за счет уменьшения уязвимости к атакам.

## Преимущества

- Анонимность: Посредники не имеют доступа к содержимому сообщений.
- Устойчивость: Нет сервера, что делает систему менее уязвимой к отключениям интернета..
- Локальность: Использование Bluetooth снижает зависимость от интернет-соединения.

Эта архитектура создает безопасный, устойчивый и приватный способ общения между пользователями.\

[Как это работает?](https://github.com/d0m-1k/p2p-net/blob/main/HOW_WORK.md)
