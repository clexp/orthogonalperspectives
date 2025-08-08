title: Contact
date: 2024-03-28
Modified: 2024-03-28
Category: pages
Tags: #contact
Slug: contact
Authors: clexp
Status: published
Summary: Contact information and form
Cover: /images/apple-touch-icon_thumb.png

# Contact Me

## Get in Touch

You can reach me through:

- LinkedIn: [Your LinkedIn Profile]
- Email: [Your Email]
- Twitter: [@YourHandle]

## Send a Message

<div class="contact-form-container">
  <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
    <input type="hidden" name="form-name" value="contact" />
    
    <!-- Honeypot field for spam protection -->
    <p class="hidden">
      <label>Don't fill this out if you're human: <input name="bot-field" /></label>
    </p>
    
    <div class="form-group">
      <label for="name">Name *</label>
      <input type="text" id="name" name="name" required />
    </div>
    
    <div class="form-group">
      <label for="email">Email *</label>
      <input type="email" id="email" name="email" required />
    </div>
    
    <div class="form-group">
      <label for="subject">Subject *</label>
      <select id="subject" name="subject" required>
        <option value="">Select a topic...</option>
        <option value="machine-learning">Machine Learning</option>
        <option value="python-programming">Python Programming</option>
        <option value="mathematics">Mathematics</option>
        <option value="medical-ai">Medical Applications of AI</option>
        <option value="engineering-ai">Engineering Applications of AI</option>
        <option value="collaboration">Collaboration Opportunity</option>
        <option value="other">Other</option>
      </select>
    </div>
    
    <div class="form-group">
      <label for="message">Message *</label>
      <textarea id="message" name="message" rows="6" required placeholder="Please provide details about your inquiry..."></textarea>
    </div>
    
    <div class="form-group">
      <button type="submit" class="submit-btn">Send Message</button>
    </div>
  </form>
</div>

<style>
.contact-form-container {
  max-width: 600px;
  margin: 30px auto;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 8px;
  border: 1px solid #e9ecef;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  font-family: inherit;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #3498DB;
  box-shadow: 0 0 5px rgba(52, 152, 219, 0.3);
}

.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

.submit-btn {
  background: #3498DB;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.submit-btn:hover {
  background: #2980B9;
}

.submit-btn:active {
  transform: translateY(1px);
}

.hidden {
  display: none;
}

/* Success/Error message styling */
.success-message {
  background: #d4edda;
  color: #155724;
  padding: 15px;
  border-radius: 4px;
  margin-bottom: 20px;
  border: 1px solid #c3e6cb;
}

.error-message {
  background: #f8d7da;
  color: #721c24;
  padding: 15px;
  border-radius: 4px;
  margin-bottom: 20px;
  border: 1px solid #f5c6cb;
}
</style>

<script>
// Handle form submission
document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form[name="contact"]');
  
  if (form) {
    form.addEventListener('submit', function(e) {
      // Basic validation
      const requiredFields = form.querySelectorAll('[required]');
      let isValid = true;
      
      requiredFields.forEach(field => {
        if (!field.value.trim()) {
          isValid = false;
          field.style.borderColor = '#dc3545';
        } else {
          field.style.borderColor = '#ddd';
        }
      });
      
      if (!isValid) {
        e.preventDefault();
        alert('Please fill in all required fields.');
      }
    });
  }
});
</script>

Feel free to reach out with any questions about:

- Machine Learning
- Python Programming
- Mathematics
- Medical Applications of AI
- Engineering Applications of AI
