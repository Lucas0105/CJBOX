<template>
  <swiper
    slidesPerView="auto"
    mousewheel
    freeMode
    navigation
    observer
  >
    <swiper-slide 
    v-for="movie in movies"
    :key="movie.id"
    style="width: 202px">
      <BannerListItem
        :image="movie.poster_path"
        :id="movie.id"
      />
    </swiper-slide>
    <div class="swiper-button-prev" slot="button-prev"></div>
    <div class="swiper-button-next" slot="button-next"></div>
  </swiper>
</template>

<script>
import BannerListItem from "./BannerListItem";
import {  Mousewheel, Navigation, } from "swiper";
import { SwiperCore, Swiper, SwiperSlide } from "swiper-vue2";

import "swiper/swiper-bundle.css";

SwiperCore.use([ Mousewheel, Navigation]);

export default {
    name:'BannerList',
    components: {
    BannerListItem,
    Swiper,
    SwiperSlide,
  },
  props:{
    movies: Array
  },
    data() {
    return {
      swiperOptions: {
        slidesPerView: "auto",
        spaceBetween: 0,
        freeMode: true,
        mousewheel: true,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      },
    };
  },
}
</script>

<style scoped>
.swiper-slide {
  display: flex;
  justify-content: center;
  flex-direction: column;
  width: 202px;
}
.swiper-container {
  height: 450px;
  width: 100%;
  z-index: 0;
}

.swiper-button-next {
  background: url("@/assets/next-icon.png") no-repeat;
  background-size: 50% auto;
  background-position: center;
}

.swiper-button-prev {
  background: url("@/assets/previous-icon.png") no-repeat;
  background-size: 50% auto;
  background-position: center;
}

.swiper-button-next::after,
.swiper-button-prev::after {
  display: none;
}

</style>