//装饰器函数演变过程 见test.js
import React from 'react'

const inject = obj => Comp => props => <Comp {...obj} {...props}/>;


/**
 * 
 * @param {url} url 
 * @param {匹配规则} re 
 */
function parse_qs(url,re=/(\w+)=([^&]+)/){//re 是正则对象 不要加 ‘’
    
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

//  url="?page=1&size=20&name=tom&age=19&hight=&aa=b"
//  reg=/(\w+)=([^&]+)/
//  console.log(parse_qs(url,reg))

export {inject,parse_qs}

