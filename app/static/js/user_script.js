var url_tag = document.getElementById("url");
var url =url_tag.innerText;



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

function buildURL(key,value){
    let flip =false;
    if (url.includes(key+'=')) {
        let index_of =url.indexOf(key+'=')
        
        let replace="";
        for(let i= index_of; i < url.length; i++){
            if(url[i]=='&') break
            else{
                replace+=url[i]
            }
        }
        let with_ = key+'='+value
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
        if(flip) url+= ('&'+key+'='+value)
        else     url+= ('?'+key+'='+value)
    }

}

function redisplay(event){

    if(event === "search"){
        
        let value =document.getElementById('search').value
        value = value.replace(/ /g, '+')
        buildURL("search",value)
        

    }

    else if(event == 'left' || event == 'right'){

        let value =document.getElementById('page_number').innerText
        if(event == 'left') value = parseInt(value)-1
        else value = parseInt(value)+1

        buildURL("page",value)
    }
    else if( event == 'step_size'){
        
        let value = document.getElementById('step_size').value
        
        buildURL('rows',value)
    }
    else{
        let flip =false;
        let name = event.target.name;
        let value = event.target.value;
        value = value.replace(/ /g, '+')
        
        buildURL(name,value)
    }
    console.log(url)
    customFetch(url,"GET")  
}

