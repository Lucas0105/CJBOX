<template>
  <div :title="movie.title" class="col-6 col-lg-3 col-xxl-2 movie-card">
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
          <div>
            <b-icon icon="heart-fill" class="loved" v-if="loved"></b-icon>
            <b-icon icon="heart"  class="loved" v-else></b-icon>
            <span style="color:aliceblue"> {{getMovie.like_users.length}}</span>
          </div>
        </div>
        <div>
          <small> 
            <b-icon icon="star-fill" class="star"></b-icon>
            <span class="star-text"> {{ getMovie.vote_average}}</span> 
            <span> ({{ getMovie.vote_count }})</span>
          </small>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'BodyListItem',
    data(){
      return{
        res_movie: null,
      }
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
 
    }
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
</style>