<script setup lang="ts">
useHead({
  title: 'Akbar Hermawan | Frontend Developer & DevOps',
})

useSeoMeta({
  title: 'Akbar Hermawan | Frontend Developer & DevOps',
  description: 'Portfolio of Akbar Hermawan - Frontend Developer, Junior DevOps, and Backend Developer with AI expertise',
  ogTitle: 'Akbar Hermawan | Frontend Developer & DevOps',
  ogDescription: 'Portfolio of Akbar Hermawan - Frontend Developer, Junior DevOps, and Backend Developer with AI expertise',
  ogType: 'website',
})

const { addRevealRef } = useScrollReveal()
</script>

<template>
  <div>
    <BgAnimation />
    <AppNavbar />
    <HeroSection />
    <AboutSection />
    <SkillsSection />
    <JourneySection />
    <ProjectsSection />
    <ContactSection />
    <AppFooter />
    <BackToTop />
  </div>
</template>
