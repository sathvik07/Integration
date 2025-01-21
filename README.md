# Integration

This file contains the code for the interview peoblem. 


The code has features like:
1. Reads data from a CSV file.
2. Converts the CSV data into JSON format.
3. Sends API requests with the following headers:
   - `Authorization: Bearer Token`
   - `Token: Bearer <actual_token>`
   - `payload`
4. request payloads based on CSV data.
5. Validates API responses.



This code has total 5 functions:
1. formated_time --> To convert date to ISO format
2. read_csv --> To read data from csv file and generate json data.
3. convert_to_json --> to write generated json data to a file.
4. def API_Request_to_add_user --> to update the request attributes like url, token, headers, payload.
5. sending_API_request --> this will send an http request and validates the API response and also displays the http status code.




End Result :
1. I was able to convert the csv data to json data, that matches the given sample json format.
2. and i have written function for sending an request with payload, token and headers.


Missing piece:
1. I tried sending an request in postman to check the functionality, but http status code 401, mentioning "Unauthorized: Not allowed from your IP".


----  If you have a moment, could you go through my code to ensure everything is in line with the expectations? I'd love to hear any thoughts you have.
---- and also i would like to get confirmed that the API endpoint is correct and accessible.(Because i have received 401 status code)

<img width="1792" alt="Screenshot 2025-01-22 at 1 39 03 AM" src="https://github.com/user-attachments/assets/3d8d9ab3-5c51-4e88-8313-3f64c76ed65f" />


