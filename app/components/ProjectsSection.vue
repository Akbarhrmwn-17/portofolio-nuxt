<script setup lang="ts">
import ticketingImg from '~/assets/images/ticketing_project.png'
import fileopsImg from '~/assets/images/fileops_project.png'
import portfolioImg from '~/assets/images/portfolio_project.png'

const projects = [
  {
    title: 'Dauroh Ticketing',
    description: 'Platform ticketing untuk event dauroh (Islamic educational events). Features include event browsing, ticket booking, QR code verification, and payment integration.',
    image: ticketingImg,
    tags: ['Vue.js', 'Nuxt.js', 'TypeScript', 'REST API'],
    demo: '#',
    github: '#'
  },
  {
    title: 'FileOps',
    description: 'A versatile file operations tool for compressing photos, merging PDFs, converting JPG to PDF, and managing document workflows with an intuitive drag-and-drop interface.',
    image: fileopsImg,
    tags: ['JavaScript', 'Node.js', 'CSS3'],
    demo: '#',
    github: '#'
  },
  {
    title: 'Portfolio Website',
    description: 'A modern, glassmorphism-themed portfolio website with animated backgrounds, smooth scroll animations, and responsive design. Built with Nuxt 4, Vue 3, and TypeScript.',
    image: portfolioImg,
    tags: ['Nuxt.js', 'Vue.js', 'TypeScript'],
    demo: '#',
    github: '#'
  }
]
</script>

<template>
  <section id="projects" class="section">
    <div class="container">
      <div class="section-header reveal">
        <h2 class="section-title">My Projects</h2>
        <p class="section-subtitle">Some of my recent work.</p>
      </div>
      
      <div class="projects-grid">
        <div v-for="project in projects" :key="project.title" class="project-card reveal">
          <img :src="project.image" :alt="project.title" class="project-image">
          <div class="project-content">
            <div class="project-tags">
              <span v-for="tag in project.tags" :key="tag" class="project-tag">{{ tag }}</span>
            </div>
            <h3 class="project-title">{{ project.title }}</h3>
            <p class="project-description">{{ project.description }}</p>
            <div class="project-links">
              <a :href="project.demo" class="project-link" target="_blank">
                <i class="fa-solid fa-external-link-alt"></i> Live Demo
              </a>
              <a :href="project.github" class="project-link" target="_blank">
                <i class="fa-brands fa-github"></i> GitHub
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
