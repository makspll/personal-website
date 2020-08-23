import React from 'react';
import {GET_ROOT_URL,GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader"
import TagFilterPlaceholder from "../component_placeholders/TagFilterPlaceholder";



class TagFilter extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            tag_list: [],
            tags_loaded : false,
        }
    }
    componentDidMount(){
        this.load_tags_page();
    }
    load_tags_page(){
        var url_href = GET_API_ROOT_URL() + `tags/projects/`;
        fetch(url_href).then(res => {
                if(res.ok){
                    return res.json();
                } else {
                    throw `Couldn't fetch tags, status code: ${res.status}`
                }
            })
            .then( 
                (result) =>{
                    let aggregated_tag_names = result.flatMap((val)=>
                        val.tag.name
                    )
                    this.setState({
                        tag_list : aggregated_tag_names,
                        tags_loaded : true,
                    });
                },
                (error)=>{
                    this.setState({
                        tags_loaded : true,
                    })
                    console.error(error);
                }
            )
    }



    selectTag(name){
        let {filters} = this.props;
        let new_filters = Object.assign({},this.props.filters);

        new_filters["selected_tags"] = [...filters.selected_tags,name];
        this.props.set_filters(new_filters);
    }

    deSelectTag(name){
        let {filters} = this.props;

        let idx_of_tag = filters.selected_tags.indexOf(name);
        let selected_tags_copy = filters.selected_tags.slice();
        selected_tags_copy.splice(idx_of_tag,1);

        let new_filters = Object.assign({},filters);
        new_filters["selected_tags"] = selected_tags_copy

        this.props.set_filters(new_filters)
    }

    render() { 
        let {tags_loaded, tag_list} = this.state;
        let {filters} = this.props;
        let content = null;
        if(tags_loaded && tag_list){

            let tags = tag_list.map((val,index)=>{

                let button = null;
                if(filters.selected_tags.includes(val)){
                    button = <button key={index} className="btn btn-secondary btn-sm p-1 m-1 active" onClick={()=>this.deSelectTag(val)} role="switch" aria-checked="true">{val}</button>
                }else{
                    button = <button key={index} className="btn btn-secondary btn-sm p-1 m-1" onClick={()=>this.selectTag(val)} role="switch" aria-checked="false">{val} </button>
                }

                return button;
            })

            content = 
                <div className="d-flex flex-row flex-wrap">
                    {tags}
                </div>

        }else if (tags_loaded){
            content =  
                    <div className="d-flex flex-row flex-wrap">
                        <p>Could not load tags, please refresh the page.</p>
                    </div>
        } else {
            content = <TagFilterPlaceholder/>
        }
        return(content);    
}

}

export default TagFilter
