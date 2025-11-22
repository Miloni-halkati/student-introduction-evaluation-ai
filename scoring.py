import re
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# ----------------------------------------
# BASIC UTILITIES
# ----------------------------------------

def clean_text(text):
    return re.sub(r'\s+', ' ', text.strip()).lower()

def count_words(text):
    return len(re.findall(r'\b\w+\b', text.lower()))

def extract_words(text):
    return re.findall(r'\b[a-zA-Z]+\b', text.lower())

# ----------------------------------------
# 1. SALUTATION (0–5)
# ----------------------------------------

def score_salutation(text):
    t = text.lower()

    if any(phrase in t for phrase in ["i am excited", "feeling great"]):
        return 5
    if any(g in t for g in ["good morning", "good afternoon", "good evening", "good day", "hello everyone"]):
        return 4
    if any(g in t for g in ["hi", "hello"]):
        return 2
    return 0

# ----------------------------------------
# 2. KEYWORD PRESENCE (20 + 10)
# ----------------------------------------

MUST_HAVE = [
    "name", "my name is", "i am", "age", "years old",
    "class", "studying in", "school",
    "family", "live with", "family members",
    "hobby", "hobbies", "interests", "free time"
]

GOOD_TO_HAVE = [
    "i am from", "origin", "hometown",
    "ambition", "goal", "dream",
    "fun fact", "unique",
    "strength", "achievement"
]

def score_keywords(text):
    t = text.lower()
    must_score, good_score = 0, 0

    for kw in MUST_HAVE:
        if kw in t:
            must_score += 4
    for kw in GOOD_TO_HAVE:
        if kw in t:
            good_score += 2

    return min(must_score, 20), min(good_score, 10)

# ----------------------------------------
# 3. FLOW DETECTION (0–5)
# ----------------------------------------

def score_flow(text):
    t = text.lower()

    has_salutation = any(s in t for s in ["hi", "hello", "good morning", "good afternoon", "good evening"])
    has_basic = any(s in t for s in ["name", "class", "age", "school"])
    has_extra = any(s in t for s in ["hobby", "interest", "goal", "fun fact", "unique"])
    has_closing = "thank you" in t

    if has_salutation and has_basic and has_extra and has_closing:
        return 5
    return 0

# ----------------------------------------
# 4. WPM SCORING (0–10)
# ----------------------------------------

def score_wpm(text, duration_seconds):
    wc = count_words(text)
    if duration_seconds <= 0:
        return 2

    wpm = (wc / duration_seconds) * 60

    if wpm > 161:
        return 2
    elif 141 <= wpm <= 160:
        return 6
    elif 111 <= wpm <= 140:
        return 10
    elif 81 <= wpm <= 110:
        return 6
    else:
        return 2

# ----------------------------------------
# 5. GRAMMAR (DEPLOYMENT SAFE — NO LANGUAGETOOL)
# ----------------------------------------

def score_grammar(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    errors = 0

    for s in sentences:
        # Error 1: sentence doesn't start with capital
        if s and not s[0].isupper():
            errors += 1
        
        # Error 2: double spaces
        if "  " in s:
            errors += 1
        
        # Error 3: repeated word (e.g., "the the")
        if re.search(r'\b(\w+)\s+\1\b', s.lower()):
            errors += 1

    wc = count_words(text)
    if wc == 0:
        return 0

    errors_per_100 = (errors / wc) * 100

    if errors_per_100 <= 5:
        return 10
    elif errors_per_100 <= 10:
        return 8
    elif errors_per_100 <= 20:
        return 6
    elif errors_per_100 <= 35:
        return 4
    else:
        return 2

# ----------------------------------------
# 6. TTR VOCABULARY (0–10)
# ----------------------------------------

def score_ttr(text):
    words = extract_words(text)
    if len(words) == 0:
        return 0

    distinct = len(set(words))
    ttr = distinct / len(words)

    if len(words) > 200:
        ttr *= 0.80  # smoothing

    if ttr >= 0.9:
        return 10
    elif ttr >= 0.7:
        return 8
    elif ttr >= 0.5:
        return 6
    elif ttr >= 0.3:
        return 4
    else:
        return 2

# ----------------------------------------
# 7. FILLER WORDS (0–15)
# ----------------------------------------

FILLERS = [
    "um", "uh", "like", "you know", "basically", "actually", "hmm",
    "sort of", "i mean", "kinda", "kind of", "well"
]

def score_filler(text):
    words = extract_words(text)
    wc = len(words)
    if wc == 0:
        return 0

    filler_count = sum(1 for w in words if w in FILLERS)
    rate = (filler_count / wc) * 100

    if rate <= 3:
        return 15
    elif rate <= 6:
        return 12
    elif rate <= 9:
        return 9
    elif rate <= 12:
        return 6
    else:
        return 3

# ----------------------------------------
# 8. SENTIMENT (0–15)
# ----------------------------------------

def score_sentiment(text):
    vs = analyzer.polarity_scores(text)
    sent = (vs['compound'] + 1) / 2  # convert -1–1 to 0–1

    if sent >= 0.70:
        return 15
    elif sent >= 0.55:
        return 12
    elif sent >= 0.40:
        return 9
    elif sent >= 0.25:
        return 6
    else:
        return 3

# ----------------------------------------
# MAIN FINAL EVALUATION
# ----------------------------------------

def evaluate_transcript(transcript, duration_seconds):
    transcript = clean_text(transcript)

    sal = score_salutation(transcript)
    must_k, good_k = score_keywords(transcript)
    flow = score_flow(transcript)
    wpm = score_wpm(transcript, duration_seconds)
    grammar = score_grammar(transcript)
    ttr = score_ttr(transcript)
    filler = score_filler(transcript)
    senti = score_sentiment(transcript)

    total = sal + must_k + good_k + flow + wpm + grammar + ttr + filler + senti

    if total > 100:
        total = 100

    return {
        "overall_score": round(total, 2),
        "details": {
            "salutation": sal,
            "keyword_must_have": must_k,
            "keyword_good_to_have": good_k,
            "flow_structure": flow,
            "wpm_score": wpm,
            "grammar_score": grammar,
            "ttr_score": ttr,
            "filler_score": filler,
            "sentiment_score": senti
        }
    }
