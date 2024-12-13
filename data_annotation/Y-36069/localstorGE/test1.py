from google.appengine.api import mail


def send_blog_message(name, email, phone, message, recipient):
    try:
        mail.send_message(sender=email,
                          to=recipient,
                          subject=f'New Message from Blog {name}',
                          body=f"{message}\n{phone}")
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


# Example usage
send_blog_message("John Doe", "sender@example.com", "123-456-7890", "This is a test message.", params["gmail-user"])
