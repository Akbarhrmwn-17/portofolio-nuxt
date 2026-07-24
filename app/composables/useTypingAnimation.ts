export const useTypingAnimation = (words: string[]) => {
  const typingText = ref('')
  let wordIndex = 0
  let charIndex = 0
  let isDeleting = false
  let timeoutId: ReturnType<typeof setTimeout> | null = null

  const type = () => {
    const currentWord = words[wordIndex]
    
    if (isDeleting) {
      typingText.value = currentWord.substring(0, charIndex - 1)
      charIndex--
    } else {
      typingText.value = currentWord.substring(0, charIndex + 1)
      charIndex++
    }

    let speed = isDeleting ? 50 : 80

    if (!isDeleting && charIndex === currentWord.length) {
      speed = 2000
      isDeleting = true
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false
      wordIndex = (wordIndex + 1) % words.length
      speed = 500
    }

    timeoutId = setTimeout(type, speed)
  }

  onMounted(() => {
    timeoutId = setTimeout(type, 1000)
  })

  onUnmounted(() => {
    if (timeoutId) clearTimeout(timeoutId)
  })

  return { typingText }
}
