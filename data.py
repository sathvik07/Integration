# import pandas as pd
#
# csv_data = pd.read_csv('sampledata.csv/sample_excel_file_integration_csv.csv')
#
#
import codecs
import csv
import json
from uuid import uuid4
from datetime import datetime
import requests


# csvfile = open("/Users/guggarisathvik/Downloads/sample_excel_file_integration_csv.csv", 'r')
# jsonfile = open("jsondata.json", 'w')

def formated_time(date_str):
    return datetime.strptime(date_str, "%d/%m/%y").strftime("%Y-%m-%d")


def read_csv():
    converted_data = []
    with codecs.open("/Users/guggarisathvik/Downloads/sample_excel_file_integration_csv.csv", "r", "utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            # print(row["Date of Birth"])
            # print(type(row["Date of Birth"]))
            json_data = {
                "requestId": str(uuid4()),
                "userId": f"user_{uuid4().hex}",
                "firstName": row["First Name"],
                "lastName": row["Last Name"],
                "emailId": row["Email"],
                "mobileNo": row["Mobile"],
                "mobile_extension": "+91",
                "dob": formated_time(row["Date of Birth"]),
                "title": "Mr." if row["Gender"] == "Male" else "Mrs.",
                "gender": row["Gender"],
                "extra_fields": {
                    "cost_centre": row["Cost Centre"],
                    "cost_category": row["Cost Category"],
                    "designation": row["Designation"],
                    "department": row["Department"],
                }

            }
            converted_data.append(json_data)
            # rows.append([{field[i] : row[field[i]] for i in range(len(field))}])
        json_output_data = json.dumps(converted_data, indent=4)
        convert_to_json("jsondata.json",json_output_data)
        # print(json_output_data)


def convert_to_json(jsonfile, data):
    with open(jsonfile, 'w', newline='') as jsonfile:
        jsonfile.write(json.dumps(data, sort_keys= False, indent=4, separators=(',',':')))
        # jsonfile.write(json.dumps(data))





def sending_API_request(url, payload, headers):
    response = requests.post(url, data=payload, headers= headers)

    if response.status_code == 200:
        data = response.json()

        userID = data["userId"]
        if userID:
            print(f"UserId recorced successfully in Happay system: {userID}")
        else:
            print("UserId not found in the response")
    else:
        print(f"API request failed:{response.status_code}")



def API_Request_to_add_user():
    url = "https://api-v2.happay.in/auth/v1/cards/add_user/"
    token = "Bearer iiKZR5dXUwwku5xjUMg0D46zQ"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer Token",
        "Token": f"{token}"
    }

    payload =  {
            "requestId": "af921218-0847-4fa8-96cb-e29a21b76f83",
            "userId": "user_dc1a051b1f974929adff44fec6111673",
            "firstName": "Shubham",
            "lastName": "",
            "emailId": "N/A",
            "mobileNo": "7184756131",
            "mobile_extension": "+91",
            "dob": "1998-11-28",
            "title": "Mr.",
            "gender": "Male",
            "extra_fields": {
                "cost_centre": "MARK",
                "cost_category": "BILLABLE",
                "designation": "Manager",
                "department": "Marketing"
            }
        }

    sending_API_request(url, payload, headers)




read_csv()
API_Request_to_add_user()
