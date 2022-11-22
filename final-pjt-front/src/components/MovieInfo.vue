<template>
<div class="info-bg" :style="{ backgroundImage: `url(${movie?.backdrop_path})` }">
  <div v-if="movie" class="content-box d-flex mx-auto">
      <div class="left-box d-flex flex-column">
        <img :src="movie.poster_path" alt="">
        <div class="mx-auto">
          <small><b-icon icon="heart"  class="loved"></b-icon></small>
          <span> My List에 담기</span>
        </div>
      </div>

      <div class=" d-flex flex-column detail-box">

        <h3 class="mx-3 mt-3">{{ movie.title}}</h3>
        <div class="rate d-flex mx-3">
          <div
          class="star"
          v-for="index in 5"
          :key ="index"
          >
              <b-icon icon="star-fill"  class="star-fill" v-if="index <= movie.vote_average/2"></b-icon>
              <b-icon icon="star"  class="star" v-else></b-icon>
          </div>
        </div>
        <div class="d-flex">
          <div v-for="(genre, index) in movie.genres" :key="index" class="mx-3">
            <router-link :to="{ name: 'genre', params: {category: genre.name} }">
              <b-button pill variant="dark">
              <span>{{genre.name}}</span>
              </b-button>
            </router-link>
          </div>
        </div>

        <div class="overview mx-3">
          <h5>줄거리</h5>
          <div>
            {{ movie.overview}}
          </div>
        </div>

      </div>
    </div>


</div>

</template>

<script>
export default {
    name:'MovieInfo',
    props:{
        movie:Object
    },
    methods:{
        ratingToPercent() {
        const score = +(this.movie.vote_average/2) * 20;
        return score+1.5;
    }
    }
}
</script>

<style scoped>
.info-bg{
  background-repeat: no-repeat;
background-size: 100% 100%;
  filter: saturate(90%);

}
.content-box{
  padding-top:120px;
  width:80%;
  color:aliceblue;
  padding-bottom: 40px;
}
.detail-box{
  margin-left:3%;
}
.left-box{
  width:20%
}
.overview{
  font-size: 16px
}
.star-fill{
    color: #FFD400;
}
</style>