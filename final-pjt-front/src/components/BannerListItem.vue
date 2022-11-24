<template>
<div>
  <div v-if="isLoading" class="movie empty" :title="title" @click="toUrl">
    <div class="content" >
    </div>
  </div>
  <div v-else class="movie" :title="title" :style="{ backgroundImage: 'url(' + image + ')' }" @click="toUrl">
    <div class="content" >
    </div>
  </div>
</div>
</template>

<script>
export default {
    name:'BannerListItem',
    data(){
      return {
        isLoading: true,
      }
    },
    props : [
    'image',
    'id',
    'title',
  ],
  methods: {
    toUrl() {
      this.$router.push({name:'detail', params:{id: this.id}})
      this.$router.go(this.$router.currentRoute)
    },
    changLoading(){
      this.isLoading = false
    }
  },
  mounted(){
    setTimeout(() => {this.changLoading()}, 1500);
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.movie{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-end;
  text-align: left;
  width : 100%;
  height : 800px;
  /* background-color: rgba(255, 255, 255, 0.7); */
  background-repeat: no-repeat;
  background-blend-mode: overlay;
  background-size: contain;
  background-position: center;
  transition: all 0.2s linear;
  cursor: pointer;
}
.empty{
  background-image: url('@/assets/CJBOX_logo2-1.gif');
}
.movie:hover{
  transform: scale(1.2);
  z-index: 100;
}
.content {
  padding: 10px;
}
</style>
