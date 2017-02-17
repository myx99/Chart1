from smtplib import SMTPException, SMTPAuthenticationError
import string
import base64
import sspi
# NTLM Guide --  CodeGo.net
SMTP_EHLO_OKAY = 250
SMTP_AUTH_CHALLENGE = 334
SMTP_AUTH_OKAY = 235
def asbase64(msg):
 return string.replace((base64.b64encode(msg)).decode("utf-8"), '\n', '')
 # return string.replace(base64.b64encode(msg.encode(encoding='utf-8')), '\n', '')
def connect_to_exchange_as_current_user(smtp):
 """Example:
 >>> import smtplib
 >>> smtp = smtplib.SMTP("mail.huajingsec.com")
 >>> connect_to_exchange_as_current_user(smtp)
 """
 # Send the SMTP EHLO command
 code, response = smtp.ehlo()
 if code != SMTP_EHLO_OKAY:
  raise SMTPException("Server did not respond as expected to EHLO command")
 sspiclient = sspi.ClientAuth('NTLM')
 # Generate the NTLM Type 1 message
 sec_buffer=None
 err, sec_buffer = sspiclient.authorize(sec_buffer)
 print(sec_buffer)
 ntlm_message = asbase64(sec_buffer[0].Buffer)
 # Send the NTLM Type 1 message -- Authentication Request
 code, response = smtp.docmd("AUTH", "NTLM " + ntlm_message)
 # Verify the NTLM Type 2 response -- Challenge Message
 if code != SMTP_AUTH_CHALLENGE:
  raise SMTPException("Server did not respond as expected to NTLM negotiate message")
 # Generate the NTLM Type 3 message
 err, sec_buffer = sspiclient.authorize(base64.b64decode(response.encode(encoding='utf-8')))
 ntlm_message = asbase64(sec_buffer[0].Buffer)
 # Send the NTLM Type 3 message -- Response Message
 code, response = smtp.docmd(ntlm_message)
 # code, response = smtp.docmd("", ntlm_message)
 if code != SMTP_AUTH_OKAY:
  raise SMTPAuthenticationError(code, response)