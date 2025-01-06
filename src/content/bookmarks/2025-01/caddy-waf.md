---
title: "Caddy WAF：基于OWASP规则的Web应用防火墙，中间件"
slug: caddy-waf
description: |
  Caddy WAF是一款简单易用的Web应用防火墙中间件，集成了OWASP规则，提供全面的网络攻击防护。它支持IP和DNS过滤、速率限制、GeoIP等多种安全特性，确保应用程序的安全。
tags: 
  - dev
  - opensource
  - security
pubDatetime: 2025-01-06T09:53:05+08:00
ogImage: https://opengraph.githubassets.com/310faf9271712e30824318d9a6fc61c71662a0b3aeb8cbaa8534e4bd917c86c3/fabriziosalmi/caddy-waf
---

[原文链接](https://github.com/fabriziosalmi/caddy-waf)

---

# 🛡️ Caddy WAF Middleware

[](#️-caddy-waf-middleware)

A **simple Web Application Firewall (WAF)** middleware for the Caddy server, designed to provide **comprehensive protection** against web attacks. This middleware integrates seamlessly with Caddy and offers a wide range of security features to safeguard your applications.

***

## 📑 Table of Contents

[](#-table-of-contents)

1. [🌟 Key Features](#-key-features)

2. [🚀 Installation](#-installation)
   * [Final Notes](#final-notes)

3. [🛠️ Configuration](#%EF%B8%8F-configuration)
   * [Basic Caddyfile Setup](#basic-caddyfile-setup)

4. [⚙️ Configuration Options](#%EF%B8%8F-configuration-options)

5. [📜 Rules Format (`rules.json`)](#-rules-format-rulesjson)
   * [Rule Fields](#rule-fields)

6. [🛡️ Protected Attack Types](#%EF%B8%8F-protected-attack-types)

7. [🚫 Blacklist Formats](#-blacklist-formats)

   * [IP Blacklist (`ip_blacklist.txt`)](#ip-blacklist-ip_blacklisttxt)
   * [DNS Blacklist (`dns_blacklist.txt`)](#dns-blacklist-dns_blacklisttxt)

8. [⏱️ Rate Limiting](#%EF%B8%8F-rate-limiting)

9. [🌍 Country Blocking](#-country-blocking)

10. [🔄 Dynamic Updates](#-dynamic-updates)

11. [🧪 Testing](#-testing)

    * [Basic Testing](#basic-testing)
    * [Load Testing](#load-testing)

* [Security Testing Suite](#security-testing-suite)

12. [🐳 Docker Support](#-docker-support)

13. [🐍 Rule/Blacklist Population Scripts](#-ruleblacklist-population-scripts)

    * [get\_owasp\_rules.py](#get_owasp_rulespy)
    * [get\_blacklisted\_ip.py](#get_blacklisted_ippy)
    * [get\_blacklisted\_dns.py](#get_blacklisted_dnspy)

14. [📜 License](#-license)

15. [🙏 Contributing](#-contributing)

***

## 🌟 Key Features

[](#-key-features)

* **Rule-based request filtering** with regex patterns.
* **IP and DNS blacklisting** to block malicious traffic.
* **Country-based blocking** using MaxMind GeoIP2.
* **Rate limiting** per IP address to prevent abuse.
* **Anomaly scoring system** for detecting suspicious behavior.
* **Request inspection** (URL, args, body, headers, cookies, user-agent).
* **Protection against common attacks** (SQL injection, XSS, RCE, Log4j, etc.).
* **Detailed logging and monitoring** for security analysis.
* **Dynamic rule reloading** without server restart.
* **Severity-based actions** (`block`, `log`, `allow`, `detect`) for fine-grained control.

## 🚀 Installation

[](#-installation)

```
# Step 1: Clone the caddy-waf repository from GitHub
# This downloads the source code for the caddy-waf module to your local machine.
git clone https://github.com/fabriziosalmi/caddy-waf.git

# Step 2: Navigate into the caddy-waf directory
# This changes your current working directory to the caddy-waf project folder.
cd caddy-waf

# Step 3: Clean up and update the go.mod file
# This ensures that your project's dependencies are up-to-date and consistent.
go mod tidy

# Step 4: Fetch and install the required Go modules
# This downloads and installs the caddy-waf module, Caddy v2, and the maxminddb-golang library.
go get -v github.com/fabriziosalmi/caddy-waf github.com/caddyserver/caddy/v2 github.com/oschwald/maxminddb-golang

# Step 5: Download the GeoLite2 Country database
# This downloads the GeoLite2 Country database, which is required for IP-based country filtering.
wget https://git.io/GeoLite2-Country.mmdb

# Step 6: Clean up previous build artifacts
# This removes any temporary build directories from previous builds to ensure a clean build environment.
rm -rf buildenv_*

# Step 7: Build Caddy with the caddy-waf module
# This compiles Caddy and includes the caddy-waf module as a custom plugin.
xcaddy build --with github.com/fabriziosalmi/caddy-waf=./

# Step 8: Run the compiled Caddy server
# This starts the Caddy server with the caddy-waf module enabled.
./caddy run
```

### Final Notes

[](#final-notes)

* If you encounter any issues, ensure that your Go environment is set up correctly and that you're using a compatible version of Go (as specified in the `caddy-waf` repository's `go.mod` file).

* After building Caddy with `xcaddy`, the resulting binary will include the WAF middleware. You can verify this by running:

  ```
  ./caddy list-modules
  ```

  Look for the `http.handlers.waf` module in the output.

## 🛠️ Configuration

[](#️-configuration)

### Basic Caddyfile Setup

[](#basic-caddyfile-setup)

```
{
    auto_https off
    admin off
    debug
}

:8080 {
    log {
        output stdout
        format console
        level DEBUG
    }

    route {
        waf {
            # Anomaly threshold will block request if the score is => the threshold
            anomaly_threshold 5

            # Rate limiting: 1000 requests per 1 minute
            rate_limit 1000 1m

            # Rules and blacklists
            rule_file rules.json
            ip_blacklist_file ip_blacklist.txt
            dns_blacklist_file dns_blacklist.txt

            # Country blocking (requires MaxMind GeoIP2 database)
            block_countries GeoLite2-Country.mmdb RU CN KP

            # Whitelist countries (requires MaxMind GeoIP2 database)
            # whitelist_countries GeoLite2-Country.mmdb US

             # Define actions based on severity
            severity critical block
            severity high block
            severity medium log
            severity low log

             # Set Log Severity
            log_severity debug

            #Set Log JSON output
            log_json
        }
        respond "Hello, world!" 200
    }
}
```

## ⚙️ Configuration Options

[](#️-configuration-options)

| Option                | Description                                              | Example                                              |
| --------------------- | -------------------------------------------------------- | ---------------------------------------------------- |
| `anomaly_threshold`   | Sets the anomaly score threshold.                        | `anomaly_threshold 20`                               |
| `rule_file`           | JSON file containing WAF rules                           | `rule_file rules.json`                               |
| `ip_blacklist_file`   | File with blocked IPs/CIDR ranges                        | `ip_blacklist_file blacklist.txt`                    |
| `dns_blacklist_file`  | File with blocked domains                                | `dns_blacklist_file domains.txt`                     |
| `rate_limit`          | Rate limiting config                                     | `rate_limit 100 1m`                                  |
| `block_countries`     | Country blocking config                                  | `block_countries GeoLite2-Country.mmdb RU CN NK`     |
| `whitelist_countries` | Country whitelisting config                              | `whitelist_countries GeoLite2-Country.mmdb US GB CA` |
| `severity`            | Define actions based on severity levels                  | `severity critical block`                            |
| `log_severity`        | Sets the minimum logging severity level for this module. | `log_severity debug`                                 |
| `log_json`            | Enables JSON log output                                  | `log_json`                                           |

## 📜 Rules Format (`rules.json`)

[](#-rules-format-rulesjson)

Rules are defined in a JSON file. Each rule specifies a pattern to match, targets to inspect, and actions to take.

```
[
    {
        "id": "wordpress-brute-force",
        "phase": 2,
        "pattern": "(?i)(?:wp-login\\.php|xmlrpc\\.php).*?(?:username=|pwd=)",
        "targets": ["URI", "ARGS"],
        "severity": "HIGH",
        "action": "block",
        "score": 8,
        "description": "Block brute force attempts targeting WordPress login and XML-RPC endpoints."
    }
]
```

### Rule Fields

[](#rule-fields)

| Field         | Description                                         | Example                         |
| ------------- | --------------------------------------------------- | ------------------------------- |
| `id`          | Unique rule identifier                              | `sql_injection`                 |
| `phase`       | Processing phase (1-2)                              | `1`                             |
| `pattern`     | Regular expression pattern                          | \`(?i)(?:select                 |
| `targets`     | Areas to inspect                                    | `["ARGS", "BODY"]`              |
| `severity`    | Rule severity (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`) | `CRITICAL`                      |
| `action`      | Action to take (`block`, `log`, `allow`, `detect`)  | `block`                         |
| `score`       | Score for anomaly detection                         | `10`                            |
| `description` | Rule description                                    | `Block SQL injection attempts.` |

## 🛡️ Protected Attack Types

[](#️-protected-attack-types)

1. **SQL Injection**

   * Basic `SELECT`/`UNION` injections
   * Time-based injection attacks
   * Boolean-based injections

2. **Cross-Site Scripting (XSS)**

   * Script tag injection
   * Event handler injection
   * SVG-based XSS

3. **Path Traversal**

   * Directory traversal attempts
   * Encoded path traversal
   * Double-encoded traversal

4. **Remote Code Execution (RCE)**

   * Command injection
   * Shell command execution
   * System command execution

5. **Log4j Exploits**

   * JNDI lookup attempts
   * Nested expressions

6. **Protocol Attacks**

   * Git repository access
   * Environment file access
   * Configuration file access

7. **Scanner Detection**

   * Common vulnerability scanners
   * Web application scanners
   * Network scanning tools

## 🚫 Blacklist Formats

[](#-blacklist-formats)

### IP Blacklist (`ip_blacklist.txt`)

[](#ip-blacklist-ip_blacklisttxt)

```
192.168.1.1
10.0.0.0/8
2001:db8::/32
```

### DNS Blacklist (`dns_blacklist.txt`)

[](#dns-blacklist-dns_blacklisttxt)

```
malicious.com
evil.example.org
```

## ⏱️ Rate Limiting

[](#️-rate-limiting)

Configure rate limits using requests count and time window:

```
# 100 requests per minute
rate_limit 100 1m

# 10 requests per second
rate_limit 10 1s

# 1000 requests per hour
rate_limit 1000 1h
```

## 🌍 Country Blocking

[](#-country-blocking)

Block traffic from specific countries using ISO country codes:

```
# Block requests from Russia, China, and North Korea
block_countries /path/to/GeoLite2-Country.mmdb RU CN KP
```

## 🔄 Dynamic Updates

[](#-dynamic-updates)

Rules and blacklists can be updated without server restart:

1. Modify `rules.json` or blacklist files.
2. Reload Caddy: `caddy reload`.

## 🧪 Testing

[](#-testing)

### Basic Testing

[](#basic-testing)

```
# Test rate limiting
for i in {1..10}; do curl -i http://localhost:8080/; done

# Test country blocking
curl -H "X-Real-IP: 1.2.3.4" http://localhost:8080/

# Test SQL injection protection
curl "http://localhost:8080/?id=1+UNION+SELECT+*+FROM+users"

# Test XSS protection
curl "http://localhost:8080/?input=<script>alert(1)</script>"
```

### Load Testing

[](#load-testing)

```
ab -n 1000 -c 100 http://localhost:8080/
```

### Security Testing Suite

[](#security-testing-suite)

A `test.sh` script is included in this repository to perform a comprehensive security test suite. This script sends a series of forged `curl` requests, each designed to simulate a different type of attack.

Below is an example of how to run the script and a sample output:

```
caddy-waf % ./test.sh
WAF Security Test Suite
Target: http://localhost:8080
Date: Dom  5 Gen 2025 16:00:37 CET
----------------------------------------
[✗] SQL Injection - SQL Server Version                           [200]
[✗] SQL Injection - SQL Server Time Delay                        [200]
[✓] SQL Injection - Oracle Time Delay                            [403]
[✗] SQL Injection - Error Based 1                                [200]
[✗] SQL Injection - Error Based 2                                [200]
[✗] SQL Injection - Error Based 3                                [200]
[✗] SQL Injection - MySQL user                                   [200]
[✗] SQL Injection - PostgreSQL user                              [200]
[✗] SQL Injection - Case Variation                               [200]
[✗] SQL Injection - Whitespace Variation                         [200]
[✗] SQL Injection - Obfuscation Variation                        [200]
[✗] SQL Injection - Unicode Variation                            [200]
[✗] SQL Injection - Triple URL Encoded Variation                 [200]
[✗] SQL Injection - OOB DNS Lookup                               [200]
[✗] SQL Injection - Oracle OOB DNS Lookup                        [200]
[✓] SQL Injection - Header - Basic Select                        [403]
[✓] SQL Injection - Cookie - Basic Select                        [403]
[✗] SQL Injection - Header - Basic Select                        [200]
[✗] SQL Injection - JSON body                                    [200]
[✓] XSS - Basic Script Tag                                       [403]
[✓] XSS - IMG Onerror                                            [403]
[✓] XSS - JavaScript Protocol                                    [403]
[✓] XSS - SVG Onload                                             [403]
[✓] XSS - Anchor Tag JavaScript                                  [403]
[✓] XSS - URL Encoded Script                                     [403]
[✓] XSS - Double URL Encoded                                     [403]
[✓] XSS - URL Encoded IMG                                        [403]
[✓] XSS - Body Onload                                            [403]
[✓] XSS - Input Onfocus Autofocus                                [403]
[✓] XSS - Breaking Out of Attribute                              [403]
[✓] XSS - HTML Encoded                                           [403]
[✓] XSS - IFRAME srcdoc                                          [403]
[✓] XSS - Details Tag                                            [403]
[✓] XSS - HTML Comment Breakout                                  [403]
[✓] Path Traversal - Basic                                       [403]
[✓] Path Traversal - Double Dot                                  [403]
[✓] Path Traversal - Triple Dot                                  [403]
[✓] Path Traversal - URL Encoded                                 [403]
[✗] Path Traversal - Double URL Encoded                          [200]
[✓] Path Traversal - Mixed Slashes                               [403]
[✗] Path Traversal - UTF-8 Encoded                               [200]
[✓] Path Traversal - Encoded and Literal                         [403]
[✓] Path Traversal - Mixed Encoding                              [403]
[✗] Path Traversal - Multiple Slashes                            [200]
[✓] RCE - Basic Command                                          [403]
[✓] RCE - Base64 Command                                         [403]
[✓] RCE - Backticks                                              [403]
[✓] RCE - List Files                                             [403]
[✓] RCE - Uname                                                  [403]
[✓] RCE - ID                                                     [403]
[✓] RCE - whoami Command                                         [403]
[✓] RCE - Echo Test                                              [403]
[✓] RCE - Hex Encoded Command                                    [403]
[✓] RCE - Curl Request                                           [403]
[✓] RCE - Wget Request                                           [403]
[✓] RCE - Ping                                                   [403]
[✓] RCE - PowerShell Command                                     [403]
[✗] Log4j - JNDI LDAP                                            [200]
[✗] Log4j - Environment                                          [200]
[✗] Log4j - JNDI RMI                                             [200]
[✗] Log4j - System Property                                      [200]
[✗] Log4j - Lowercase                                            [200]
[✗] Log4j - Uppercase                                            [200]
[✗] Log4j - Date                                                 [200]
[✓] Log4j - Base64                                               [403]
[✗] Log4j - Partial Lookup                                       [200]
[✗] Log4j - URL Encoded                                          [200]
[✓] Header - SQL Injection                                       [403]
[✓] Header - XSS Cookie                                          [403]
[✓] Header - Path Traversal                                      [403]
[✓] Header - Custom X-Attack                                     [403]
[✗] Header -  X-Forwarded-Host                                   [200]
[✓] Header - User-Agent SQL                                      [403]
[✗] Header -  Host Spoof                                         [200]
[✓] Header -  Accept-Language                                    [403]
[✓] Protocol - Git Access                                        [403]
[✓] Protocol - Env File                                          [403]
[✓] Protocol - htaccess                                          [403]
[✗] Protocol - Web.config Access                                 [200]
[✓] Protocol - Java Web Descriptor                               [403]
[✓] Protocol - SVN Access                                        [403]
[✗] Protocol - Robots.txt                                        [200]
[✗] Protocol - VS Code Settings                                  [200]
[✗] Protocol - config.php Access                                 [200]
[✗] Protocol - Apache Server Status                              [200]
[✓] Valid - Homepage                                             [200]
[✓] Valid - API Endpoint                                         [200]
[✓] Scanner - SQLMap                                             [403]
[✓] Scanner - Acunetix                                           [403]
[✓] Scanner - Nikto                                              [403]
[✓] Scanner - Nmap                                               [403]
[✓] Scanner - Dirbuster                                          [403]
[✓] Valid - Health Check                                         [200]
[✓] Valid - Chrome Browser                                       [200]
[✗] Scanner -  Burp Suite                                        [200]
[✓] Scanner - OWASP ZAP                                          [403]
[✓] Scanner - Nessus                                             [403]
[✓] Scanner - Qualys                                             [403]
[✗] Scanner -  Wfuzz                                             [200]
[✓] Scanner -  OpenVAS                                           [403]
----------------------------------------
Results Summary
Total Tests: 100
Passed: 63
Failed: 37
Pass Percentage: 63%
```

The script performs 100 tests for different attack vectors, and shows the result for each test.

## 🐳 Docker Support

[](#-docker-support)

A `Dockerfile` is included to simplify building a Docker image with the Caddy server and WAF middleware. Here's how to use it:

```
# Build the Docker image
docker build -t caddy-waf .

# Run the Docker container
docker run -p 8080:8080 caddy-waf
```

The Dockerfile sets up the required environment, builds the Caddy server with the WAF middleware, and exposes port 8080.

## 🐍 Rule/Blacklist Population Scripts

[](#-ruleblacklist-population-scripts)

Three Python scripts are provided in this repository to help automate the population of your rules and blacklists:

### `get_owasp_rules.py`

[](#get_owasp_rulespy)

This script fetches the OWASP core rules and converts them into the JSON format required for the WAF rules. You can use this script to automatically download and update your rules with the latest OWASP configurations.

```
python3 get_owasp_rules.py
```

### `get_blacklisted_ip.py`

[](#get_blacklisted_ippy)

This script downloads the blacklisted IPs from several external sources. It consolidates the IPs into a single `ip_blacklist.txt` file, which can be used for blocking IPs.

```
python3 get_blacklisted_ip.py
```

### `get_blacklisted_dns.py`

[](#get_blacklisted_dnspy)

This script downloads blacklisted domains from various sources and consolidates them into the `dns_blacklist.txt` file.

```
python3 get_blacklisted_dns.py
```

These scripts provide a quick start and enable users to dynamically update their rules and blacklists using third-party sources.

## 📜 License

[](#-license)

This project is licensed under the **AGPLv3 License**.

## 🙏 Contributing

[](#-contributing)

Contributions are welcome! Please open an issue or submit a pull request.


