import axios from 'axios'
import router from '../../router'


const URL = 'http://127.0.0.1:8000'

const state = () => {
    return {
      token : null, 
      login_user : {
        nickname : null,
        my_image : null,
      },
      background : null,
      recommend: null,
      user_review: null
    }
  }
  const getters = {
    isLogin(state){
      return state.token ? true : false
    },
    isCreate(state){
      return state.user_review
    }
  }
  const mutations = {
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({ name: 'movies' })
    },
    LOG_OUT(state){
      state.token = null
      state.login_user.nickName = null
      state.login_user.my_image = null
    },
    USER_STATE(state, payload){
      console.log(payload)
      state.login_user.nickname = payload.nickname
      state.login_user.my_image =URL+payload.my_image
    },
    SIGN_UP(){
      router.push({ name: 'login' })
    },
    INIT_BACKGROUND(state, payload){
      state.background = payload
    },
    CHANGE_REVIEW(state, data){
      state.user_review = data
    }
  }
  const actions = {
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
        context.commit('SIGN_UP')
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
      .then(()=>{
        axios({
          method:'get',
          url: `${URL}/accounts/userStatus`,
          headers:{
            Authorization : `Token ${context.state.token}`
          }
        })
        .then((res)=>{
          console.log(res)
          const payload ={
            nickname:res.data.user.nickname,
            my_image:res.data.user.my_image
          }
          context.commit('USER_STATE',payload )
        })
        .catch((err)=>{
          console.log(err)
        })
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    backDrop(context){
      let token;
      if (context.state.token) {
        token = `Token ${context.state.token}`
      }
      axios({
        method:'get',
        url: `${URL}/accounts/userStatus`,
        headers:{
          Authorization : token
        }
      })
      .then((res)=>{
        context.commit('INIT_BACKGROUND', res.data.backdrop_path)
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
        context.commit('CHANGE_REVIEW', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
     
    },
    logOut(context){
      axios({
        method:'post',
        url: `${URL}/accounts/logout/`,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(()=>{
        context.commit('LOG_OUT')
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    recommend(context){
      let token;
      if (context.state.token) {
        token = `Token ${context.state.token}`
      }
      axios({
        method:'get',
        url: `${URL}/movies/recommend/`,
        headers:{
          Authorization : token
        }
      })
      .then((res) => {
        console.log('test')
        console.log(res)
        console.log('test')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteReview(context, id){
      axios({
        method:'delete', 
        url:`${URL}/reviews/`,
        data:{
          review_id: id
        },
        headers:{
          Authorization : `Token ${context.state.token}`
        }
      })
      .then((res)=>{
        console.log(res)
        context.commit('CHANGE_REVIEW', [])
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    // updateReview(context, payload){
    //   axios({
    //     method:'put', 
    //     url:`${URL}/reviews/`,
    //     data:{
    //       review_id: id
    //     },
    //     headers:{
    //       Authorization : `Token ${context.state.token}`
    //     }
    //   })
    //   .then((res)=>{
    //     console.log(res)
    //     context.commit('CHANGE_REVIEW', [])
    //   })
    //   .catch((err)=>{
    //     console.log(err)
    //   })
    // }
  }
  
  export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions,
  }
  