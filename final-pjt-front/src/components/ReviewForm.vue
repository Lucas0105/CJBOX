<template>
  <div class="review-list">
    <form @submit.prevent="inputReview" class="review-form">
      <div v-if="isLogin">
        <h3>
        유저평점 ☆☆☆☆☆
        </h3>
        <label class="d-flex flex-column">
          <textarea name="" id="" cols="10" rows="4"  wrap="hard" maxlength="250" v-model="content"></textarea>
          <b-button type="submit" class="t-btn mt-3">등록</b-button>
        </label>

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

<style scoped>
textarea{
  border:none;
  color:aliceblue;
  background-color: #6b778d;
  width:100%;
  resize: none;
  border-radius: 4px;
}
textarea:focus{
    outline: 0;
}

.review-list{
  text-align: center;
}

.t-btn{
  margin-left:90%;
  width: 10%;
  margin-right:0%;
  background-color: #ff6768;
  border:none;

}
.btn:hover{
  background-color: #6b778d !important;
}
</style>