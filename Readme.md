# About
<b>
Supervisor is a powerful process control system for managing and monitoring processes on Unix-like operating systems.<br> It is particularly useful for managing long-running processes, handling failures, <br>and ensuring that critical applications are always running.
</b>

# Install
```sh
sudo apt-get update
sudo apt-get install supervisor
```
# Get all commands help
```sh
sudo supervisorctl ?
```

# Create a Supervisor Configuration File
```sh
sudo vim /etc/supervisor/conf.d/app1.conf
```

# Update Supervisor Configuration
```sh
sudo supervisorctl reread
sudo supervisorctl update
```

# Start Your Application
```sh
sudo supervisorctl start app1
```

# Check Status
```sh
sudo supervisorctl status
```

# Stop or Restart the Application
```sh
sudo supervisorctl stop app1
```
```sh
sudo supervisorctl restart app1
```

# To stop or restart all applications:
```sh
sudo supervisorctl stop all
sudo supervisorctl restart all
```

# Enable Web Interface For Monitoring

```sh
sudo vim /etc/supervisor/supervisord.conf
```

### Add in supervisord.conf
<b>
[inet_http_server]<br>
port = 127.0.0.1:9001<br>
username = user<br>
password = pass<br>
</b>

```sh
sudo systemctl restart supervisor
```

```sh
http://127.0.0.1:9001
```