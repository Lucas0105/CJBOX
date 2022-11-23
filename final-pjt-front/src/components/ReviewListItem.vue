<template>
  <div class="review-item">
    <div class="d-flex mx-auto justify-content-between mt-3 mb-2" style="width:90%;" >
      <div class="d-flex" style="width:100%; ">
      <div class="profile-img my-auto">
        <div style="text-align: center;" @click="goToProfile(review.user.nickname)">
          <div class="d-flex img-box">
            <div class="r-box" style="background-color:white;   ">
              <img class="r-profile" :src="userImage" alt="userImg">
            </div>
          </div>
            <span class="nickname">{{ review.user.nickname}}</span>
        </div>
      </div>
      <div class="center-box">
        <p>작성일: {{ review.created_at }}</p>
        <p>★★★★★</p>
        <div class="content"><span class="s">{{ review.content}}</span></div>
      </div>
      </div>
      <div class="d-flex heart-box my-auto love-review">
        <p class="h3 d-flex my-auto mx-1"><b-icon icon="heart"></b-icon></p>
        <h5 class="my-auto mx-2"> 0</h5>
      </div>
    </div>
    <div class="foot d-flex justify-content-between mx-auto" >
      <div class="comment-box" @click="showModal">
        <div>
          <b-icon icon="chat-right-dots"  class="message "></b-icon>
          <span class="s">댓글 {{ review.comment_cnt}}</span>
          </div>
      </div>
      <div class="foot-span-box">
        <span class="s" style="margin-left:5px" @click="requestUpdate">
          수정
        </span>
        <span class="s" @click="deleteReview">
          삭제
        </span>
      </div>
    </div>
    
    <ReviewComment
      @close="closeModal"
      v-if="isModalVisible"
      :reviewId="review.id"
    />

  </div>
</template>

<script>
import ReviewComment from '@/components/ReviewComment'
export default {
    name:'ReviewListItem',
    props:{
      review:Object
    },
    components:{
      ReviewComment
    },
    data(){
      return{
        isModalVisible: false,
      }
    },
    methods:{
      deleteReview(){
        this.$store.dispatch('user/deleteReview', this.review.id)
      },
      requestUpdate(){
        this.$store.commit('user/REQUEST_UPDATE', this.review)
      },
      showModal() {
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
      },
      goToProfile(nickname){
      this.$router.push({name: 'mypage', params: {nickname: nickname}})

      }
    },
    computed:{
      userImage(){
        console.log(this.review.user.my_image)
        if (this.review.user.my_image){
          const index = this.review.user.my_image.indexOf("k.kakaocdn.net")
          if (index === -1){
            return "http://127.0.0.1:8000" + this.review.user.my_image
          } else {
            return 'http://' + this.review.user.my_image.slice(index,)
          }
          } else{
            return null
        }
      }
    },
}
</script>

<style scoped>
.review-item{
  width: 100%;
}

.heart-box{
  padding:10px;
  border:solid gray 1px;
  border-radius:10px;
}
.nickname{
  font-size:1.2em;

}

p{
  text-align: left;
  margin-bottom:4px;
}

.content{
  text-align: left;
  height: 100px;
}

.r-box{
  width: 70px;
  height: 70px; 
  border-radius: 100%;
  overflow: hidden;
}

.r-profile{
  position: relative;
  width: 70px;
  height: 70px;
  border-radius: 50%; /*둥그런 원으로 만들기 위함*/
  overflow: hidden;
}

.center-box{
  margin-left:2%;
  margin-right:2%;
  width:100%;
  word-break: break-all;
}

.s{
  font-size:1.15em
}
.foot{
  width: 90%;
  border-bottom:solid 1px white;
  padding-bottom:0.3em
}
.foot-span-box{
  width:9%

}

.foot-span-box>span{
  margin-right:3%
}

.foot-span-box:hover, .comment-box:hover, .love-review{
  cursor: pointer;
}

.comment-box{
  margin-left:10%
}


.message{
  margin-right:5px;
}
</style>