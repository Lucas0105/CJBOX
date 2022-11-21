<template>
  <div class="review-item">
    {{ review}}
    
  </div>
</template>

<script>
export default {
    name:'ReviewListItem',
    props:{
      review:Object
    }
}
</script>

<style scoped>
.review-item{
  border:solid 1px red
}

</style>