"""
Spam scoring and classification logic.
"""
import re

# List of suspicious keywords common in spam
SPAM_KEYWORDS = [
    r"crypto", r"bitcoin", r"investment", r"seo", r"marketing", 
    r"casino", r"betting", r"lottery", r"winner", r"prize",
    r"buy now", r"discount", r"offer", r"urgent", r"official"
]

# Domains often used for temporary/burner emails
TEMP_EMAIL_DOMAINS = [
    "temp-mail.org", "10minutemail.com", "guerrillamail.com", 
    "mailinator.com", "sharklasers.com", "yopmail.com"
]

def calculate_spam_score(message: str, email: str) -> int:
    """
    Calculates a spam score based on message content and email domain.
    0-30: Likely normal
    30-70: Suspicious
    >70: Likely spam
    """
    score = 0
    message_lower = message.lower()
    
    # Rule 1: Message too short (though usually caught by validation)
    if len(message.strip()) < 10:
        score += 10
        
    # Rule 2: Excessive links (http/https occurrences)
    links = len(re.findall(r"https?://", message_lower))
    if links >= 3:
        score += 25
    elif links >= 1:
        score += 5
        
    # Rule 3: Spam keywords
    keyword_matches = 0
    for kw in SPAM_KEYWORDS:
        if re.search(kw, message_lower):
            keyword_matches += 1
            
    if keyword_matches >= 2:
        score += 30
    elif keyword_matches == 1:
        score += 15
        
    # Rule 4: Temporary email domains
    email_domain = email.split('@')[-1].lower() if '@' in email else ""
    if email_domain in TEMP_EMAIL_DOMAINS:
        score += 40
        
    # Rule 5: No spaces in long message (obfuscation)
    if len(message) > 50 and ' ' not in message:
        score += 20
        
    return score
