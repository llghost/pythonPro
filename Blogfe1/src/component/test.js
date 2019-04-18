// //装饰器函数演变过程
// import {React} from 'react'
// //原型
// class Reg extends React.Component{
//     render(){
//         return <_Reg service={service}/>
//     }
// }
// //匿名组件
// const Reg= class  extends React.Component{
//     render(){
//         return <_Reg service={service}/>
//     }
// }

// //提取参数
// function inject(Comp){
//     return class  extends React.Component{
//         render(){
//             return <Comp service={service}/>
//         }
//     }
// }

// function inject(s,Comp){
//     return class  extends React.Component{
//         render(){
//             return <Comp service={s}/>
//         }
//     }
// }

// //props
// function inject(obj,Comp){
//     return class  extends React.Component{
//         render(){
//             return <Comp {...obj}/>
//         }
//     }
// }
// //柯里化
// function inject(obj){
//     function wrapper(Comp){
//         return class  extends React.Component{
//             render(){
//                 return <Comp {...obj}/>
//             }
//         }
//     }
//     return wrapper;
// }
// //变形
// function inject(obj){
//     return function wrapper(Comp){
//         return class  extends React.Component{
//             render(){
//                 return <Comp {...obj}/>
//             }
//         }
//     }
// }

// const inject = obj =>{
//     return Comp => {
//         return class  extends React.Component{
//             render(){
//                 return <Comp {...obj}/>
//             }
//         }
//     }
// }

// const inject = obj => Comp => { 
//      return props => <Comp {...obj}/>  
// }

function parse_qs(url,re='/(\w+)=([^&]+)/'){
    
    let ret={}
    if (url.startsWith('?'))
        url=url.substr(1)
    let qs=url.split('&')
    qs.forEach(element => {
        console.log(element)
          let match= re.exec(element)
          if (match)
             ret[match[1]]=match[2]
    });
    return ret;

}

 url="?page=1&size=20&name=tom&age=19&hight=&aa=b"
 reg=/(\w+)=([^&]+)/
 console.log(parse_qs(url,reg))
