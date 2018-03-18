# ConnTestD
ConnTestD is a very simple connection testing daemon / service for monitoring internet connections periodically using the speedtest.net API written in Python.

A perfect use case is for monitoring your home internet connection using a Raspberry Pi (obviously your speed test will be limited to the speed of the Pi's NIC).
At the moment ConnTestD has a very basic feature set which includes:

* Periodic testing of your internet connection using the speedtest.net API
* Storage of the results in any SQLAlchemy compatible DB (defaults to SQLite)
* Basic web dashboard with recent test results and graphs for the last week

On the roadmap for the future are features including:

* Alerting if a connection is down (obviously you'll need some way to get the message out without your internet connection, maybe a 3G dongle)
* Alerting if your connection falls below the minimum gauranteed speed as specified in your ISPs service level agreement
* Alerting for high round trip times
* Other storage backends such as time series databases rather than traditional SQLAlchemy RDBMS

## Debian Installation Guide


