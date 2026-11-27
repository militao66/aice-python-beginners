
#simulated messy registration data
messy_name = "   chinedu okafor   "
messy_email = "   CHINEDU.OKafor@Example.COM    "

messy_phone = " +234 956 985 12345"


# Clean each field using method chaining
name = messy_name.strip().title()
email = messy_email.strip().lower()

phone = messy_phone.strip().replace(" ", "")

is_email_valid = "@" in email and "." in email
is_phone_valid = len(phone) >= 10

print("---- User Cleaned Profile ----")
print(f"Name : {name}")
print(f"Email address : {email} (valid:{is_email_valid})")
print(f"Phone No : {phone} (valid:{is_phone_valid})")







