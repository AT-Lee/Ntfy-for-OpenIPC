#!/usr/bin/haserl
<%in p/common.cgi %>
<%
page_title="Ntfy Notifications"
config_file=/etc/webui/ntfy.conf
# Список параметров, которые мы будем сохранять
params="enabled server topic user pass caption heif priority"

# === ЛОГИКА ТЕСТОВОЙ ОТПРАВКИ ===
if [ "$GET_send" = "test" ]; then
    echo "Content-type: text/html; charset=UTF-8"
    echo
    # Запускаем скрипт отправки.
    # Вывод перенаправляем в /dev/null, чтобы не засорять ответ.
    # Проверяем код возврата (exit code). 0 = успех.
    if /usr/sbin/ntfy > /dev/null 2>&1; then
        echo "OK"
    else
        echo "FAIL"
    fi
    exit 0
fi

# === ЛОГИКА СОХРАНЕНИЯ НАСТРОЕК ===
if [ "$REQUEST_METHOD" = "POST" ]; then
    for p in $params; do
        eval ntfy_${p}=\$POST_ntfy_${p}
    done

    # Валидация
    if [ "$ntfy_enabled" = "true" ]; then
        [ -z "$ntfy_server" ] && set_error_flag "Server URL cannot be empty."
        [ -z "$ntfy_topic" ] && set_error_flag "Topic cannot be empty."
    fi

    # Запись в файл
    if [ -z "$error" ]; then
        rm -f "$config_file"
        for p in $params; do
            echo "ntfy_${p}=\"$(eval echo \$ntfy_${p})\"" >> "$config_file"
        done
        redirect_back "success" "Ntfy config updated."
    fi

    redirect_to "$SCRIPT_NAME"
fi

# === ЗАГРУЗКА ТЕКУЩИХ НАСТРОЕК ===
[ -e "$config_file" ] && include $config_file

# Значения по умолчанию
[ -z "$ntfy_server" ] && ntfy_server="http://192.168.0.50:8080"
[ -z "$ntfy_priority" ] && ntfy_priority="4"
%>

<%in p/header.cgi %>

    <!-- Блок с кнопкой и статусом -->
    <div class="alert alert-info">
        <button type="button" class="btn btn-primary btn-sm" onclick="sendTestNtfy()">Send Test Notification</button>
        <span id="ntfy-status" style="margin-left: 15px; font-weight: bold;"></span>
    </div>

<form action="<%= $SCRIPT_NAME %>" method="post">
    <% field_switch "ntfy_enabled" "Enable Ntfy" "eval" %>
    
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 mb-4">
        <div class="col">
            <h6>Connection Settings</h6>
            <% field_text "ntfy_server" "Server URL" "e.g., http://ntfy.sh" %>
            <% field_text "ntfy_topic" "Topic" "Unique topic name for notifications" %>
            <% field_text "ntfy_user" "Username" "Leave empty if no auth" %>
            <% field_text "ntfy_pass" "Password" "Leave empty if no auth" %>
        </div>

        <div class="col">
            <h6>Message Settings</h6>
            <% field_text "ntfy_caption" "Caption" "Supports: %hostname, %datetime, %soctemp" %>
            <% field_string "ntfy_priority" "Priority" "eval" "1 2 3 4 5" "1=Min, 5=Max (Urgent)" %>
            <% field_switch "ntfy_heif" "Use HEIF format" "eval" "Requires H265 codec on Video0." %>
        </div>

        <div class="col">
            <h6>Current Config File</h6>
            <% [ -e "$config_file" ] && ex "cat $config_file" %>
        </div>
    </div>
    
    <% button_submit %>
</form>

<script>
// Функция для отправки тестового уведомления через AJAX
function sendTestNtfy() {
    var statusSpan = document.getElementById('ntfy-status');
    statusSpan.innerText = 'Sending...';
    statusSpan.style.color = 'blue';

    fetch('?send=test')
        .then(response => response.text())
        .then(data => {
            // data содержит ответ от сервера ("OK" или "FAIL")
            if (data.trim() === 'OK') {
                statusSpan.innerText = 'Success: Test notification sent!';
                statusSpan.style.color = 'green';
            } else {
                statusSpan.innerText = 'Error: Failed to send (check script path).';
                statusSpan.style.color = 'red';
            }
        })
        .catch(error => {
            statusSpan.innerText = 'Request error!';
            statusSpan.style.color = 'red';
        });
}

// Логика для отключения HEIF, если кодек не h265
<% if [ "$(yaml-cli -g .video0.codec)" != "h265" ]; then %>
    $('#ntfy_heif').checked = false;
    $('#ntfy_heif').disabled = true;
<% fi %>
</script>

<%in p/footer.cgi %>