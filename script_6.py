# Create partial EJS templates
header_ejs = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title><%= title %></title>
  <link rel=\"stylesheet\" href=\"/css/style.css\">
  <script defer src=\"/js/main.js\"></script>
</head>
<body>
  <!-- Navbar -->
  <nav>
    <div class=\"logo\">
      <span>Q</span><span>U</span><span>I</span>ZZICLES
    </div>
    <span class=\"menu-toggle\">☰</span>
    <ul>
      <li><a class=\"<%= currentPage === 'home' ? 'active' : '' %>\" href=\"/\">Home</a></li>
      <li><a class=\"<%= currentPage === 'about' ? 'active' : '' %>\" href=\"/about\">About</a></li>
      <li><a class=\"<%= currentPage === 'questions' ? 'active' : '' %>\" href=\"/questions\">Sample Questions</a></li>
      <li><a class=\"<%= currentPage === 'team' ? 'active' : '' %>\" href=\"/team\">Team</a></li>
      <li><a href=\"/register\">Exam</a></li>
      <li><a class=\"<%= currentPage === 'contact' ? 'active' : '' %>\" href=\"/contact\">Contact</a></li>
    </ul>
  </nav>
  <!-- Marquee for announcements -->
  <div class=\"marquee\">
    <p>
      <% announcements && announcements.forEach((a, idx) => { %>
        <%= a.title %> <%= idx < announcements.length - 1 ? ' | ' : '' %>
      <% }) %>
    </p>
  </div>
"""

footer_ejs = """
  <footer>
    &copy; <%= new Date().getFullYear() %> QUIZZICLES • Math & Physics Competition • Designed with ❤
  </footer>
</body>
</html>
"""

home_ejs = """<%- include('../partials/header') %>
  <section class=\"hero\">
    <h1><span>Q</span><span>U</span><span>I</span>ZZICLES</h1>
    <p>Annual Maths & Physics Competition • Edition <%= editionNumber || '2' %> • For Classes 8-12 & UG 1st Year</p>
    <a href=\"/register\" class=\"btn-primary\">Register Now</a>
  </section>

  <section id=\"about\">
    <h2>About the Competition</h2>
    <p>QUIZZICLES is a unique platform for budding mathematicians and physicists to showcase their problem-solving prowess. Participants from Class 8 to UG 1st Year compete in challenging quizzes designed by expert educators. The competition fosters curiosity, analytical thinking, and collaborative learning.</p>
  </section>

  <section id=\"sponsors\">
    <h2>Our Sponsors</h2>
    <div class=\"sponsors-grid\">
      <% sponsors.forEach(s => { %>
        <div class=\"sponsor-item\">
          <% if (s.logo_url) { %>
            <img src=\"<%= s.logo_url %>\" alt=\"<%= s.name %>\">
          <% } else { %>
            <span><%= s.name %></span>
          <% } %>
        </div>
      <% }) %>
    </div>
  </section>
<%- include('../partials/footer') %>
"""

about_ejs = """<%- include('../partials/header') %>
  <section>
    <h2>About QUIZZICLES</h2>
    <p>QUIZZICLES began in 2024 with the goal of inspiring students to pursue excellence in Mathematics and Physics. Now in its 2nd edition, we continue to push boundaries with innovative question formats and engaging challenges.</p>

    <h3>Competition Format</h3>
    <p>The competition consists of two rounds: an online qualifier followed by an on-site final. Questions span algebra, geometry, mechanics, electromagnetism, and more.</p>

    <h3>Important Dates</h3>
    <ul>
      <li>Registration Opens: <strong>[Add Date]</strong></li>
      <li>Online Qualifier: <strong>[Add Date]</strong></li>
      <li>Final Round: <strong>[Add Date]</strong></li>
    </ul>
  </section>
<%- include('../partials/footer') %>
"""

questions_ejs = """<%- include('../partials/header') %>
  <section>
    <h2>Sample Questions</h2>
    <% groupedQuestions.forEach(group => { %>
      <h3><%= group.subject %> • Class <%= group.class_level %></h3>
      <div class=\"cards\">
        <% group.questions.forEach(q => { %>
          <div class=\"card\">
            <h4>Q<%= q.id %></h4>
            <p><%= q.question_text %></p>
          </div>
        <% }) %>
      </div>
    <% }) %>
  </section>
<%- include('../partials/footer') %>
"""

team_ejs = """<%- include('../partials/header') %>
  <section>
    <h2>Meet the Team</h2>
    <div class=\"cards\">
      <% teamMembers.forEach(member => { %>
        <div class=\"card\">
          <h3><%= member.name %></h3>
          <p><strong><%= member.role %></strong></p>
          <p><%= member.bio %></p>
        </div>
      <% }) %>
    </div>
  </section>
<%- include('../partials/footer') %>
"""

contact_ejs = """<%- include('../partials/header') %>
  <section>
    <h2>Contact Us</h2>
    <% if (error) { %><p style=\"color:#ff7777;\"><%= error %></p><% } %>
    <form action=\"/contact\" method=\"post\" class=\"card\" style=\"max-width:600px;margin:auto;\">
      <label>Name*: <input type=\"text\" name=\"name\" required></label><br>
      <label>Email*: <input type=\"email\" name=\"email\" required></label><br>
      <label>Phone: <input type=\"tel\" name=\"phone\"></label><br>
      <label>Subject: <input type=\"text\" name=\"subject\"></label><br>
      <label>Message*: <textarea name=\"message\" required></textarea></label><br>
      <button type=\"submit\" class=\"btn-primary\">Send Message</button>
    </form>
  </section>
<%- include('../partials/footer') %>
"""

register_ejs = """<%- include('../partials/header') %>
  <section>
    <h2>Register for QUIZZICLES <%= editionNumber %> Edition</h2>
    <p>Fill out the registration form below to participate. Fields marked * are mandatory.</p>
    <% if (error) { %><p style=\"color:#ff7777;\"><%= error %></p><% } %>
    <form action=\"/register\" method=\"post\" class=\"card\" style=\"max-width:700px;margin:auto;\">
      <label>Student Name*: <input type=\"text\" name=\"student_name\" required></label><br>
      <label>Email*: <input type=\"email\" name=\"email\" required></label><br>
      <label>Phone*: <input type=\"tel\" name=\"phone\" required></label><br>
      <label>School/College*: <input type=\"text\" name=\"school_name\" required></label><br>
      <label>Class Level*: <select name=\"class_level\" required>
        <option value=\"8\">8</option><option value=\"9\">9</option><option value=\"10\">10</option>
        <option value=\"11\">11</option><option value=\"12\">12</option><option value=\"UG1\">UG 1st Year</option>
      </select></label><br>
      <button type=\"submit\" class=\"btn-primary\">Submit Registration</button>
    </form>
  </section>
<%- include('../partials/footer') %>
"""

# Write EJS files
paths = {
    './quizzicles/views/partials/header.ejs': header_ejs,
    './quizzicles/views/partials/footer.ejs': footer_ejs,
    './quizzicles/views/pages/home.ejs': home_ejs,
    './quizzicles/views/pages/about.ejs': about_ejs,
    './quizzicles/views/pages/questions.ejs': questions_ejs,
    './quizzicles/views/pages/team.ejs': team_ejs,
    './quizzicles/views/pages/contact.ejs': contact_ejs,
    './quizzicles/views/pages/register.ejs': register_ejs,
}

for file_path, content in paths.items():
    with open(file_path, 'w') as f:
        f.write(content)

print("✅ EJS template files created:")
for file_path in paths.keys():
    print(f"   📄 {file_path.replace('./quizzicles/', '')}")