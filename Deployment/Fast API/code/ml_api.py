# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:46:45 2024

@author: sayon
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy as np
import os
from tld import get_tld
from urllib.parse import urlparse

def get_url_length(url):
    return len(url)

def get_domain_length(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domain_length = len(domain)
    return domain_length

import ipaddress

def is_domain_ip(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc  # Extract the domain part from the URL
        ipaddress.ip_address(domain)  # Check if the domain is a valid IP address
        return 1
    except ValueError:
        return 0

def tld_length(tld):
    if tld:
        return len(tld)
    else:
        return -1

def char_continuation_rate(url):
    continuous_count = 0
    total_count = len(url)

    for i in range(1, len(url)):
        if url[i] == url[i - 1]:
            continuous_count += 1

    if total_count > 0:
        continuation_rate = continuous_count / total_count
    else:
        continuation_rate = 0.0

    return continuation_rate

def url_character_prob(url):
    char_count = {}
    total_chars = len(url)

    for char in url:
        char_count[char] = char_count.get(char, 0) + 1

    char_prob = {char: count / total_chars for char, count in char_count.items()}

    # Calculate the mean probability
    mean_prob = sum(char_prob.values()) / len(char_prob)

    return mean_prob

def number_of_subdomains(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    if domain:
        num_subdomains = domain.count('.')
    else:
        num_subdomains = 0

    return num_subdomains

def has_obfuscation(url):
    # List of common obfuscation patterns to detect
    obfuscation_patterns = [
        '%',                     # Percentage encoding
        '\\x',                   # Hexadecimal encoding
        '&#',                    # HTML entity encoding
        '\\u',                   # Unicode encoding (corrected)
        'javascript:',           # JavaScript code injection
        'data:',                 # Data URL scheme
        'blob:',                 # Blob URL scheme
        'onerror', 'onload',     # Event handlers
        'document.cookie',       # Access to cookies
        'eval(', 'exec(',        # Evaluation functions
        'unescape(',             # Unescaping
        'String.fromCharCode(', # Constructing strings
        'String.fromCodePoint(', # Constructing strings
        'String.raw(',           # Constructing strings
    ]

    # Check if any obfuscation pattern is found in the URL
    for pattern in obfuscation_patterns:
        if pattern in url.lower():
            return 1  # Obfuscation detected

    return 0  # No obfuscation detected

def number_of_obfuscated_chars(url):
    # List of common obfuscation patterns to detect
    obfuscation_patterns = [
        '%',     # Percentage encoding
        '&#',    # HTML entity encoding
        '\\u',   # Unicode encoding
        '\\x',   # Hexadecimal encoding
        '\u202E', '\u200E', '\u200F', '\u202A', '\u202B', '\u202C'  # Directional formatting characters
    ]

    # Initialize the counter for obfuscated characters
    num_obfuscated_chars = 0

    # Check for each obfuscation pattern in the URL
    for pattern in obfuscation_patterns:
        # Count the occurrences of the obfuscation pattern in the URL
        num_obfuscated_chars += url.lower().count(pattern)

    return num_obfuscated_chars

def obfuscation_ratio(url):
    # List of common obfuscation patterns to detect
    obfuscation_patterns = [
        '%',     # Percentage encoding
        '&#',    # HTML entity encoding
        '\\u',   # Unicode encoding
        '\\x',   # Hexadecimal encoding
        '\u202E', '\u200E', '\u200F', '\u202A', '\u202B', '\u202C'  # Directional formatting characters
    ]

    # Count the total number of characters in the URL
    total_chars = len(url)

    # Initialize the counter for obfuscated characters
    num_obfuscated_chars = 0

    # Check for each obfuscation pattern in the URL
    for pattern in obfuscation_patterns:
        # Count the occurrences of the obfuscation pattern in the URL
        num_obfuscated_chars += url.lower().count(pattern)

    # Calculate the obfuscation ratio
    obfuscation_ratio = num_obfuscated_chars / total_chars if total_chars > 0 else 0.0

    return obfuscation_ratio

def number_of_letters_in_url(url):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    num_letters = sum(url.count(letter) for letter in letters)

    return num_letters

def letter_ratio_in_url(url):
    num_letters = number_of_letters_in_url(url)

    total_chars = len(url)

    if total_chars > 0:
        letter_ratio = num_letters / total_chars
    else:
        letter_ratio = 0.0

    return letter_ratio

def number_of_digits_in_url(url):
    digits = '0123456789'

    num_digits = sum(url.count(digit) for digit in digits)

    return num_digits

def digit_ratio_in_url(url):
    num_digits = number_of_digits_in_url(url)

    total_chars = len(url)

    if total_chars > 0:
        digit_ratio = num_digits / total_chars
    else:
        digit_ratio = 0.0

    return digit_ratio

def number_of_ampersand_in_url(url):
    num_ampersand = url.count('&')

    return num_ampersand

def number_of_other_special_chars_in_url(url):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./:?&=%'

    num_other_special_chars = sum(1 for char in url if char not in allowed_chars)

    return num_other_special_chars

def special_char_ratio_in_url(url):
    num_special_chars = number_of_other_special_chars_in_url(url)

    total_chars = len(url)

    if total_chars > 0:
        special_char_ratio = num_special_chars / total_chars
    else:
        special_char_ratio = 0.0

    return special_char_ratio

def is_https(url):
    # Check if the URL starts with "https://"
    if url.startswith("https://"):
        return 1
    else:
        return 0
    
def calculate_tld_legitimate_prop(url):
    try:
        # Get the Top-Level Domain (TLD) from the URL
        tld = get_tld(url, fail_silently=True)

        # List of commonly recognized TLDs used by legitimate websites
        legitimate_tlds = ['com', 'net', 'org', 'edu', 'gov']

        # Check if the extracted TLD is in the list of legitimate TLDs
        if tld in legitimate_tlds:
            return 1.0  # TLD is considered legitimate
        else:
            return 0.0  # TLD is not considered legitimate
    except:
        return -1  # Error: Unable to extract TLD

import re
#Use of IP or not in domain
def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        # print match.group()
        return 1
    else:
        # print 'No matching pattern found'
        return 0

def abnormal_url(url):
    hostname = urlparse(url).hostname
    hostname = str(hostname)
    match = re.search(hostname, url)
    if match:
        # print match.group()
        return 1
    else:
        # print 'No matching pattern found'
        return 0

def count_per(url):
    return url.count('%')

def count_ques(url):
    return url.count('?')

def count_hyphen(url):
    return url.count('-')

def count_equal(url):
    return url.count('=')

def count_www(url):
  url.count('www')
  return url.count('www')

def count_atrate(url):
  return url.count('@')

def no_of_dir(url):
  urldir = urlparse(url).path
  return urldir.count('/')

def no_of_embed(url):
  urldir = urlparse(url).path
  return urldir.count('//')

def count_https(url):
    return url.count('https')

def count_http(url):
    return url.count('http')

def count_dot(url):
  count_dot = url.count('.')
  return count_dot

def shortening_service(url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',
                      url)
    if match:
        return 1
    else:
        return 0

def hostname_length(url):
    return len(urlparse(url).netloc)

def suspicious_words(url):
    match = re.search('PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr',
                      url)
    if match:
        return 1
    else:
        return 0

def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits

def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters

from googlesearch import search

def google_index(url):
  site = search(url, 5)
  return 1 if site else 0

def fd_length(url):
    urlpath= urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0
    
# Request functions
    
import requests

# Function to check if the URL is accessible
def check_url_access(url):
    try:
        response = requests.get(url)
        return 1  # Return 1 if the URL is accessible
    except requests.exceptions.RequestException:
        return 0  # Return 0 if there's an error accessing the URL

# Function to check if the URL is redirected
def check_redirect(url):
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 301 or response.status_code == 302:
            return 0  # Return 0 if the URL is redirected
        else:
            return 1  # Return 1 if the URL is not redirected
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None
    
import whois
import ssl
import socket
import urllib.parse
import tldextract

# Function to send an HTTP request to the given URL and retrieve the response
def send_http_request(url):
    try:
        response = requests.get(url, timeout=10)  # Set a timeout for the request
        if response.status_code == 200:
            return 1 if not analyze_content(response) else 0
        else:
            print(f"Error accessing {url}: Status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None

# Function to analyze the content of the response for phishing indicators
def analyze_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            # Implement content analysis logic here
            # Example: Check for presence of known phishing keywords or patterns
            phishing_keywords = ['login', 'password', 'bank', 'secure']
            for keyword in phishing_keywords:
                if re.search(keyword, content, re.IGNORECASE):
                    return 0  # Phishing indicator found
            return 1  # No phishing indicator found
        else:
            print(f"Error: Unable to fetch content from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error analyzing content for {url}: {e}")
        return None

import datetime

def verify_ssl_certificate(url):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=url) as ssock:
                cert = ssock.getpeercert()
                if cert:
                    # Check if the certificate is valid and issued by a trusted CA
                    if ssl.match_hostname(cert, url):
                        # Check if the certificate is not expired
                        cert_not_after = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                        if cert_not_after > datetime.datetime.now():
                            return 1  # Valid SSL certificate
                        else:
                            return 0  # Expired SSL certificate
                    else:
                        return 0  # Certificate does not match hostname
                else:
                    return 0  # No certificate available
    except Exception as e:
        print(f"Error verifying SSL certificate for {url}: {e}")
        return None  # Error occurred

def query_whois(url):
    try:
        # Extract domain from the URL
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        
        # Perform WHOIS query for the extracted domain
        w = whois.whois(domain)
        
        if w:
            # Check if WHOIS information indicates the domain is legitimate
            # Note: WHOIS information alone might not be sufficient for a definitive conclusion
            if 'creation_date' in w and 'expiration_date' in w:
                return 1  # Legitimate domain
            else:
                return 0  # Suspicious domain
        else:
            return 0  # Suspicious domain
    except Exception as e:
        # Handle any errors that occur during the WHOIS query
        print(f"Error querying WHOIS information for {domain}: {e}")
        return 0  # Suspicious domain due to error

def check_domain_reputation(url):
    # Extract domain from the URL
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    # Example: Using a hypothetical API for domain reputation check
    api_url = "https://example.com/domain-reputation-api"
    payload = {'domain': domain}
    
    try:
        response = requests.get(api_url, params=payload)
        if response.status_code == 200:
            result = response.json()
            if result['blacklisted']:
                return 0  # Domain is blacklisted
            else:
                return 1  # Domain is not blacklisted
        else:
            # API request failed, return an error code or handle the error as needed
            return -1  # Error occurred
    except Exception as e:
        # Handle exceptions such as network errors
        print("Exception occurred:", e)
        return -1  # Error occurred

def check_url_blacklist(url):
    # Example: Using a hypothetical API for URL blacklist check
    api_url = "https://example.com/blacklist-api"
    payload = {'url': url}
    try:
        response = requests.get(api_url, params=payload)
        if response.status_code == 200:
            result = response.json()
            if result['blacklisted']:
                return 0  # Phishing URL
            else:
                return 1  # Safe URL
        else:
            # API request failed, return an error code or handle the error as needed
            return -1  # Error occurred
    except Exception as e:
        # Handle exceptions such as network errors
        print("Exception occurred:", e)
        return -1  # Error occurred

# Function to analyze the IP address associated with the URL
def analyze_ip_address(url):
    try:
        # Extract domain from the URL
        domain = urllib.parse.urlparse(url).netloc
        
        # Get the IP address associated with the domain
        ip_address = socket.gethostbyname(domain)
        
        # Check the IP address against threat intelligence sources
        if check_blacklist(ip_address):
            return 1  # Malicious IP address
        else:
            return 0  # Clean IP address
    except Exception as e:
        print(f"Error analyzing IP address for {url}: {e}")
        return None

def check_blacklist(ip_address):
    # Example: Check against a public blacklist
    blacklist_url = f"https://www.abuseipdb.com/check/{ip_address}"
    try:
        response = requests.get(blacklist_url)
        if response.status_code == 200:
            # Check if the IP address is listed in the blacklist
            if "This IP address has been reported" in response.text:
                return True
            else:
                return False
        else:
            print(f"Error checking blacklist for {ip_address}: Status code {response.status_code}")
            return False
    except Exception as e:
        print(f"Error checking blacklist for {ip_address}: {e}")
        return False

# Function to handle different user-agent strings to evade detection
def spoof_user_agent(url):
    try:
        custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36"
        headers = {
            'User-Agent': custom_user_agent
        }
        response = requests.get(url, headers=headers, timeout=10)  # Set a timeout for the request
        if response.status_code == 200:
            return 1 if not analyze_content(response) else 0
        else:
            print(f"Error accessing {url}: Status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None

# Function to handle sessions and cookies
def handle_sessions(url):
    session = requests.Session()
    try:
        response = session.get(url, timeout=10)  # Set a timeout for the request
        if response.status_code == 200:
            return 1 if not analyze_content(response) else 0
        else:
            print(f"Error accessing {url}: Status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None

# Function to handle request timeouts
def handle_request_timeout(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return 1 if not analyze_content(response) else 0
        else:
            print(f"Error accessing {url}: Status code {response.status_code}")
            return None
    except requests.exceptions.Timeout:
        print(f"Timeout accessing {url}")
        return 0  # Treat as clean (no phishing indicators) due to timeout
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None

# Function to perform more advanced checks based on TLD and subdomain
def advanced_url_analysis(url):
    try:
        # Extract domain and subdomain information from the URL
        extracted = tldextract.extract(url)
        domain = extracted.domain
        subdomain = extracted.subdomain
        
        # Check if the domain or subdomain contains known malicious patterns
        if check_malicious_pattern(domain) or check_malicious_pattern(subdomain):
            return 0  # Phishing indicator found
        else:
            # Query WHOIS information for the domain
            if query_whois(domain):
                return 1  # Legitimate domain
            else:
                return 0  # Phishing indicator found
    except Exception as e:
        print(f"Error performing advanced URL analysis for {url}: {e}")
        return None

def check_malicious_pattern(text):
    # Implement logic to check for known malicious patterns in text
    malicious_patterns = ['paypal', 'security', 'login', 'bank', 'phish']
    for pattern in malicious_patterns:
        if pattern in text.lower():
            return True
    return False

def query_whois(domain):
    try:
        w = whois.whois(domain)
        if w:
            # Check if WHOIS information indicates the domain is legitimate
            if 'creation_date' in w and 'expiration_date' in w:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(f"Error querying WHOIS information for {domain}: {e}")
        return False
    
def mainly(url):

    status = []

    status.append(get_url_length(url))
    status.append(get_domain_length(url))
    status.append(is_domain_ip(url))
    tld = get_tld(url,fail_silently=True)
    status.append(tld_length(tld))
    status.append(char_continuation_rate(url))
    status.append(url_character_prob(url))
    status.append(number_of_subdomains(url))
    status.append(has_obfuscation(url))
    status.append(number_of_obfuscated_chars(url))
    status.append(obfuscation_ratio(url))
    status.append(number_of_letters_in_url(url))
    status.append(letter_ratio_in_url(url))
    status.append(number_of_digits_in_url(url))
    status.append(digit_ratio_in_url(url))
    status.append(number_of_ampersand_in_url(url))
    status.append(number_of_other_special_chars_in_url(url))
    status.append(special_char_ratio_in_url(url))
    status.append(is_https(url))
    status.append(calculate_tld_legitimate_prop(url))
    status.append(having_ip_address(url))
    status.append(abnormal_url(url))
    status.append(count_per(url))
    status.append(count_ques(url))
    status.append(count_hyphen(url))
    status.append(count_equal(url))
    status.append(count_www(url))
    status.append(count_atrate(url))
    status.append(no_of_dir(url))
    status.append(no_of_embed(url))
    status.append(count_https(url))
    status.append(count_dot(url))
    status.append(count_http(url))
    status.append(shortening_service(url))
    status.append(hostname_length(url))
    status.append(suspicious_words(url))
    status.append(digit_count(url))
    status.append(letter_count(url))
    status.append(google_index(url))
    status.append(fd_length(url))

    return status

def get_prediction_from_url(test_url):
    
    if(check_url_access(test_url) == 0):
        return "PHISHING"
    
    if(check_url_blacklist(test_url) == 0):
        return "PHISHING"
    
    if(verify_ssl_certificate(test_url) == 0):
        return "PHISHING"
    
    if(send_http_request(test_url) == 0):
        return "PHISHING"
    
    if(check_domain_reputation(test_url) == 0):
        return "PHISHING"
    
    if(spoof_user_agent(test_url) == 0):
        return "PHISHING"
    
    if(handle_sessions(test_url) == 0):
        return "PHISHING"
    
    if(handle_request_timeout(test_url, timeout=5) == 0):
        return "PHISHING"
    
    if(advanced_url_analysis(test_url) == 0):
        return "PHISHING"
    
    #if(analyze_ip_address(test_url) == 0):
        #return "PHISHING"
    
    #if(query_whois(test_url) == 0):
        #return "PHISHING"
    
    #if(analyze_content(test_url) == 0):
        #return "PHISHING"
    
    features_test = mainly(test_url)

    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    features_test = np.array(features_test).reshape((1, -1))

    pred = loaded_model.predict(features_test)
    
    return pred

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv("C:/Users/sayon/Downloads/ML Projects/Malicious URL Detection/hosting/Jojo-URL-Detection/deployment/.env")
#load_dotenv(".env")

# Connect to MongoDB
try:
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("MONGO_PREDICT_DB")]
    collection = db[os.getenv("MONGO_PREDICT_COLLECTION")]
    connection_status = True
except Exception as e:
    connection_status = False
    
# Function to check if URL exists in the database and return its type
def check_url_type(url):
    if not connection_status:
        return False
    
    result = collection.find_one({"url": url})
    if result:
        return result["type"]
    else:
        return False 
    
def add_url_to_database(url, url_type):
    if not connection_status:
        return False
    
    try:
        collection.insert_one({"url": url, "type": url_type})
        return True
    except Exception as e:
        return False

app = FastAPI()

class model_input(BaseModel):
    url : str

# loading the saved model
loaded_model = pickle.load(open('C:/Users/sayon/Downloads/ML Projects/Malicious URL Detection/hosting/Jojo-URL-Detection/model/one.sav','rb'))
#loaded_model = pickle.load(open('trained_model.sav','rb'))

def get_main_website_url(long_url):
    # Parse the URL to extract its components
    parsed_url = urlparse(long_url)

    # Construct the main website URL
    main_website_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"

    return main_website_url

@app.post('/url_prediction')
def url_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    url = input_dictionary['url']
    
    url = get_main_website_url(url)
    
    input_list = [url]
    
    url_type = check_url_type(url)
    if url_type:
        return f"'{url_type}'"
    else:
        prediction = get_prediction_from_url(url)
        
        if prediction[0] == 0:
            diagnosis = "SAFE"

        elif prediction[0] == 1:
            diagnosis = "PHISHING"
        
        # Add URL and its type to the database
        if add_url_to_database(url, diagnosis):
            return diagnosis
        else:
            return "Failure"
