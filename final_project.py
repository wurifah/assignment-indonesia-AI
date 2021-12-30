import smtplib

gmail_user = input(str("Masukkan akun gmail    : "))
gmail_app_password = input(str("Masukkan password gmail: "))
subject = input(str("Masukkan subject email : "))
penerima = []
with open('kontak.txt', 'r') as file:
	for line in file:
		penerima.append(line.rstrip())

sent_from = gmail_user
email_text = input(str("Masukkan pesan anda    : "))
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (gmail_user, ", ".join(penerima), subject, email_text)


for i in penerima:
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(gmail_user, gmail_app_password)
	server.sendmail(sent_from, i ,  email_text)
	server.close()
print(' ')
print('Email berhasil dikirim!')
print(' ')

# referensi https://windows10review.blogspot.com/2021/06/dwonload-code-python-to-send-email.html
