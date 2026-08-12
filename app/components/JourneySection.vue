<script setup lang="ts">
const journeys = [
  {
    year: '2026 - Present',
    title: 'Diving into DevOps & Infrastructure',
    description: 'Expanding my skill set by setting up a personal VPS, configuring Nginx as a reverse proxy, managing background processes with PM2, and containerizing applications with Docker. Currently exploring Home Lab setups.',
    icon: 'fa-solid fa-server',
  },
  {
    year: '2026',
    title: 'Developed Ticketing System',
    description: 'Built a robust ticketing and helpdesk system. Focused on implementing secure RESTful APIs, role-based access control, and efficient database modeling for issue tracking.',
    icon: 'fa-solid fa-ticket',
  },
  {
    year: '2025 - 2026',
    title: 'Created FileOps',
    description: 'Engineered a comprehensive file management application to handle secure file operations, storage optimizations, and structured document handling on the backend.',
    icon: 'fa-solid fa-folder-open',
  },
  {
    year: '2025',
    title: 'Frontend Mastery & Portfolio',
    description: 'Mastered modern web development with Vue.js, Nuxt.js, and advanced CSS techniques (Glassmorphism, animations). Built this interactive portfolio to showcase my journey.',
    icon: 'fa-solid fa-code',
  }
]
</script>

<template>
  <section id="journey" class="section">
    <div class="container">
      <div class="section-header reveal">
        <h2 class="section-title">Learning Journey</h2>
        <p class="section-subtitle">My continuous path of learning and building.</p>
      </div>

      <div class="timeline">
        <div 
          v-for="(item, index) in journeys" 
          :key="index" 
          class="timeline-item reveal"
        >
          <div class="timeline-dot">
            <i :class="item.icon"></i>
          </div>
          <div class="timeline-content">
            <div class="timeline-year">{{ item.year }}</div>
            <h3 class="timeline-title">{{ item.title }}</h3>
            <p class="timeline-description">{{ item.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.timeline {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 0;
}

.timeline::before {
  content: '';
  position: absolute;
  top: 0;
  left: 24px;
  height: 100%;
  width: 2px;
  background: rgba(0, 212, 255, 0.2);
}

.timeline-item {
  position: relative;
  margin-bottom: 40px;
  padding-left: 70px;
}

.timeline-item:last-child {
  margin-bottom: 0;
}

.timeline-dot {
  position: absolute;
  left: 0;
  top: 0;
  width: 50px;
  height: 50px;
  background: var(--bg-dark);
  border: 2px solid var(--accent-cyan);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent-cyan);
  font-size: 1.2rem;
  z-index: 1;
  box-shadow: 0 0 15px rgba(0, 212, 255, 0.2);
  transition: var(--transition);
}

.timeline-item:hover .timeline-dot {
  background: var(--accent-cyan);
  color: var(--bg-dark);
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
  transform: scale(1.1);
}

.timeline-content {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  padding: 24px;
  transition: var(--transition);
}

.timeline-item:hover .timeline-content {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 212, 255, 0.1);
  border-color: rgba(0, 212, 255, 0.3);
}

.timeline-year {
  display: inline-block;
  padding: 4px 12px;
  background: rgba(0, 212, 255, 0.1);
  color: var(--accent-cyan);
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 12px;
}

.timeline-title {
  font-size: 1.25rem;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.timeline-description {
  color: var(--text-secondary);
  line-height: 1.6;
  font-size: 0.95rem;
}

@media (min-width: 768px) {
  .timeline::before {
    left: 50%;
    transform: translateX(-50%);
  }

  .timeline-item {
    width: 50%;
    padding-left: 0;
    padding-right: 40px;
    margin-bottom: 60px;
  }

  .timeline-item:nth-child(even) {
    margin-left: auto;
    padding-right: 0;
    padding-left: 40px;
  }

  .timeline-dot {
    left: 100%;
    transform: translateX(-50%);
  }

  .timeline-item:nth-child(even) .timeline-dot {
    left: 0;
    transform: translateX(-50%);
  }
  
  .timeline-item:hover .timeline-dot {
    transform: translateX(-50%) scale(1.1);
  }
}
</style>
