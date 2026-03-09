# Failed Login Activity Analyzer

## Project Overview

This project simulates a basic security monitoring tool used to detect abnormal authentication behavior. Excessive login attempts can indicate potential security threats such as brute-force attacks, credential stuffing, or compromised user accounts.

The script analyzes login activity by comparing the number of login attempts for the current day against the user's historical average. If the activity exceeds a defined threshold, the script generates an alert indicating potentially suspicious behavior.

This project demonstrates entry-level cybersecurity skills in Python scripting, security monitoring logic, and simple anomaly detection techniques.

---

## Security Use Case

Security teams regularly monitor authentication logs to identify unusual login patterns that may indicate malicious activity.

Example scenario:

A user typically logs in **3 times per day**, but suddenly has **9 login attempts** in a single day. This spike in activity could indicate an attempted compromise or automated login attack.

This script calculates the ratio between current login activity and historical averages and generates an alert when activity exceeds normal behavior thresholds.

Similar analysis techniques are commonly used in security monitoring tools and SIEM platforms such as Splunk.

---

## Technologies Used

* Python
* Basic anomaly detection logic
* Security monitoring concepts

---

## Project Structure

```
failed-login-analyzer/
│
├── analyze_logins.py
└── README.md
```

---

## Example Code

```python
login_analysis = analyze_logins("ejones", 9, 3)
```

Example output:

```
Current day login total for ejones is 9
Average logins per day for ejones is 3
Alert! This account has more login activity than normal.
login_analysis=3.0
```

---

## Skills Demonstrated

* Python scripting for cybersecurity tasks
* Basic anomaly detection and alert logic
* Security event analysis
* Conditional alert generation for suspicious activity
* Technical documentation of security processes

---

## Possible Future Improvements

* Parse authentication logs from a file instead of manual input
* Analyze login activity across multiple users
* Export alerts to a CSV or report format
* Integrate with simulated log datasets
* Visualize authentication anomalies over time
