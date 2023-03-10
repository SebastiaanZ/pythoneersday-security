# Pythoneersday Security
- **Date:** 10 May 2023
- **Topic:** Common Vulnerabilities & Security Testing
- **Authors:** Ordina Pythoneers / Sebastiaan Zeeff & Jeremy Vriens

## IMPORTANT: Do not browse the repository

While you may want to immediately explore the repository, this will ruin most of
the fun.

One of the goals today is to find vulnerabilities in websites using a
security testing tool and your creativity. Since the source code of the views is
available in this repository, looking at the implementation may already reveal
those deliberate vulnerabilities.

Please don't explore the repository beyond this README-file before completing 
the exercises unless specifically instructed to do so.

# Part 1: Common Vulnerabilities

1. Go to https://www.hacksplaining.com/lessons
2. Sign up for free with an OAuth account
3. Learn about common vulnerabilities
    - We recommend that you start with SQL Injection, Privilege Escalation,
      and Broken Access Control. These will be the most relevant for the second
      half of the workshop.

If you're done quickly and have already achieved your yellow belt in the
security journey, check out the "Web App Testing" track.


# Part 2: The Hacky Notes App

## Preparation

First of all, make sure that you have a **recent version of Python** (3.10+)
installed. We are not going to write code in Python today, but we are going to 
create a virtual environment to run an instance of the website that we're going
to attack with our security testing tools.

### OWASP ZAP 2.12.0
If you've followed the instructions in the email, you should have already 
installed the OWASP ZAP application. If not, follow these instructions.

All instructions in this readme were written for ZAP 2.12.0, so I'd recommend
making sure you install that version.

#### Step 1: Install a Java Development Kit (Windows/Linux only)
OWASP Zap requires Java 11+ to run. **It's included in the Apple installer**,
but you need to install Java separately if you're using Windows or Linux.

1. Please visit https://www.oracle.com/java/technologies/downloads/
2. Install the JDK for either Java 17 LTS or Java 19 for your platform

#### Step 2: Install OWASP Zed Attack Proxy

1. Please install OWASP Zap from https://www.zaproxy.org/download/ 

### Configuring ZAP and your browser

ZAP works by intercepting, and allowing you to modify, the traffic between your
browser and a web server. This means that you need to configure your browser to
use ZAP as an intermediate proxy.

Personally, I use Firefox, but the steps are similar for other browsers, such as
Chrome and Edge.


#### Step 1: Configure the ZAP Proxy
1. Open ZAP.
2. Select "No, I do not want to persist this session at this moment in time" and
   click start.
3. In the top menu, go to `Tools > Options`
4. Navigate to `Options > Network > Local Servers/Proxies`
5. Check that main proxy is configured as:
    - Address: localhost
    - Port: 8080 (or another port, as long as you remember it)

#### Step 2: Configure the ZAP Root CA Certificate (Optional)
This step is optional, as our localhost webserver will not use SSL, but I've
included these instruction for if you want to use ZAP on TLS-enabled connections
in the future.

**Full disclosure:** This will install a Root CA Certificate for ZAP in your
browser. This allows ZAP to proxy between your browser and a web server even if
the connection is (supposed to be) secured with TLS.

1. Open the options menu again (`Tools > Options`)
2. Navigate to `Options > Network > Server Certificates`
3. Click `Generate` to generate a new Root CA Certificate for ZAP
4. Click on `Save` to save the certificate to a file
    - Remember where you save the file! You'll need it later.
5. Click "Ok" to exit the options menu
6. Open Firefox
7. Go to the Firfox Settings (`Hamburger Menu > Settings`)
8. Go to `Privacy & Security`
9. Scroll down to `Certificates`
10. Click on `View Certificates...`
11. Click on `Import...`
12. Navigate to the certificates file you exported from ZAP and import it

#### Step 3: Configure Firefox to use the ZAP Proxy

1. Open the Firefox menu (`Hamburger Menu > Add-ons and themes`) 
2. Search for "FoxyProxy Standard" in the `Find more add-ons` search bar
3. Install "FoxyProxy Standard" (author: Eric H. Jung) and enable it
4. Click on the FoxyProxy and click on the `Options` button in the modal
5. Click on `+ Add` in the left-hand menu
6. Fill in these details:
    - **Title or Description:** ZAP
    - **Proxy Type:** HTTP
    - **Proxy IP address or DNS name:** localhost
    - **Port:** 8080 (or the other port from earlier)
7. Click `Save & Edit Patterns`
8. In the `White Patterns` list, modify the first (and only) line:
    - Change the `Name` from "all URLs" to "localhost"
    - Change the pattern to `localhost`
    - Change the `Type` to "Reg Exp"
9. Click `Save`
10. You can now close the FoxyProxy settings screen
11. Click on the FoxyProxy extension icon and select the option "Use Enabled
    Proxies By Patterns and Order". This should make sure that FoxyProxy only
    redirects traffic to `localhost` to the ZAP proxy.


#### Step 4: Get hacking!

Before you clone the repository, this is another friendly reminder not to browse
the repository. It takes all the fun out of the challenges!

1. Clone the repository using `git`
2. Create virtual environment with Python 3.10+ and activate it
3. Install the requirements with `pip install -r requirements.txt`
4. Run `python manage.py start` to start the project
5. Visit http://localhost:8888
6. Start with the tutorial
7. Try other challenges afterwards

Tip: If you think you've screwed up the database, you can reset the project
by running `python manage.py reset`.

---

If you're done quickly, consider doing a few modules of the Security Journey. I
recommend "DevSecOps" and "Web App Testing" as highly relevant Green Belt tracks
for developers.
