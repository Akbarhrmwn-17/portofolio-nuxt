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
          <a href="#" aria-label="GitHub"><i class="fa-brands fa-github"></i></a>
          <a href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
          <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
          <a href="#" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
        </div>
      </div>
      <div class="hero-scroll-indicator">
        <div class="mouse">
          <div class="mouse-dot"></div>
        </div>
        <span>Scroll Down</span>
      </div>
    </div>
  </section>
</template>
