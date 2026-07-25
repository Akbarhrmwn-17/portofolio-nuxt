<script setup lang="ts">
const { animateCounter } = useCounterAnimation()
const statsRef = ref<HTMLElement | null>(null)
const statsAnimated = ref(false)
const stats = [
  { target: 10, label: 'Projects Completed' },
  { target: 2, label: 'Years Experience' },
  { target: 5, label: 'Tech Stacks' }
]
const activeStatIndex = ref(0)

const handleStatScroll = (e: Event) => {
  const container = e.target as HTMLElement
  const maxScroll = container.scrollWidth - container.clientWidth
  if (maxScroll <= 0) return
  const progress = container.scrollLeft / maxScroll
  activeStatIndex.value = Math.round(progress * (stats.length - 1))
}

onMounted(() => {
  if (!statsRef.value) return

  const observer = new IntersectionObserver((entries) => {
    const entry = entries[0]
    if (entry.isIntersecting && !statsAnimated.value) {
      statsAnimated.value = true
      const statElements = statsRef.value?.querySelectorAll('.stat-number')
      statElements?.forEach((el) => {
        const target = parseInt(el.getAttribute('data-target') || '0', 10)
        animateCounter(el as HTMLElement, target)
      })
      observer.disconnect()
    }
  }, { threshold: 0.5 })

  observer.observe(statsRef.value)
})
</script>

<template>
  <section id="about" class="section">
    <div class="container">
      <div class="section-header reveal">
        <h2 class="section-title">About Me</h2>
        <p class="section-subtitle">Get to know me better.</p>
      </div>
      
      <div class="about-grid">
        <div class="about-image-wrapper reveal reveal-left">
          <div class="about-image-placeholder">
            <i class="fa-solid fa-code"></i>
          </div>
        </div>
        
        <div class="about-text reveal reveal-right">
          <h3>My coding journey</h3>
          <p>
            I'm a dedicated web developer based in Indonesia, with a strong passion for building digital products that provide great user experiences. 
          </p>
          <p>
            With a background in both frontend and backend technologies, I bring a well-rounded perspective to the development process. I enjoy diving deep into technical challenges and figuring out elegant solutions.
          </p>
          <p>
            When I'm not coding, I'm usually exploring new AI tools, contributing to open-source, or learning the latest advancements in the tech world.
          </p>
          
          <div class="about-stats-container">
            <div class="about-stats" ref="statsRef" @scroll="handleStatScroll">
              <div v-for="(stat, index) in stats" :key="index" class="stat-card">
                <div class="stat-number" :data-target="stat.target">0</div>
                <div class="stat-label">{{ stat.label }}</div>
              </div>
            </div>
            <div class="slider-dots">
              <div v-for="(_, index) in stats" :key="index" class="slider-dot" :class="{ active: activeStatIndex === index }"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
