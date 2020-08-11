import React from 'react';
import {GET_API_ROOT_URL} from '../DynamicVariables';
import {LazyLoadImage} from 'react-lazy-load-image-component';

class LinkCardBlock extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            loaded_photo: false,
            loaded_link: false,
            link_json: null,
            photo_json: null,
        }
    }
    componentDidMount(){
        let {json} = this.props;

        //link
        fetch(`${GET_API_ROOT_URL()}pages/${json.linked_page}`)
            .then((res)=>{
                if(res.ok){
                    return res.json()
                }else {
                    throw `Could not fetch linked page. status code: ${res.status}`
                }
            })
            .then((res)=>{
                this.setState({
                    loaded_link:true,
                    link_json:res,
                })
            },(err)=>{
                console.error(err);
            })

        // photo
        fetch(`${GET_API_ROOT_URL()}images/${json.miniature_image}`)
            .then((res)=>{
                if(res.ok){
                    return res.json()
                }else {
                    throw `Could not fetch link photo. status code: ${res.status}`
                }
            })
            .then((res)=>{
                this.setState({
                    loaded_photo:true,
                    photo_json:res,
                })
            },(err)=>{
                console.error(err);
            })
    }

    render(){
        // --blue: #007bff;
        // --indigo: #6610f2;
        // --purple: #6f42c1;
        // --pink: #e83e8c;
        // --red: #dc3545;
        // --orange: #fd7e14;
        // --yellow: #ffc107;
        // --green: #28a745;
        // --teal: #20c997;
        // --cyan: #17a2b8;
        // --white
        let {isLoaded,json,index} = this.props;
        let {loaded_photo,photo_json,loaded_link,link_json} = this.state
        let content = null;
        let loaded_content = loaded_link;
        if(isLoaded && json && loaded_content){

            let color_variables = ["blue","green","yellow"]
            let color_hexes = color_variables.map((value,index)=>{
                return getComputedStyle(document.documentElement)
                            .getPropertyValue("--"+value);
            })
            let current_color = color_hexes[index % color_hexes.length]

            let image = null;
            if(photo_json){
                let image_title = photo_json.title;
                image = 
                        <LazyLoadImage
                            alt={image_title}
                            src={photo_json.meta.download_url}
                            height={photo_json.height}
                            width={photo_json.width}
                            className="img-fluid"
                        />
            }
            content = 
                <div className="card shadow bg-secondary text-dark text-center m-5" style={{width:"300px"}}>
                    <div className="border-bottom-0 card-header bg-white position-relative" >
                        {image}
                        <div className=" absolute-side-right" style={{backgroundColor:current_color,height:"100%",width:"10px"}}>
                        </div>
                    </div>
                    <div className="card-body position-relative">
                        <h3 className="card-title">{json.heading}</h3>
                        <hr/>
                        <p className="card-text">{json.text}</p>
                        <a href={link_json.meta.html_url} className="btn absolute-bottom-right" style={{backgroundColor:current_color,borderRadius:"0",borderColor:color_hexes[index]}}><i class="fas fa-chevron-right"></i></a>
                    </div>
                </div>
        } else if(isLoaded){

        } else {

        }

        return content;
    }
}

export default LinkCardBlock;