<template>
  <div>
    <Hero />
    <Products />
    <Banner />
    <Products />
    <BannerT />
    <Blog />
  </div>
</template>
<script>
import Hero from "../components/Hero";
import Products from "../components/Products";
import Banner from "../components/Banner";
import Blog from "../components/Blog";
import BannerT from "../components/BannerT";
export default {
  components: {
    Hero,
    Products,
    Banner,
    Blog,
    BannerT,
  },
};
</script>
