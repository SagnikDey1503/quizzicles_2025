# QUIZZICLES Website Project

Welcome to the source code for the official **QUIZZICLES** Mathematics & Physics competition website.

---

## 📂 Project Structure

```text
quizzicles/
├── app.js                  # Express entry-point
├── .env                    # Environment variables (edit with your DB creds)
├── package.json            # Node dependencies & scripts
├── config/
│   └── database-setup.js   # One-time script to create tables & seed sample data
├── db/
│   └── database.js         # PostgreSQL connection pool (pg)
├── models/                 # Data-access models (Announcement, TeamMember, etc.)
├── routes/                 # Express route modules
├── views/                  # EJS templates (partials & pages)
├── public/
│   ├── css/style.css       # Animated gradient, navbar, components
│   └── js/main.js          # Responsive nav toggle
└── ... (images uploads go here)
```

---

## 🚀 Quick-Start

1. **Clone** the repository:
   ```bash
   git clone <repo-url> && cd quizzicle
   ```
2. **Install** dependencies (Node ≥16):
   ```bash
   npm install
   ```
3. **Configure** PostgreSQL credentials in `.env`.
4. **Initialise** the database & seed demo data:
   ```bash
   npm run setup-db
   ```
5. **Run** the development server:
   ```bash
   npm run dev
   ```
6. Visit `http://localhost:3000` – enjoy the animated hero, marquee announcements, sample questions & more.

---

## ✨ Highlights

- Vibrant **CSS gradient** background with smooth animation
- Color-coded **QUIZZICLES** logotype (Q-yellow, U-blue, I-red)
- Sticky **navbar** with active-link underline & mobile burger
- **Marquee** banner pulls announcements from the database
- Modular EJS pages: Home, About, Sample Questions, Meet the Team, Sponsors, Exam/Registration & Contact
- Fully **PostgreSQL-backed** – run `database-setup.js` once to create all tables (announcements, team, sponsors, questions, contacts, registrations)
- Minimal **Admin portal** (`/admin/login`) to read contact forms & announcements (credentials admin / quizzicles2025)

---

## 🗃️ Database Schema

See `config/database-setup.js`. Tables:

```
announcements, team_members, sponsors, sample_questions,
contact_submissions, registrations
```
Seed data is inserted automatically (sample questions, sponsors, etc.).

---

## ⚙️ Customisation Tips

* **Colors / Branding** – tweak `:root` variables in `public/css/style.css`.
* **Questions** – insert rows into `sample_questions` using your preferred SQL client.
* **Sponsors** – update `sponsors` with logo URLs (store in `public/images`).
* **Announcements** – manage via Admin dashboard or direct SQL.

---

## 🔒 Security Notes

This is a demo starter. Before production:

1. Replace the hard-coded admin credentials & session secret.
2. Serve over HTTPS & set `cookie: { secure: true }`.
3. Validate / sanitise all form inputs.
4. Deploy PostgreSQL with strong passwords + restricted network rules.

---

## 📦 Packaging as ZIP

After creating the project files (they’re all inside `quizzicles/`), you can zip everything:

```bash
# macOS / Linux
zip -r quizzicles.zip quizzicles

# Windows – right-click folder > “Send to → Compressed (zipped) folder”
```

Distribute `quizzicles.zip` to your teammates or hosting provider – they only need to `npm install && npm run setup-db && npm start`.

---

Happy quizzing! ✨
