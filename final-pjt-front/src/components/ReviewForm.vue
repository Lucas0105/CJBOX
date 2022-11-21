<template>
  <div class="review-list">
    <form @submit.prevent="inputReview" class="review-form">
      <div v-if="isLogin">
        <h3>
        유저평점 ☆☆☆☆☆
        </h3>
        <input type="text" v-model="content">
        <b-button type="submit">등록</b-button>
      </div>
      <div v-else>
        <p>로그인이 필요한 서비스입니다.
          <router-link :to="{name:'login'}">로그인하러 가기</router-link>

        </p>
      </div>
    </form>

  </div>
</template>

<script>
export default {
    name:'ReviewForm',
    data() {
      return{
        content:null
      }
    },
    props:{
      movie:Object
    },
    computed:{
      isLogin(){
        return this.$store.getters['user/isLogin']
      }
    },
    methods:{
      inputReview() {
        const movie_id = this.movie.id
        const content = this.content
        const payload ={
          movie_id,content
        }

        this.$store.dispatch('user/inputReview', payload)
        
        this.content = null
      },
    }
}
</script>

<style>
.review-list{
  text-align: center;
}
</style>