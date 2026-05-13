from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'mnu_ai_engineering_2026_key'


def get_feedback_message(attempts):
    """Generate sarcastic feedback based on attempts"""
    if attempts <= 6:
        return random.choice([
            "إنت مخاوي؟ ولا ده ذكاء اصطناعي فعلاً؟ 🧠",
            "عاش يا وحش! إنت هكر رسمي 😎"
        ])
    elif attempts <= 8:
        return random.choice([
            "أداء مقبول.. محتاج زقه 🤔",
            "ماشي حالك، بس اشتغل على نفسك شوية 🤨"
        ])
    else:
        return random.choice([
            "ميت مفيش أمل فيك.. روح ذاكر أحسن 💀",
            "يا ابني ركز، إنت بتهبد؟ 😭"
        ])


def init_game():
    """Initialize game session"""
    session['target_number'] = random.randint(1, 100)
    session['attempts'] = 0
    session['history'] = []
    session['game_over'] = False

    if 'best_score' not in session:
        session['best_score'] = None


@app.route('/', methods=['GET', 'POST'])
def index():

    # Initialize game if not exists
    if 'target_number' not in session:
        init_game()

    message = ""
    status = "normal"
    sarcastic_comment = ""

    
