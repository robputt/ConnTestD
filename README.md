# ConnTestD
ConnTestD is a very simple connection testing daemon / service for monitoring internet connections periodically using the speedtest.net API written in Python.

A perfect use case is for monitoring your home internet connection using a Raspberry Pi (obviously your speed test will be limited to the speed of the Pi's NIC).
At the moment ConnTestD has a very basic feature set which includes:

* Periodic testing of your internet connection using the speedtest.net API
* Storage of the results in any SQLAlchemy compatible DB (defaults to SQLite)
* Basic web dashboard with recent test results and graphs for the last week

On the roadmap for the future are features including:

* Alerting if a connection is down
* Alerting if your connection falls below the minimum gauranteed speed as specified in your ISPs service level agreement
* Alerting for high round trip times
* Other storage backends such as time series databases rather than traditional SQLAlchemy RDBMS

## Installation Guide (Debian Variants, e.g. Debian, Ubuntu, Raspbian)

Works with either Python 2.7 or Python 3. This guide will install in a Python VirtualEnv to avoid clogging up your system Python installation.

Install required OS packages::

	apt-get update
	apt-get install python3 python3-dev python3-setuptools git

Install required Python packages::

	easy_install3 pip
	pip install virtualenv

Create VirtualEnv for application::

	virtualenv /opt/conntestd

Assume the VirtualEnv and install ConnTestD::

	source /opt/conntestd/bin/activate
	pip install git+https://github.com/robputt796/ConnTestD.git

Create a new SystemD service file with the contents below in the following location with your favourite editor... /lib/systemd/system/conntestd.service::

	[Unit]
	Description=ConnTestD
	After=multi-user.target
	StandardOutput=syslog
	StandardError=syslog
	SyslogIdentifier=conntestd
	
	[Service]
	Type=idle
	ExecStart=/opt/conntestd/bin/conntestd
	
	[Install]
	WantedBy=multi-user.target

Configure syslog to log to a specific file, open /etc/rsyslog.d/conntestd.conf in your favourite editor and configure as follows::

	if $programname == 'conntestd' then /var/log/conntestd.log

Reload SystemD to load the new service file, start the service and configure to run at boot time::

	systemctl daemon-reload
	systemctl start conntestd
	systemctl enable conntestd

Check the application has started logging to the specified log file::

	cat /var/log/conntestd.log 

Next visit your server's IP in your browser on port 5000, you should see a speed test result, a new one should get added at 10 minute intervals.

![screenshot](https://raw.githubusercontent.com/robputt796/ConnTestD/master/docs/screenshot.png)

## Installation Guide (Redhat Variants, e.g. RedHat, CentOS)

This needs completing, but you can probably work it out by adapting the Debian install guide, sorry!
