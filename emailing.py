import imghdr
import smtplib
from email.message import EmailMessage

sender = "samikpandit02@gmail.com"
password = "rtjyewfelflmapzh"
receiver = "samikpandit02@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Object detected!"
    email_message.set_content("Alert, new object detected!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/19.png")
