url = input("enter website URL:").lower()
suspicious__words = ["login","verify","free","prize","password"]
if not
url.startswith("https://"):
print("warning:HTTPS not detected!")
if any(word in url for word in suspicious_words):
    print("warning:suspicious words detected!")
else:
    print("no suspicious keywords detected.")
    print("futureshield AI - Basic URL Checker")
    