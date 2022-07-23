# KBRA Data Scraper


A Python script to scrape business registration data from ARBK's website.
The Business Registration Agency [KBRA](https://arbk.rks-gov.net/) is the only responsible institution for the registration of Kosovo businesses.

## Requirements
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/)

## Installation

```
python -m pip install requests
python -m pip install selenium
```

Install requirements from requirements.txt file
```
pip install -r requirements.txt
```

## Usage
```
Business Number: 80400721

Emri i biznesit: .GashI-Test B.I.
==================================================
Emri tregtar: N.N.Sh..,,Gashi-Test"
==================================================
Lloji biznesit: Biznes individual
==================================================
Numri unik identifikues: ///
==================================================
Numri i biznesit: 80400721
==================================================
Numri Fiskal: ///
==================================================
Numri punëtorëve: 1
==================================================
Data e regjistrimit: 06/03/2001
==================================================
Komuna: Pejë
==================================================
Adresa: Dubovë
==================================================
Telefoni: ///
==================================================
E-mail: ///
==================================================
Statusi në ARBK: Shuar
==================================================
Statusi në ATK: ///
==================================================
```
