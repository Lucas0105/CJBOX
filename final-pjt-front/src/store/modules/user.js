import axios from 'axios'



const URL = 'http://127.0.0.1:8000'

const state = () => {
    return {
      token : null, 
      login_user : {
        nickname : null,
        my_image : null
      }
    }
  }
  const getters = {
    isLogin(state){
      return state.token ? true : false
    }
  }
  const mutations = {
    SAVE_TOKEN(state, token){
      state.token = token
      // console.log(state.token)
    }
  }
  const actions = {
    // 400 오류
    signUp(context, payload) {
      console.log(payload)
      axios({
        method:'post',
        url: `${URL}/accounts/signup/`,
        data:{
          username : payload.username,
          nickname : payload.nickName,
          email : payload.email,
          password1 : payload.password1,
          password2 : payload.password2,
          intro : payload.intro,
          my_image : payload.image
        },
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then((res)=>{
        console.log(res)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    logIn(context, payload) {
      axios({
        method:'post',
        url: `${URL}/accounts/login/`,
        data:{
          username : payload.username,
          password : payload.password,
        }
      })
      .then((res)=>{
        console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    inputReview(context,payload){
      console.log(payload)
      axios({
        method:'post',
        url:`${URL}/reviews/`,
        data:{
          content:payload.content,
          movie_id:payload.movie_id,
          vote:4,
        },
        headers:{
          Authorization : `Token ${context.state.token}`
        }
      })
      .then((res)=>{
        console.log(res)
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
  
  export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions,
  }
  