import pandas as pd
import random

# Set a seed for reproducibility
random.seed(42)

# Service names
services = [
    "XYZ Bank", "ABC Telecom", "PayQuick", "ShopEase", "SecureMail",
    "FastPay", "GlobalCard", "QuickLoan", "MyWallet", "PrimeServices"
]

# Variations of OTP request phrases
otp_phrases = [
    "please send the OTP sent to your registered mobile number",
    "kindly share the OTP sent to your registered mobile number",
    "please give the OTP sent to your registered mobile number",
    "provide the OTP sent to your registered mobile number",
    "enter the OTP sent to your registered mobile number",
    "submit the OTP sent to your registered mobile number",
    "forward the OTP sent to your registered mobile number",
    "type the OTP sent to your registered mobile number",
    "paste the OTP sent to your registered mobile number",
    "key in the OTP sent to your registered mobile number"
]

# Filler words to reach 50 words
filler_words = [
    "urgent", "security", "verification", "important", "confirm",
    "account", "alert", "device", "compliance", "protect",
    "immediately", "risk", "system", "information", "confirm",
    "notice", "protocol", "update", "verify", "support"
]

def generate_otp_message(service, phrase, filler_words):
    # Split phrase into words
    phrase_words = phrase.split()
    
    # Base structure without filler to count words
    base = [
        "Dear", "customer,", "this", "is", "an", "automated", "message", "from",
        service + ","
    ] + phrase_words + [
        "for", "security", "verification.", "Use", "the", "OTP", "now",
        "to", "finalize", "the", "authentication", "procedure."
    ]
    
    # Calculate how many filler words needed
    filler_count = 50 - len(base)
    
    # Select random filler words
    selected_fillers = random.choices(filler_words, k=filler_count)
    
    # Combine and join
    words = base + selected_fillers
    return " ".join(words)

# Generate 100 messages
messages = []
for i in range(100):
    service = services[i % len(services)]
    phrase = otp_phrases[i % len(otp_phrases)]
    msg = generate_otp_message(service, phrase, filler_words)
    messages.append({"label": "spam", "message": msg})

# Create DataFrame
df = pd.DataFrame(messages)

# save to CSV
df.to_csv("otp_messages.csv", index=False)