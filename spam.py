# Function to count how many spam words are in the text
def get_spam_score(text):
    # A simple list of common spam phrases
    spam_words = [
        "100% free", "act now", "ad", "amazing", "apply now",
        "billing address", "buy", "cash bonus", "cheap", "congratulations",
        "credit card", "dear friend", "debt", "double your income", "earn extra cash",
        "expire", "free investment", "get paid", "guaranteed", "increase sales",
        "instant", "limited time", "lose weight", "million dollars", "no cost",
        "no obligation", "prize", "risk-free", "urgent", "winner"
    ]

    score = 0
    flagged_items = []

    # Check each word in our list against the user's message
    for word in spam_words:
        if word in text.lower():
            # Add a point for every time the word appears
            count = text.lower().count(word)
            score += count
            flagged_items.append(word)

    return score, flagged_items


# Function to turn the number score into a readable rating
def get_rating(score):
    if score == 0:
        return "Safe"
    elif score <= 2:
        return "Likely Legitimate (Low Risk)"
    elif score <= 5:
        return "Possibly Spam (Medium Risk)"
    else:
        return "Highly Likely Spam (High Risk)"


# Main part of the program
print("--- Simple Spam Detector ---")
message = input("Paste the email message here: ")

# Run the functions
final_score, found_words = get_spam_score(message)
likelihood = get_rating(final_score)

# Show the results
print("\nRESULTS:")
print(f"Spam Score: {final_score}")
print(f"Verdict: {likelihood}")

if final_score > 0:
    # Convert list to a string to look nicer when printing
    print(f"Trigger words found: {', '.join(found_words)}")
else:
    print("No spam keywords detected.")