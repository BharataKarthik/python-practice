import pywhatkit  # This package allows for automating WhatsApp messages

try:
    # "+9193900xxxxx" is the phone number (make sure to format it with the country code)
    # "Hi Python" is the message you want to send
    # 22 is the hour in 24-hour format, and 19 is the minute (this sends the message at 10:19 PM)
    pywhatkit.sendwhatmsg("+9193900xxxxx", "Hi Python", 22, 19)
    print("Successfully Sent!")

except:
    print("An unexpected error occurred")
