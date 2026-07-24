<script setup lang="ts">
const activeCategory = ref('all')
const categories = [
  { name: 'All', value: 'all' },
  { name: 'Frontend', value: 'frontend' },
  { name: 'Backend', value: 'backend' },
  { name: 'DevOps & Tools', value: 'devops' }
]

const skills = [
  { name: 'HTML5', icon: 'fa-brands fa-html5', level: 90, levelText: 'Advanced', category: 'frontend' },
  { name: 'CSS3', icon: 'fa-brands fa-css3-alt', level: 85, levelText: 'Advanced', category: 'frontend' },
  { name: 'JavaScript', icon: 'fa-brands fa-js', level: 85, levelText: 'Advanced', category: 'frontend' },
  { name: 'TypeScript', icon: 'fa-solid fa-code', level: 75, levelText: 'Intermediate', category: 'frontend' },
  { name: 'Vue.js', icon: 'fa-brands fa-vuejs', level: 80, levelText: 'Advanced', category: 'frontend' },
  { name: 'Nuxt.js', icon: 'fa-brands fa-vuejs', level: 75, levelText: 'Intermediate', category: 'frontend' },
  
  { name: 'Node.js', icon: 'fa-brands fa-node-js', level: 70, levelText: 'Intermediate', category: 'backend' },
  { name: 'Python', icon: 'fa-brands fa-python', level: 65, levelText: 'Intermediate', category: 'backend' },
  { name: 'REST API', icon: 'fa-solid fa-plug', level: 75, levelText: 'Intermediate', category: 'backend' },
  { name: 'AI/ML', icon: 'fa-solid fa-brain', level: 60, levelText: 'Intermediate', category: 'backend' },
  
  { name: 'Git', icon: 'fa-brands fa-git-alt', level: 80, levelText: 'Advanced', category: 'devops' },
  { name: 'Docker', icon: 'fa-brands fa-docker', level: 65, levelText: 'Intermediate', category: 'devops' },
  { name: 'Linux', icon: 'fa-brands fa-linux', level: 70, levelText: 'Intermediate', category: 'devops' },
  { name: 'CI/CD', icon: 'fa-solid fa-rotate', level: 60, levelText: 'Intermediate', category: 'devops' },
  { name: 'Nginx', icon: 'fa-solid fa-server', level: 60, levelText: 'Intermediate', category: 'devops' }
]

const filteredSkills = computed(() => {
  if (activeCategory.value === 'all') return skills
  return skills.filter(skill => skill.category === activeCategory.value)
})

const setCategory = (cat: string) => {
  activeCategory.value = cat
  setTimeout(() => {
    initSkillBars()
  }, 50)
}

const initSkillBars = () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target.querySelector('.skill-bar') as HTMLElement
        if (bar) {
          bar.style.width = bar.getAttribute('data-width') + '%'
        }
        observer.unobserve(entry.target)
      }
    })
  }, { threshold: 0.1 })

  document.querySelectorAll('.skill-card').forEach(card => {
    const bar = card.querySelector('.skill-bar') as HTMLElement
    if (bar) {
      bar.style.width = '0%'
    }
    observer.observe(card)
  })
}

onMounted(() => {
  initSkillBars()
})
</script>

<template>
  <section id="skills" class="section">
    <div class="container">
      <div class="section-header reveal">
        <h2 class="section-title">My Skills</h2>
        <p class="section-subtitle">Technologies and tools I work with.</p>
      </div>
      
      <div class="skills-categories reveal">
        <button 
          v-for="cat in categories" 
          :key="cat.value"
          class="skill-category-btn"
          :class="{ active: activeCategory === cat.value }"
          @click="setCategory(cat.value)"
        >
          {{ cat.name }}
        </button>
      </div>
      
      <div class="skills-grid">
        <TransitionGroup name="fade">
          <div 
            v-for="skill in filteredSkills" 
            :key="skill.name" 
            class="skill-card" 
            :data-category="skill.category"
          >
            <div class="skill-header">
              <div class="skill-icon">
                <i :class="skill.icon"></i>
              </div>
              <div>
                <div class="skill-name">{{ skill.name }}</div>
                <div class="skill-level">{{ skill.levelText }}</div>
              </div>
            </div>
            <div class="skill-bar-wrapper">
              <div class="skill-bar" :data-width="skill.level" style="width: 0%;"></div>
            </div>
          </div>
        </TransitionGroup>
      </div>
    </div>
  </section>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
