<template>
  <swiper
    slidesPerView="auto"
    mousewheel
    freeMode
    navigation
  >
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--4NgMf3RF--/v1521804358/avengers.jpg"
        title="Avengers : Infinity War"
        description="Thanos is around"
        duration="2hrs"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--BmgguRnX--/v1521804402/thor.jpg"
        title="Thor : Ragnarok"
        description="Thor lost his hair"
        duration="2hrs30mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--qXaW5V3E--/v1521804426/wakanda.jpg"
        title="Black Panther"
        description="Wakanda Forever"
        duration="2hrs15mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--4NgMf3RF--/v1521804358/avengers.jpg "
        title="Avengers : Infinity War"
        description="Thanos is around"
        duration="2hrs"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--BmgguRnX--/v1521804402/thor.jpg"
        title="Thor : Ragnarok"
        description="Thor lost his hair"
        duration="2hrs30mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--qXaW5V3E--/v1521804426/wakanda.jpg"
        title="Black Panther"
        description="Wakanda Forever"
        duration="2hrs15mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--4NgMf3RF--/v1521804358/avengers.jpg "
        title="Avengers : Infinity War"
        description="Thanos is around"
        duration="2hrs"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--BmgguRnX--/v1521804402/thor.jpg"
        title="Thor : Ragnarok"
        description="Thor lost his hair"
        duration="2hrs30mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--qXaW5V3E--/v1521804426/wakanda.jpg"
        title="Black Panther"
        description="Wakanda Forever"
        duration="2hrs15mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--4NgMf3RF--/v1521804358/avengers.jpg"
        title="Avengers : Infinity War"
        description="Thanos is around"
        duration="2hrs"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--BmgguRnX--/v1521804402/thor.jpg"
        title="Thor : Ragnarok"
        description="Thor lost his hair"
        duration="2hrs30mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--qXaW5V3E--/v1521804426/wakanda.jpg"
        title="Black Panther"
        description="Wakanda Forever"
        duration="2hrs15mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--4NgMf3RF--/v1521804358/avengers.jpg "
        title="Avengers : Infinity War"
        description="Thanos is around"
        duration="2hrs"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--BmgguRnX--/v1521804402/thor.jpg"
        title="Thor : Ragnarok"
        description="Thor lost his hair"
        duration="2hrs30mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--qXaW5V3E--/v1521804426/wakanda.jpg"
        title="Black Panther"
        description="Wakanda Forever"
        duration="2hrs15mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--4NgMf3RF--/v1521804358/avengers.jpg "
        title="Avengers : Infinity War"
        description="Thanos is around"
        duration="2hrs"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--BmgguRnX--/v1521804402/thor.jpg"
        title="Thor : Ragnarok"
        description="Thor lost his hair"
        duration="2hrs30mins"
      />
    </swiper-slide>
    <swiper-slide style="width: 202px">
      <BannerListItem
        image="http://res.cloudinary.com/og-tech/image/upload/s--qXaW5V3E--/v1521804426/wakanda.jpg"
        title="Black Panther"
        description="Wakanda Forever"
        duration="2hrs15mins"
      />
    </swiper-slide>
    <div class="swiper-button-prev" slot="button-prev"></div>
    <div class="swiper-button-next" slot="button-next"></div>
  </swiper>
</template>

<script>
import BannerListItem from "./BannerListItem";
import {  Mousewheel, Navigation } from "swiper";
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