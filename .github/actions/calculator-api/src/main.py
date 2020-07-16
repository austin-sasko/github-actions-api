import urllib.parse
import requests
import random
import os


#define app_id to use for API
app_id = os.environ['WOLFRAM_APP_KEY']
calc_result = ""

#Generate a random math expression with four random nums and a random operator
ops = ["+", "-", "/", "*", "sqrt", "%", "**"]
first_num = random.randint(0, 999999999)
second_num = random.randint(0, 999999999)
third_num = random.randint(0, 999999999)
fourth_num = random.randint(0, 999999999)
expression = f"{first_num}{ops[random.randint(0, len(ops)-1)]}{second_num}{ops[random.randint(0, len(ops)-1)]}{third_num}{ops[random.randint(0, len(ops)-1)]}{fourth_num}"

#need to encode the URL as some operators cause issues
expression_encoded = urllib.parse.quote(expression)

# Make an HTTP GET request to the calculator API that outputs JSON and only fetches the results and decimalapproximation values
calc_url = f"http://api.wolframalpha.com/v2/query?appid={app_id}&output=json&includepodid=Result&includepodid=DecimalApproximation&includepodid=PowerOf 10Representation&input={expression_encoded}"
calc_resp = requests.get(calc_url).json()

# Print the calculation results in decimal format and standard format and  save to variable

for pod in calc_resp['queryresult']['pods']:
    print(pod['subpods'][0]['plaintext'])
    calc_result = f"{calc_result}{pod['subpods'][0]['plaintext']}<br />"

print(calc_result)
# Set the fact-output to resulting value of expression and calc_result
print(f"::set-output name=input_fact::{expression}")
print(f"::set-output name=output_fact::{calc_result}")
