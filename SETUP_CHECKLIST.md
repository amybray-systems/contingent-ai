# 🚀 ContingentAI Setup Checklist

## Your Path: C:\Users\amyma\Desktop\GitHub\contingent-ai

Follow these steps in order to get ContingentAI running!

---

## ✅ Step 1: Copy All Files to Your Project Folder

You need to copy these files from the outputs folder into your contingent-ai folder:

### Core Python Files (Root folder)
- [ ] `app.py` → Copy to root
- [ ] `config.py` → Copy to root
- [ ] `requirements.txt` → Copy to root
- [ ] `seed_data.py` → Copy to root
- [ ] `.env.example` → Copy to root
- [ ] `README.md` → Copy to root

### Templates (Create templates folder first if needed)
- [ ] `templates/base.html`
- [ ] `templates/index.html`
- [ ] `templates/dashboard.html`
- [ ] `templates/workers.html`
- [ ] `templates/ai_chat.html`
- [ ] `templates/scenarios.html`
- [ ] `templates/vendors.html`

### Static Files
- [ ] `static/css/main.css` (you already created this!)
- [ ] `static/js/main.js`

---

## ✅ Step 2: Verify Folder Structure

Your folder should look like this:

```
C:\Users\amyma\Desktop\GitHub\contingent-ai\
│
├── venv\                      ✅ (you already have this!)
├── app.py                     ← Copy from outputs
├── config.py                  ← Copy from outputs
├── requirements.txt           ← Copy from outputs
├── seed_data.py              ← Copy from outputs
├── .env.example              ← Copy from outputs
├── README.md                 ← Copy from outputs
│
├── templates\
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── workers.html
│   ├── ai_chat.html
│   ├── scenarios.html
│   └── vendors.html
│
├── static\
│   ├── css\
│   │   └── main.css          ✅ (you already have this!)
│   ├── js\
│   │   └── main.js
│   └── images\
│
├── models\
│   └── __init__.py
├── routes\
│   └── __init__.py
├── services\
│   └── __init__.py
└── utils\
    └── __init__.py
```

---

## ✅ Step 3: Create Empty __init__.py Files

In VS Code terminal (with venv activated):

```bash
# Make sure you're in the right place
cd C:\Users\amyma\Desktop\GitHub\contingent-ai

# Create empty __init__.py files for Python packages
type nul > models\__init__.py
type nul > routes\__init__.py
type nul > services\__init__.py
type nul > utils\__init__.py
```

---

## ✅ Step 4: Create .env File

```bash
# Copy the example file
copy .env.example .env
```

Now open `.env` in VS Code and edit it:

```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=change-this-to-something-random-123456789
DATABASE_URL=sqlite:///contingent_ai.db
OPENAI_API_KEY=your-key-here-if-you-have-one
```

**Note:** You don't need an OpenAI key yet - the basic dashboard will work without it!

---

## ✅ Step 5: Install Dependencies

Make sure your venv is activated (you should see `(venv)` in your terminal):

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

This will take 2-3 minutes. Let it run!

---

## ✅ Step 6: Initialize the Database

```bash
# Create the database tables
flask init-db
```

You should see: `✅ Database initialized!`

---

## ✅ Step 7: Load Sample Data

```bash
# Populate with sample workforce data
flask seed-db
```

You should see:
```
✅ Created 5 departments
✅ Created 3 sample workers
✅ Database seeded successfully!
```

---

## ✅ Step 8: RUN IT! 🎉

```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
```

---

## ✅ Step 9: Open in Browser

Open your web browser and go to:
```
http://127.0.0.1:5000
```

You should see the ContingentAI home page! 🎉

---

## ✅ Step 10: Test the Pages

Click through and make sure these work:
- [ ] Home page (/)
- [ ] Dashboard (/dashboard) - should show charts!
- [ ] Workers (/workers) - should show 3 sample workers
- [ ] AI Assistant (/ai) - placeholder for now
- [ ] Scenarios (/scenarios) - placeholder
- [ ] Vendors (/vendors) - placeholder

---

## 🎨 Bonus: Verify Professional Colors

The site should have:
- ✅ Deep blue navbar (not pink/purple!)
- ✅ Teal accents
- ✅ Clean white cards
- ✅ Professional, enterprise look

---

## 🚨 Troubleshooting

### Issue: "Module not found" errors
**Fix:** Make sure you ran `pip install -r requirements.txt`

### Issue: Database errors
**Fix:** Delete `contingent_ai.db` file and run `flask init-db` again

### Issue: Templates not found
**Fix:** Make sure all templates are in the `templates` folder

### Issue: Port already in use
**Fix:** 
```bash
# Use a different port
python app.py --port 5001
```

Or:
```bash
# In app.py, change the last line to:
app.run(debug=True, port=5001)
```

### Issue: Can't see static files (CSS/JS)
**Fix:** Hard refresh the browser: Ctrl+Shift+R (or Cmd+Shift+R on Mac)

---

## 📸 What Success Looks Like

When everything is working, you should see:

1. **Home Page**: Clean, professional landing page with feature cards
2. **Dashboard**: 
   - 4 metric cards (Total Workers, Contractors, FTE, Monthly Cost)
   - 2 charts (Department bar chart, Worker type pie chart)
   - Department table
3. **Workers Page**: Table with 3 sample workers
4. **Professional blue/teal color scheme throughout**

---

## 🎯 Next Steps After It's Running

1. **Take screenshots** for your portfolio
2. **Commit to Git**:
   ```bash
   git add .
   git commit -m "Initial ContingentAI setup with dashboard"
   git push
   ```
3. **Start building Phase 1 features**
4. **Show it to someone!** (Even just friends/family to practice your story)

---

## 💡 Quick Commands Reference

```bash
# Activate venv
venv\Scripts\activate

# Run the app
python app.py

# Reset database
flask init-db
flask seed-db

# Install new package
pip install package-name
pip freeze > requirements.txt
```

---

## ✨ You Got This!

Once you see that home page render, you'll have a working foundation! Then you can start customizing and adding features.

**Remember:** The hardest part is getting started. You're doing great! 🚀

---

**Questions? Issues?** Let me know what you see and I'll help you troubleshoot!
