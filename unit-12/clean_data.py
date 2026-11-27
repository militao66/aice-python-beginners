
raw_name = "Adebayo basit      "
raw_email = "deVB2026@GMAIL.com    "
raw_tel = "+234-48-8203-8217"
clean_name = raw_name.strip().title()
clean_email = raw_email.strip().lower()
clean_tel = raw_tel.replace("-", " ")
print(raw_name)
print(raw_email)
print(raw_tel)
print(clean_name)
print(clean_email)
print(clean_tel)

