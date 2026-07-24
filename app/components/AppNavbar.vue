<script setup lang="ts">
const { activeSection } = useActiveSection()
const isScrolled = ref(false)
const isMobileMenuOpen = ref(false)
const navItems = [
  { name: 'Home', href: '#hero', section: 'hero' },
  { name: 'About', href: '#about', section: 'about' },
  { name: 'Skills', href: '#skills', section: 'skills' },
  { name: 'Projects', href: '#projects', section: 'projects' },
  { name: 'Contact', href: '#contact', section: 'contact' }
]

const toggleMobileMenu = () => { isMobileMenuOpen.value = !isMobileMenuOpen.value }
const closeMobileMenu = () => { isMobileMenuOpen.value = false }

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

const handleClickOutside = (e: Event) => {
  if (isMobileMenuOpen.value && !(e.target as Element).closest('.navbar')) {
    closeMobileMenu()
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  document.removeEventListener('click', handleClickOutside)
})
</script>

<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="container">
      <a href="#" class="nav-logo">AH<span class="highlight">.</span></a>
      <ul class="nav-links" :class="{ active: isMobileMenuOpen }">
        <li v-for="item in navItems" :key="item.section">
          <a :href="item.href" :class="{ active: activeSection === item.section }" @click="closeMobileMenu">{{ item.name }}</a>
        </li>
      </ul>
      <button class="nav-toggle" :class="{ active: isMobileMenuOpen }" @click.stop="toggleMobileMenu" aria-label="Toggle navigation">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
</template>
