<template>
<div  class="col-6 col-lg-3 col-xxl-2 movie-card image-hover-text-container" >
    <div class="image-hover-image">
          <b-img :src="movie.poster_path" fluid alt="Responsive image" @click="goToDetail" style="cursor: pointer"></b-img>
        <div class="image-hover-text">
        <div class="image-hover-text-bubble">
        <span class="image-hover-text-title">Sample</span>
        This is a sample image
        </div>
    </div>
</div>

    <!-- <b-card :img-src="movie.poster_path" img-alt="Image" img-top @click="goToDetail">  -->
    <!-- <b-card-text>
    {{ movie.title }}
    <star-rating :rating="movie.vote_average/2" :read-only="true" :increment="0.01" :star-size="16" :show-rating="false"></star-rating><span>({{movie.vote_count}})</span>
    </b-card-text> -->
    <!-- </b-card> -->
    <!-- <div class="love-box">
        <small><b-icon icon="heart-fill"  class="loved" @click="addMyList"></b-icon><span class="cnt" @click="addMyList">좋아요 취소</span></small>
    </div> -->
</div>

</template>

<script>
// import StarRating from 'vue-star-rating'

export default {
    name:'MyList',
    data(){
        return{
            res_mylist :null
        }
    },
    components:{
    //   StarRating
    },
    props:{
        movie:Object,
    },
    methods:{
      goToDetail(){
        this.$router.push({name:'detail', params:{id: this.movie.id}})
      },
      addMyList(){
        this.$store.dispatch('user/addMyList', this.movie.id)
      }
    },

}
</script>

<style scoped>


.card{
   margin:auto !important;
  --bs-card-bg: none;
  transition: all 0.2s linear;
  cursor: pointer;
  overflow-block: auto;
}

.card-body{
    padding:none
}
.loved{
    color: red;
    
}

.cnt{
    font-weight: bold;
}
img{
    border-radius:10px
}
.love-box{
    cursor: pointer
}
.image-hover-text-container 
{
  position: relative;
  display: inline-block;
  width: auto;
  height: auto;
  transition: all 0.2s linear;
}

.image-hover-image 
{
 display: block;
}
/* Make the image round */
.image-hover-image img
{
  border-radius: 4px;
  width:7em;
}


.image-hover-text 
{
  position: absolute;
  top: 0;
  width: 100%;  
  height: 100%;
  margin: 0 auto;
  opacity: 0;
  cursor: default;
  transition: opacity 0.2s linear;
}
.image-hover-text:hover 
{
  opacity: 1;
}


.image-hover-text-bubble 
{
  position: relative;
  box-sizing: border-box;
  top: 0; left: 0; right: 100%;
  height: 100%;
  text-align: center;
  background: rgba(218, 211, 211, 0.9);
  border-radius: 0%;
  margin: 0 auto;
  padding: 30% 0px;
  overflow: hidden;
  font-size: 17px;
  text-align: center;
  word-wrap: break-word;
}

.image-hover-text .image-hover-text-title
{
  font-size: 25px;
  display: block;
}

</style>