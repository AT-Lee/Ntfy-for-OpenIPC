# ntfy-for-OpenIPC
### Ntfy notification integration for OpenIPC cameras (Script + Web UI) / Интеграция уведомлений Ntfy для камер OpenIPC (скрипт + веб-интерфейс)

#### ! Создано при помощи GLM-5 от Z.ai на основании скрипта telegram OpenIPC<br>(в коде сохранены комментарии ИИ)

### Возможности
Веб-интерфейс: Настройка всех параметров через стандартную веб-морду OpenIPC (Extensions -> Ntfy).

Локальный сервер: Поддержка работы с локальным сервером Ntfy (например, на роутере OpenWRT).

Безопасность: Поддержка авторизации (логин/пароль).

Гибкость: Настройка заголовков, приоритетов, формата фото (JPG/HEIF).

Тестирование: Кнопка проверки отправки прямо из интерфейса без перезагрузки страницы (AJAX).


### Установка:

##### 1. Установка файлов:

Скопируйте файлы на камеру (например, через WinSCP):

ntfy -> /usr/sbin/ntfy

ext-ntfy.cgi -> /var/www/cgi-bin/ext-ntfy.cgi

ntfy.conf -> /etc/webui/ntfy.conf


##### 2. Настройка прав
   
Зайдите на камеру по SSH и выполните команды:

<code>chmod +x /usr/sbin/ntfy</code>

<code>chmod +x /var/www/cgi-bin/ext-ntfy.cgi</code>
	
##### 3. Использование
<img width="700" alt="image" src="https://github.com/user-attachments/assets/fbace184-0abc-4d27-b0f7-efcbba6e3267" />

* Зайдите в веб-интерфейс камеры.
* Перейдите по адресу http://<ip_адрес_вашей_камеры>/cgi-bin/ext-ntfy.cgi.
   
  Прим. можно добавить пункт меню во вкладку "Extensions" отредактировав файл /var/www/cgi-bin/p/header.cgi 
  добавив после 71 строки новую строку: 
  <pre>&lt;li&gt;&lt;a class="dropdown-item" href="ext-ntfy.cgi"&gt;Ntfy&lt;/a&gt;&lt;/li&gt;</pre>
  <img width="800" alt="image" src="https://github.com/user-attachments/assets/37299712-a9e9-425f-959d-bdfa8353becd" />


* Введите адрес сервера (например, http://192.168.1.1:8080 для локального или https://ntfy.sh для публичного).
* Укажите топик (канал) и нажмите Save Changes.
* Нажмите Send Test Notification для проверки.

  
