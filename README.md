# MIcrosoft-Autolicense
Adds or Removes a license from your Microsoft Tenant

# What Works?
Adding a License to your microsoft Tenant
Removing a License from your microsoft Tenant

# What does not work:
Logging into using MFA (More explained below)

# Prerequisites:
* python3 - https://www.python.org/downloads/ <br>
* Selenium (the version I have is 3.141.0) - https://selenium-python.readthedocs.io/installation.html

* A webdriver from either chrome, firefox, or edge (I use chrome)
  * Selenium Webdriver links and info - https://selenium-python.readthedocs.io/installation.html#drivers
  * chrome webdriver (Make sure to get the same exact version as the version of chrome you have installed) - https://sites.google.com/chromium.org/driver/downloads?authuser=0
* A microsoft account that has Billing Admin rights - https://docs.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide

<b>NOTE</b>: This account cannot have MFA on it as there is no way to pyotp with a 64base qrcode picture. If anyone has any ideas let me know. :)

# Instructions:
Download the `microsoftlicense.py` file into a folder.<br>
Open the `microsoftlicense.py` file using your editor of choice. Look for the dictionary object called `msdata` and enter the following information:
 * msun = your Billing Admin's microsoft account or UPN
 * mspd = your Billing Admin's password (Make sure its insanely long since MFA can't be added to this yet)
 * licensehoice = Either `Add License` or `Remove License` 
 * skuurl = the url of the sku you are trying to increase or decrease in license. An example would be "https://admin.microsoft.com/#/subscriptions/webdirect/93806cd6-849f-4a09-8332-987rb0fdb51a" <br>
 * 
Then (as an admin) from CMD, powershell, or vscode run `python3 microsoftlicense.py` or `python microsoftlicense.py` depending on your version of python and OS.

<b>How can I find my skuurl for the subscription I want to manipulate?</b> - Go to https://admin.microsoft.com/Adminportal/Home#/subscriptions then click on the subscription you want. Use that url for the `skuurl`
