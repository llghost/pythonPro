import axios from 'axios';
import { observable } from 'mobx';
import store from 'store'

//加入过期插件
store.addPlugin(require('store/plugins/expire'))

export default class UserService{
 @observable loginin=false
 @observable regin=false
 @observable errmsg=""
 login(email,password,obj){

 console.log(email,password)
 axios.post('api/user/login',{
    email:email,
    password:password
 })
 .then(
     //function(response){
        (response)=>{ //使用箭头函数 解决this 取不到的问题
        //  console.log(response)
        //  console.log(response.data)
        //  console.log(response.status)
        //  console.log(response.statusText)
        //  console.log(response.headers)
        //  console.log(response.config)
         //obj.setState({ret:10000})
         console.log(response.data.token)

         //设置localstore
         store.set('token',response.data.token,(new Date()).getTime()+(8*3600*1000))
         this.loginin=true
     }
 )
 .catch(
     (error) => {
     console.log(error)
     this.errmsg="用户名或密码错误"
     }
 )
 }

 reg(name,email,password){
    console.log(email,password)
    axios.post('api/user/reg',{
        name:name,
       email:email,
       password:password
    })
    .then(
        (response) => {
            console.log(response)
            console.log(response.data)
            console.log(response.status)
            this.regin=true
   
        }
    ) .catch(
        (error)=>{
        console.log(error)
        this.errmsg="该邮箱已被占用"
        }
    )
    }

}