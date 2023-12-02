from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

users = {}
peer_groups = {}


@app.route('/')
def index():
  if 'username' in session:
    return redirect(url_for('dashboard'))
  return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    if username and password:
      if username not in users:
        users[username] = {
            'password': generate_password_hash(password),
            'moods': []
        }
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
      else:
        flash('Username already exists. Please choose another.', 'danger')
    else:
      flash('Invalid registration data. Please try again.', 'danger')

  return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    if username in users and check_password_hash(users[username]['password'],
                                                 password):
      session['username'] = username
      return redirect(url_for('dashboard'))
    else:
      flash('Invalid username or password. Please try again.', 'danger')

  return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
  if 'username' in session:
    if request.method == 'POST':
      mood = request.form['mood']
      users[session['username']]['moods'].append(mood)
      flash('Mood logged successfully!', 'success')

    return render_template('dashboard.html',
                           moods=users[session['username']]['moods'])
  else:
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('index'))

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
  data = request.json
  if data is not None:
    user_message = data.get('message')
    chatbot_response = f"Chatbot says : {user_message} "
    return jsonify({'repsonse': chatbot_response})
  else:
    return jsonify({'error': 'Bad Request, no JSON data provided'}), 400
    
@app.route('/teletherapy')
def teletherapy():
  if 'username' in session:
    return render_template('teletherapy.html', username=session['username'])
  else:
    return redirect(url_for('index'))

@app.route('/daily_emotion_log', methods=['POST'])
def daily_emotion_log():
  if 'username' in session:
    data = request.json
    emotion = data.get('emotion')
    if emotion:
      users[session['username']]['moods'].append(emotion)
      return jsonify({'message': 'Emotion logged successfully'})
    else:
      return jsonify({'message': 'No emotion provided'}), 400
  else:
    return jsonify({'message': 'User not found'}), 404


@app.route('/crisis_response', methods=['GET'])
def crisis_response():
  if 'username' in session:
    return render_template('crisis_response.html')
  else:
    return redirect(url_for('index'))


@app.route('/feedback', methods=['POST'])
def feedback():
  if 'username' in session:
    data = request.json
    feedback_message = data.get('message')
    print(f"Feedback from {session['username']}: {feedback_message}")
    return jsonify({'message': 'Feedback received successfully'})
  else:
    return jsonify({'message': 'User not found'}), 404


@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
  if 'username' in session:
    if request.method == 'POST':
      group_name = request.form['group_name']
      if group_name:
        peer_groups[group_name] = {
            'members': [session['username']],
            'messages': []
        }
        flash(f'Group "{group_name}" created successfully!', 'success')
        return redirect(url_for('dashboard'))
      else:
        flash('Invalid group name. Please try again.', 'danger')

    return render_template('create_group.html')
  else:
    return redirect(url_for('index'))


@app.route('/join_group', methods=['GET', 'POST'])
def join_group():
  if 'username' in session:
    if request.method == 'POST':
      group_name = request.form['group_name']
      if group_name in peer_groups:
        peer_groups[group_name]['members'].append(session['username'])
        flash(f'Joined group "{group_name}" successfully!', 'success')
        return redirect(url_for('dashboard'))
      else:
        flash('Group not found. Please try again.', 'danger')

    return render_template('join_group.html')
  else:
    return redirect(url_for('index'))


@app.route('/peer_group_chat', methods=['GET', 'POST'])
def peer_group_chat():
  if 'username' in session:
    group_name = request.args.get('group_name')
    if group_name in peer_groups and session['username'] in peer_groups[
        group_name]['members']:
      if request.method == 'POST':
        message = request.form['message']
        if message:
          peer_groups[group_name]['messages'].append({
              'user':
              session['username'],
              'message':
              message
          })
        else:
          flash('Empty messages are not allowed.', 'danger')

      return render_template('peer_group_chat.html',
                             group_name=group_name,
                             messages=peer_groups[group_name]['messages'])
    else:
      flash('You are not a member of this group.', 'danger')
      return redirect(url_for('dashboard'))
  else:
    return redirect(url_for('index'))


@app.route('/mental_health_activities')
def mental_health_activities():
  if 'username' in session:
    return render_template('mental_health_activities.html')
  else:
    return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(debug=True)
