# Phishing and Social Engineering Email Filter
# This program checks an email for words commonly associated with suspicious messages and estimates its threat level.

email_text = input("PEnter the email message: ")
# Convert everything to lowercase
# versions of a keyword receive the same treatment.
email = email_text.lower()
threat_score = 1
# Examine the message one word at a time such that Each matching keyword adds one point to the threat score.
for word in email.split():
    if (word == "urgent" or word == "click" or
        word == "password" or word == "bank" or
        word == "verify" or word == "free"):
        threat_score = threat_score + 1

# Use the final score to decide how the email should be classified.
print("\nScan complete.")
print("Threat score:", threat_score)

if threat_score == 1:
    print("[SAFE] Email passed security parameters.")
elif threat_score == 2:
    print("[LOW RISK] Minor indicators noted. Keep an eye out.")
elif threat_score <= 4:
    print("[SUSPICIOUS] High risk flagged. Diverted to Spam.")
else:
    print("[ALERT] Critical Social Engineering attack caught and neutralized!")