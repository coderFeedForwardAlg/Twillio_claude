# Twilio Webhook Server

This is a Python web server that acts as a webhook for Twilio SMS messages, processing incoming messages using the Orgo Computer API.

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- Twilio account (for production use)
- Orgo API key

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd twillio_python
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install flask python-dotenv
   ```

4. Create a `.env` file in the project root and add your Orgo API key:
   ```
   ORGO_API_KEY=your_orgo_api_key_here
   ```

## Running the Server

1. Start the Flask development server:
   ```bash
   python server.py
   ```
   The server will start on `http://localhost:5000` by default.

2. For local development, you'll need to expose your local server to the internet. You can use ngrok:
   ```bash
   ngrok http 5000
   ```

## Setting Up Twilio Webhook

1. Go to your Twilio Console
2. Navigate to Phone Numbers > Manage > Active numbers
3. Select your Twilio phone number
4. Under "Messaging", set the webhook URL to your public ngrok URL (or your production URL) followed by `/twilio-webhook`
   Example: `https://your-ngrok-url.ngrok.io/twilio-webhook`
5. Set the request type to `HTTP POST`
6. Save the configuration

## Testing

You can test the webhook locally using curl:

```bash
curl -X POST http://localhost:5000/twilio-webhook \
  --data-urlencode "Body=Your message here" \
  --data-urlencode "From=+15551234567" \
  --data-urlencode "To=+15557654321"
```

## Environment Variables

- `ORGO_API_KEY`: Your Orgo Computer API key (required)
- `PORT`: Port to run the server on (default: 5000)

## Project Structure

- `server.py`: Main application file with the webhook endpoint
- `.env`: Environment variables (not committed to version control)
- `.gitignore`: Specifies intentionally untracked files to ignore

