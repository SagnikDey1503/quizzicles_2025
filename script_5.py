# CSS styling including gradient background, navbar, hero, sections, cards, marquee
css_content = """/* QUIZZICLES Main Styles */
:root {
  --primary: #ff9f1c;
  --secondary: #2ec4b6;
  --tertiary: #e71d36;
  --dark: #011627;
  --light: #fdfffc;
  --gradient-start: #007cf0;
  --gradient-middle: #00dfd8;
  --gradient-end: #ff0080;
}

html, body {
  margin: 0;
  padding: 0;
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(-45deg, var(--gradient-start), var(--gradient-middle), var(--gradient-end));
  background-size: 300% 300%;
  animation: gradientBackground 15s ease infinite;
  color: var(--light);
}

@keyframes gradientBackground {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Navbar */
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: rgba(1, 22, 39, 0.8);
  backdrop-filter: blur(6px);
  position: sticky;
  top: 0;
  z-index: 100;
}

nav .logo {
  font-size: 1.8rem;
  font-weight: 700;
  letter-spacing: 1px;
}

nav .logo span:nth-child(1) { color: #ffd700; }
nav .logo span:nth-child(2) { color: #1e90ff; }
nav .logo span:nth-child(3) { color: #ff4040; }

nav ul {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  margin: 0;
}

nav ul li a {
  color: var(--light);
  text-decoration: none;
  font-weight: 500;
  position: relative;
  padding: 0.2rem 0;
}

nav ul li a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--secondary);
  transition: width 0.3s ease-in-out;
}

nav ul li a:hover::after, nav ul li a.active::after {
  width: 100%;
}

/* Marquee */
.marquee {
  width: 100%;
  overflow: hidden;
  background: rgba(0, 0, 0, 0.4);
  white-space: nowrap;
  box-sizing: border-box;
  padding: 0.6rem 0;
}

.marquee p {
  display: inline-block;
  padding-left: 100%;
  animation: marqueeAnim 18s linear infinite;
  font-weight: 600;
  letter-spacing: 0.5px;
}

@keyframes marqueeAnim {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-100%); }
}

/* Hero */
.hero {
  min-height: 70vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 2rem;
}

.hero h1 {
  font-size: clamp(2.5rem, 8vw, 6rem);
  margin: 0;
  line-height: 1.1;
  font-weight: 800;
}

.hero h1 span:nth-child(1) { color: #ffd700; }
.hero h1 span:nth-child(2) { color: #1e90ff; }
.hero h1 span:nth-child(3) { color: #ff4040; }

.hero p {
  font-size: 1.3rem;
  max-width: 650px;
  margin-top: 1rem;
}

.btn-primary {
  display: inline-block;
  margin-top: 1.5rem;
  background: var(--secondary);
  color: var(--dark);
  padding: 0.8rem 2rem;
  border-radius: 40px;
  font-weight: 600;
  text-decoration: none;
  transition: transform 0.2s ease, background 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-3px);
  background: #3be8d6;
}

/* Sections */
section {
  padding: 3rem 2rem;
  background: rgba(0, 0, 0, 0.3);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

section h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 2rem;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 1.5rem;
  backdrop-filter: blur(8px);
  transition: transform 0.3s ease, background 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  background: rgba(255, 255, 255, 0.2);
}

.card h3 {
  margin-top: 0;
  margin-bottom: 0.8rem;
  color: var(--primary);
}

.card p {
  color: var(--light);
  font-size: 0.95rem;
}

/* Grid for sponsors */
.sponsors-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1.2rem;
  align-items: center;
  justify-items: center;
}

.sponsor-item img, .sponsor-item span {
  max-width: 120px;
  filter: brightness(0) invert(1);
}

/* Footer */
footer {
  text-align: center;
  padding: 1rem;
  background: rgba(1, 22, 39, 0.9);
  font-size: 0.9rem;
}

/* Responsive */
@media (max-width: 768px) {
  nav ul { display: none; }
  nav .menu-toggle { display: block; cursor: pointer; }
}
"""

# Main JS for nav toggle
js_content = """document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.menu-toggle');
  const navList = document.querySelector('nav ul');
  if (toggle) {
    toggle.addEventListener('click', () => {
      navList.classList.toggle('open');
    });
  }
});
"""

# Write CSS and JS files
with open('./quizzicles/public/css/style.css', 'w') as f:
    f.write(css_content)

with open('./quizzicles/public/js/main.js', 'w') as f:
    f.write(js_content)

print("✅ CSS and JS files created:")
print("   📄 public/css/style.css")
print("   📄 public/js/main.js")