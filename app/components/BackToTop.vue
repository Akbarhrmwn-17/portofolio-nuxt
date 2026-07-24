<script setup lang="ts">
const isVisible = ref(false)

const handleScroll = () => {
  isVisible.value = window.scrollY > 500
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <button class="back-to-top" :class="{ visible: isVisible }" @click="scrollToTop" aria-label="Back to top">
    <i class="fa-solid fa-arrow-up"></i>
  </button>
</template>
