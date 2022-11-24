<template>
<div class="info-bg" :style="{ backgroundImage: `url(${movie?.backdrop_path})` }">
  <div v-if="movie" class="content-box d-flex mx-auto px-5">
      <div class="left-box d-flex flex-column">
        <img :src="movie.poster_path" alt="">
        <div class="mx-auto">
          <small><b-icon icon="heart"  class="loved"></b-icon></small>
          <span> My List에 담기</span>
        </div>
      </div> 

      <div class=" d-flex flex-column detail-box">

        <h3 class="mx-3 mt-3">{{ movie.title}}</h3>
        <div class="star-rating">
            <star-rating :rating="movie.vote_average/2" :read-only="true" :increment="0.01" :star-size="20" :show-rating="false"></star-rating>
        </div>
        <div class="d-flex justify-content-between my-4">

        <div class="d-flex">
          <div v-for="(genre, index) in movie.genres" :key="index" class="mx-3">
            <router-link :to="{ name: 'genre', params: {category: genre.name} }">
              <b-button pill variant="dark">
              <span>{{genre.name}}</span>
              </b-button>
            </router-link>
          </div>
        </div>
        <iframe class="mt-5 ms-5" id="player" type="text/html" width="400" height="200"
          :src="getVideo"
          frameborder="0">
        </iframe>
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
import StarRating from 'vue-star-rating'

export default {
    name:'MovieInfo',
    props:{
        movie:Object
    },
    components:{
      StarRating
    },
    computed:{
      getVideo(){
        return this.$store.state.movie.detailVideo ? 'http://www.youtube.com/embed/' + this.$store.state.movie.detailVideo:false
      }
    },
    methods:{
      ratingToPercent() {
        const score = +(this.movie.vote_average/2) * 20;
        return score+1.5;
      },
    },
}
</script>

<style scoped>
.info-bg{
  background-repeat: no-repeat;
background-size: 100% 100%;
  filter: saturate(90%);

}
.content-box{
  padding-top:60px;
  width:80%;
  color:aliceblue;
  padding-bottom: 40px;
  background-color: rgb(0, 0, 0);
  opacity: 0.9;
  margin-top: 4.2%;
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
#player{
  position: absolute;
  top: 10%;
  right: 15%;
}
</style>