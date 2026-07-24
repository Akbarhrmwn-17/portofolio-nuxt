export const useScrollReveal = () => {
  const revealElements = ref<HTMLElement[]>([])
  let observer: IntersectionObserver | null = null

  const addRevealRef = (el: Element | ComponentPublicInstance | null) => {
    if (el instanceof HTMLElement && !revealElements.value.includes(el)) {
      revealElements.value.push(el)
    }
  }

  onMounted(() => {
    observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('active')
            observer?.unobserve(entry.target)
          }
        })
      },
      { threshold: 0.15, rootMargin: '0px 0px -50px 0px' }
    )

    // Observe elements added via ref
    revealElements.value.forEach((el) => observer?.observe(el))
    
    // Also observe any elements with .reveal class already in DOM
    document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach((el) => {
      observer?.observe(el)
    })
  })

  onUnmounted(() => {
    observer?.disconnect()
  })

  return { addRevealRef }
}
