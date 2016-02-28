# Import dependent modules
from email.mime.text import MIMEText
# Interdependent modules
from email_layout import setup_email
from api_connections import server

# Setup email
body, email_subject = setup_email()

# Send email
msg = MIMEText(body, 'html')
msg['From'] = "FROM_EMAIL_ADDRESS"
msg['To'] = "TO_EMAIL_ADDRESS"
msg['Subject'] = email_subject
server.send_message(msg)
server.quit()

