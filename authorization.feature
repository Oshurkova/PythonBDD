# language: ru

Функционал: Авторизация на сайте
  Как пользователь, я хочу авторизоваться на сайте, чтобы получить доступ к моим персональным данным.

  Структура сценария: Успешная авторизация
    Допустим я открываю страницу авторизации
    Когда я ввожу логин "<username>" и пароль "<password>"
    И отправляю форму авторизации
    Тогда авторизация должна пройти успешно

    Примеры:
      | username | password |
      | user1    | 12345    |
      | user2    | 12345    |

  Структура сценария: Неуспешная авторизация
    Допустим я открываю страницу авторизации
    Когда я ввожу неправильный логин "<username>" или пароль "<password>"
    И отправляю форму авторизации
    Тогда авторизация не должна пройти успешно

    Примеры:
      | username | password |
      | user3    | 123456   |
      | user4    | 123456   |