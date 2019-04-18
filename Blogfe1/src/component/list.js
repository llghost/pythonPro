import React from 'react';
import '../css/login.css'
import { observer } from 'mobx-react';
import {Link} from 'react-router-dom';
import 'antd/lib/message/style'
import {inject,parse_qs} from '../util'
import BlogService from '../service/blog';
import 'antd/lib/message/style'
import 'antd/lib/list/style'  //3.1.5 才有 list  如果要用 package.json 该antd 版本 然后 npm update
import {List,Pagination} from 'antd'

const service=new BlogService()

@inject({service}) //装饰器函数
@observer //使用mobx 的观察者 监控被观察者状态
export default class L extends React.Component{  
  constructor(props){
    super(props);
    console.log(props)
    console.log(props.location)
    props.service.list(props.location.search)//表示取连接后参数
  }
  getUrl(c){
    let obj=parse_qs(this.props.location.search)
    let {size=20} =obj //默认值解构
    return "/list?page="+c+'&size='+size;
  }
  handleChange(pageNo,pageSize){
   console.log(pageNo,pageSize)
   let search='?page='+pageNo+"&size="+pageSize;
   this.props.service.list(search)//每次分页重新请求
  }
  itemRender(current,type,originalElement){
    console.log(current)
    if(current==0) return originalElement;
    
    if(type==="page")
       return <Link to={this.getUrl(current)}>{current}</Link>;
    if(type==="next" )
       return <Link to={this.getUrl(current)} className='ant-pagination-item-link' ></Link>;
    if( type==='prev')
       return <Link to={this.getUrl(current)} className='ant-pagination-item-link' ></Link>;
     
    return originalElement;

  }

  render(){
    let data=this.props.service.posts
    if(data.length){
      const pagination=this.props.service.pagination
      return (<List
        itemLayout="horizontal"
        dataSource={data}
        renderItem={item => (
          <List.Item><List.Item.Meta title={
          <Link to={"/post/"+item.postid}>
          
          {item.title}
          </Link>
          }/></List.Item>
        )}
         pagination={{
           current:pagination.page,
           pageSize:pagination.size,
           total:pagination.count,
           onChange:this.handleChange.bind(this),
           itemRender:this.itemRender.bind(this)
         }}
         />);
    }else{
      return (<div></div>);
    }

  }
}
