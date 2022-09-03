var url_tag = document.getElementById("url");
var url =url_tag.innerText;
// url = new URL(url)


function customFetch(url,type,data){

    if(type== "GET"){
        fetch(url,{
            mehtod: type
        })
        .then( res => {
            if(res.ok){
                console.log("GET Successfull")
            }
        })
    }
    else if(type == "POST"){
        fetch(url,{
            mehtod: type,
            header: {
                "Content-type": "application/json"
            },
            body : JSON.stringify(data)
        })
        .then( res => {
            if(res.ok){
                console.log("POST Successfull")
            }
        })
    }
}
obj={};
function buildURL(key,value){
    obj[key] =value;
}

function redisplay(event){

    if(event === "search"){
        let flip =false;
        let value =document.getElementById('search').value

        if (url.includes('search=')) {
            let index_of =url.indexOf('search=')
            
            let replace="";
            //+url[index_of+5]+url[index_of+6]
            for(let i= index_of; i < url.length; i++){
                if(url[i]=='&') break
                else{
                    replace+=url[i]
                }
            }
            let with_ = 'search='+value
            console.log(replace)
            url= url.replace(replace,with_)
        }
        else{
            for(var i=0;i<(url).length;i++){
                if('?' == url[i]){
                    flip =true;
                    break;
                }    
            }
            if(flip) url+= ('&'+'search'+'='+value)
            else     url+= ('?'+'search'+'='+value)
        }

    }

    else if(event == 'left' || event == 'right'){
        let flip =false;
        
        let value =document.getElementById('page_number').innerText
        
        if(event == 'left') value = parseInt(value)-1
        else value = parseInt(value)+1

        if (url.includes('page=')) {
            let index_of =url.indexOf('page=')
            
            let replace="";
            //+url[index_of+5]+url[index_of+6]
            for(let i= index_of; i < url.length; i++){
                if(url[i]=='&') break
                else{
                    replace+=url[i]
                }
            }
            let with_ = 'page='+value
            console.log(replace)
            url= url.replace(replace,with_)
        }
        else{
            for(var i=0;i<(url).length;i++){
                if('?' == url[i]){
                    flip =true;
                    break;
                }    
            }
            if(flip) url+= ('&'+'page'+'='+value)
            else     url+= ('?'+'page'+'='+value)
        }
        

    }
    else if( event == 'step_size'){
        
        let flip =false;
        let value = document.getElementById('step_size').value
      
        alert(value)
        if (url.includes('rows=')) {
            let index_of =url.indexOf('rows=')
            
            let replace="";
            //+url[index_of+5]+url[index_of+6]
            for(let i= index_of; i < url.length; i++){
                if(url[i]=='&') break
                else{
                    replace+=url[i]
                }
            }
            let with_ = 'rows='+value
            console.log(replace)
            url= url.replace(replace,with_)
        }
        else{
            for(var i=0;i<(url).length;i++){
                if('?' == url[i]){
                    flip =true;
                    break;
                }    
            }
            if(flip) url+= ('&'+'rows'+'='+value)
            else     url+= ('?'+'rows'+'='+value)
        }
        
    
    }
    else{
        let flip =false;
        let name = event.target.name;
        let value = event.target.value;
        value = value.replace(/ /g, '+')

        if (url.includes(name)) {
            let index_of =url.indexOf(name)
            
            let replace="";
            //+url[index_of+5]+url[index_of+6]
            for(let i= index_of; i < url.length; i++){
                if(url[i]=='&') break
                else{
                    replace+=url[i]
                }
            }
            let with_ = name+'='+value
            console.log(replace)
            url= url.replace(replace,with_)
        }
        else{
            for(var i=0;i<(url).length;i++){
                if('?' == url[i]){
                    flip =true;
                    break;
                }    
            }
            if(flip) url+= ('&'+name+'='+value)
            else     url+= ('?'+name+'='+value)
        }


        // for(var i=0;i<(url).length;i++){
        //     if('?' == url[i]){
        //         flip =true;
        //         break;
        //     }    
        // }

        // if(flip) url+= ('&'+name+'='+value)
        // else     url+= ('?'+name+'='+value)
    
    }
    console.log(url)
    customFetch(url,"GET")
}

function mainCount(){
    alert("main")
}