<template>
<div class="col-6 col-lg-3 col-xxl-2">
  <Transition name="slide-fade">
  <div v-if="isLoading" class="movie-card">
       <b-card
        img-src="/img/CJBOX_logo2-2.7c08a6c4.gif"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 15rem;"
        class="mb-2 border-0"
        @click="toDetail"
      >
      </b-card>
  </div>
  </Transition>
  <Transition name="slide-fade">
  <div v-if="nextLoading" :title="movie.title" class="movie-card">
       <b-card
        :img-src="movie.poster_path"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 15rem;"
        class="mb-2 border-0"
        @click="toDetail"
      >
      </b-card>
      <b-card-text >
        <span :title="movie.title">
          {{ movie.title | resize }}
        </span><br>
        
      </b-card-text>

      <div class="bottom-icon d-flex justify-content-between mx-auto mb-2" >
        <div @click="addMyList" style="cursor: pointer">
          <div :title="`${getMovie.like_users.length}명이 이 영화를 좋아합니다.`">
            <b-icon icon="heart-fill" class="loved" v-if="loved"></b-icon>
            <b-icon icon="heart"  class="loved" v-else></b-icon>
            <span style="color:aliceblue"> </span>
          </div>
        </div>
        <!-- <div class="d-flex">
            <star-rating :rating="getMovie.vote_average/2" :read-only="true" :increment="0.01" :star-size="16" :show-rating="false" ></star-rating>
            <div style="color:snow"> ({{ getMovie.vote_count }})</div>
        </div> -->
      </div>
  </div>
  </Transition>
</div>
</template>

<script>
import axios from 'axios'
// import StarRating from 'vue-star-rating'

export default {
    name:'BodyListItem',
    data(){
      return{
        res_movie: null,
        isLoading: true,
        nextLoading: false,
      }
    },
    components:{
      // StarRating
    },
    props:{
      movie : Object,
    },
    filters:{
      resize(value){
        if(value.length >= 18){
          value = value.slice(0,17) + '...'
          return value
        }else{
          return value
        }
      }
    },
    methods:{
      toDetail() {
        this.$router.push({name:'detail', params:{id: this.movie.id}})
      },
      addMyList(){
        axios({
          method:'post',
          url:`http://127.0.0.1:8000/accounts/myList/`,
          data:{
            movie_id:this.movie.id
          },
          headers:{
            Authorization : `Token ${this.$store.state.user.token}`
          }
        })
        .then((res)=>{
          this.res_movie = res.data
        })
        .catch((err)=>{
          console.log(err)
        })

      },
      changeLoading(){
        this.isLoading = false
        setTimeout(() => {
          this.nextLoading = true
      }, 800)
      }
    },
    computed:{
      loginUserName(){
        return this.$store.state.user.login_user.nickname
      },
      loved(){
        return this.getMovie.like_users.some(user=>user.nickname === this.loginUserName)
      },
      getMovie(){
        if (this.res_movie) {
          return this.res_movie
        } else {
          return this.movie
        }
      }
 
    },
    mounted(){
      setTimeout(() => {
        this.changeLoading()
      }, 1500)
    },
  }
</script>

<style scoped>

.card{
  margin:auto !important;
  --bs-card-bg: none;
  transition: all 0.2s linear;
  cursor: pointer;
}
.card:hover{
  transform: scale(1.2);
}
.card-body{
  background-color: #17223b !important;
}
.card-text{
  color:aliceblue  !important;
  font-size:15px;
  margin-bottom: 0;
}
.card-img-top{
  height:300px !important;
}

.loved{
  color:red
}
.star, .star-text{
  color:#FFD400
}
.bottom-icon{
  max-width: 15rem;
  padding-left: 1em;
  padding-right: 1em;
  padding-bottom: 1em;
}
span{
  color:aliceblue
}
.card-body{
  padding-bottom: 0 !important;
}
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>