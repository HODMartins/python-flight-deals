# ✈️ Flight Deals Tracker

A Python application that searches for affordable flights, compares current ticket prices against target prices stored in Google Sheets, and sends automated SMS notifications when cheaper flight deals are found.

## 📌 Project Overview

The Flight Deals Tracker automates the process of monitoring airline ticket prices across multiple destinations.

The application retrieves destination information from Google Sheets using the Sheety API, searches for available flights using the SerpApi Google Flights engine, identifies the cheapest available flights, and sends price alerts through Twilio.

The project demonstrates practical Python programming, REST API integration, data processing, environment variable management, and workflow automation.

## 🚀 Features

- **Flight Search:** Retrieves available flight information using SerpApi Google Flights.
- **Price Comparison:** Identifies the lowest available flight price.
- **Google Sheets Integration:** Retrieves destination information and updates flight prices using the Sheety API.
- **SMS Notifications:** Sends flight price alerts using Twilio.
- **Response Caching:** Uses `requests-cache` to reduce repeated API requests.
- **Secure Configuration:** Stores API keys and credentials in environment variables.
- **Object-Oriented Design:** Organizes application functionality into reusable Python classes.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| SerpApi | Google Flights search |
| Sheety API | Google Sheets data integration |
| Twilio | SMS notifications |
| Requests | HTTP requests |
| Requests Cache | API response caching |
| Python Dotenv | Environment variable management |
| Git and GitHub | Version control |

## 📁 Project Structure

```text
python-flight-deals/
│
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

### File Descriptions

**main.py**

Coordinates the application workflow, including retrieving destinations, searching for flights, comparing prices, and triggering notifications.

**data_manager.py**

Communicates with the Sheety API to retrieve destination information and update flight prices.

**flight_search.py**

Sends flight search requests to SerpApi and retrieves flight information.

**flight_data.py**

Processes flight search results and identifies the cheapest available flight.

**notification_manager.py**

Handles SMS notifications through Twilio.

**requirements.txt**

Contains the Python packages required to run the application.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/HODMartins/python-flight-deals.git
cd python-flight-deals
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project's root directory.

Add the required credentials:

```dotenv
SHEETY_URL=your_sheety_endpoint
SHEETY_TOKEN=your_sheety_token

SERPAPI_API_KEY=your_serpapi_key

TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
RECIPIENT_PHONE_NUMBER=your_recipient_phone_number
```

Ensure that the environment variable names match those used in your Python code.

**Security:** Never commit your `.env` file or expose API credentials in your GitHub repository.

### 5. Configure Google Sheets

Create a Google Sheet containing the destination information used by the application.

Example:

| City | IATA Code | Lowest Price |
|---|---|---|
| Lagos | LOS | 900 |
| Toronto | YYZ | 500 |
| Tokyo | HND | 1200 |
| Manchester | MAN | 850 |

Connect the spreadsheet to Sheety and configure the required API permissions.

### 6. Run the application

```bash
python main.py
```

## 🔄 Application Workflow

1. Retrieve destination information from Google Sheets.
2. Select the departure airport and destination airports.
3. Search for available flights using SerpApi.
4. Extract flight prices and travel information.
5. Identify the cheapest available flight.
6. Compare the flight price with the stored target price.
7. Update the Google Sheet when a lower price is found.
8. Send an SMS notification when the configured alert conditions are met.

## 📱 Example Price Alert

```text
LOW PRICE ALERT!

From YYZ to MAN
For only CAD 836 on 2026-11-20
```

The message includes the departure airport, destination airport, flight price, and departure date.

## 🔐 Security

The application uses environment variables to manage sensitive information.

The following files should be excluded from version control:

```gitignore
.env
.env.*
!.env.example
.venv/
__pycache__/
*.pyc
*.sqlite
*.sqlite-shm
*.sqlite-wal
```

API keys, authentication tokens, and other credentials should never be hardcoded into the source code.

## 📈 Future Improvements

- Support searches across multiple departure dates.
- Add email notifications.
- Track historical flight prices.
- Create an interactive dashboard for monitoring flight deals.
- Automate scheduled flight searches.
- Deploy the application to a cloud platform.

## 👨‍💻 Author

**Martins Edegbe**

GitHub: [HODMartins](https://github.com/HODMartins)

## 📄 License

No license has been specified for this project.
