from orgo import Computer
import os


# Perform some actions
computer: Computer = Computer(project_id="computer-sxy7vqx", api_key=os.environ.get("ORGO_API_KEY", "no api key"))


from flask import Flask, request
app = Flask(__name__)



def run_computer_prompt(prompt_text: str) -> None:
    # This will run in a separate thread
    message = f"prompt roo code to {prompt_text} by writing an appropriate prompt. then keep hitting Accept as needed."
    computer.prompt(message)



@app.route('/twilio-webhook', methods=['POST'])
def twilio_webhook() -> str:
    # Twilio sends data as form parameters in a POST request
    incoming_message: str | None = request.form.get('Body')
    
    if incoming_message is not None:

        run_computer_prompt(incoming_message)
        response: str = "okay, working on it!" 
        # Twilio expects a TwiML (Twilio Markup Language) response
        # to know how to respond to the sender.
        # For simply acknowledging receipt, you can send an empty TwiML <Response/>
        # or if you want to reply to the user, you can use <Message>
        # from twilio.twiml.messaging_response import MessagingResponse
        # resp = MessagingResponse()
        # resp.message(response_text)
        # return str(resp)
        
        # For now, let's just return a simple string for demonstration.
        # Twilio might show a warning if it doesn't get TwiML, but your code will still run.
        return response # An empty response tells Twilio you received it.
    else:
        return "No message body found." # Bad request if no body
        
if __name__ == '__main__':
    # When deploying, you'll likely use a production-ready WSGI server like Gunicorn
    # For local testing, you can run: python app.py
    app.run(debug=True, port=5000)