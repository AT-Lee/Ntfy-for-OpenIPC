# ntfy-for-OpenIPC
### Ntfy Notification Integration for OpenIPC Cameras (script + web interface)

#### ! Created with GLM-5 from Z.ai based on the OpenIPC telegram script<br>(AI comments preserved in the code)

### Features
Web Interface: Configure all settings through the standard OpenIPC web interface (Extensions -> Ntfy).

Local Server: Support for working with a local Ntfy server (e.g., on an OpenWRT router).

Security: Support for authorization (login/password).

Flexibility: Customize headers, priorities, photo format (JPG/HEIF).

Testing: Test send button directly from the interface without page reload (AJAX).


### Installation:

##### 1. File Installation:

Copy the files to the camera (e.g., via WinSCP):

ntfy -> /usr/sbin/ntfy

ext-ntfy.cgi -> /var/www/cgi-bin/ext-ntfy.cgi

ntfy.conf -> /etc/webui/ntfy.conf


##### 2. Setting Permissions
   
Connect to the camera via SSH and run the commands:

<code>chmod +x /usr/sbin/ntfy</code>

<code>chmod +x /var/www/cgi-bin/ext-ntfy.cgi</code>
        
##### 3. Usage
<img width="700" alt="image" src="https://github.com/user-attachments/assets/fbace184-0abc-4d27-b0f7-efcbba6e3267" />

* Open the camera's web interface.
* Navigate to http://<your_camera_ip_address>/cgi-bin/ext-ntfy.cgi.
   
  Note: You can add a menu item to the "Extensions" tab by editing the file /var/www/cgi-bin/p/header.cgi 
  and adding after line 71 a new line: 
  <pre>&lt;li&gt;&lt;a class="dropdown-item" href="ext-ntfy.cgi"&gt;Ntfy&lt;/a&gt;&lt;/li&gt;</pre>
  <img width="800" alt="image" src="https://github.com/user-attachments/assets/37299712-a9e9-425f-959d-bdfa8353becd" />


* Enter the server address (e.g., http://192.168.1.1:8080 for local or https://ntfy.sh for public).
* Specify the topic (channel) and click Save Changes.
* Click Send Test Notification to test.

