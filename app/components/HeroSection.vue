<script setup lang="ts">
const { typingText } = useTypingAnimation(['Frontend Developer', 'Junior DevOps', 'Backend Developer', 'AI Enthusiast'])
</script>

<template>
  <section id="hero" class="hero">
    <div class="container">
      <div class="hero-content">
        <div class="hero-badge">
          <span class="badge-dot"></span> Available for work
        </div>
        <h1 class="hero-title">Hi, I'm <span class="name">Akbar Hermawan</span></h1>
        <p class="hero-subtitle">
          I build things as a <span class="hero-typing">{{ typingText }}</span><span class="cursor">|</span>
        </p>
        <p class="hero-description">
          I'm a passionate developer focused on crafting clean, modern web experiences. I love blending beautiful design with robust engineering.
        </p>
        <div class="hero-buttons">
          <a href="#projects" class="btn btn-primary">
            <i class="fa-solid fa-rocket"></i> View Projects
          </a>
          <a href="#contact" class="btn btn-secondary">
            <i class="fa-solid fa-paper-plane"></i> Contact Me
          </a>
        </div>
        <div class="hero-social">
          <a href="https://github.com/Akbarhrmwn-17" target="_blank" aria-label="GitHub"><i class="fa-brands fa-github"></i></a>
          <a href="https://www.linkedin.com/in/akbar-hermawan-819699268" target="_blank" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
          <a href="https://www.instagram.com/akbar.hrmwn?igsh=bTdlaXRxczU4Nnlu" target="_blank" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
          <a href="mailto:akbarhrmwn74@gmail.com" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
        </div>
      </div>
    </div>
  </section>
</template>
