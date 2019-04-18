import axios from 'axios';
import { observable } from 'mobx';
import store from 'store'

export default class BlogService{
    constructor(){
        this.instance=axios.create(
            {baseURL :'/api/post/'}
        );
    }
@observable errmsg=""
@observable posts=[] //博文列表
@observable pagination={
    "page":1,//当前页
    "size":20,//每页条数
    "count":0,//总条数
    "pages":1//总页数
} //分页数据

@observable post={} //博文


    getJwt (){
    return store.get('token',null);
    }

 pub(title,content){

 console.log(title,content)
 this.instance.post('pub',
 {
     title,content
 },
 {headers:{'JWT':store.get('token',null)}}
 )
 .then(
        (response)=>{
            console.log(response.data)
        console.log(response.status)
         this.errmsg='发布成功'
     }
 )
 .catch(
     (error) => {
     console.log(error)
     this.errmsg='发布失败'
     }
 )
 }
 list(search){

    console.log(search)
    this.instance.get(search)
    .then(
           (response)=>{
               console.log(response.data)
           console.log(response.status)
            this.posts=response.data.posts
            this.pagination=response.data.pagination
        }
    )
    .catch(
        (error) => {
        console.log(error)
        this.errmsg='发布失败'
        }
    )
    }

getPost(id){

        console.log(id)
        this.instance.get(id)
        .then(
               (response)=>{
                   console.log(response.data)
               console.log(response.status)
                this.post=response.data.post

            }
        )
        .catch(
            (error) => {
            console.log(error)
            this.errmsg='发布失败'
            }
        )
        }

}
