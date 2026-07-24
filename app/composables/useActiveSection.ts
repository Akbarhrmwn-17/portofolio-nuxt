export const useActiveSection = () => {
  const activeSection = ref('hero')

  const updateActiveSection = () => {
    const sections = document.querySelectorAll('section[id]')
    const scrollY = window.scrollY

    sections.forEach((section) => {
      const el = section as HTMLElement
      const top = el.offsetTop - 100
      const height = el.offsetHeight
      const id = el.getAttribute('id')

      if (scrollY >= top && scrollY < top + height && id) {
        activeSection.value = id
      }
    })
  }

  onMounted(() => {
    window.addEventListener('scroll', updateActiveSection, { passive: true })
  })

  onUnmounted(() => {
    window.removeEventListener('scroll', updateActiveSection)
  })

  return { activeSection }
}
