# typ szyfrowania
# login i haslo poczty
# adres do kogo
# jakie porty potrzeba
# konto gmail - logowanie - zezwalaj na mniej bezpieczne aplikacje

from smtplib import SMTP

from email.mime.text import MIMEText

from secrets.log import login, haslo

odbiorca = login
nadawca = login
haslo = haslo
wiadomosc = "tooo magia tych swiat"
temat = "hej to znowu rzepa"
tresc = "jest o magia tych swiat"

wiadomosc = MIMEText(tresc,_charset='utf-8')
wiadomosc['Subject'] = temat

mailer = SMTP("smtp.gmail.com", 587)
mailer.ehlo()
#witam sie z serwerem
mailer.starttls()
#szyfrowanie
mailer.login(login, haslo)
mailer.sendmail(nadawca, odbiorca, wiadomosc)
print("wyslano maila")
mailer.close()
#zamykam polaczenie z serwerem