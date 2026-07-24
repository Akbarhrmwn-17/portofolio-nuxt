export const useCounterAnimation = () => {
  const animateCounter = (element: HTMLElement, target: number) => {
    const duration = 2000
    const startTime = performance.now()

    const update = (currentTime: number) => {
      const elapsed = currentTime - startTime
      const progress = Math.min(elapsed / duration, 1)
      const eased = 1 - Math.pow(1 - progress, 3)
      const current = Math.floor(eased * target)
      element.textContent = current.toString()

      if (progress < 1) {
        requestAnimationFrame(update)
      } else {
        element.textContent = target + '+'
      }
    }

    requestAnimationFrame(update)
  }

  return { animateCounter }
}
