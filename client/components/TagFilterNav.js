import React from 'react';
import {GET_ROOT_URL,GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader"
import TagFilterNavPlaceholder from '../component_placeholders/TagFilterNavPlaceholder';

class TagFilterNav extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            tag_list: [],
            tags_loaded : false,
        }
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

    componentDidMount() {
        this.load_tags_page()
    }

    selectTag(name){
        this.props.set_selected_tags_handler([...this.props.selected_tags,name])
    }

    deSelectTag(name){
        let idx_of_tag = this.props.selected_tags.indexOf(name);
        let selected_tags_copy = this.props.selected_tags.slice();
        selected_tags_copy.splice(idx_of_tag,1);
        this.props.set_selected_tags_handler(selected_tags_copy)
    }

    render() { 

        let {tags_loaded, tag_list} = this.state;
        
        let content = null;
        if(tags_loaded && tag_list){

            let tags = tag_list.map((val,index)=>{

                let button = null;
                if(this.props.selected_tags.includes(val)){
                    button = <button className="btn btn-secondary btn-sm p-1 m-1 active" onClick={()=>this.deSelectTag(val)} role="switch" aria-checked="true">{val}</button>
                }else{
                    button = <button className="btn btn-secondary btn-sm p-1 m-1" onClick={()=>this.selectTag(val)} role="switch" aria-checked="false">{val} </button>
                }

                return button;
            })

            content = 
                <nav className="bg-primary text-light border border-gray p-2 overflow-auto">
                    <div className="d-flex">
                        <p className="m-0 text-left h3">Filters</p>

                        <button 
                            className="btn btn-warning btn-sm ml-auto"
                            onClick={()=>this.props.set_selected_tags_handler([])}
                            >
                            Clear Filters
                        </button>

                    </div>
                    <hr className="my-2 bg-light"/>
                    <div className="d-flex flex-row flex-wrap">
                        {tags}
                    </div>
                </nav>
        }else if (tags_loaded){
            content =  
                <nav className="bg-primary text-light border border-gray p-2 overflow-auto">
                    <div className="d-flex">
                        <p className="m-0 text-left h3">Filters</p>

                        <button 
                            className="btn btn-warning btn-sm ml-auto disabled"
                            >
                            Clear Filters
                        </button>

                    </div>
                    <hr className="my-2 bg-light"/>
                    <div className="d-flex flex-row flex-wrap">
                        <p>Could not load tags, please refresh the page.</p>
                    </div>
                </nav>;
        } else {
            content = <TagFilterNavPlaceholder/>
        }
        return(content);    
}

}

export default TagFilterNav
