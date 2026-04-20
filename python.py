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

    if request.method == 'POST' and not session['game_over']:
        raw_guess = request.form.get('guess', '').strip()

        # ✅ Validation using try/except
        try:
            guess = int(raw_guess)

            if guess < 1 or guess > 100:
                message = "الرقم لازم يكون من 1 لـ 100.. ركز! 🙄"
                status = "error"
            else:
                session['attempts'] += 1
                session['history'].append(guess)

                # مهم مع الليست
                session.modified = True

                if guess < session['target_number']:
                    message = "Too low! 📉"
                    status = "low"

                elif guess > session['target_number']:
                    message = "Too high! 📈"
                    status = "high"

                else:
                    # 🎉 Win case
                    message = f"مبروك! الرقم الصح هو {session['target_number']} 🎉"
                    status = "win"
                    session['game_over'] = True

                    sarcastic_comment = get_feedback_message(session['attempts'])

                    # Update best score
                    if (session['best_score'] is None or
                            session['attempts'] < session['best_score']):
                        session['best_score'] = session['attempts']

        except ValueError:
            message = "أدخل رقم صحيح يا هندسة! 🛑"
            status = "error"

    return render_template(
        'index.html',
        message=message,
        status=status,
        attempts=session['attempts'],
        best_score=session['best_score'],
        game_over=session['game_over'],
        sarcastic_comment=sarcastic_comment,
        history=session['history']
    )


@app.route('/reset')
def reset():
    """Reset the game"""
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)