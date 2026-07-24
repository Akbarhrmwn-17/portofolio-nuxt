<script setup lang="ts">
const name = ref('')
const email = ref('')
const subject = ref('')
const message = ref('')

const showNotification = ref(false)
const notificationMessage = ref('')

const contactMethods = [
  { icon: 'fa-solid fa-envelope', title: 'Email', value: 'hello@akbarhermawan.dev' },
  { icon: 'fa-solid fa-location-dot', title: 'Location', value: 'Indonesia' },
  { icon: 'fa-brands fa-linkedin-in', title: 'LinkedIn', value: 'Akbar Hermawan' }
]

const handleSubmit = () => {
  notificationMessage.value = `Thanks for reaching out, ${name.value}! I'll get back to you soon.`
  showNotification.value = true
  
  name.value = ''
  email.value = ''
  subject.value = ''
  message.value = ''
  
  setTimeout(() => {
    showNotification.value = false
  }, 5000)
}
</script>

<template>
  <section id="contact" class="section">
    <div class="container">
      <div class="section-header reveal">
        <h2 class="section-title">Get In Touch</h2>
        <p class="section-subtitle">Let's build something together.</p>
      </div>
      
      <div class="contact-grid">
        <div class="contact-info reveal reveal-left">
          <h3>Contact Information</h3>
          <p>Feel free to reach out to me for any questions or opportunities!</p>
          
          <div class="contact-methods">
            <div v-for="method in contactMethods" :key="method.title" class="contact-method">
              <i :class="method.icon"></i>
              <div>
                <h4>{{ method.title }}</h4>
                <p>{{ method.value }}</p>
              </div>
            </div>
          </div>
        </div>
        
        <form class="contact-form reveal reveal-right" @submit.prevent="handleSubmit">
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" id="name" v-model="name" required>
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" v-model="email" required>
          </div>
          <div class="form-group">
            <label for="subject">Subject</label>
            <input type="text" id="subject" v-model="subject" required>
          </div>
          <div class="form-group">
            <label for="message">Message</label>
            <textarea id="message" v-model="message" rows="5" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary form-submit">Send Message</button>
        </form>
      </div>
    </div>
  </section>

  <Teleport to="body">
    <Transition name="slide-up">
      <div v-if="showNotification" class="notification-glass">
        {{ notificationMessage }}
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.slide-up-enter-active,
.slide-up-leave-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}
.slide-up-enter-from,
.slide-up-leave-to {
  transform: translateY(20px) translateX(-50%);
  opacity: 0;
}
.notification-glass {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 1rem 2rem;
  border-radius: 8px;
  color: white;
  z-index: 1000;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
